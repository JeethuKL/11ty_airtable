# Sample Airtable Data for AI Conference 2024

Copy this data into your Airtable base to match the speakers we just created locally.

## 📋 Table 1: Speakers

**Create these fields in your Speakers table:**
- `title` (Single line text)
- `company` (Single line text) 
- `role` (Single line text)
- `bio` (Long text)
- `image` (Single line text)
- `social_twitter` (Single line text)
- `social_linkedin` (Single line text) 
- `social_website` (Single line text)
- `social_github` (Single line text)
- `talks` (Multiple select)
- `expertise` (Multiple select)
- `status` (Single select: Active, Confirmed, Pending)

**Records to add:**

### Record 1: Dr. Sarah Chen
- **title**: Dr. Sarah Chen
- **company**: TechCorp AI Research
- **role**: Director of AI Research
- **bio**: Leading expert in deep learning and neural architecture search with over 10 years of experience in artificial intelligence research and development.
- **image**: /images/speakers/sarah-chen.jpg
- **social_twitter**: @sarahchen_ai
- **social_linkedin**: sarah-chen-ai
- **social_website**: https://sarahchen.ai
- **social_github**: (leave empty)
- **talks**: The Future of Neural Architecture Search, Scaling Deep Learning in Production
- **expertise**: Deep Learning, Neural Networks, MLOps, Computer Vision
- **status**: Active

### Record 2: Dr. Michael Rodriguez
- **title**: Dr. Michael Rodriguez
- **company**: Google DeepMind
- **role**: Senior Research Scientist
- **bio**: Pioneering researcher in reinforcement learning and AI safety, with groundbreaking work in large language models and autonomous systems.
- **image**: /images/speakers/michael-rodriguez.jpg
- **social_twitter**: @mrodriguez_ai
- **social_linkedin**: michael-rodriguez-ai
- **social_website**: (leave empty)
- **social_github**: mrodriguez
- **talks**: The Ethics of AI: Building Responsible Systems, Reinforcement Learning in Real-World Applications
- **expertise**: Reinforcement Learning, AI Safety, Large Language Models, Ethics in AI
- **status**: Active

### Record 3: Dr. Amanda Lee
- **title**: Dr. Amanda Lee
- **company**: OpenAI
- **role**: Principal Research Engineer
- **bio**: Expert in multimodal AI and computer vision, leading breakthrough research in vision-language models and their practical applications.
- **image**: /images/speakers/amanda-lee.jpg
- **social_twitter**: @amanda_ai_vision
- **social_linkedin**: amanda-lee-ai
- **social_website**: https://amandaleecv.com
- **social_github**: (leave empty)
- **talks**: Multimodal AI: When Vision Meets Language, Computer Vision in Production: Lessons Learned
- **expertise**: Computer Vision, Multimodal AI, Deep Learning, Production ML
- **status**: Active

---

## 📋 Table 2: Sessions

**Create these fields in your Sessions table:**
- `title` (Single line text)
- `description` (Long text)
- `speaker` (Link to another record - Speakers table)
- `date` (Date)
- `time` (Single line text)
- `duration` (Number)
- `type` (Single select: Keynote, Workshop, Panel, Talk)
- `track` (Single select: AI Research, Industry Applications, Ethics & Safety, Computer Vision)
- `location` (Single line text)
- `capacity` (Number)
- `status` (Single select: Scheduled, Confirmed, Cancelled)

**Records to add:**

### Record 1: The Future of Neural Architecture Search
- **title**: The Future of Neural Architecture Search
- **description**: Explore cutting-edge developments in automated neural network design and the future of architecture optimization.
- **speaker**: Dr. Sarah Chen (link to speaker record)
- **date**: 2024-10-15
- **time**: 09:00 AM
- **duration**: 45
- **type**: Keynote
- **track**: AI Research
- **location**: Main Auditorium
- **capacity**: 500
- **status**: Confirmed

### Record 2: The Ethics of AI: Building Responsible Systems
- **title**: The Ethics of AI: Building Responsible Systems
- **description**: A comprehensive look at ethical frameworks for AI development and deployment in real-world scenarios.
- **speaker**: Dr. Michael Rodriguez (link to speaker record)
- **date**: 2024-10-15
- **time**: 10:30 AM
- **duration**: 60
- **type**: Keynote
- **track**: Ethics & Safety
- **location**: Main Auditorium
- **capacity**: 500
- **status**: Confirmed

### Record 3: Multimodal AI Workshop
- **title**: Multimodal AI: When Vision Meets Language
- **description**: Hands-on workshop exploring the latest in vision-language models and their practical applications.
- **speaker**: Dr. Amanda Lee (link to speaker record)
- **date**: 2024-10-15
- **time**: 02:00 PM
- **duration**: 120
- **type**: Workshop
- **track**: Computer Vision
- **location**: Workshop Room A
- **capacity**: 50
- **status**: Confirmed

### Record 4: Scaling Deep Learning in Production
- **title**: Scaling Deep Learning in Production
- **description**: Practical insights and lessons learned from deploying deep learning models at scale.
- **speaker**: Dr. Sarah Chen (link to speaker record)
- **date**: 2024-10-16
- **time**: 11:00 AM
- **duration**: 45
- **type**: Talk
- **track**: Industry Applications
- **location**: Room B
- **capacity**: 200
- **status**: Confirmed

