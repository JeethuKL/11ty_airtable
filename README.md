# AI Conference CMS (Airtable + 11ty)

This project is a static website for an AI Conference, powered by [11ty (Eleventy)](https://www.11ty.dev/) and using [Airtable](https://airtable.com/) as a headless CMS. All content (speakers, posts, sessions) is managed in Airtable and synced to local markdown files for static site generation.

---

## 🚀 How It Works

- **Airtable is your CMS**: All content is managed in Airtable tables (Speakers, Posts, Sessions).
- **Sync script**: Run `npm run sync` to pull the latest data from Airtable and generate markdown files in the `content/` directory.
- **11ty builds the site**: Run `npm run dev` to start the local server and see your site at [http://localhost:8080](http://localhost:8080).
- **One-way sync**: Changes in Airtable overwrite local files. Editing local markdown files will NOT update Airtable and will be overwritten on next sync.

---

## 🛠️ Setup

1. **Clone the repo & install dependencies**
   ```bash
   git clone <your-repo-url>
   cd CMS_Airtable
   npm install
   pip3 install -r requirements.txt
   ```

2. **Configure Airtable**
   - Create a base with tables: `Speakers`, `Posts`, `Sessions`.
   - Add your fields (see below for mapping).
   - Get your API key from https://airtable.com/account
   - Find your Base ID from the Airtable API docs URL.

3. **Create a `.env` file**
   ```env
   AIRTABLE_API_KEY=patXXXXXXXXXXXXXX
   AIRTABLE_BASE_ID=appXXXXXXXXXXXXXX
   AIRTABLE_TABLE_NAME=Posts
   ```

4. **Sync your content**
   ```bash
   npm run sync
   ```

5. **Run the local dev server**
   ```bash
   npm run dev
   # Visit http://localhost:8080
   ```

---

## 🗂️ Airtable Field Mapping

**Speakers Table:**
- `Speaker Name` → Speaker name/title
- `Company and Job` → Company and role (split on " - ")
- `Presentation Abstract` → Bio/description
- `Presentation Date` → Date
- `Speaker Social Media` → Social media info (string)
- `Presentation Summary` → Summary (optional)

**Posts/Sessions:**
- Add fields as needed. The sync script will flatten all values to strings for YAML compatibility.

---

## 🔄 Content Workflow

- **Edit content in Airtable** (recommended)
- Run `npm run sync` to update local markdown files
- Run/build the site with 11ty
- **Do NOT edit markdown files directly** (changes will be overwritten on next sync)

---

## 🧩 Customization
- To add new fields, update your Airtable and (if needed) adjust the sync script's field mapping.
- To change the site design, edit the 11ty templates in `src/`.

---

## 🧹 Clean Codebase
- All test/debug scripts and sample/demo content have been removed.
- Only production code, config, and your real content remain.

---

## 📦 Scripts
- `npm run sync` — Sync Airtable data to local markdown
- `npm run dev` — Start 11ty dev server
- `npm run build` — Build static site

---

## ❓ FAQ
- **Q: Can I edit markdown files directly?**
  - A: You can, but changes will be lost on next sync. Always edit in Airtable.
- **Q: Can I push changes from markdown to Airtable?**
  - A: Not with this setup. This is a one-way sync (Airtable → site).

---

## 📝 License
MIT or your preferred license. 