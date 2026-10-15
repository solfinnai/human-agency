# Human Agency — Dev Handoff

**Positioning:** Human Agency, the talent agency for fandom: the people behind the panels and the stars around them.

- **Year-1 core desks:** webtoon, comic & manga creators; cosplayers; voice actors; indie VTubers; anime & gaming creators.
- **Services:** talent management, brand-deals desk, licensing & adaptation desk (film/TV deals through a licensed partner agency), events & conventions, merch.
- **Differentiators:** talent keeps their IP; transparent payouts; fandom-native brand packages.
- **Niches we're building:** 52 niches in 13 clusters (fandom is the flagship), each with its specific roles, plus 21 universal roles. Source: the Oct 15 2026 niche research ([report](https://docs.google.com/document/d/1K0Y9-RZnAx8ezqfZFcgFYWtB_sDajYKoADVCBs2jLlA/edit), [sheet](https://docs.google.com/spreadsheets/d/1aWpjW8tMw4RKE1IeAkjW0fsF3A-HvwjUPfogKrDoZvM/edit)).
- Commission rates are deliberately **not** on the public site.

## Links
| What | URL |
|---|---|
| Live site (Vercel, free tier) | https://human-agency-cyan.vercel.app |
| GitHub repo | https://github.com/solfinnai/human-agency |
| Linear project (roadmap issues HEN-486…HEN-491) | https://linear.app/henryfinnai/project/human-agency-5a307358cf8d |
| Google Drive folder (docs / design / exports / data) | https://drive.google.com/drive/folders/1Uvx30UaaOQyJn8LM14C4TnDUceyG0U0f |
| Notion project page | https://app.notion.com/p/3fafdcf928578162851bf9cdf7e2b9cc |
| Handoff Google Doc | https://docs.google.com/document/d/17UEuHOE7OSvad2sTMhFDPrmjssakZNCSRZ2eIW23XR0/edit |
| Vercel project | https://vercel.com/henryfinnai-1359s-projects/human-agency |

## Architecture (v0)
Plain static HTML/CSS, zero dependencies, zero backend.
- `build.py` — tiny Python generator. Core desks (`DESKS`), services (`SERV`), differentiators (`DIFF`), nav and every page body live here. Writes HTML to `public/`.
- `data/niches.json` — niche taxonomy (52 niches: cluster, fit score 1-5, roles; plus 21 universal roles), exported from the research `taxonomy.py`. Drives the "Niches we're building" sections.
- `public/styles.css` — all styling (dark theme, pink→purple gradient, CSS grid cards, responsive).
- `public/*.html` — generated pages: `index` (home), `talent` (5 core desks + 52 expandable niches grouped by cluster + universal roles), `roster` (placeholder cards), `services`, `about`, `apply` (contact/apply form).
- `vercel.json` — serves `public/` as static output, no build step.

## Run / deploy
```bash
python3 build.py              # regenerate public/*.html after editing build.py
python3 -m http.server -d public 8000   # preview at http://localhost:8000
vercel deploy --prod          # deploys (project is linked to henryfinnai's Vercel scope)
```
The Vercel project was deployed via CLI and is **not yet connected to the GitHub repo** for auto-deploys — connect it in Vercel → Project → Settings → Git (or import solfinnai/human-agency).

## What's placeholder
- Roster: 10 generic "Talent Name" cards (2 per core desk) with emoji avatars — no real talent.
- Apply/contact form: opens the visitor's email app (`mailto:`) to `hello@humanagency.example` (fake address). No data is stored.
- Brand: text logo only, no real imagery, no OG images, no favicon.
- Copy is first-draft marketing copy.
- No analytics, no sitemap, no custom domain.

## Prioritized upgrade list
1. **Next.js + CMS migration** (HEN-486) — App Router; content in a free/git-based CMS (Sanity free tier, Decap, or MDX).
2. **Talent profiles + filterable roster** (HEN-487) — `/talent/[slug]`, portfolio gallery, socials, stats, booking CTA; filters by category/region/platform.
3. **Applications pipeline** (HEN-488) — replace mailto with serverless submission → email/Notion/Sheet, portfolio upload, spam protection, review states.
4. **Booking / brand inquiry flow** (HEN-489) — budget, dates, shortlist, proposal tracking.
5. **Auth: talent portal + admin** (HEN-490).
6. **SEO, analytics, branding, domain** (HEN-491) — OG images, sitemap, robots, JSON-LD, Vercel Web Analytics, brand kit, custom domain, real inbox.

## Legal: California talent-agency licence (blocker before procuring work)
California's Talent Agencies Act requires a Labor Commissioner talent-agency licence for anyone who procures employment for artists, even incidentally by managers (Marathon v. Blasi). Before Human Agency procures bookings/deals for talent, it must either get licensed or operate as management working with a licensed agency partner. The site already says screen deals go through a licensed partner agency. Tracked in Linear: [HEN-493](https://linear.app/henryfinnai/issue/HEN-493).

## Rules from Henry
- No Supabase or paid databases. Ask Henry before anything that costs money (domains, paid plans, paid CMS/auth tiers).
