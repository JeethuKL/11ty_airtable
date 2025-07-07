# 🚀 Airtable Setup Instructions for AI Conference CMS

**Copy and follow these exact steps to create your Airtable base:**

---

## 📋 **Step 1: Create New Base**

1. Go to **https://airtable.com**
2. Click **"Create a base"** → **"Start from scratch"**
3. Name your base: **"AI Conference CMS"**
4. Delete the default table

---

## 📝 **Step 2: Create "Posts" Table**

### Create the Table
1. Click **"Add a table"** → Name it **"Posts"** (exact spelling)
2. Delete all default fields first

### Add These Exact Fields:

#### Field 1: `title`
- **Field Type**: Single line text
- **Required**: ✅ Yes
- **Description**: Blog post title

#### Field 2: `content` 
- **Field Type**: Long text
- **Required**: ✅ Yes
- **Rich text formatting**: ✅ Enable
- **Description**: Main blog post content (supports Markdown)

#### Field 3: `date`
- **Field Type**: Date
- **Required**: ✅ Yes
- **Date format**: YYYY-MM-DD
- **Include time**: ❌ No
- **Description**: Publication date

#### Field 4: `author`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: Author name

#### Field 5: `tags`
- **Field Type**: Multiple select
- **Required**: ❌ No
- **Options to add**:
  - `conference` (Color: Blue)
  - `speakers` (Color: Green) 
  - `ai` (Color: Purple)
  - `technology` (Color: Red)
  - `announcement` (Color: Orange)
  - `workshop` (Color: Yellow)
  - `research` (Color: Pink)
  - `industry` (Color: Gray)

#### Field 6: `published`
- **Field Type**: Checkbox
- **Required**: ✅ Yes
- **Default**: ✅ Checked
- **Description**: Whether to publish this post

#### Field 7: `featured`
- **Field Type**: Checkbox
- **Required**: ❌ No
- **Default**: ❌ Unchecked
- **Description**: Featured post (appears prominently)

#### Field 8: `slug`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: Custom URL slug (auto-generated if empty)

#### Field 9: `excerpt`
- **Field Type**: Long text
- **Required**: ❌ No
- **Description**: Short description for previews

---

## 👥 **Step 3: Create "Speakers" Table**

### Create the Table
1. Click **"Add a table"** → Name it **"Speakers"** (exact spelling)
2. Delete all default fields

### Add These Exact Fields:

#### Field 1: `title`
- **Field Type**: Single line text
- **Required**: ✅ Yes
- **Description**: Speaker full name (e.g., "Dr. Sarah Chen")

#### Field 2: `bio`
- **Field Type**: Long text
- **Required**: ✅ Yes
- **Rich text formatting**: ✅ Enable
- **Description**: Speaker biography

#### Field 3: `company`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: Company or organization

#### Field 4: `role`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: Job title or position

#### Field 5: `twitter`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: Twitter handle (without @)

#### Field 6: `linkedin`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: LinkedIn profile username

#### Field 7: `published`
- **Field Type**: Checkbox
- **Required**: ✅ Yes
- **Default**: ✅ Checked
- **Description**: Whether to show this speaker

#### Field 8: `slug`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: Custom URL slug (auto-generated if empty)

---

## 🎯 **Step 4: Create "Sessions" Table**

### Create the Table
1. Click **"Add a table"** → Name it **"Sessions"** (exact spelling)
2. Delete all default fields

### Add These Exact Fields:

#### Field 1: `title`
- **Field Type**: Single line text
- **Required**: ✅ Yes
- **Description**: Session or workshop title

#### Field 2: `content`
- **Field Type**: Long text
- **Required**: ✅ Yes
- **Rich text formatting**: ✅ Enable
- **Description**: Session description and details

#### Field 3: `session_time`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: Time slot (e.g., "9:00 AM - 10:30 AM")

#### Field 4: `session_track`
- **Field Type**: Single select
- **Required**: ❌ No
- **Options to add**:
  - `Research Track` (Color: Blue)
  - `Industry Track` (Color: Green)
  - `Workshop` (Color: Orange)
  - `Keynote` (Color: Red)
  - `Panel Discussion` (Color: Purple)

#### Field 5: `speaker_name`
- **Field Type**: Link to another record
- **Required**: ❌ No
- **Link to**: Speakers table
- **Description**: Link to speaker profile

#### Field 6: `published`
- **Field Type**: Checkbox
- **Required**: ✅ Yes
- **Default**: ✅ Checked
- **Description**: Whether to show this session

#### Field 7: `slug`
- **Field Type**: Single line text
- **Required**: ❌ No
- **Description**: Custom URL slug (auto-generated if empty)

---

## ✅ **Step 5: Add Sample Data**

### Sample Posts Record:
```
title: "Welcome to AI Conference 2024"
content: "# Welcome!\n\nWe're excited to announce our upcoming AI Conference 2024..."
date: 2024-01-15
author: "Conference Team"
tags: conference, announcement
published: ✅ (checked)
featured: ✅ (checked)
```

### Sample Speakers Record:
```
title: "Dr. Sarah Chen"
bio: "Leading expert in deep learning and neural architecture search..."
company: "TechCorp AI Research"
role: "Director of AI Research"
twitter: "sarahchen_ai"
linkedin: "sarah-chen-ai"
published: ✅ (checked)
```

### Sample Sessions Record:
```
title: "Introduction to Neural Architecture Search"
content: "This workshop will cover the fundamentals of automated neural network design..."
session_time: "9:00 AM - 10:30 AM"
session_track: Workshop
speaker_name: [Link to Dr. Sarah Chen]
published: ✅ (checked)
```

---

## 🔑 **Step 6: Get Your API Credentials**

### Get Personal Access Token:
1. Go to **https://airtable.com/create/tokens**
2. Click **"Create new token"**
3. Token name: **"AI Conference Sync"**
4. Add these scopes:
   - ✅ `data.records:read`
   - ✅ `data.records:write` (if you want script to update records)
5. Add your base: Select **"AI Conference CMS"**
6. Click **"Create token"**
7. **Copy the token** (starts with `pat...`)

### Get Base ID:
1. Go to **https://airtable.com/api**
2. Select your **"AI Conference CMS"** base
3. **Copy the Base ID** from the URL or API docs (starts with `app...`)

---

## 📋 **Step 7: Provide These Details**

**Once you've created everything, provide me with:**

```
AIRTABLE_API_KEY=pat_YOUR_TOKEN_HERE
AIRTABLE_BASE_ID=app_YOUR_BASE_ID_HERE
```

**Example format:**
```
AIRTABLE_API_KEY=patAbC123xyz789.1234567890abcdefghijklmnopqrstuvwxyz
AIRTABLE_BASE_ID=appABC123DEF456
```

---

## 🎯 **Important Notes**

- ✅ **Exact field names**: Use exactly as specified (case-sensitive)
- ✅ **Required fields**: Mark required fields properly
- ✅ **Default values**: Set checkboxes to checked as specified
- ✅ **Multiple select options**: Add all the color-coded options
- ✅ **Table names**: "Posts", "Speakers", "Sessions" (exact spelling)

**After setup, your sync script will automatically:**
- Fetch all published records
- Generate MDX files with proper frontmatter
- Create beautiful pages on your website
- Handle updates automatically

---

## 🚀 **Ready to Go!**

Once you provide the API credentials, I'll:
1. Update your `.env` file
2. Test the sync
3. Show you how content flows from Airtable to your website

Your content team will then be able to manage the entire website through Airtable! 🎊 