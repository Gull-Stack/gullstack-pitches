#!/usr/bin/env python3
"""Generate the Pickleball Hall of Fame concept site.

One template, one nav, one footer. Run from the repo root:

    python3 hall-of-fame/build.py

Writes pickleball-hall-of-fame.html and pickleball-hall-of-fame/*.html.
Content lives in hall-of-fame/data.py; every fact there is from
pickleballhalloffame.global (read 17 Nov 2026).
"""

import html
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from data import INDUCTEES, PARTNERS, KEEPERS  # noqa: E402

B = "/pickleball-hall-of-fame"
IMG = "/hall-of-fame/img"
HOST = "https://pitches.gullstack.com"
REAL = "https://pickleballhalloffame.global"
OUT_DIR = ROOT / "pickleball-hall-of-fame"

NAV = [
    ("inductees", "Inductees", f"{B}/inductees"),
    ("weekend", "Induction Weekend", f"{B}/weekend"),
    ("nominate", "Nominate", f"{B}/nominate"),
    ("support", "Support", f"{B}/support"),
]
YEARS = sorted({y for y, *_ in INDUCTEES}, reverse=True)
e = html.escape


def slug(name):
    return name.lower().replace(" ", "-").replace(".", "")


# --------------------------------------------------------------------------
# shell
# --------------------------------------------------------------------------

def page(key, title, desc, body, path):
    nav = "".join(
        f'<a href="{href}"{" aria-current=page" if k == key else ""}>{label}</a>' for k, label, href in NAV
    )
    drawer = "".join(f'<a href="{href}">{label}</a>' for _, label, href in [("home", "Home", B)] + NAV)
    url = HOST + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="noindex,nofollow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Pickleball Hall of Fame (concept)">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{HOST}/hall-of-fame/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Pickleball Hall of Fame. Preserving pickleball history.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{HOST}/hall-of-fame/og.jpg">
<meta name="theme-color" content="#0b0a08">
<link rel="icon" href="{IMG}/pb-hall-of-fame-logo-web.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Mulish:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/hall-of-fame/site.css">
</head>
<body>
<header class="hdr"><div class="wrap">
  <a class="brand" href="{B}"><img src="{IMG}/pb-hall-of-fame-logo-web.png" alt="Pickleball Hall of Fame"><span>Pickleball <b>Hall of Fame</b></span></a>
  <nav class="nav" aria-label="Main">{nav}<a class="btn" href="{B}/support"><span>Become a Keeper</span></a></nav>
  <button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i><i></i></button>
</div></header>
<div class="drawer">{drawer}</div>
<main>
{body}
</main>
{band()}
{footer()}
<div class="concept">Concept by GullStack</div>
<script src="/hall-of-fame/site.js"></script>
</body>
</html>
"""


def band():
    words = ["Honor the past", "Connect generations", "Inspire the future"] * 2
    spans = "".join(f"<span>{w}</span>" for w in words)
    return f'<div class="band" aria-hidden="true"><div class="marq">{spans}{spans}</div></div>'


def footer():
    return f"""<footer class="foot"><div class="wrap">
  <div class="cols">
    <div><a class="brand" href="{B}"><img src="{IMG}/pb-hall-of-fame-logo-web.png" alt=""><span>Pickleball <b>Hall of Fame</b></span></a>
      <p style="margin-top:18px;max-width:34ch">Preserving the history of the game, and the people who built it. Est. 2017.</p></div>
    <div><h4>Explore</h4><a href="{B}/inductees">Inductees</a><a href="{B}/melissa-mccurley">Inductee stories</a><a href="{B}/weekend">Induction Weekend</a></div>
    <div><h4>Take part</h4><a href="{B}/nominate">Nominate</a><a href="{B}/support">Keepers 100</a><a href="{B}/support#ways">Donate or sponsor</a></div>
    <div><h4>Follow</h4><a href="https://www.facebook.com/PickleballHallOfFame">Facebook</a><a href="https://www.instagram.com/pickleballhalloffame/">Instagram</a></div>
  </div>
  <div class="base"><span>A concept design by GullStack for the Pickleball Hall of Fame. Content from pickleballhalloffame.global.</span><span>Not the live site.</span></div>
