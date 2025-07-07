---
layout: base
title: "Blog"
description: "Latest news and updates from the AI Conference"
permalink: /posts/
---

<section class="bg-gradient-to-b from-white to-gray-50 min-h-screen py-16">
  <div class="max-w-5xl mx-auto px-4">
    <h1 class="text-5xl font-extrabold text-ai-blue-700 mb-2 text-center drop-shadow-lg">Blog Posts</h1>
    <p class="text-lg text-gray-500 mb-12 text-center">Latest news and updates from the AI Conference</p>
    {% if collections.posts and collections.posts.length > 0 %}
    <div class="grid md:grid-cols-2 gap-10">
      {% for post in collections.posts %}
        {% if post.data.published !== false %}
        <article class="bg-white rounded-2xl shadow-xl hover:shadow-2xl transition-shadow duration-300 border border-gray-100 p-8 flex flex-col justify-between h-full">
          <div>
            <h2 class="text-2xl font-bold mb-2 text-ai-blue-800 hover:text-ai-blue-600 transition-colors">
              <a href="{{ post.url }}">{{ post.data.title }}</a>
            </h2>
            <div class="flex items-center text-gray-400 text-xs mb-3 gap-2">
              {% if post.data.author %}
                <span class="inline-flex items-center px-2 py-1 bg-ai-blue-100 text-ai-blue-700 rounded-full font-medium">{{ post.data.author }}</span>
              {% endif %}
              {% if post.data.date %}
                <span class="inline-flex items-center px-2 py-1 bg-gray-100 text-gray-600 rounded-full font-medium">{{ post.data.date | dateDisplay }}</span>
              {% endif %}
            </div>
            {% if post.data.excerpt %}
              <p class="text-gray-600 mb-4">{{ post.data.excerpt }}</p>
            {% endif %}
            {% if post.data.tags %}
              <div class="flex flex-wrap gap-2 mb-4">
                {% for tag in post.data.tags %}
                  <span class="text-xs bg-ai-purple-100 text-ai-purple-700 px-2 py-1 rounded-full font-semibold">#{{ tag }}</span>
                {% endfor %}
              </div>
            {% endif %}
          </div>
          <a href="{{ post.url }}" class="inline-block mt-4 bg-ai-blue-600 text-white px-5 py-2 rounded-lg font-semibold shadow hover:bg-ai-blue-700 transition-colors">Read More →</a>
        </article>
        {% endif %}
      {% endfor %}
    </div>
    {% else %}
    <div class="text-center py-12">
      <h3 class="text-xl font-semibold text-gray-700 mb-4">No blog posts found</h3>
      <p class="text-gray-600 mb-4">Check back soon for new content!</p>
    </div>
    {% endif %}
  </div>
</section> 