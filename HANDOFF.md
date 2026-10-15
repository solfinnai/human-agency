# Human Agency — Dev Handoff

Talent agency site for anime, webtoons and comics: artists, webtoon creators, illustrators, writers, animators, voice actors, VTubers, streamers, content creators, influencers, cosplayers, models, actors, celebrities, musicians, dancers, esports talent, podcasters, photographers, translators.

## Links
| What | URL |
|---|---|
| Live site (Vercel, free tier) | https://human-agency-cyan.vercel.app |
| GitHub repo | https://github.com/solfinnai/human-agency |
| Linear project (roadmap issues HEN-486…HEN-491) | https://linear.app/henryfinnai/project/human-agency-5a307358cf8d |
| Google Drive folder (docs / design / exports / data) | https://drive.google.com/drive/folders/1Uvx30UaaOQyJn8LM14C4TnDUceyG0U0f |
| Notion project page | NOTION_URL |
| Vercel project | https://vercel.com/henryfinnai-1359s-projects/human-agency |

## Architecture (v0)
Plain static HTML/CSS, zero dependencies, zero backend.
- `build.py` — tiny Python generator. Category list (`CATS`), services (`SERV`), nav and every page body live here. Writes HTML to `public/`.
- `public/styles.css` — all styling (dark theme, pink→purple gradient, CSS grid cards, responsive).
- `public/*.html` — generated pages: `index` (home), `talent` (20 category cards), `roster` (placeholder cards), `services`, `about`, `apply` (contact/apply form).
- `vercel.json` — serves `public/` as static output, no build step.

## Run / deploy
```bash
python3 build.py              # regenerate public/*.html after editing build.py
python3 -m http.server -d public 8000   # preview at http://localhost:8000
vercel deploy --prod          # deploys (project is linked to henryfinnai's Vercel scope)
```
The Vercel project was deployed via CLI and is **not yet connected to the GitHub repo** for auto-deploys — connect it in Vercel → Project → Settings → Git (or import solfinnai/human-agency).

## What's placeholder
- Roster: 12 generic "Talent Name" cards with emoji avatars — no real talent.
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

## Rules from Henry
- No Supabase or paid databases. Ask Henry before anything that costs money (domains, paid plans, paid CMS/auth tiers).