</div></footer>"""


def partners():
    cells = "".join(
        f'<div><img src="{IMG}/{f}" alt="{e(n)}" loading="lazy"><small>{e(role)}</small></div>' for role, n, f in PARTNERS
    )
    return f'<div class="partners rv">{cells}</div>'


HONOR_SVG = {
    "plaque": '<svg viewBox="0 0 88 88"><path d="M18 10h52v68H18z"/><path d="M25 17h38v54H25z"/><circle cx="44" cy="36" r="10"/><path d="M32 56h24M35 62h18"/></svg>',
    "jacket": '<svg viewBox="0 0 88 88"><path d="M30 12l14 10 14-10 16 8 6 26-10 4v28H18V50L8 46l6-26z"/><path d="M44 22v56M36 14l8 18 8-18"/><path d="M52 40h10"/></svg>',
    "ring": '<svg viewBox="0 0 88 88"><circle cx="44" cy="52" r="24"/><circle cx="44" cy="52" r="17"/><path d="M32 30l6-16h12l6 16"/><path d="M38 14l6 8 6-8"/></svg>',
}


def honors():
    rows = [
        ("plaque", "The plaque", "Each inductee receives a plaque at the induction banquet."),
        ("jacket", "The jacket", "The Hall of Fame jacket, worn by every member of every class."),
        ("ring", "The ring", "A Hall of Fame ring. A photo and bio of each inductee stays on the site for good."),
    ]
    return '<div class="honors">' + "".join(
        f'<div class="honor">{HONOR_SVG[k]}<h3>{t}</h3><p>{d}</p></div>' for k, t, d in rows
    ) + "</div>"


def ring():
    years = "  ·  ".join(str(y) for y in sorted(YEARS)) + "  ·  "
    return f"""<div class="ring" aria-hidden="true">
  <svg viewBox="0 0 400 400">
    <defs><path id="yrs" d="M200,200 m-172,0 a172,172 0 1,1 344,0 a172,172 0 1,1 -344,0"/></defs>
    <g class="turn2"><circle cx="200" cy="200" r="196" stroke="#c4a55f" stroke-opacity=".5" stroke-dasharray="1 9" fill="none" stroke-width="2"/></g>
    <circle class="draw" cx="200" cy="200" r="150" stroke="#c4a55f" stroke-opacity=".6" fill="none" stroke-width="1"/>
    <g class="turn"><text><textPath href="#yrs" textLength="1075" lengthAdjust="spacing">{years}</textPath></text></g>
  </svg>
  <div class="logo"><img src="{IMG}/pb-hall-of-fame-logo-web.png" alt=""></div>
</div>"""


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

def home():
    by_year = {}
    for y, n, c, f in INDUCTEES:
        by_year.setdefault(y, []).append((n, c, f))

    half = len(INDUCTEES) // 2
    def face(y, n, c, f):
        href = f' href="{B}/melissa-mccurley"' if n == "Melissa McCurley" else f' href="{B}/inductees"'
        return f'<a class="face"{href}><img src="{IMG}/{f}" alt="{e(n)}" loading="lazy"><div class="cap"><b>{e(n)}</b><span>Class of {y}</span></div></a>'
    r1 = "".join(face(*i) for i in INDUCTEES[:half])
    r2 = "".join(face(*i) for i in INDUCTEES[half:])

    plaques = ""
    for i, y in enumerate(YEARS):
        lis = "".join(
            f'<li><img src="{IMG}/{f}" alt="" loading="lazy"><div style="min-width:0"><b>{e(n)}</b><small>{e(c)}</small></div></li>'
            for n, c, f in by_year[y]
        )
        k = len(by_year[y])
        plaques += f'<article class="plaque{" cur" if i == 0 else ""}"><div class="yr">{y}</div><div class="ct"><span class="label">Class of {y}</span><span>{k} inductees</span></div><ul>{lis}</ul></article>'

    spot = "".join(
        f'<a class="rv" href="{B}/inductees"><figure><img src="{IMG}/{f}" alt="{e(n)}" loading="lazy"></figure><b>{e(n)}</b><small>{e(c)}</small></a>'
        for n, c, f in by_year[2026]
    )

    body = f"""
