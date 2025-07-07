---
title: "Dr. Sarah Chen"
company: "TechCorp AI Research"
role: "Director of AI Research"
bio: "Leading expert in deep learning and neural architecture search with over 10 years of experience in artificial intelligence research and development."
image: "/images/speakers/sarah-chen.jpg"
social:
  twitter: "@sarahchen_ai"
  linkedin: "sarah-chen-ai"
  website: "https://sarahchen.ai"
talks:
  - "The Future of Neural Architecture Search"
  - "Scaling Deep Learning in Production"
expertise: ["Deep Learning", "Neural Networks", "MLOps", "Computer Vision"]
---

# {{ title }}

**{{ role }}** at **{{ company }}**

{{ bio }}

## Biography

Dr. Sarah Chen is a renowned researcher and practitioner in the field of artificial intelligence, currently serving as the Director of AI Research at TechCorp. With a Ph.D. in Computer Science from Stanford University, she has published over 40 peer-reviewed papers in top-tier conferences including NeurIPS, ICML, and ICLR.

Her research focuses on:
- **Neural Architecture Search (NAS)**: Developing automated methods for designing optimal neural network architectures
- **Efficient Deep Learning**: Creating lightweight models that maintain high performance while reducing computational requirements
- **MLOps and Production AI**: Bridging the gap between research and real-world deployment

## Notable Achievements

- **2023**: Winner of the prestigious AI Innovation Award for breakthrough work in automated neural architecture design
- **2022**: Led the team that developed TechCorp's award-winning computer vision platform, now used by millions of users
- **2021**: Keynote speaker at the International Conference on Machine Learning (ICML)
- **2020**: Published influential paper "Efficient Neural Architecture Search via Parameter Sharing" (1000+ citations)

## Conference Presentations

{% for talk in talks %}
- {{ talk }}
{% endfor %}

## Research Interests

<div class="grid grid-cols-2 md:grid-cols-4 gap-4 my-8">
  {% for skill in expertise %}
  <div class="bg-ai-blue-50 text-ai-blue-800 px-3 py-2 rounded-lg text-center font-medium">
    {{ skill }}
  </div>
  {% endfor %}
</div>

## Connect

<div class="flex gap-4 my-8">
  {% if social.twitter %}
  <a href="https://twitter.com/{{ social.twitter | replace('@', '') }}" 
     class="btn btn-outline text-blue-600 border-blue-600 hover:bg-blue-600 hover:text-white">
    Twitter
  </a>
  {% endif %}
  
  {% if social.linkedin %}
  <a href="https://linkedin.com/in/{{ social.linkedin }}" 
     class="btn btn-outline text-blue-700 border-blue-700 hover:bg-blue-700 hover:text-white">
    LinkedIn
  </a>
  {% endif %}
  
  {% if social.website %}
  <a href="{{ social.website }}" 
     class="btn btn-outline text-gray-600 border-gray-600 hover:bg-gray-600 hover:text-white">
    Website
  </a>
  {% endif %}
</div>

---

<div class="bg-gray-50 p-6 rounded-lg mt-12">
  <h3 class="text-lg font-semibold mb-4">Don't miss Dr. Chen's presentations!</h3>
  <p class="text-gray-600 mb-4">
    Be sure to attend her keynote on "The Future of Neural Architecture Search" 
    and her technical workshop on "Scaling Deep Learning in Production."
  </p>
  <a href="/schedule/" class="btn btn-primary">View Full Schedule</a>
</div> 