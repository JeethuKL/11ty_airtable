# 📊 Airtable CMS Integration Guide

Complete guide to storing data in Airtable and automatically syncing it to your 11ty website.

## 🔄 How It Works

### The Complete Workflow
1. **📝 Content Creation**: You add content to Airtable tables
2. **🐍 Python Script**: Fetches data from Airtable API
3. **📄 MDX Generation**: Converts Airtable records to MDX files with YAML frontmatter
4. **⚙️ 11ty Build**: Processes MDX files into static HTML
5. **🌐 Website Update**: New content appears on your site

---

## 📊 Airtable Table Setup

### 1. Posts Table Structure

Create a table called **"Posts"** in Airtable with these fields:

| Field Name | Field Type | Required | Description |
|------------|------------|----------|-------------|
| `title` | Single line text | ✅ | Blog post title |
| `slug` | Single line text | ❌ | URL slug (auto-generated if empty) |
| `content` | Long text | ✅ | Main content (supports Markdown/MDX) |
| `date` | Date | ✅ | Publication date |
| `author` | Single line text | ❌ | Author name |
| `tags` | Multiple select | ❌ | Tags/categories |
| `published` | Checkbox | ✅ | Whether to publish (default: true) |
| `featured` | Checkbox | ❌ | Featured post flag |
| `excerpt` | Long text | ❌ | Short description |

### 2. Speakers Table Structure

Create a table called **"Speakers"**:

| Field Name | Field Type | Required | Description |
|------------|------------|----------|-------------|
| `title` | Single line text | ✅ | Speaker name (e.g., "Dr. Sarah Chen") |
| `slug` | Single line text | ❌ | URL slug |
| `bio` | Long text | ✅ | Speaker biography |
| `company` | Single line text | ❌ | Company/organization |
| `role` | Single line text | ❌ | Job title |
| `twitter` | Single line text | ❌ | Twitter handle |
| `linkedin` | Single line text | ❌ | LinkedIn profile |
| `published` | Checkbox | ✅ | Whether to publish |

### 3. Sessions Table Structure

Create a table called **"Sessions"**:

| Field Name | Field Type | Required | Description |
|------------|------------|----------|-------------|
| `title` | Single line text | ✅ | Session title |
| `slug` | Single line text | ❌ | URL slug |
| `content` | Long text | ✅ | Session description |
| `session_time` | Single line text | ❌ | Time slot |
| `session_track` | Single select | ❌ | Track (Research, Industry, etc.) |
| `speaker_name` | Link to Speakers | ❌ | Link to speaker record |
| `published` | Checkbox | ✅ | Whether to publish |

---

## 🔑 Setup Instructions

### Step 1: Get Airtable Credentials

1. **Get API Key**:
   - Go to https://airtable.com/create/tokens
   - Create a new personal access token
   - Grant permissions: `data.records:read`

2. **Get Base ID**:
   - Open your Airtable base
   - Go to https://airtable.com/api
   - Select your base
   - Copy the Base ID (starts with `app...`)

### Step 2: Configure Environment

Create `.env` file:
```bash
# Copy from env.example
cp env.example .env
```

Edit `.env` with your credentials:
```bash
# Airtable Configuration
AIRTABLE_API_KEY=patXXXXXXXXXXXXXX.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX
AIRTABLE_TABLE_NAME=Posts

# Optional: Additional tables
AIRTABLE_SPEAKERS_TABLE=Speakers
AIRTABLE_SESSIONS_TABLE=Sessions
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🐍 How the Python Script Works

### Core Process

```python
# 1. Connect to Airtable
syncer = AirtableSync()

# 2. Fetch records from each table
records = syncer.fetch_records('Posts')

# 3. Convert each record to MDX
for record in records:
    syncer.create_mdx_file(record, 'posts')

# 4. Commit changes to git
syncer.commit_changes()
```

### Data Transformation Example

**Airtable Record**:
```json
{
  "id": "recXXXXXXX",
  "fields": {
    "title": "AI Trends in 2024",
    "content": "# Main Content\n\nThis is the blog post content...",
    "date": "2024-01-15",
    "author": "John Doe",
    "tags": ["AI", "Trends", "Technology"],
    "published": true,
    "featured": false
  }
}
```

**Generated MDX File** (`content/posts/ai-trends-in-2024.mdx`):
```markdown
---
title: "AI Trends in 2024"
date: "2024-01-15"
author: "John Doe"
tags:
  - AI
  - Trends
  - Technology
published: true
featured: false
generated_at: "2024-01-15T10:30:00.000Z"
layout: "post"
---

# Main Content

This is the blog post content...
```

---

## ⚡ Running the Sync

### Manual Sync
```bash
# Run the sync script
python3 scripts/sync_airtable.py