<section class="hero">
  <div class="bg"><img src="{IMG}/phof-cover-image-court-v2.jpg" alt=""></div><div class="shade"></div>
  <div class="wrap">
    <div>
      <div class="label rv fade">Pickleball Hall of Fame · Est. 2017</div>
      <h1 class="split">Preserving <em>pickleball</em> history.</h1>
      <p class="lede rv">Honoring the champions and contributors who built the game, and connecting them to every player still to come.</p>
      <div class="ctas rv"><a class="btn" href="{B}/inductees"><span>Meet the inductees</span></a><a class="btn ghost" href="#class-2026"><span>The Class of 2026</span></a></div>
    </div>
    {ring()}
  </div>
  <div class="scrollcue"></div>
</section>

<section class="facts"><div class="wrap">
  <div class="fact rv"><div class="n" data-count="2017" data-from="1965" data-plain>2017</div><div class="t">The year the Hall was founded</div></div>
  <div class="fact rv"><div class="n" data-count="10">10</div><div class="t">Induction classes, 2017 to 2026</div></div>
  <div class="fact rv"><div class="n" data-count="{len(INDUCTEES)}">{len(INDUCTEES)}</div><div class="t">Champions and contributors inducted</div></div>
  <div class="fact rv"><div class="n" data-count="75" data-plus="%">75%</div><div class="t">Selection committee vote needed to get in</div></div>
</div></section>

<section class="light mission pad"><div class="wrap grid">
  <figure class="photo rv zoom" style="margin:0"><img src="{IMG}/Joel-Pritchard-and-Dan-Evans-800-v2.jpg" alt="Joel Pritchard and Dan Evans" loading="lazy"><figcaption>Joel Pritchard, Class of 2017, with Dan Evans.</figcaption></figure>
  <div>
    <div class="label">Our mission</div>
    <p class="big words">The Pickleball Hall of Fame memorializes the *Champions and *Contributors of the past while creating a connection to present and future players. We preserve the history of the game while reinforcing the value of pickleball as a *sport *for *all.</p>
    <p class="lede rv" style="margin-top:36px">Every candidate has shown character, integrity, sportsmanship and consideration for others, and earned the respect of their peers.</p>
    <a class="btn ghost rv" href="{B}/nominate" style="margin-top:12px"><span>How inductees are chosen</span></a>
  </div>
</div></section>

<section class="pad" style="padding-bottom:40px"><div class="wrap" style="display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap">
  <div><div class="label rv">{len(INDUCTEES)} inductees</div><h2 class="split" style="margin-top:14px">The wall.</h2></div>
  <p class="lede rv" style="max-width:40ch;margin:0">Every member, every class. Hover to stop the wall and meet them.</p>
</div></section>
<div class="wall" aria-label="Inductee portraits">
  <div class="row">{r1}{r1}</div>
  <div class="row rev">{r2}{r2}</div>
</div>

<section class="hall" style="--hall-h:{120 + len(YEARS) * 46}vh"><div class="stick">
  <div class="wrap head">
    <div><div class="label">Ten classes</div><h2 class="split" style="margin-top:14px">One hall.</h2></div>
    <div class="meter"><i></i></div>
  </div>
  <div class="track">{plaques}</div>
</div></section>

<section class="light pad" id="class-2026"><div class="wrap">
  <div class="label rv">Inducted November 2026 · Gold Canyon and Mesa, Arizona</div>
  <h2 class="split" style="margin-top:14px">The Class of 2026.</h2>
  <div class="spot">{spot}</div>
  <a class="btn ghost rv" href="{B}/weekend" style="margin-top:48px"><span>Inside induction weekend</span></a>
</div></section>

<section class="pad"><div class="wrap">
  <div class="label rv">What an inductee receives</div>
  <h2 class="split" style="margin:14px 0 36px">Plaque. Jacket. Ring.</h2>
  {honors()}
</div></section>

<section class="light pad"><div class="wrap">
  <div class="label rv">Our partners</div>
  <h2 class="split" style="margin:14px 0 32px;font-size:clamp(36px,4.6vw,60px)">The game's biggest names stand behind its history.</h2>
  {partners()}
