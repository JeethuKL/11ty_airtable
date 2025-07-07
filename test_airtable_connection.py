#!/usr/bin/env python3
"""
Test Airtable Connection and Debug Data Structure
"""
import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')

def test_connection():
    """Test Airtable connection and show data structure"""
    
    if not AIRTABLE_API_KEY or AIRTABLE_API_KEY == 'your_airtable_api_key_here':
        print("❌ AIRTABLE_API_KEY not set in .env file")
        print("\nTo get your API key:")
        print("1. Go to https://airtable.com/account")
        print("2. Generate an API key in the 'API' section")
        print("3. Update the .env file with your real API key")
        return False
    
    if not AIRTABLE_BASE_ID:
        print("❌ AIRTABLE_BASE_ID not set in .env file")
        return False
    
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    base_url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}'
    
    # Test with Speakers table
    print("🔍 Testing connection to Speakers table...")
    try:
        response = requests.get(f'{base_url}/Speakers', headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])
            print(f"✅ Successfully connected! Found {len(records)} speaker records.")
            
            if records:
                print("\n📋 Sample speaker data structure:")
                first_record = records[0]
                fields = first_record.get('fields', {})
                
                print(f"Record ID: {first_record.get('id')}")
                print("Fields:")
                for field_name, field_value in fields.items():
                    print(f"  - {field_name}: {type(field_value).__name__} = {field_value}")
                
                print(f"\n📊 All speakers found:")
                for i, record in enumerate(records, 1):
                    speaker_name = record.get('fields', {}).get('Speaker Name', 'Unnamed')
                    company = record.get('fields', {}).get('Company Name', 'No Company')
                    print(f"  {i}. {speaker_name} ({company})")
                    
            return True
            
        elif response.status_code == 404:
            print("❌ Table 'Speakers' not found. Check your table name in Airtable.")
            print("\nYour Airtable base should have a table named exactly 'Speakers'")
            return False
            
        elif response.status_code == 403:
            print("❌ Access denied. Check your API key permissions.")
            return False
            
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.RequestException as e:
        print(f"❌ Connection error: {e}")
        return False

def list_all_tables():
    """List all tables in the base to help with debugging"""
    if not AIRTABLE_API_KEY or AIRTABLE_API_KEY == 'your_airtable_api_key_here':
        print("Need API key to list tables")
        return
    
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    # Try to get base schema (this might not work with all API keys)
    print("\n🔍 Attempting to list all tables in your base...")
    base_url = f'https://api.airtable.com/v0/meta/bases/{AIRTABLE_BASE_ID}/tables'
    
    try:
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            tables = data.get('tables', [])
            print(f"Found {len(tables)} tables:")
            for table in tables:
                print(f"  - {table.get('name', 'Unknown')}")
        else:
            print(f"Could not list tables (status: {response.status_code})")
            print("This is normal - trying common table names instead...")
            
            # Try common table names
            common_tables = ['Speakers', 'Posts', 'Sessions', 'speakers', 'posts', 'sessions']
            print("\n🔍 Testing common table names:")
            
            for table_name in common_tables:
                test_url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{table_name}'
                test_response = requests.get(test_url, headers=headers)
                status = "✅ Exists" if test_response.status_code == 200 else f"❌ {test_response.status_code}"
                print(f"  - {table_name}: {status}")
    
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("🧪 Airtable Connection Test")
    print("=" * 40)
    
    success = test_connection()
    
    if success:
        list_all_tables()
        print("\n✅ Connection test completed successfully!")
        print("You can now run 'npm run sync' to sync your data.")
    else:
        print("\n❌ Connection test failed.")
        print("\nNext steps:")
        print("1. Get your Airtable API key from https://airtable.com/account")
        print("2. Update the AIRTABLE_API_KEY in your .env file")
        print("3. Make sure your table is named exactly 'Speakers'")
        print("4. Run this test again: python3 test_airtable_connection.py") 