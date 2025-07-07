# AI Conference 2024 - Static Website

A modern static website for AI Conference 2024 built with [Eleventy (11ty)](https://www.11ty.dev/), [Tailwind CSS](https://tailwindcss.com/), and integrated with [Airtable](https://airtable.com/) for content management.

## 🚀 Features

- **Static Site Generation**: Fast, secure, and SEO-friendly using Eleventy
- **Modern Styling**: Beautiful, responsive design with Tailwind CSS
- **Content Management**: Dynamic content sync from Airtable
- **Blog Support**: MDX format with YAML frontmatter
- **Automated Deployment**: GitHub Actions for continuous integration
- **Performance Optimized**: Minimal JavaScript, optimized images, fast loading
- **Accessibility**: WCAG 2.1 compliant, keyboard navigation, screen reader support
- **Mobile First**: Responsive design that works on all devices

## 📂 Project Structure

```
ai-conference-cms/
├── content/                    # Content files (synced from Airtable)
│   ├── posts/                 # Blog posts
│   ├── speakers/              # Speaker profiles
│   ├── sessions/              # Conference sessions
│   └── index.md               # Homepage content
├── src/                       # Source files
│   ├── _includes/             # Reusable components
│   ├── _layouts/              # Page layouts
│   ├── css/                   # Compiled CSS
│   ├── js/                    # JavaScript files
│   └── input.css              # Tailwind CSS source
├── scripts/                   # Python sync scripts
│   └── sync_airtable.py       # Airtable sync script
├── _site/                     # Generated site (git ignored)
├── .eleventy.js               # Eleventy configuration
├── tailwind.config.js         # Tailwind CSS configuration
├── postcss.config.js          # PostCSS configuration
├── package.json               # Node.js dependencies
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🛠️ Tech Stack

### Core Technologies
- **[Eleventy (11ty)](https://www.11ty.dev/)** - Static site generator
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **[Airtable](https://airtable.com/)** - Content management system
- **[Python](https://python.org/)** - Sync script for Airtable integration

### Development Tools
- **[PostCSS](https://postcss.org/)** - CSS processing
- **[Autoprefixer](https://github.com/postcss/autoprefixer)** - CSS vendor prefixing
- **[GitHub Actions](https://github.com/features/actions)** - CI/CD pipeline
- **[Netlify](https://netlify.com/)** or **[Vercel](https://vercel.com/)** - Deployment platform

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18.0.0 or higher
- **Python** 3.8 or higher
- **Git** for version control
- **Airtable Account** for content management

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-conference-cms.git
cd ai-conference-cms
```

### 2. Install Dependencies

#### Node.js Dependencies
```bash
npm install
```

#### Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Copy the environment example file and configure your variables:

```bash
cp env.example .env
```

Edit `.env` with your Airtable credentials:

```env
# Airtable Configuration
AIRTABLE_API_KEY=your_airtable_api_key_here
AIRTABLE_BASE_ID=your_airtable_base_id_here
AIRTABLE_TABLE_NAME=Posts

# Optional: Additional tables
AIRTABLE_SPEAKERS_TABLE=Speakers
AIRTABLE_SESSIONS_TABLE=Sessions
```

### 4. Airtable Setup

Create an Airtable base with the following tables and fields:

#### Posts Table
- `title` (Single line text)
- `slug` (Single line text)
- `content` (Long text)
- `date` (Date)
- `author` (Single line text)
- `published` (Checkbox)
- `tags` (Multiple select)
- `category` (Single select)
- `excerpt` (Long text)
- `featured` (Checkbox)

#### Speakers Table (Optional)
- `speaker_name` (Single line text)
- `bio` (Long text)
- `company` (Single line text)
- `twitter` (Single line text)
- `linkedin` (Single line text)
- `published` (Checkbox)

#### Sessions Table (Optional)
- `title` (Single line text)
- `content` (Long text)
- `session_time` (Date)
- `session_track` (Single select)
- `speaker_name` (Single line text)
- `published` (Checkbox)

### 5. Sync Content from Airtable

```bash
# Run the sync script
python scripts/sync_airtable.py

# Or use the npm script
npm run sync
```

### 6. Build and Serve

#### Development Server
```bash
# Start development server with live reload
npm run dev

# Build CSS and start server
npm run build:css & npm run dev
```

#### Production Build
```bash
# Build the site
npm run build

# Preview the built site
npx @11ty/eleventy --serve --dir=_site
```

## 📝 Content Management

### Airtable Workflow

1. **Add Content**: Create new records in your Airtable base
2. **Set Published**: Check the "published" checkbox for content to appear on site
3. **Sync**: Run the sync script or wait for automatic sync (if using GitHub Actions)
4. **Deploy**: Changes are automatically built and deployed

### Content Types

#### Blog Posts
- Written in Markdown with YAML frontmatter
- Automatically generated from Airtable "Posts" table
- Support for tags, categories, and featured posts
- SEO-optimized with meta descriptions and social sharing

#### Speakers
- Speaker profiles with bio, photo, and social links
- Automatically generated speaker pages
- Integration with session scheduling

#### Sessions
- Conference session details
- Schedule integration
- Speaker association

### Manual Content Creation

You can also create content manually by adding `.md` or `.mdx` files to the `content/` directory:

```markdown
---
title: "Your Post Title"
date: "2024-01-15"
author: "Your Name"
tags: ["ai", "conference"]
layout: "post"
---

Your content goes here...
```

## 🎨 Styling and Customization

### Tailwind CSS

The site uses Tailwind CSS for styling. Key files:

- `tailwind.config.js` - Tailwind configuration and custom theme
- `src/input.css` - Main CSS file with Tailwind directives
- Custom color palette for AI Conference branding

### Customizing Colors

Edit `tailwind.config.js` to modify the color scheme:

```javascript
theme: {
  extend: {
    colors: {
      'ai-blue': {
        // Your custom blue colors
      },
      'ai-purple': {
        // Your custom purple colors
      }
    }
  }
}
```

### Layouts and Components

- `src/_layouts/` - Page layouts (base, post, etc.)
- `src/_includes/` - Reusable components (header, footer, etc.)

## 🚀 Deployment

### GitHub Actions (Recommended)

The repository includes a GitHub Actions workflow that:

1. Automatically syncs content from Airtable
2. Builds the site
3. Deploys to GitHub Pages or Netlify
4. Runs on schedule and on code changes

#### Setup GitHub Actions

1. Add secrets to your GitHub repository:
   - `AIRTABLE_API_KEY`
   - `AIRTABLE_BASE_ID`
   - `AIRTABLE_TABLE_NAME`

2. Enable GitHub Pages in repository settings

3. The workflow will run automatically

### Manual Deployment

#### Netlify
```bash
# Build the site
npm run build

# Deploy to Netlify (install Netlify CLI first)
netlify deploy --prod --dir=_site
```

#### Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

#### GitHub Pages
```bash
# Build the site
npm run build

# Deploy to gh-pages branch
npm install -g gh-pages
gh-pages -d _site
```

## 🛠️ Development

### NPM Scripts

```bash
npm run dev          # Start development server
npm run build        # Build production site
npm run sync         # Sync content from Airtable
npm run build:css    # Build CSS with Tailwind
npm run clean        # Clean build directory
```

### Adding New Features

1. **New Page Types**: Add new layouts in `src/_layouts/`
2. **New Components**: Add includes in `src/_includes/`
3. **New Content Types**: Modify the sync script and Eleventy config
4. **Styling Changes**: Update Tailwind classes or add custom CSS

### Troubleshooting

#### Common Issues

1. **Airtable Sync Failing**
   - Check API key and base ID
   - Verify table and field names
   - Check network connectivity

2. **Build Errors**
   - Clear node_modules and reinstall: `rm -rf node_modules && npm install`
   - Check for syntax errors in templates
   - Verify all dependencies are installed

3. **Styling Issues**
   - Rebuild CSS: `npm run build:css`
   - Check Tailwind configuration
   - Clear browser cache

## 📋 Content Guidelines

### Blog Posts
- Use clear, descriptive titles
- Include excerpt for better SEO
- Add relevant tags and categories
- Use proper heading hierarchy (H2, H3, etc.)

### Speaker Profiles
- Professional headshots (square aspect ratio)
- Concise but informative bios
- Include social media links
- Mention key accomplishments

### Sessions
- Clear session titles and descriptions
- Include time and track information
- Link to speaker profiles
- Add learning objectives

## 🔧 Configuration

### Eleventy Configuration

Key settings in `.eleventy.js`:

- Input directory: `content/`
- Output directory: `_site/`
- Template formats: Markdown, Nunjucks, HTML
- Collections for posts, speakers, sessions

### Tailwind Configuration

Custom theme settings in `tailwind.config.js`:

- AI Conference color palette
- Typography plugin for blog content
- Custom component classes
- Responsive breakpoints

## 📈 Performance

### Optimization Features

- **Static Generation**: Pre-built HTML for fast loading
- **Minimal JavaScript**: Only essential JS for interactivity
- **Optimized CSS**: Purged unused styles in production
- **Image Optimization**: WebP format with fallbacks
- **Caching**: Aggressive caching for static assets

### Performance Monitoring

The GitHub Actions workflow includes Lighthouse CI for performance testing on pull requests.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Add tests if applicable
5. Commit your changes: `git commit -am 'Add new feature'`
6. Push to the branch: `git push origin feature/new-feature`
7. Create a Pull Request

### Code Style

- Use Prettier for code formatting
- Follow Tailwind CSS best practices
- Write semantic HTML
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♀️ Support

- **Documentation**: Check this README and inline code comments
- **Issues**: Report bugs and request features via GitHub Issues
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Email**: Contact the organizing committee at tech@aiconference2024.com

## 🎯 Roadmap

### Upcoming Features

- [ ] Multi-language support
- [ ] Advanced search functionality
- [ ] Newsletter subscription integration
- [ ] Social media feed integration
- [ ] Progressive Web App (PWA) features
- [ ] Advanced analytics dashboard

### Version History

- **v1.0.0** - Initial release with basic CMS integration
- **v1.1.0** - Added speaker and session management
- **v1.2.0** - GitHub Actions automation
- **v2.0.0** - Complete redesign with Tailwind CSS

---

**Built with ❤️ for the AI community**

For more information about AI Conference 2024, visit [aiconference2024.com](https://aiconference2024.com) 