</div></section>
"""
    return page("home", "Pickleball Hall of Fame · Preserving pickleball history",
                "Honoring the champions and contributors who built pickleball. 41 inductees across ten classes since 2017.",
                body, B)


def inductees():
    cat_chips = "".join(
        f'<button class="chip" data-kind="cat" data-val="{v}" aria-pressed="{"true" if v == "all" else "false"}">{l}</button>'
        for v, l in [("all", "All"), ("Competitor", "Competitors"), ("Contributor", "Contributors")]
    )
    yr_chips = '<button class="chip" data-kind="year" data-val="all" aria-pressed="true">Every class</button>' + "".join(
        f'<button class="chip" data-kind="year" data-val="{y}" aria-pressed="false">{y}</button>' for y in YEARS
    )
    cards = ""
    for y, n, c, f in INDUCTEES:
        if n == "Melissa McCurley":
            tag, end, more = f'<a class="card" href="{B}/melissa-mccurley"', "</a>", '<span class="more">Read her story</span>'
        else:
            tag, end, more = '<div class="card"', "</div>", ""
        cards += (f'{tag} data-cat="{e(c)}" data-year="{y}"><div class="in3d"><figure><img src="{IMG}/{f}" alt="{e(n)}" loading="lazy">'
                  f'<span class="yrtag">{y}</span></figure><b>{e(n)}</b><small>{e(c)}</small>{more}</div>{end}')
    body = f"""
<section class="phero"><div class="wrap">
  <div class="label rv fade">The members</div>
  <h1 class="split">The <em>inductees.</em></h1>
  <p class="lede rv">Competitors who dominated the game for years, and contributors who built it for everyone else. {len(INDUCTEES)} members across ten classes.</p>
</div><div class="ghostyr" aria-hidden="true">{len(INDUCTEES)}</div></section>
<section style="padding-bottom:120px"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter inductees">{cat_chips}<span class="sep"></span>{yr_chips}</div>
  <div class="count">{len(INDUCTEES)} inductees</div>
  <div class="grid">{cards}</div>
</div></section>
"""
    return page("inductees", "Inductees · Pickleball Hall of Fame",
                "All 41 members of the Pickleball Hall of Fame, by class and category, 2017 to 2026.", body, f"{B}/inductees")


def melissa():
    steps = [
        ("U.S. Navy", "Hospital Corpsman Second Class",
         "Served during Operation Desert Storm, caring for service members, their families and World War II veterans."),
        ("EDS", "The Navy's first common network",
         "Led the build-out of NMCI for the Navy and Marine Corps. Set up the Navy's Crisis Response Center after 9/11, and its emergency team that restored communications after Hurricane Katrina."),
        ("EDS", "Global Service Delivery Executive",
         "Kept mission-critical data and voice running for American Express call centers, merchants and customers worldwide."),
        ("2014", "PickleballTournaments.com",
         "Took over the platform and turned it into the sport's engine for technology, operations consulting and data."),
        ("UTPR", "The sport's first data-driven rating",
         "Co-created the Universal Tournament Pickleball Rating with USA Pickleball, so ratings stayed fair as players grew almost 20-fold."),
        ("CBS Sports", "A first in the booth",
         "The first woman to broadcast pickleball on CBS Sports, and the first co-host of the syndicated Pickleball Show."),
        ("2025", "Pickleball Hall of Fame",
         "Inducted with the Class of 2025 as a Contributor."),
        ("Today", "Still serving the game",
         "Executive Vice President, Competition, for the APP Tour, and Acting President of the Pickleball Hall of Fame."),
    ]
    st = "".join(f'<div class="step"><div class="when">{a}</div><h3>{b}</h3><p>{c}</p></div>' for a, b, c in steps)
    built = [
        ("Bracketing and seeding", "An online system for every format governing bodies and operators run: single and double elimination, round robin and more."),
        ("Tournament operations platform", "Took events from a few hundred players to 3,000 or more, on as many as 58 courts at once."),
        ("Operations playbook", "Kept the biggest tournaments running through weather, power and internet failures, and moved match calls to text."),
        ("UTPR", "With USA Pickleball, the first algorithmic, data-driven rating system in the sport."),
    ]
    bl = "".join(f'<div class="rv"><b>{a}</b><p>{b}</p></div>' for a, b in built)
    body = f"""
