import syntaxHighlight from "@11ty/eleventy-plugin-syntaxhighlight";
import markdownIt from "markdown-it";
import markdownItAttrs from "markdown-it-attrs";

export default async function(eleventyConfig) {
  // Set input and output directories
  eleventyConfig.setInputDirectory("content");
  eleventyConfig.setOutputDirectory("_site");
  
  // Add plugins
  eleventyConfig.addPlugin(syntaxHighlight);
  
  // Configure Markdown
  const markdownLibrary = markdownIt({
    html: true,
    breaks: true,
    linkify: true
  }).use(markdownItAttrs);
  
  eleventyConfig.setLibrary("md", markdownLibrary);
  
  // Add template formats (MDX support)
  eleventyConfig.setTemplateFormats(["md", "mdx", "njk", "html", "liquid"]);
  
  // Copy static assets
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/js");
  eleventyConfig.addPassthroughCopy("src/images");
  eleventyConfig.addPassthroughCopy("src/fonts");
  
  // Watch CSS files for changes
  eleventyConfig.addWatchTarget("src/css/");
  eleventyConfig.addWatchTarget("src/input.css");
  
  // Collections
  eleventyConfig.addCollection("posts", function(collectionApi) {
    return collectionApi.getFilteredByGlob("content/posts/*.md*");
  });
  
  eleventyConfig.addCollection("speakers", function(collectionApi) {
    return collectionApi.getFilteredByGlob("content/speakers/*.md*");
  });
  
  eleventyConfig.addCollection("sessions", function(collectionApi) {
    return collectionApi.getFilteredByGlob("content/sessions/*.md*");
  });
  
  // Global data
  eleventyConfig.addGlobalData("metadata", {
    title: "AI Conference 2024",
    description: "Join us for the premier AI Conference 2024 - featuring cutting-edge research, industry insights, and networking opportunities.",
    url: "https://ai-conference-2024.com", // Change this to your actual domain
    author: {
      name: "AI Conference Organization",
      email: "contact@ai-conference-2024.com"
    }
  });

  // Filters
  eleventyConfig.addFilter("dateDisplay", function(date) {
    return new Date(date).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  });
  
  eleventyConfig.addFilter("isoDate", function(date) {
    return new Date(date).toISOString();
  });

  eleventyConfig.addFilter("absoluteUrl", function(url, base) {
    try {
      return new URL(url, base).toString();
    } catch(e) {
      console.warn(`Warning: could not create absolute URL for ${url} with base ${base}. Returning relative URL.`);
      return url;
    }
  });
  
  // Transform to process CSS through Tailwind
  eleventyConfig.addTransform("postcss", async function(content, outputPath) {
    if (outputPath && outputPath.endsWith(".html")) {
      return content;
    }
    return content;
  });
  
  return {
    dir: {
      input: "content",
      includes: "../src/_includes",
      layouts: "../src/_layouts",
      output: "_site"
    },
    templateFormats: ["md", "mdx", "njk", "html", "liquid"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    dataTemplateEngine: "njk"
  };
} 