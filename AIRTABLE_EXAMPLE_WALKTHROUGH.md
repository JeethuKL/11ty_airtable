# 🎯 Airtable Example Walkthrough

**Step-by-step guide**: Add content in Airtable → See it on your website

---

## 📊 Step 1: Create Your Airtable Base

### Setting Up the Posts Table

1. **Go to Airtable.com** → Create new base → Name it "AI Conference CMS"

2. **Create "Posts" table** with these exact field names:

```
┌─────────────────────────────────────────────────────────────┐
│ Posts Table Structure                                       │
├─────────────────────────────────────────────────────────────┤
│ title          │ Single line text │ ✅ Required           │
│ content        │ Long text        │ ✅ Required           │
│ date           │ Date             │ ✅ Required           │
│ author         │ Single line text │ Optional              │
│ tags           │ Multiple select  │ Optional              │
│ published      │ Checkbox         │ ✅ Required (default) │
│ featured       │ Checkbox         │ Optional              │
│ slug           │ Single line text │ Optional              │
└─────────────────────────────────────────────────────────────┘
```

### Setting Up Tags (Multiple Select)

For the `tags` field, add these options:
- `conference`
- `speakers`
- `ai`
- `technology`
- `announcement`
- `workshop`

---

## ✏️ Step 2: Add Sample Content

### Example Record 1: Conference Announcement

```
┌─────────────────────────────────────────────────────────────┐
│ Field         │ Value                                       │
├─────────────────────────────────────────────────────────────┤
│ title         │ AI Conference 2024 Registration Open       │
│ content       │ # Registration is Now Open!                │
│               │                                             │
│               │ We're excited to announce that             │
│               │ registration for **AI Conference 2024**    │
│               │ is now open!                               │
│               │                                             │
│               │ ## What to Expect                          │
│               │ - 50+ world-class speakers                 │
│               │ - 30+ technical sessions                   │
│               │ - Networking opportunities                 │
│               │                                             │
│               │ [Register Now](/register/)                 │
├─────────────────────────────────────────────────────────────┤
│ date          │ 2024-01-20                                 │
│ author        │ Conference Team                            │
│ tags          │ conference, announcement                   │
│ published     │ ✅ (checked)                               │
│ featured      │ ✅ (checked)                               │
│ slug          │ (leave empty - auto-generated)             │
└─────────────────────────────────────────────────────────────┘
```

### Example Record 2: Technical Blog Post

```
┌─────────────────────────────────────────────────────────────┐
│ Field         │ Value                                       │
├─────────────────────────────────────────────────────────────┤
│ title         │ Latest Trends in Neural Architecture       │
│ content       │ # Neural Architecture Search in 2024      │
│               │                                             │
│               │ The field of **Neural Architecture Search  │
│               │ (NAS)** has evolved rapidly...             │
│               │                                             │
│               │ ## Key Developments                        │
│               │ 1. Automated design optimization           │
│               │ 2. Efficient search algorithms             │
│               │ 3. Hardware-aware architectures            │
├─────────────────────────────────────────────────────────────┤
│ date          │ 2024-01-18                                 │
│ author        │ Dr. Sarah Chen                            │
│ tags          │ ai, technology                             │
│ published     │ ✅ (checked)                               │
│ featured      │ ❌ (unchecked)                             │
│ slug          │ neural-architecture-trends                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔑 Step 3: Get Your Credentials

### Get API Key
1. Go to https://airtable.com/create/tokens
2. Click "Create new token"
3. Name: "AI Conference Sync"
4. Add scope: `data.records:read`
5. Add your base to the token
6. Copy the token: `patXXXXXXXXXXXXXX.xxxxxxxxxxxxxxxx`

### Get Base ID
1. Go to https://airtable.com/api
2. Select your "AI Conference CMS" base
3. Copy Base ID: `appXXXXXXXXXXXXXX`

---

## ⚙️ Step 4: Configure Your Project

### Update .env file:
```bash
# Your actual credentials
AIRTABLE_API_KEY=patAbCd123456789.EfGhIjKlMnOpQrStUvWxYz
AIRTABLE_BASE_ID=appABC123DEF456
AIRTABLE_TABLE_NAME=Posts
```

---

## 🚀 Step 5: Run the Sync

```bash
# Install dependencies (if not done)
pip install -r requirements.txt