<section class="phero"><div class="wrap prof">
  <div class="portrait rv zoom"><img src="{IMG}/Melissa-McCurley-Contributor.png" alt="Melissa McCurley"></div>
  <div>
    <div class="label rv fade">Class of 2025 · Contributor</div>
    <h1 class="split">Melissa McCurley</h1>
    <p class="lede rv">Veteran, tournament pioneer, software entrepreneur and broadcaster. Often called the hardest working person in pickleball. Her goal was to help those who want to help pickleball grow.</p>
    <div class="roles rv"><span>Acting President, PHOF</span><span>EVP Competition, APP Tour</span><span>U.S. Navy veteran</span></div>
  </div>
</div><div class="ghostyr" aria-hidden="true">2025</div></section>

<section class="light pad"><div class="wrap">
  <div class="label rv">PickleballTournaments.com, 2014 to 2023</div>
  <h2 class="split" style="margin-top:14px">An industry, built on her desk.</h2>
  <div class="growth">
    <div><div class="from">Tournaments supported · 93 in 2014</div><div class="n" data-count="1200" data-from="93" data-plus="+">1,200+</div><div>events in 2023</div><div class="bar"><i style="--w:1"></i></div></div>
    <div><div class="from">Players served · about 10,000 in 2014</div><div class="n" data-count="200000" data-from="10000" data-plus="+">200,000+</div><div>amateur and pro players in 2023</div><div class="bar"><i style="--w:1"></i></div></div>
  </div>
</div></section>

<section class="pad"><div class="wrap" style="display:grid;grid-template-columns:minmax(0,1fr);max-width:980px">
  <div class="label rv">Her road</div>
  <h2 class="split" style="margin-top:14px">From the front lines to center court.</h2>
  <div class="career" data-rail><div class="rail"><i></i></div><div class="ball"><img src="{IMG}/phof-pickleball-image.png" alt=""></div>{st}</div>
</div></section>

<section class="light pad"><div class="wrap">
  <blockquote class="quote rv" style="margin:0">When you've been on the front lines responsible for restoring communications that saves lives, running tournament desk operations where life and death isn't on the line, it's not pressure.</blockquote>
  <cite class="rv">Melissa McCurley, on staying calm at the biggest events</cite>
  <div class="list2" style="margin-top:80px">{bl}</div>
</div></section>

<section class="pad"><div class="wrap">
  <div class="label rv">Recognition</div>
  <div class="awards">
    <div class="rv"><b>2020</b><span>Racquet Sports Industry Service Award</span></div>
    <div class="rv"><b>2022</b><span>Inaugural McCurley Cup</span></div>
    <div class="rv"><b>2022</b><span>US Open Impact Award</span></div>
    <div class="rv"><b>2025</b><span>Pickleball Hall of Fame</span></div>
  </div>
  <a class="btn ghost rv" href="{B}/inductees" style="margin-top:56px"><span>Back to every inductee</span></a>
</div></section>
"""
    return page("inductees", "Melissa McCurley · Class of 2025 · Pickleball Hall of Fame",
                "Navy veteran, tournament pioneer and broadcaster. Melissa McCurley, Class of 2025 Contributor.",
                body, f"{B}/melissa-mccurley")


def weekend():
    days = [
        (12, "Thu", "Documentary Night", "A screening of “The Power of Pickleball” to open the weekend.", "Gold Canyon, Arizona", f'<figure><img src="{IMG}/documentary-night-2026-v2.jpg" alt="Documentary night" loading="lazy"></figure>'),
        (13, "Fri", "Banquet and Induction", "Meet-and-greet cocktail hour, dinner, and the induction of the Class of 2026.", "Gold Canyon Golf Resort &amp; Spa", f'<figure><img src="{IMG}/banquet-night-2026-v2.jpg" alt="Banquet and induction ceremony" loading="lazy"></figure>'),
        (14, "Sat", "Recognition Ceremony", "An on-court ceremony where the community honors the newest members. Family, friends and fans welcome.", "2:00 PM · Arizona Athletic Grounds, Mesa", '<div class="typo"><span>14</span></div>'),
    ]
    dd = "".join(
        f'<article class="day rv">{media}<div class="body"><div class="d">{d}<small>{w} · Nov</small></div><h3>{t}</h3><p>{p}</p><div class="where">{where}</div></div></article>'
        for d, w, t, p, where, media in days
    )
    by26 = [(n, c, f) for y, n, c, f in INDUCTEES if y == 2026]
    spot = "".join(
        f'<a class="rv" href="{B}/inductees"><figure><img src="{IMG}/{f}" alt="{e(n)}" loading="lazy"></figure><b>{e(n)}</b><small>{e(c)}</small></a>'
        for n, c, f in by26
    )
    body = f"""
