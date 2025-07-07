# 🔄 Complete Sync Workflow Setup

**Your Airtable → Local → Git sync workflow is ready!**

---

## ✅ **What's Already Done**

- ✅ Git repository initialized  
- ✅ All project files committed
- ✅ .env file created from template
- ✅ Python dependencies installed
- ✅ 11ty development server running

---

## 🔧 **Step 1: Update Your Credentials**

Since you mentioned you've added your Airtable APIs, update your `.env` file:

```bash
# Edit your .env file with actual credentials
AIRTABLE_API_KEY=pat_YOUR_ACTUAL_TOKEN_HERE
AIRTABLE_BASE_ID=app_YOUR_ACTUAL_BASE_ID_HERE
```

**Example:**
```bash
AIRTABLE_API_KEY=patAbC123xyz789.1234567890abcdefghijklmnopqrstuvwxyz
AIRTABLE_BASE_ID=appABC123DEF456
```

---

## 🚀 **Step 2: Test Your First Sync**

### Manual Sync Test
```bash
# Test the Python sync script
python3 scripts/sync_airtable.py
```

**Expected Output:**
```
INFO - Starting Airtable sync...
INFO - Syncing table: Posts -> posts
INFO - Fetched X records from Posts
INFO - Created/updated: content/posts/your-post.mdx
INFO - Sync completed successfully. X files created/updated.
```

### Using NPM Script (Recommended)
```bash
# This runs sync + builds the site
npm run sync
```

### Check Results
```bash
# List generated content files
ls -la content/posts/
ls -la content/speakers/
ls -la content/sessions/
```

---

## 🌐 **Step 3: See Your Content Live**

Your development server should already be running at **http://localhost:8080/**

If not, start it:
```bash
npm run dev
```

**Visit these URLs to see your Airtable content:**
- Homepage: http://localhost:8080/
- Posts: http://localhost:8080/posts/
- Speakers: http://localhost:8080/speakers/
- About: http://localhost:8080/about/

---

## 🔄 **Step 4: Complete Workflow Test**

### 1. Add Content in Airtable
- Add a new record to your "Posts" table
- Set `published` = true

### 2. Sync to Local
```bash
npm run sync
```

### 3. Check Git Changes
```bash
git status
git diff
```

### 4. Commit Changes
```bash
git add .
git commit -m "Sync from Airtable: New content added"
```

---

## 🤖 **Step 5: Automatic Sync (Optional)**

### GitHub Actions (Already Configured!)
Your project includes `.github/workflows/sync.yml` which will:
- Run sync every 6 hours
- Sync on push to main branch
- Build and deploy automatically

### To Enable:
1. Push to GitHub:
```bash
git remote add origin https://github.com/yourusername/your-repo.git
git branch -M main
git push -u origin main
```

2. Add Repository Secrets:
   - Go to GitHub → Settings → Secrets
   - Add `AIRTABLE_API_KEY`
   - Add `AIRTABLE_BASE_ID`

---

## 📋 **Daily Workflow**

### For Content Team (Airtable):
1. **Add/Edit content** in Airtable tables
2. **Set published = true** when ready
3. **Content appears** on website automatically (within 6 hours)

### For Developers (Manual Sync):
```bash
# Pull latest Airtable content
npm run sync

# See changes locally
npm run dev

# Commit and push
git add .
git commit -m "Content update from Airtable"
git push
```

---

## 🎯 **Content Management Flow**

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│  Airtable   │───▶│ Python Script│───▶│ Local Files │───▶│   Website    │
│   Tables    │    │     Sync     │    │  (MDX/Git)  │    │    (Live)    │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
     ▲                     ▲                  ▲                   ▲
     │                     │                  │                   │
 Add Content          npm run sync       git commit         Auto Deploy
```

---

## 🚨 **Troubleshooting**

### "API Key Invalid"
```bash
# Check your .env file
cat .env | grep AIRTABLE

# Verify token has data.records:read permission
```

### "No Records Found"
```bash
# Check table names match exactly:
# - Posts (not posts)
# - Speakers (not speakers)  
# - Sessions (not sessions)

# Verify records have published=true
```

### "Module Not Found"
```bash
# Reinstall Python dependencies
pip3 install -r requirements.txt
```

### Sync Script Errors
```bash
# Run with debug info
python3 scripts/sync_airtable.py

# Check logs
tail -f sync_airtable.log
```

---

## 🎊 **Success Checklist**

- ✅ Airtable tables created with correct field names
- ✅ API credentials added to .env
- ✅ Manual sync works: `npm run sync`
- ✅ Content appears on website: http://localhost:8080/
- ✅ Git tracking changes: `git status` shows new files
- ✅ Ready for team: Non-technical users can manage content!

---

## 🔗 **Key Commands Reference**

```bash
# Sync Airtable → Local
npm run sync

# Start development server  
npm run dev

# Build for production
npm run build

# Check sync status
python3 scripts/sync_airtable.py

# Git workflow
git add .
git commit -m "Content update"
git push
```

Your CMS is ready! Content team can now manage the entire website through Airtable! 🚀 