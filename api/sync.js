export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();

  // Simple static password check
  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch {}
  }
  const { password } = body || {};
  if (password !== '12345678') {
    return res.status(401).json({ ok: false, error: 'Unauthorized' });
  }

  // GitHub repo and token
  const repo = 'JeethuKL/11ty_airtable'; // <-- CHANGE THIS
  const githubToken = process.env.GH_PAT; // Set this in Vercel dashboard

  // Trigger the workflow
  const response = await fetch(`https://api.github.com/repos/${repo}/dispatches`, {
    method: 'POST',
    headers: {
      'Authorization': `token ${githubToken}`,
      'Accept': 'application/vnd.github.everest-preview+json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ event_type: 'airtable-sync' })
  });

  if (response.ok) {
    res.status(200).json({ ok: true });
  } else {
    res.status(500).json({ ok: false, error: await response.text() });
  }
} 