<section class="phero"><div class="wrap">
  <div class="label rv fade">November 12 to 14, 2026 · Arizona</div>
  <h1 class="split">Induction <em>weekend.</em></h1>
  <p class="lede rv">Three days in Gold Canyon and Mesa to honor the Class of 2026, and every legend who came before them.</p>
  <div class="days">{dd}</div>
</div><div class="ghostyr" aria-hidden="true">2026</div></section>

<section class="light pad"><div class="wrap">
  <div class="label rv">Honored this year</div>
  <h2 class="split" style="margin-top:14px">The Class of 2026.</h2>
  <div class="spot">{spot}</div>
</div></section>

<section class="pad"><div class="wrap">
  <div class="label rv">At the banquet</div>
  <h2 class="split" style="margin:14px 0 36px">Plaque. Jacket. Ring.</h2>
  {honors()}
</div></section>

<section class="light pad" style="padding-top:0"><div class="wrap">
  <figure class="rv zoom" style="margin:0"><img src="{IMG}/pickleball-class-2025-cover.jpg" alt="Class of 2025" loading="lazy" style="width:100%"></figure>
  <div style="display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap;margin-top:28px">
    <p class="lede rv" style="margin:0">Last year: Cammy MacGregor, Chris Miller and Melissa McCurley joined the Hall.</p>
    <a class="btn ghost rv" href="{B}/nominate"><span>Nominate for the next class</span></a>
  </div>
</div></section>
"""
    return page("weekend", "Induction Weekend 2026 · Pickleball Hall of Fame",
                "Documentary night, the banquet and induction, and the recognition ceremony. November 12 to 14, 2026, in Arizona.",
                body, f"{B}/weekend")


def nominate():
    stages = [
        ("01", "Nominate", "Anyone can put a name forward. The form includes an essay of at least 300 words.", "Due July 8"),
        ("02", "Nominating committee", "Nine members vote by secret ballot in two rounds. Up to six competitors and three contributors move on.", ""),
        ("03", "Selection committee", "Seven members choose up to five inductees a year: up to three players and two contributors. Each needs 75% approval.", "Decided by August 15"),
        ("04", "The announcement", "The new class is announced to the pickleball world in August.", "August"),
        ("05", "Induction", "Inductees receive their plaque, jacket and ring at the induction banquet.", ""),
    ]
    sg = "".join(
        f'<div class="stage"><div class="side"><div class="no">{n}</div><h3>{t}</h3><p>{p}</p>{f"<span class=tag>{tag}</span>" if tag else ""}</div></div>'
        for n, t, p, tag in stages
    )
    body = f"""
<section class="phero"><div class="wrap">
  <div class="label rv fade">Guidelines for entry</div>
  <h1 class="split">Nominate a <em>legend.</em></h1>
  <p class="lede rv">The Hall recognizes exceptional results on the court over a career, and exceptional contributions to the growth, development and leadership of the game.</p>
  <div class="crit">
    <div class="rv"><div class="big">5<small>years</small></div><h3>Competitors</h3><p>Dominated the game for at least a five-year period. Think podium finishes at the US Open, USA Pickleball Nationals, the PPA or the APP.</p></div>
    <div class="rv"><div class="big">8<small>years</small></div><h3>Contributors</h3><p>Moved the sport at the national or international level for at least eight years.</p></div>
  </div>
</div></section>

<section class="light pad"><div class="wrap">
  <div class="label rv">The path to the Hall</div>
  <h2 class="split" style="margin-top:14px">Five steps. One class a year.</h2>
  <div class="path" data-rail><div class="rail"><i></i></div><div class="ball"><img src="{IMG}/phof-pickleball-image.png" alt=""></div>{sg}</div>
  <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:20px">
    <a class="btn" href="{REAL}/nominating-form/"><span>Open the nomination form</span></a>
    <a class="btn ghost" href="{B}/inductees"><span>See who made it</span></a>
  </div>