### Record 5: Reinforcement Learning in Real-World Applications
- **title**: Reinforcement Learning in Real-World Applications
- **description**: Deep dive into applying reinforcement learning techniques to solve complex real-world problems.
- **speaker**: Dr. Michael Rodriguez (link to speaker record)
- **date**: 2024-10-16
- **time**: 02:30 PM
- **duration**: 90
- **type**: Workshop
- **track**: AI Research
- **location**: Workshop Room B
- **capacity**: 75
- **status**: Confirmed

### Record 6: Computer Vision in Production
- **title**: Computer Vision in Production: Lessons Learned
- **description**: Real-world deployment challenges and solutions for computer vision systems at scale.
- **speaker**: Dr. Amanda Lee (link to speaker record)
- **date**: 2024-10-16
- **time**: 04:00 PM
- **duration**: 45
- **type**: Panel
- **track**: Computer Vision
- **location**: Room A
- **capacity**: 150
- **status**: Confirmed

---

## 📋 Table 3: Posts

**Create these fields in your Posts table:**
- `title` (Single line text)
- `content` (Long text)
- `excerpt` (Long text)
- `author` (Single line text)
- `date` (Date)
- `published` (Checkbox)
- `featured` (Checkbox)
- `tags` (Multiple select)
- `image` (Single line text)
- `category` (Single select: News, Speaker Spotlight, Industry Insights, Conference Updates)

**Records to add:**

### Record 1: Welcome to AI Conference 2024
- **title**: Welcome to AI Conference 2024: Where Innovation Meets Intelligence
- **content**: We're thrilled to announce the launch of AI Conference 2024, the premier gathering for artificial intelligence researchers, practitioners, and enthusiasts. This year's conference promises to be our most exciting yet, featuring groundbreaking research presentations, hands-on workshops, and unparalleled networking opportunities. Join us as we explore the cutting edge of AI technology and its transformative impact across industries.
- **excerpt**: Join us for the premier AI Conference 2024 - featuring cutting-edge research, industry insights, and networking opportunities with the world's leading AI experts.
- **author**: Conference Team
- **date**: 2024-08-01
- **published**: ✓ (checked)
- **featured**: ✓ (checked)
- **tags**: Conference, AI, Machine Learning, Welcome
- **image**: /images/posts/welcome-banner.jpg
- **category**: Conference Updates

### Record 2: Speaker Spotlight
- **title**: Speaker Spotlight: Dr. Sarah Chen on the Future of Neural Architecture Search
- **content**: We're excited to spotlight Dr. Sarah Chen, Director of AI Research at TechCorp, who will be delivering a keynote on "The Future of Neural Architecture Search" at AI Conference 2024. Dr. Chen's groundbreaking work in automated neural network design has revolutionized how we approach model architecture optimization. With over 40 published papers and numerous industry applications, her insights into the future of AI model design are not to be missed.
- **excerpt**: Meet Dr. Sarah Chen, our keynote speaker who will share insights on the revolutionary field of neural architecture search and its impact on AI development.
- **author**: Sarah Johnson
- **date**: 2024-08-15
- **published**: ✓ (checked)
- **featured**: (unchecked)
- **tags**: Speaker Spotlight, Neural Networks, Deep Learning, Keynote
- **image**: /images/posts/sarah-chen-spotlight.jpg
- **category**: Speaker Spotlight

### Record 3: AI Ethics Panel
- **title**: Building Responsible AI: Ethics Panel Discussion
- **content**: As AI systems become more powerful and prevalent, the importance of ethical considerations in AI development cannot be overstated. Our ethics panel, featuring Dr. Michael Rodriguez from Google DeepMind and other leading experts, will explore frameworks for responsible AI development, addressing bias, fairness, and accountability in AI systems.
- **excerpt**: Explore the critical topic of AI ethics with our expert panel, discussing frameworks for responsible AI development and deployment.
- **author**: Ethics Committee
- **date**: 2024-09-01
- **published**: ✓ (checked)
- **featured**: (unchecked)
- **tags**: Ethics, AI Safety, Panel Discussion, Responsible AI
- **image**: /images/posts/ethics-panel.jpg
- **category**: Industry Insights

---

## 🔧 Quick Setup Instructions

1. **Create your Airtable base** with three tables: `Speakers`, `Sessions`, and `Posts`
2. **Add the fields** as specified above for each table
3. **Copy the sample data** into each table
4. **Set up the link** between Sessions and Speakers tables
5. **Update your .env file** with the correct Airtable API key and Base ID
6. **Run the sync** with `npm run sync`

## 🔗 Field Relationships

- **Sessions → Speakers**: Each session can link to one speaker
- **Posts**: Independent table for blog content
- **Multiple select fields**: Add options as you enter data (Airtable will create them automatically)

## 📝 Notes

- **Images**: The image paths in this sample data are placeholder paths. You can either:
  - Add actual images to your `src/images/` folder with these names
  - Update the image paths to point to actual images
  - Leave them as placeholders (the site will show default gradients)
  
- **Dates**: All dates are set for October 2024. Update them to your actual conference dates.

- **Capacity and Duration**: Numbers are in standard units (people for capacity, minutes for duration).

Once you add this data to Airtable and run `npm run sync`, your speakers section will be fully populated! 