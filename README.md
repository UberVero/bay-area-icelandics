# Bay Area Icelandics

Landing page and member signup for the Bay Area Icelandics club — a community for Icelandic horse owners, riders, breeders, and enthusiasts in the San Francisco Bay Area.

**Live site:** [bayareaicelandics.club](https://bayareaicelandics.club)

## What's in this repo

| File | What it is |
|------|------------|
| `index.html` | The entire website — one self-contained file |
| `hero.jpeg` | Hero background photo (Veronica + horse at Woodside, 2017) |
| `CNAME` | Tells GitHub Pages to serve the site at bayareaicelandics.club |

## Editing the site

The site is a single HTML file with all styles embedded. Open `index.html` in any text editor to make changes. Key sections and roughly where to find them:

- **Hero headline & tagline** — search for `hero-content`
- **About / mission text** — search for `about-text`
- **Why Icelandic Horses cards** — search for `why-cards`
- **Activities** — search for `activities-grid`
- **Signup form embed** — search for `notion-form-wrap`
- **Footer contact info** — search for `<footer>`

## Signup form (Notion)

Member signups go into a Notion database:
**Bay Area Icelandics — Member Signups** (in Teamspace Home)

Fields collected: First Name, Last Name, Email, Phone (WhatsApp), I am a..., Experience Level, USIHC Member?, How did you hear about us?, Notes.

## Deploying changes

This site is hosted on GitHub Pages. To publish an update:

1. Make your edits to `index.html`
2. Open Terminal and run:
   ```
   cd ~/Code/bay-area-icelandics
   git add -A
   git commit -m "describe your change here"
   git push
   ```
3. Changes go live at bayareaicelandics.club within a minute or two.

## Custom domain DNS records

If you ever need to re-point the domain (e.g. switching registrars), set these DNS records:

| Type | Name | Value |
|------|------|-------|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `ubervero.github.io` |
