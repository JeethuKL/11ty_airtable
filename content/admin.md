---
layout: base
title: Admin Sync
permalink: /admin/
---

<section class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-white to-gray-50">
  <div class="bg-white rounded-xl shadow-xl p-8 max-w-md w-full">
    <h1 class="text-2xl font-bold mb-6 text-center text-ai-blue-700">Admin: Airtable Sync Trigger</h1>
    <form id="syncForm" class="space-y-4">
      <input
        type="password"
        id="adminPassword"
        class="w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-ai-blue-500"
        placeholder="Enter admin password"
        required
      />
      <button
        type="submit"
        class="w-full bg-ai-blue-600 text-white font-semibold py-2 rounded hover:bg-ai-blue-700 transition"
      >
        Trigger Airtable Sync
      </button>
    </form>
    <div id="syncResult" class="mt-4 text-center text-sm"></div>
  </div>
</section>

<script>
document.getElementById('syncForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  const password = document.getElementById('adminPassword').value;
  const resultDiv = document.getElementById('syncResult');
  resultDiv.textContent = 'Triggering sync...';
  const res = await fetch('/api/sync', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ password })
  });
  const data = await res.json();
  if (data.ok) {
    resultDiv.textContent = '✅ Sync started! Check GitHub Actions for progress.';
    resultDiv.className = 'mt-4 text-center text-green-600 text-sm';
  } else {
    resultDiv.textContent = '❌ ' + (data.error || 'Sync failed');
    resultDiv.className = 'mt-4 text-center text-red-600 text-sm';
  }
});
</script> 