# Or using npm script
npm run sync
```

### Automated Sync (GitHub Actions)
The sync runs automatically:
- **Every 6 hours** (scheduled)
- **On push** to main branch
- **Manual trigger** from GitHub Actions tab

### What Happens During Sync

1. **Fetch Data**: Script connects to Airtable API
2. **Check Changes**: Compares with existing files
3. **Create/Update Files**: Generates new MDX files
4. **Git Commit**: Commits changes with timestamp
5. **Build Site**: 11ty rebuilds the website
6. **Deploy**: Updated site goes live

---

## 📝 Content Management Workflow

### Adding a New Blog Post

1. **Open Airtable** → Go to "Posts" table
2. **Add New Record**:
   ```
   Title: "My New Blog Post"
   Content: "# Welcome\n\nThis is my content..."
   Date: 2024-01-20
   Author: "Your Name"
   Tags: AI, Blog
   Published: ✅ (checked)
   ```
3. **Save** → Script will sync automatically
4. **Wait** → New post appears at `/posts/my-new-blog-post/`

### Adding a Speaker Profile

1. **Open Airtable** → Go to "Speakers" table
2. **Add New Record**:
   ```
   Title: "Dr. Jane Smith"
   Bio: "Leading AI researcher with 10+ years..."
   Company: "Tech University"
   Role: "Professor of AI"
   Twitter: "janesmith_ai"
   Published: ✅
   ```
3. **Save** → Profile appears at `/speakers/dr-jane-smith/`

---

## 🎯 Advanced Features

### Custom Field Mapping

The script maps Airtable fields to YAML frontmatter:

```python
field_mapping = {
    'title': 'title',           # Airtable → YAML
    'slug': 'slug',
    'date': 'date',
    'published': 'published',
    'author': 'author',
    'tags': 'tags',
    'bio': 'bio',
    'company': 'company',
    'twitter': 'twitter'
}
```

### Content Types Support

- **Posts**: Blog articles, news, updates
- **Speakers**: Speaker profiles and bios
- **Sessions**: Conference sessions, workshops
- **Custom**: Add your own content types

### Smart Updates

- **Skip Unchanged**: Only updates files when content changes
- **Git Integration**: Automatic commits with meaningful messages
- **Error Handling**: Continues processing if one record fails
- **Logging**: Detailed logs of sync operations

---

## 🔧 Customization

### Adding New Content Types

1. **Create Airtable Table** (e.g., "Sponsors")
2. **Add to Script**:
   ```python
   content_tables = [
       ('Posts', 'posts'),
       ('Speakers', 'speakers'),
       ('Sessions', 'sessions'),
       ('Sponsors', 'sponsors')  # New!
   ]
   ```
3. **Create Directory**: `mkdir content/sponsors`
4. **Add to 11ty Config**: Update `.eleventy.js` collections

### Custom Field Handling

```python
# In create_frontmatter method
if 'custom_field' in fields:
    frontmatter += f'custom: "{fields["custom_field"]}"\n'
```

---

## 📋 Example Airtable Data

### Sample Posts Table

| title | content | date | author | tags | published |
|-------|---------|------|--------|------|-----------|
| AI Conference 2024 Announcement | # Big News... | 2024-01-10 | Conference Team | conference, announcement | ✅ |
| Speaker Spotlight: Dr. Chen | Meet our keynote... | 2024-01-15 | Marketing Team | speakers, spotlight | ✅ |
| Workshop Registration Open | Registration is now... | 2024-01-20 | Registration Team | workshops, registration | ✅ |

### Sample Speakers Table

| title | bio | company | role | twitter | published |
|-------|-----|---------|------|---------|-----------|
| Dr. Sarah Chen | Leading expert in... | TechCorp | Director of AI | @sarahchen_ai | ✅ |
| Prof. Michael Johnson | Pioneering researcher... | Stanford | Professor | @profmikej | ✅ |
| Dr. Aisha Rodriguez | Expert in AI ethics... | Ethics Institute | VP Ethics | @aisharodriguez | ✅ |

---

## 🚨 Troubleshooting

### Common Issues

**"API Key Invalid"**
```bash
# Check your .env file
cat .env | grep AIRTABLE_API_KEY

# Verify token has correct permissions
```

**"No Records Found"**
```bash
# Check table name matches exactly
# Verify records have published=true
```

**"Permission Denied"**
```bash
# Check file permissions
chmod +x scripts/sync_airtable.py
```

### Debug Mode

```bash
# Run with verbose logging
python3 scripts/sync_airtable.py --debug

# Check sync logs
tail -f sync_airtable.log
```

---

## 🎉 Benefits

✅ **No Technical Knowledge Required**: Content team uses familiar Airtable interface  
✅ **Real-time Collaboration**: Multiple people can edit content simultaneously  
✅ **Version Control**: All changes tracked in git history  
✅ **Automated Publishing**: Content goes live automatically  
✅ **Data Validation**: Airtable ensures required fields are filled  
✅ **Rich Content**: Support for Markdown, images, links in content  
✅ **SEO Friendly**: Proper frontmatter for meta tags and structure  

---

## 🔗 Related Commands

```bash
# Manual sync
npm run sync

# Development server
npm run dev

# Production build  
npm run build

# Check sync logs
cat sync_airtable.log
```

Your Airtable is now your CMS! 🎊 