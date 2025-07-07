---
layout: base
title: "Speakers"
description: "Meet our distinguished speakers at AI Conference 2024"
permalink: /speakers/
---

# Our Distinguished Speakers

Join us for insights from world-renowned experts in artificial intelligence, machine learning, and emerging technologies.

<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mt-12">
  {% for speaker in collections.speakers %}
  <div class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow">
    {% if speaker.data.image %}
    <img src="{{ speaker.data.image }}" alt="{{ speaker.data.title }}" class="w-full h-48 object-cover">
    {% else %}
    <div class="w-full h-48 bg-gradient-to-br from-ai-blue-400 to-ai-purple-600 flex items-center justify-center">
      <span class="text-white text-4xl font-bold">{{ speaker.data.title | first }}</span>
    </div>
    {% endif %}
    
    <div class="p-6">
      <h3 class="text-xl font-bold text-gray-900 mb-2">{{ speaker.data.title }}</h3>
      <p class="text-ai-blue-600 font-medium mb-2">{{ speaker.data.role }}</p>
      <p class="text-gray-600 mb-4">{{ speaker.data.company }}</p>
      <p class="text-gray-700 text-sm mb-4 line-clamp-3">{{ speaker.data.bio }}</p>
      
      {% if speaker.data.expertise %}
      <div class="flex flex-wrap gap-2 mb-4">
        {% for skill in speaker.data.expertise | slice(0, 3) %}
        <span class="bg-ai-blue-50 text-ai-blue-700 text-xs px-2 py-1 rounded-full">{{ skill }}</span>
        {% endfor %}
        {% if speaker.data.expertise.length > 3 %}
        <span class="text-gray-500 text-xs">+{{ speaker.data.expertise.length - 3 }} more</span>
        {% endif %}
      </div>
      {% endif %}
      
      <a href="{{ speaker.url }}" class="btn btn-outline btn-sm w-full">View Profile</a>
    </div>
  </div>
  {% endfor %}
</div>

{% if collections.speakers.length === 0 %}
<div class="text-center py-12">
  <div class="bg-gray-50 rounded-lg p-8">
    <h3 class="text-xl font-semibold text-gray-900 mb-4">Speakers Coming Soon!</h3>
    <p class="text-gray-600 mb-6">We're finalizing our incredible lineup of speakers. Check back soon for updates!</p>
    <a href="/" class="btn btn-primary">Back to Home</a>
  </div>
</div>
{% endif %}

---

<div class="bg-gradient-to-r from-ai-blue-600 to-ai-purple-600 text-white rounded-lg p-8 mt-16">
  <div class="text-center">
    <h2 class="text-2xl font-bold mb-4">Want to Speak at AI Conference 2024?</h2>
    <p class="text-ai-blue-100 mb-6">
      We're always looking for passionate experts to share their knowledge with our community.
    </p>
    <a href="/contact/" class="btn btn-secondary">Submit Speaker Proposal</a>
  </div>
</div> 