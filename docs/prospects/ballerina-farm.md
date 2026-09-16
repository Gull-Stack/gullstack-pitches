# Ballerina Farm — prospect notes

**Status (14 Sept 2026):** pitch built. Bryce sends the first message himself on **LinkedIn**
(no hiring email is public; careers run through ballerinafarm.bamboohr.com).

**The personal hook (Bryce):** his wife loves their Bone Broth Hot Cocoa. The message offers to
discount the whole engagement for a hot cocoa subscription. Bryce's own words; keep the offer
light, it is an opener, not a price.

## Why we're talking to them

Ballerina Farm (Kamas, UT; store in Midway) posted a **Director of E-Commerce** role on
LinkedIn (~2 weeks old on 14 Sept, 118 applicants). It is a senior-leadership seat owning
e-commerce and customer support. Bryce's read: "We can crush this for them."

**Pitch shape (decided 14 Sept):** do NOT pitch replacing the leader. Pitch the system
under the seat: Morning Report, support reply drafts, launch checks, subscription care.
A leadership seat that runs two teams cannot be a vendor.

## The posting (BambooHR, read 14 Sept 2026)

- https://ballerinafarm.bamboohr.com/careers/79 — **Director of E-Commerce**, department
  **Executive**, full-time, **Springville UT 84663**, posted **28 Aug 2026**, no pay listed.
- Hiring for marketing at the same time: **#71 Growth Marketing Analyst** (Midway) and
  **#78 Manager, Integrated & Brand Marketing** (Kamas). The Morning Report serves those seats too.
- Careers API (public JSON): `/careers/list` and `/careers/<id>/detail`.

## The BambooHR application (filled 16 Sept 2026, NOT submitted by Claude)

Filled in Chrome on job #79. Bryce clicks the reCAPTCHA and **Submit Application** — an agent
may not complete a CAPTCHA, and the submit is his identity.

- Bryce Morgan · bryce@gullstack.com · (540) 424-0317 · 226 W Founders Blvd, Saratoga Springs,
  UT 84045 (home address, his choice over the GullStack business address).
- Website field: pitches.gullstack.com/ballerina-farm
- Sponsorship required: **No**. Authorized to work in the US: **Yes**. Both are attestations
  about Bryce — he confirms them before submitting.
- Left blank on purpose: Desired Pay (price is Bryce's call), Date Available, LinkedIn, Referred by.
🔴 **BambooHR gotcha, hit 16 Sept:** an upload that has sat on the page too long fails at submit
with *"We had a problem saving the Resume... the Cover Letter"*, and **the failed submit wipes every
field**, including the ones that were fine. Fill the form, upload the two files LAST, and submit
immediately. Two more traps in the same form: the State control looks like `<select name="state.value">`
but the real one is a searchable button dropdown (click its search box first — typing straight after
opening goes nowhere), and the radio buttons ignore programmatic value-setting, so click them.

- Uploads (source HTML + PDFs in `docs/prospects/ballerina-farm-app/`):
  **Bryce-Morgan-GullStack-Resume.pdf** — one page, opens with "This is not a standard
  application", lists what we built for them and the four findings, then his real bio (facts taken
  verbatim from walkthrulabs.com: PPA employee no. 1 in 2019, President today, $200M+ Apollo
  Sports Capital raise, 100+ events, 1.05M peak CBS, Blip Billboards, SUSE).
  **Bryce-Morgan-Cover-Letter.pdf** — the hot cocoa message.

## Live pages

- Deck: https://pitches.gullstack.com/ballerina-farm (9 slides, house deck style, PDF + Save HTML)
- Morning Report demo: https://pitches.gullstack.com/ballerina-farm-demo (`?sample` shows sample figures)
- Analysis: https://pitches.gullstack.com/ballerina-farm-analysis

## Verified facts (public site, 14 Sept 2026)

- Stack: Shopify (theme "Nostalgia" 2.1.0), Skio + Recharge, Attentive, Northbeam, Redo,
  Stamped, ShopMy, back-in-stock / free-gifts / gift-note / form-builder / product-options apps.
- **Gorgias is NOT installed.** The word appears only in a CSS rule that hides chat widgets.
  No help desk visible; support = contact form + support@ballerinafarm.com, reply window
  "1-3 business days (M-F)".
- **Subscription move in progress:** live theme name "v2.2026.8.6.production + Skio Pre-Launch
  Filter"; product-page selling plans are `app_id: SKIO`; footer "Manage Subscriptions" →
  `/tools/recurring/get-subscription-access` (Recharge portal); `SkioHidePlansInRechargeUpsell`
  hides 15 Skio plans in the Recharge cart overlay.
- **Free-shipping exclusions disagree:** cart drawer lists 8, FAQ lists 11. Cart-only: Einkorn
  Flour, Gift Cards, All Subscriptions. FAQ-only: Baked Goods Box, Breakfast Box, Dandy Table,
  Flowers, Everyday Bowl, ready-made boxes. Checkout behaviour not tested (no order placed).
- **Processing time disagrees:** FAQ "2-7 business days", shipping policy "2-8 business days".
- /pages/faq, /pages/help, /pages/shipping, /pages/subscriptions all 301 to the homepage.
- Catalog (`/products.json`): 144 published records, 75 tagged hidden, 69 not; 57 in stock,
  12 sold out (incl. Lemon Poppyseed Farmer Protein, a Bestseller; Farmer Jerky).
- Semrush US: 5,092 keywords, 52,926 organic visits/mo. "ballerina farm" 74,000/mo #1;
  sourdough starter kit #3 (18,100); high protein flour #3 (8,100); bone broth hot chocolate #1 (4,400).

## Not measured — do not claim

Sales, conversion, AOV, ROAS, subscriber counts, ticket volume, site speed, mobile UX,
what checkout charges. Every figure in the demo's sample mode is invented and labelled.

## Commercial (internal only — never on a client page)

- Director of E-Commerce, Utah average ~$119,913 (Indeed, only 2 salaries — thin). × 1.3
  loaded ≈ $156k/yr ≈ $13k/mo. Our estimate, not a quote.
- **No price set.** Bryce decides when they hear a number.

## Do-not-say

- Don't pitch speed or "AI did this in an afternoon" — the brand sells care.
- No public-controversy or family commentary. Business only.
- Don't name Gorgias. Don't claim a help desk is missing; say none is visible.
