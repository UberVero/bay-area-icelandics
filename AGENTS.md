# Working on this website

- Explain changes to Veronica in plain English and use a separate worktree.
- Preserve the existing Fathom pageview tracker in the document head during all edits and redesigns: `https://cdn.usefathom.com/script.js`, site ID `HIYUJOPT`, with `defer`.
- Do not remove, disable, duplicate, or change the analytics tracker or bypass its publishing check unless Veronica explicitly requests an analytics change.
- Before publishing, run `python3 -m unittest discover -s tests -v` and `python3 scripts/check_analytics.py`.
- GitHub Pages must use the guarded GitHub Actions workflow, not direct branch publishing. A failed check must leave the last successful website live.
- If adding public HTML pages, include them in the deployment package and analytics validation.
- After publishing, verify the live HTML contains the tracker. For analytics changes, also verify a normal site visit reaches the existing Fathom dashboard; avoid repeated artificial test visits.
