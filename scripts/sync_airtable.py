#!/usr/bin/env python3
"""
Airtable to MDX Sync Script for AI Conference Website
Fetches content from Airtable and creates/updates MDX files with YAML frontmatter
"""

import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import requests
from dotenv import load_dotenv
import git
import slugify

# Load environment variables
load_dotenv()

# Configuration
AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME', 'Posts')
CONTENT_DIR = Path('content')
POSTS_DIR = CONTENT_DIR / 'posts'
SPEAKERS_DIR = CONTENT_DIR / 'speakers'
SESSIONS_DIR = CONTENT_DIR / 'sessions'

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sync_airtable.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class AirtableSync:
    def __init__(self):
        if not AIRTABLE_API_KEY or not AIRTABLE_BASE_ID:
            raise ValueError("AIRTABLE_API_KEY and AIRTABLE_BASE_ID must be set in environment variables")
        
        self.api_key = AIRTABLE_API_KEY
        self.base_id = AIRTABLE_BASE_ID
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        self.base_url = f'https://api.airtable.com/v0/{self.base_id}'
        
        # Ensure directories exist
        self.ensure_directories()
        
        # Git repo for commits
        try:
            self.repo = git.Repo('.')
        except git.InvalidGitRepositoryError:
            logger.warning("Not a git repository. Git operations will be skipped.")
            self.repo = None
    
    def ensure_directories(self):
        """Ensure content directories exist"""
        directories = [CONTENT_DIR, POSTS_DIR, SPEAKERS_DIR, SESSIONS_DIR]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def fetch_records(self, table_name: str, fields: Optional[List[str]] = None) -> List[Dict]:
        """Fetch all records from an Airtable table"""
        url = f'{self.base_url}/{table_name}'
        params = {}
        
        if fields:
            params['fields[]'] = fields
        
        all_records = []
        offset = None
        
        while True:
            if offset:
                params['offset'] = offset
            
            try:
                response = requests.get(url, headers=self.headers, params=params)
                response.raise_for_status()
                data = response.json()
                
                all_records.extend(data.get('records', []))
                offset = data.get('offset')
                
                if not offset:
                    break
                    
            except requests.RequestException as e:
                logger.error(f"Error fetching records from {table_name}: {e}")
                return []
        
        logger.info(f"Fetched {len(all_records)} records from {table_name}")
        return all_records
    
    def sanitize_slug(self, text: str) -> str:
        """Create a safe filename slug from text"""
        return slugify.slugify(text, lowercase=True, max_length=50)
    
    def create_frontmatter(self, fields: Dict) -> str:
        """Create YAML frontmatter from Airtable fields"""
        frontmatter = "---\n"
        
        # Standard fields mapping
        field_mapping = {
            'title': 'title',
            'slug': 'slug', 
            'date': 'date',
            'published': 'published',
            'author': 'author',
            'tags': 'tags',
            'category': 'category',
            'excerpt': 'excerpt',
            'featured': 'featured',
            'speaker_name': 'speaker',
            'session_time': 'time',
            'session_track': 'track',
            'bio': 'bio',
            'company': 'company',
            'twitter': 'twitter',
            'linkedin': 'linkedin'
        }
        
        for airtable_field, yaml_field in field_mapping.items():
            if airtable_field in fields and fields[airtable_field]:
                value = fields[airtable_field]
                
                # Handle different data types
                if isinstance(value, list):
                    frontmatter += f"{yaml_field}:\n"
                    for item in value:
                        frontmatter += f"  - {item}\n"
                elif isinstance(value, bool):
                    frontmatter += f"{yaml_field}: {str(value).lower()}\n"
                elif isinstance(value, (int, float)):
                    frontmatter += f"{yaml_field}: {value}\n"
                else:
                    # Escape quotes in strings
                    escaped_value = str(value).replace('"', '\\"')
                    frontmatter += f'{yaml_field}: "{escaped_value}"\n'
        
        # Add generated fields
        frontmatter += f'generated_at: "{datetime.now().isoformat()}"\n'
        frontmatter += f'layout: "post"\n'
        frontmatter += "---\n\n"
        
        return frontmatter
    
    def create_mdx_file(self, record: Dict, content_type: str = 'posts') -> bool:
        """Create or update an MDX file from an Airtable record"""
        fields = record.get('fields', {})
        
        # Get required fields
        title = fields.get('title', 'Untitled')
        slug = fields.get('slug') or self.sanitize_slug(title)
        content = fields.get('content', '')
        
        # Determine target directory
        if content_type == 'speakers':
            target_dir = SPEAKERS_DIR
        elif content_type == 'sessions':
            target_dir = SESSIONS_DIR
        else:
            target_dir = POSTS_DIR
        
        # Create filename
        filename = f"{slug}.mdx"
        filepath = target_dir / filename
        
        # Check if file exists and has same content (skip if unchanged)
        if filepath.exists():
            existing_content = filepath.read_text(encoding='utf-8')
            # Simple check - could be more sophisticated
            if title in existing_content and content in existing_content:
                logger.debug(f"Skipping unchanged file: {filepath}")
                return False
        
        # Create frontmatter
        frontmatter = self.create_frontmatter(fields)
        
        # Combine frontmatter and content
        full_content = frontmatter + content
        
        # Write file
        try:
            filepath.write_text(full_content, encoding='utf-8')
            logger.info(f"Created/updated: {filepath}")
            return True
        except Exception as e:
            logger.error(f"Error writing file {filepath}: {e}")
            return False
    
    def sync_table(self, table_name: str, content_type: str = 'posts') -> int:
        """Sync a specific Airtable table to MDX files"""
        logger.info(f"Syncing table: {table_name} -> {content_type}")
        
        records = self.fetch_records(table_name)
        if not records:
            logger.warning(f"No records found in table: {table_name}")
            return 0
        
        created_count = 0
        for record in records:
            fields = record.get('fields', {})
            
            # Skip unpublished records
            if not fields.get('published', True):
                continue
            
            if self.create_mdx_file(record, content_type):
                created_count += 1
        
        logger.info(f"Created/updated {created_count} files from {table_name}")
        return created_count
    
    def commit_changes(self, message: str = None):
        """Commit changes to git repository"""
        if not self.repo:
            logger.warning("No git repository found. Skipping commit.")
            return
        
        try:
            # Check for changes
            if not self.repo.is_dirty(untracked_files=True):
                logger.info("No changes to commit.")
                return
            
            # Add all changes
            self.repo.git.add('.')
            
            # Create commit message
            if not message:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"Auto-sync from Airtable - {timestamp}"
            
            # Commit
            self.repo.index.commit(message)
            logger.info(f"Committed changes: {message}")
            
            # Push if origin exists
            try:
                origin = self.repo.remote(name='origin')
                origin.push()
                logger.info("Pushed changes to origin")
            except (git.exc.InvalidGitRepositoryError, git.exc.GitCommandError) as e:
                logger.warning(f"Could not push to origin: {e}")
                
        except Exception as e:
            logger.error(f"Error committing changes: {e}")
    
    def run_sync(self):
        """Run the complete sync process"""
        logger.info("Starting Airtable sync...")
        
        try:
            total_created = 0
            
            # Sync different content types
            content_tables = [
                ('Posts', 'posts'),
                ('Speakers', 'speakers'), 
                ('Sessions', 'sessions')
            ]
            
            for table_name, content_type in content_tables:
                try:
                    created = self.sync_table(table_name, content_type)
                    total_created += created
                except Exception as e:
                    logger.error(f"Error syncing {table_name}: {e}")
                    continue
            
            # Summary
            if total_created > 0:
                logger.info(f"Sync completed successfully. {total_created} files created/updated.")
                self.commit_changes()
            else:
                logger.info("Sync completed. No new changes.")
                
        except Exception as e:
            logger.error(f"Sync failed: {e}")
            sys.exit(1)

def main():
    """Main entry point"""
    try:
        syncer = AirtableSync()
        syncer.run_sync()
    except Exception as e:
        logger.error(f"Failed to initialize sync: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 