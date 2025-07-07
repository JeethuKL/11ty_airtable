---
layout: base
title: "Dr. Amanda Lee"
company: "OpenAI"
role: "Principal Research Engineer"
bio: "Expert in multimodal AI and computer vision, leading breakthrough research in vision-language models and their practical applications."
image: "/images/speakers/amanda-lee.jpg"
permalink: /speakers/dr-amanda-lee/
social:
  twitter: "@amanda_ai_vision"
  linkedin: "amanda-lee-ai"
  website: "https://amandaleecv.com"
talks:
  - "Multimodal AI: When Vision Meets Language"
  - "Computer Vision in Production: Lessons Learned"
expertise: ["Computer Vision", "Multimodal AI", "Deep Learning", "Production ML"]
---

# {{ title }}

**{{ role }}** at **{{ company }}**

{{ bio }}

## Biography

Dr. Amanda Lee is at the forefront of multimodal AI research, currently serving as Principal Research Engineer at OpenAI. Her groundbreaking work in vision-language models has shaped how AI systems understand and interact with both visual and textual information.

Before joining OpenAI, Dr. Lee spent 5 years at Meta's AI Research lab, where she led the computer vision team that developed several production systems used by billions of users. Her work bridges the gap between cutting-edge research and real-world applications.

## Research Contributions

Dr. Lee's research has fundamentally advanced several areas of AI:

- **Vision-Language Models**: Pioneering architectures that enable AI to understand images and text together
- **Multimodal Learning**: Developing methods for AI systems to learn from multiple types of data simultaneously
- **Production Computer Vision**: Scaling CV models to handle billions of images daily
- **Few-Shot Learning**: Creating models that can learn new visual concepts from minimal examples

## Notable Projects

- **2023**: Lead architect of OpenAI's CLIP-successor model with 40% improved accuracy
- **2022**: Developed Meta's real-time content moderation system processing 2B+ images daily
- **2021**: Co-created the VisionBERT architecture, now used in dozens of production systems
- **2020**: Published seminal work on "Cross-Modal Attention in Vision-Language Tasks"

## Speaking Topics

{% for talk in talks %}
- **{{ talk }}** - Deep dive into the latest research and practical implementation strategies
{% endfor %}

## Technical Expertise

<div class="grid grid-cols-2 md:grid-cols-4 gap-4 my-8">
  {% for skill in expertise %}
  <div class="bg-green-50 text-green-800 px-3 py-2 rounded-lg text-center font-medium">
    {{ skill }}
  </div>
  {% endfor %}
</div>

## Academic Background

- **Ph.D. in Computer Science** - Carnegie Mellon University (2018)
  - Thesis: "Learning Visual Representations through Cross-Modal Supervision"
- **M.S. in Computer Vision** - Stanford University (2014)
- **B.S. in Computer Science** - MIT (2012)

## Publications & Impact

Dr. Lee has authored over 35 peer-reviewed papers with more than 8,000 citations. Her most influential works include:

1. **"CLIP-V2: Enhanced Vision-Language Understanding"** (NeurIPS 2023) - 500+ citations
2. **"Scaling Multimodal Models to Production"** (ICML 2022) - 1,200+ citations
3. **"Few-Shot Learning in Computer Vision"** (CVPR 2021) - 2,100+ citations

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
     class="btn btn-outline text-purple-600 border-purple-600 hover:bg-purple-600 hover:text-white">
    Website
  </a>
  {% endif %}
</div>

---

<div class="bg-gradient-to-r from-green-50 to-blue-50 p-6 rounded-lg mt-12">
  <h3 class="text-lg font-semibold mb-4 text-green-800">Don't Miss These Sessions!</h3>
  <div class="grid md:grid-cols-2 gap-4">
    <div class="bg-white p-4 rounded shadow-sm">
      <h4 class="font-medium text-green-700">Multimodal AI Workshop</h4>
      <p class="text-sm text-gray-600 mt-1">Hands-on experience with vision-language models</p>
      <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded mt-2 inline-block">Day 1 • 3:00 PM</span>
    </div>
    <div class="bg-white p-4 rounded shadow-sm">
      <h4 class="font-medium text-blue-700">Production CV Panel</h4>
      <p class="text-sm text-gray-600 mt-1">Real-world deployment challenges and solutions</p>
      <span class="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded mt-2 inline-block">Day 2 • 11:00 AM</span>
    </div>
  </div>
  <a href="/schedule/" class="btn btn-primary mt-4">View Complete Schedule</a>
</div> 