# Run the sync
python3 scripts/sync_airtable.py
```

### Expected Output:
```bash
2024-01-20 10:30:00 - INFO - Starting Airtable sync...
2024-01-20 10:30:01 - INFO - Syncing table: Posts -> posts
2024-01-20 10:30:02 - INFO - Fetched 2 records from Posts
2024-01-20 10:30:02 - INFO - Created/updated: content/posts/ai-conference-2024-registration-open.mdx
2024-01-20 10:30:02 - INFO - Created/updated: content/posts/neural-architecture-trends.mdx
2024-01-20 10:30:02 - INFO - Created/updated 2 files from Posts
2024-01-20 10:30:03 - INFO - Sync completed successfully. 2 files created/updated.
2024-01-20 10:30:03 - INFO - Committed changes: Auto-sync from Airtable - 2024-01-20 10:30:03
```

---

## 📄 Step 6: Check Generated Files

### File: `content/posts/ai-conference-2024-registration-open.mdx`
```markdown
---
title: "AI Conference 2024 Registration Open"
date: "2024-01-20"
author: "Conference Team"
tags:
  - conference
  - announcement
published: true
featured: true
generated_at: "2024-01-20T10:30:02.123Z"
layout: "post"
---

# Registration is Now Open!

We're excited to announce that registration for **AI Conference 2024** is now open!

## What to Expect
- 50+ world-class speakers
- 30+ technical sessions
- Networking opportunities

[Register Now](/register/)
```

### File: `content/posts/neural-architecture-trends.mdx`
```markdown
---
title: "Latest Trends in Neural Architecture"
date: "2024-01-18"
author: "Dr. Sarah Chen"
tags:
  - ai
  - technology
published: true
featured: false
slug: "neural-architecture-trends"
generated_at: "2024-01-20T10:30:02.456Z"
layout: "post"
---

# Neural Architecture Search in 2024

The field of **Neural Architecture Search (NAS)** has evolved rapidly...

## Key Developments
1. Automated design optimization
2. Efficient search algorithms
3. Hardware-aware architectures
```

---

## 🌐 Step 7: See Your Content Live

### Start Development Server
```bash
npm run dev
```

### Visit Your Pages:
- **Homepage**: http://localhost:8080/
- **Blog Posts**: 
  - http://localhost:8080/posts/ai-conference-2024-registration-open/
  - http://localhost:8080/posts/neural-architecture-trends/

---

## 🔄 Step 8: Making Updates

### Update Content in Airtable
1. Go back to your Airtable base
2. Edit the "AI Conference 2024 Registration Open" record
3. Change content to:
   ```markdown
   # Registration is Now Open - Early Bird Special!
   
   🎉 **Limited Time**: Save 30% with early bird pricing!
   
   We're excited to announce that registration for **AI Conference 2024** is now open!
   ```
4. Save the record

### Run Sync Again
```bash
python3 scripts/sync_airtable.py
```

### See Updated Content
- Refresh http://localhost:8080/posts/ai-conference-2024-registration-open/
- Content automatically updates!

---

## 📊 Advanced Example: Speakers Table

### Create Speakers Table
Add these fields to a new "Speakers" table:

```
title     → "Dr. Emily Watson"
bio       → "Leading researcher in computer vision..."
company   → "Stanford University"
role      → "Professor of Computer Science"
twitter   → "emilywatson_ai"
linkedin  → "emily-watson-stanford"
published → ✅ (checked)
```

### Update Script Configuration
Add to your `.env`:
```bash
AIRTABLE_SPEAKERS_TABLE=Speakers
```

### Run Sync
```bash
python3 scripts/sync_airtable.py
```

### Result
New file created: `content/speakers/dr-emily-watson.mdx`
Available at: http://localhost:8080/speakers/dr-emily-watson/

---

## 🎯 Real-World Workflow

### Daily Content Management
1. **Morning**: Content team adds new posts in Airtable
2. **Automatic**: GitHub Actions runs sync every 6 hours
3. **Afternoon**: New content appears on live website
4. **No Code**: Non-technical team members manage all content

### Content Types You Can Manage:
- ✅ **Blog Posts**: News, announcements, articles
- ✅ **Speaker Profiles**: Bios, contact info, talks
- ✅ **Session Details**: Workshops, presentations, schedules
- ✅ **Sponsors**: Company profiles, logos, descriptions
- ✅ **Custom Content**: Whatever your conference needs!

---

## 🎊 Success!

You now have a complete CMS workflow:

**Airtable** (Content Creation) → **Python Script** (Sync) → **11ty** (Static Site) → **Website** (Live Content)

Your content team can now manage the entire website without touching any code! 🚀 