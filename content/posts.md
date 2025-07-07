---
layout: base
title: "Blog"
description: "Latest news and updates from the AI Conference"
permalink: /posts/
---

# Blog Posts

{% if collections.posts and collections.posts.length > 0 %}
<div class="grid md:grid-cols-2 gap-8 mt-8">
  {% for post in collections.posts %}
    {% if post.data.published !== false %}
      <article class="bg-white rounded-lg shadow-lg p-6 mb-6 hover:shadow-xl transition-shadow duration-200">
        <h2 class="text-2xl font-bold mb-3">
          <a href="{{ post.url }}" class="text-gray-900 hover:text-ai-blue-600 transition-colors">{{ post.data.title }}</a>
        </h2>
        <div class="flex items-center text-gray-600 text-sm mb-3">
          {% if post.data.author %}
            <span class="mr-3">By {{ post.data.author }}</span>
          {% endif %}
          {% if post.data.date %}
            <time datetime="{{ post.data.date }}" class="mr-3">{{ post.data.date | dateDisplay }}</time>
          {% endif %}
        </div>
        {% if post.data.excerpt %}
          <p class="text-gray-600 mb-4">{{ post.data.excerpt }}</p>
        {% endif %}
        {% if post.data.tags %}
          <div class="flex flex-wrap gap-2 mb-4">
            {% for tag in post.data.tags %}
              <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">#{{ tag }}</span>
            {% endfor %}
          </div>
        {% endif %}
        <a href="{{ post.url }}" class="inline-block bg-ai-blue-600 text-white px-4 py-2 rounded hover:bg-ai-blue-700 transition-colors">Read More →</a>
      </article>
    {% endif %}
  {% endfor %}
</div>
{% else %}
<div class="text-center py-12">
  <h3 class="text-xl font-semibold text-gray-700 mb-4">Debug Information</h3>
  <p class="text-gray-600 mb-4">No blog posts found in the collection.</p>
  <div class="bg-gray-100 p-4 rounded-lg text-left">
    <p class="font-mono text-sm">Posts directory contents:</p>
    <pre class="text-xs mt-2">
    {% for post in collections.all %}
      {{ post.inputPath }} ({{ post.data.published }})
    {% endfor %}
    </pre>
  </div>
</div>
{% endif %} 