</div></section>

<section class="pad"><div class="wrap">
  <div class="label rv">Beyond the record</div>
  <p class="quote rv" style="margin-top:22px">Character, integrity, sportsmanship and consideration for others.</p>
  <p class="lede rv" style="margin-top:28px">Every candidate is weighed on how they played and served, not only what they won.</p>
</div></section>
"""
    return page("nominate", "Nominate · Pickleball Hall of Fame",
                "How to nominate a competitor or contributor for the Pickleball Hall of Fame, and how the class is chosen.",
                body, f"{B}/nominate")


def support():
    names = "".join(f"<p>{e(n)}</p>" for n in KEEPERS)
    body = f"""
<section class="phero"><div class="wrap keep">
  <div>
    <div class="label rv fade">Keepers 100</div>
    <h1 class="split">Keep the <em>story.</em></h1>
    <p class="lede rv">One hundred people and organizations each gave $500 to build a lasting foundation for the Hall. Their support keeps the people, stories and moments that built our sport alive for generations.</p>
    <div class="facts" style="border:0;margin-top:24px"><div style="display:flex;gap:48px">
      <div class="rv"><div class="n" data-count="100" style="font:600 clamp(54px,6vw,88px)/1 var(--serif);font-variant-numeric:lining-nums;color:var(--gold-hi)">100</div><div class="t" style="color:var(--on-ink-2);font-size:15px">Inaugural Keepers</div></div>
      <div class="rv"><div style="font:600 clamp(54px,6vw,88px)/1 var(--serif);font-variant-numeric:lining-nums;color:var(--gold-hi)">$500</div><div class="t" style="color:var(--on-ink-2);font-size:15px">From each Keeper</div></div>
    </div></div>
  </div>
  <div class="names rv fade" aria-label="Inaugural Keepers"><div class="col">{names}{names}</div></div>
</div></section>

<section class="pad poem" style="padding-top:40px"><div class="wrap">
  <p class="rv">The game has changed.</p>
  <p class="rv">The equipment has changed.</p>
  <p class="rv">The courts have multiplied.</p>
  <p class="rv">Millions have discovered pickleball.</p>
  <p class="rv" style="margin-top:28px">But the people and stories that brought us here should never disappear.</p>
  <p class="g rv" style="margin-top:28px">That is why we are Keepers.</p>
</div></section>

<section class="light pad" id="ways"><div class="wrap">
  <div class="label rv">Ways to give</div>
  <h2 class="split" style="margin-top:14px">Help preserve the game.</h2>
  <div class="ways">
    <div class="rv"><div class="amt">$500</div><h3>Become a Keeper</h3><p>Join the people and organizations building the Hall's foundation.</p><a class="btn ghost" href="{REAL}/keepers/"><span>Keepers 100</span></a></div>
    <div class="rv"><div class="amt">Any</div><h3>Donate</h3><p>The Hall is a non-profit. Every gift, no matter the size, helps preserve the game's history.</p><a class="btn ghost" href="{REAL}/donate/"><span>Donate online</span></a></div>
    <div class="rv"><div class="amt">Partner</div><h3>Sponsor</h3><p>Put your name behind the history of the sport, alongside USA Pickleball, the APP, the US Open and DUPR.</p><a class="btn ghost" href="{REAL}/sponsors/"><span>Become a sponsor</span></a></div>
  </div>
  <div style="margin-top:72px">{partners()}</div>
</div></section>
"""
    return page("support", "Support the Hall · Keepers 100 · Pickleball Hall of Fame",
                "Join the Keepers 100, donate or sponsor the Pickleball Hall of Fame.", body, f"{B}/support")


def main():
    OUT_DIR.mkdir(exist_ok=True)
    files = {
        ROOT / "pickleball-hall-of-fame.html": home(),
        OUT_DIR / "inductees.html": inductees(),
        OUT_DIR / "melissa-mccurley.html": melissa(),
        OUT_DIR / "weekend.html": weekend(),
        OUT_DIR / "nominate.html": nominate(),
        OUT_DIR / "support.html": support(),
    }
    for p, s in files.items():
        p.write_text(s)
        print("wrote", p.relative_to(ROOT), len(s))


if __name__ == "__main__":
    main()
