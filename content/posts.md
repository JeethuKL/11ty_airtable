---
layout: base
title: "Blog"
description: "Latest news and updates from the AI Conference"
permalink: /posts/
---

# Blog

<div class="grid md:grid-cols-2 gap-8 mt-8">
  {% for post in collections.posts | reverse %}
  <div class="bg-white rounded-lg shadow p-6 mb-6">
    <h2 class="text-xl font-bold mb-2">
      <a href="{{ post.url }}">{{ post.data.title }}</a>
    </h2>
    <p class="text-gray-600 text-sm mb-2">{{ post.data.date | dateDisplay }}</p>
    <p class="mb-4">{{ post.data.excerpt }}</p>
    <a href="{{ post.url }}" class="btn btn-outline btn-sm">Read More</a>
  </div>
  {% endfor %}
</div>

{% if collections.posts.length === 0 %}
<p>No blog posts yet. Add some in Airtable!</p>
{% endif %} 