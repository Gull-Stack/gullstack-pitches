# gullstack-pitches

Single-file HTML pitch decks and concept demos for GullStack prospects. Each
prospect gets one or two files at the repo root:

- `<client>.html` — the pitch/proposal (dark, editorial, house style)
- `<client>-demo.html` — an optional working concept site for that client
- `<client>/` — any images downloaded for that client

Deployed to Vercel project `gullstack-pitches` (team `gull-stack`) on push to
`main`. `vercel.json` rewrites `/(.*)` → `/$1.html`, so `/jack-holders` serves
`jack-holders.html`.

**Known issue:** the project has Vercel SSO protection enabled
(`all_except_custom_domains`) and no custom domain attached, so
`gullstack-pitches-gull-stack.vercel.app/*` returns a 302 to Vercel login for
anyone outside the team. Prospect links will not open. Fix is either turning
SSO off for the project or attaching a custom domain (e.g.
`pitches.gullstack.com`). Until then, share via a `?_vercel_share=` bypass link
(23h expiry).

## Session Log

### 2026-07-31 — Jack Holder's Restaurant & Bar (Willow Glen, San Jose)

- **Lead source:** Kyle Dickson referral. Owner is shopping an "AIO" pitch from
  Alex Hult, currently on Toast, wants gift cards + online ordering + DoorDash +
  Uber Eats. Kyle takes 10% of this deal per Bryce.
- **Shipped two pages** (commit `cd63303`):
  - `jack-holders-demo.html` — full concept site. Editorial Light, Fraunces +
    Inter, crimson/cream palette sampled from their logo. Real menu content
    transcribed from jackholders.com (breakfast, lunch & dinner, bar), their own
    photography pulled into `jackholders/`, tabbed menus, live open/closed
    status in the header, `Restaurant` + `FAQPage` schema, Toast ordering and
    gift-card CTAs everywhere, sticky mobile order bar.
  - `jack-holders.html` — the pitch, built off their **June 2026 merchant
    statement** (photo Kyle sent). All figures verified against the statement
    to the penny.
- **The numbers** (statement period 6/1/26–6/30/26, MID ending 394988):
  $493,680.75 volume · 6,779 txns · $72.83 avg ticket · $9,989.31 fees ·
  **2.02% blended**. Card-present V/MC/D is 1.733% + $0.15 — genuinely sharp,
  so the pitch does *not* promise a rate cut. Annualized: $5.92M volume,
  $119,872 card fees + $8,772 Toast software = **$128,644/yr**.
- **Pitch angle:** three buckets — (1) move card cost to the customer via a
  compliant CA cash-price/card-price program, (2) replace the $731/mo Toast
  software line, (3) push first-party ordering instead of 15–30% marketplace
  commissions. Site is offered free with the payments relationship.
- **Open items for next session:**
  - Fix the Vercel SSO problem above before sending anything to the owner.
  - Confirm the "website is free with payments" offer framing — that's the
    assumption baked into the pitch's pricing FAQ.
  - Bucket 3 ($2,000/mo delivery savings) is modeled at $10k/mo delivery
    volume, not measured. Swap in real numbers if the owner shares them.
  - Social proof on the demo uses real aggregate ratings only (4.4 Google,
    4.4 across platforms, 750+ Yelp). No review quotes were invented — add
    three real Google quotes before this becomes a live site.
  - No prices on the demo menus (their site doesn't publish them). Menus link
    to Toast for live pricing.
