#!/usr/bin/env python3
"""Generate the Jack Holder's concept site.

One template, one nav, one footer — output is six static pages so the pitch repo
stays flat HTML. Run from the repo root:

    python3 jackholders/build.py

Writes jack-holders-demo.html and jack-holders-demo/*.html.
"""

import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "jack-holders-demo"

PHONE_DISPLAY = "(408) 613-2365"
PHONE_LINK = "tel:+14086132365"
ORDER = "https://order.toasttab.com/online/jackholders"
GIFT = "https://www.toasttab.com/jackholders/giftcards"
MAPS = "https://maps.google.com/?q=3153+Meridian+Ave+Ste+20,+San+Jose,+CA+95124"
IMG = "/jackholders"

NAV = [
    ("breakfast", "Breakfast", "/jack-holders-demo/breakfast"),
    ("lunch-dinner", "Lunch & Dinner", "/jack-holders-demo/lunch-dinner"),
    ("bar", "The Bar", "/jack-holders-demo/bar"),
    ("about", "Our Story", "/jack-holders-demo/about"),
    ("visit", "Visit", "/jack-holders-demo/visit"),
]


# --------------------------------------------------------------------------
# menu data
# --------------------------------------------------------------------------

BREAKFAST = [
    ("Signature Breakfast", None, [
        ("Chile Verde & Eggs", "Two eggs, spicy pork, refried beans, salsa verde, hash browns, corn tortillas"),
        ("Chorizo Scramble", "Chorizo, onion, tomato, jalapeño, pico de gallo, jack &amp; cheddar, hash browns, corn tortillas"),
        ("Joe's Special", "Scrambled eggs, ground beef, spinach, onion, mushroom, jack &amp; cheddar, hash browns, toast or pancakes"),
        ("Breakfast Burrito", "Flour tortilla, scrambled eggs, chorizo, avocado, tomatoes, pinto beans, jack &amp; white cheddar, hash browns, tomatillo salsa"),
        ("Biscuits &amp; Gravy Deluxe", "Two eggs, biscuits, country gravy, two pieces of bacon"),
        ("Meat Lovers Scramble", "Scrambled eggs, linguica, sausage, bacon, ham, mushrooms, onions, jack &amp; cheddar, hash browns, toast or pancakes"),
        ("Santa Cruz Scramble", "Scrambled eggs, artichoke hearts, mushrooms, onion, spinach, jack &amp; cheddar, hash browns, toast or pancakes"),
        ("Chicken Fried Steak &amp; Eggs", "Country gravy"),
    ]),
    ("Omelette Soufflés", "All served with jack &amp; white cheddar, hash browns and toast or pancakes.", [
        ("Supreme", "Linguica, pork sausage, bacon, ham, mushroom, bell peppers, Spanish sauce"),
        ("Crab", "Lump and snow crab, fresh avocado, tomato, hollandaise"),
        ("Philly", "Rib-eye sliced thin, melted Swiss, mushrooms, bell peppers, onions"),
        ("California", "Avocado, tomato, mushrooms"),
        ("Mushroom &amp; Avocado", "Mushrooms, avocado, spinach"),
        ("Bacon &amp; Avocado", "Bacon, avocado, mushroom"),
        ("Garden", "Zucchini, onion, bell pepper, mushrooms, spinach, avocado"),
        ("Denver", "Ham, onion, bell pepper"),
    ]),
    ("Benedicts", "Poached eggs, English muffin, hollandaise and hash browns.", [
        ("Eggs Benedict", "Thick-cut Canadian bacon"),
        ("California Benedict", "Canadian bacon, avocado, tomato"),
        ("Steak &amp; Avocado", "Thinly sliced Angus steak, avocado, tomato"),
        ("Blackened Salmon", "Fresh filet strips, spinach, avocado, cilantro, red onions, sour cream"),
        ("Crab &amp; Avocado", "Lump crab, spinach, avocado, cilantro, red onions, sour cream"),
    ]),
    ("The Classics", "Two large eggs, hash browns and toast or pancakes.", [
        ("Rib Eye Steak &amp; Eggs", "10 oz. aged Angus beef"),
        ("Portuguese Linguica &amp; Eggs", "Mildly spiced Evergood sausage"),
        ("Bacon &amp; Eggs", "Four thick slices of hickory smoked bacon"),
        ("Chicken Apple Sausage &amp; Eggs", "All natural Evergood"),
        ("Hash &amp; Eggs", "Old fashioned corned beef hash"),
        ("Ham &amp; Eggs", "Hickory smoked"),
        ("Sausage &amp; Eggs", "All natural skinless sausage"),
    ]),
    ("Hot Off the Griddle", None, [
        ("Buttermilk Pancakes", "Full stack of three, or a short stack of two"),
        ("Swedish Crepes", "Four French crepes, lingonberry butter, powdered sugar"),
        ("Fresh Fruit Crepes", "Three French crepes, strawberries, blueberries, bananas, powdered sugar, whipped cream"),
        ("French Toast", "Texas toast dipped in special egg batter, two strips of bacon, powdered sugar"),
        ("Berries &amp; Cream French Toast", "Strawberries, blueberries, powdered sugar, whipped cream"),
        ("Belgian Waffle", "Plain, blueberry, strawberry, chocolate or banana walnut"),
        ("Banana Walnut Pancakes", "Three buttermilk pancakes, banana, walnut, powdered sugar, whipped cream"),
        ("Chocolate Pancakes", "Three buttermilk pancakes, Hershey's chocolate &amp; chips, powdered sugar, whipped cream"),
    ]),
    ("Healthy Choice", None, [
        ("Fresh Veggie Scramble", "Egg whites, zucchini, onion, bell pepper, spinach, avocado, mushroom, fire roasted salsa, fresh fruit, toast"),
        ("Protein Scramble", "Egg whites, chicken apple sausage, spinach, onion, mushrooms, fire roasted salsa, fresh fruit, toast"),
        ("Keto Scramble", "Three eggs, broccoli, cauliflower, zucchini, avocado, Swiss, two strips of bacon, cup of fresh fruit"),
        ("Petite Steak", "6 oz. flat iron, egg whites, avocado, fresh fruit, toast, charred corn salsa"),
        ("Morning Starter", "Oatmeal, raisin, banana, fresh fruit, toast"),
    ]),
]

LUNCH = [
    ("Small Plates", None, [
        ("Jack's Chicken Wings", "Large drumettes and wings with your choice of Korean BBQ, bourbon glaze, mango, parmesan garlic, sweet and spicy or spicy"),
        ("Pecan Smoked Ribs", "Meaty St. Louis ribs, French fries, house BBQ sauce"),
        ("Blackened Salmon Tacos", "Shredded cabbage, avocado, jalapeño vinaigrette, cilantro aioli, pinto beans"),
        ("Shrimp &amp; Grits", "Large shrimp, chipotle garlic sauce, southern white grits"),
        ("Thai Chicken Lettuce Wraps", "Asian slaw, rice noodles, peanut sauce"),
        ("Fish and Chips", "Beer battered Alaskan cod, French fries, cole slaw"),
        ("Calamari", "Fresh calamari, panko bread crumbs, deep fried, chipotle tartar"),
        ("Tempura Green Beans", "Crispy green beans, saffron aioli"),
    ]),
    ("Harris Ranch Burgers", None, [
        ("Hamburger", "Lettuce, tomato, pickles, special sauce"),
        ("Bacon Cheeseburger", "Aged cheddar cheese, bacon, lettuce, tomato, pickles, special sauce"),
        ("49er Burger", "Bacon, grilled onion, jack &amp; cheddar, special sauce, grilled sourdough"),
        ("Black n Bleu", "Bleu cheese crumbles, cajun spice, lettuce, tomato, pickles, special sauce"),
        ("California Burger", "Swiss, avocado, lettuce, tomato, pickles, special sauce"),
        ("Mushroom Burger", "Mushrooms, Swiss, lettuce, tomato, pickles, special sauce"),
        ("Vegetarian Burger", "Black bean patty, Swiss, avocado, lettuce, tomato, sprouts, special sauce"),
        ("Cheeseburger Special", "The cheeseburger, your choice of cheese, and an old-fashioned milkshake"),
    ]),
    ("Signature Sandwiches", None, [
        ("Steak &amp; Avocado", "Thinly sliced Angus steak, chipotle aioli, avocado, grilled onions, jack &amp; white cheddar, ciabatta roll"),
        ("Prime Rib Dip", "Thinly sliced prime rib of beef, Swiss cheese, au jus, ciabatta roll"),
        ("Crab Melt", "Lump crab, prawns, avocado, tomato, jack &amp; cheddar on grilled sourdough"),
        ("Crispy Chicken Sandwich", "All natural breast, cabbage, dijon mustard, ciabatta roll"),
        ("The Reuben", "Tender corned beef, sauerkraut, Swiss, 1000 Island, pickles, grilled rye"),
        ("Clubhouse", "Triple decker, turkey, bacon, lettuce, tomato, sourdough toast"),
        ("Rosemary Chicken", "All natural chicken breast, bacon, lettuce, pesto aioli, Swiss, tomatoes, ciabatta roll"),
        ("Turkey &amp; Avocado", "Turkey, avocado, jack &amp; white cheddar, lettuce, sprouts, pesto aioli, ciabatta roll"),
        ("Grilled B.L.T.", "Bacon, lettuce, tomato, mayonnaise, grilled sourdough"),
        ("The Vegetarian", "Avocado, lettuce, tomatoes, cucumber, sprouts, pesto aioli, jack &amp; white cheddars, ciabatta roll"),
    ]),
    ("Steak &amp; Pasta", None, [
        ("Rib Eye Steak", "10 oz. aged Angus beef, maître d' butter, fresh veggies, mashed potatoes"),
        ("New York Steak", "12 oz. Angus beef, bell peppers, mushrooms, demi-glace, fresh veggies, mashed potatoes"),
        ("Pasta Jambalaya", "Shrimp, chicken, cajun hot sausage, sweet peppers, tomato, chipotle cream sauce, penne, garlic bread"),
        ("Prawn Pomodoro", "Large prawns, tomato, basil, garlic, olive oil, parmesan, linguini, garlic bread"),
        ("Rosemary Chicken Raviolis", "Pasta stuffed with rosemary chicken, provolone, white garlic cream sauce, mushroom, pancetta, garlic bread"),
        ("Chicken Pesto Pasta", "All natural chicken breast, mushrooms, pine nuts, basil, olive oil, linguini, garlic bread"),
        ("Pasta Bolognese", "Ground beef, sausage, marinara, penne pasta, garlic bread"),
        ("Pasta Primavera", "Fresh broccoli, cauliflower, zucchini, squash, red onions, marinara over linguine, garlic bread"),
    ]),
    ("Farm Fresh Salads", None, [
        ("Apple Harvest Salad", "Grilled chicken breast, apple, avocado, tomato, cucumber, walnuts, cranberries, crumbled bleu cheese, apple cider dressing"),
        ("Blackened Salmon Salad", "Seared salmon filet, tomatoes, cucumbers, olives, mixed greens, balsamic vinaigrette"),
        ("Steakhouse Salad", "Aged Angus flat iron steak, bleu cheese crumbles, tomatoes, cucumbers, mixed greens, balsamic vinaigrette"),
        ("Crab Salad", "Lump and snow crab meat, cucumbers, tomato, boiled egg, avocado, fresh greens, choice of dressing"),
        ("Chinese Chicken Salad", "All natural chicken breast, shredded lettuce, cabbage, peanuts, rice noodles, spicy mandarin dressing"),
        ("Chopped Cobb Salad", "All natural chicken breast, mixed greens, bacon bits, avocado, tomatoes, cucumbers, hard boiled eggs, bleu cheese crumbles"),
    ]),
    ("Flatbreads &amp; Jack's Fries", None, [
        ("Margherita Flatbread", "Tomato, mozzarella, fresh basil, olive oil, parmesan"),
        ("BBQ Chicken Flatbread", "BBQ sauce, mozzarella, chicken breast, red onion, cilantro"),
        ("Rio Grande Flatbread", "Nacho cheese sauce, chorizo, sliced jalapeño, onions, cilantro, sour cream"),
        ("Pepperoni Flatbread", "Tomato sauce, pepperoni, mozzarella cheese"),
        ("Gilroy Garlic Fries", "Garlic, parmesan, fresh parsley"),
        ("Truffle Fries", "Truffle oil, shaved parmesan, parsley"),
        ("Buffalo Fries", "Spicy buffalo sauce, bleu cheese crumbles, fresh parsley, buttermilk ranch"),
        ("Chili Cheese Fries", "Nacho cheese sauce, chorizo, sliced jalapeño, onions, cilantro, sour cream"),
    ]),
]

BAR = [
    ("Sunrise Cocktails", "Poured from the moment we open at 7am.", [
        ("Brazilian Mimosa", "Brazilian mango mix, simple syrup, sparkling wine"),
        ("Mimosa Sunrise", "Sauza silver tequila, champagne, orange &amp; pineapple juice, grenadine"),
        ("Classic Mimosa", "Wolf Blass Brut"),
        ("Bellini", "Peach purée, simple syrup, sparkling wine"),
        ("Aperol Spritz", "Prosecco, Aperol, soda water, orange slice"),
        ("Chavela", "Modelo Especial, salted rim, lime juice"),
        ("Michelada", "Modelo, tomato juice"),
        ("Jack's Iced Coffee", "Stoli vanilla, Kahlúa, alchemist spiced syrup, coffee, cream, nutmeg"),
    ]),
    ("On Tap", "Fourteen rotating handles — local Bay Area brewers, West Coast IPAs, lagers and seasonals. Ask your server what just kicked.", [
        ("Draft Beer", "Fourteen taps, poured cold all day"),
        ("Bottles &amp; Cans", "Domestics, imports and non-alcoholic options"),
        ("Wine by the Glass", "Reds, whites and sparkling"),
    ]),
    ("God Bless Bourbon", "Our bourbon program — the reason the sign says what it says.", [
        ("Bourbon Flights", "Three pours, side by side, picked by the bar"),
        ("Old Fashioned", "Your bourbon, sugar, bitters, big cube"),
        ("Craft Cocktails", "Classics done right, plus whatever the bar is playing with this month"),
    ]),
]


# --------------------------------------------------------------------------
# template
# --------------------------------------------------------------------------

def nav_html(current):
    links = []
    for key, label, href in NAV:
        cls = ' class="current"' if key == current else ""
        links.append(f'      <a href="{href}"{cls}>{label}</a>')
    links.append(f'      <a href="{GIFT}">Gift Cards</a>')
    return "\n".join(links)


def page(current, title, description, body, schema="", canonical=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<!-- Concept demo on a third-party domain: canonical points at the real site and
     noindex keeps this copy of their menu from cannibalising their own rankings. -->
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="https://jackholders.com{canonical}">
<link rel="icon" href="{IMG}/cropped-Jack_Holders_Logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{IMG}/site.css">
</head>
<body>

<div class="demo-ribbon">
  CONCEPT DEMO &mdash; built for Jack Holder's by <a href="https://gullstack.com">GullStack</a>. Not the live site.
</div>

<div class="utility">
  <div class="wrap">
    <div class="utility-left">
      <span class="dot-open"></span>
      <span id="open-status">Open today &middot; 7:00am &ndash; 9:00pm</span>
    </div>
    <div class="utility-right">
      <span class="hide-sm">3153 Meridian Ave, Willow Glen</span>
      <a href="{PHONE_LINK}">{PHONE_DISPLAY}</a>
    </div>
  </div>
</div>

<nav class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="/jack-holders-demo" aria-label="Jack Holder's Restaurant &amp; Bar">
      <img src="{IMG}/cropped-Jack_Holders_Logo.png" alt="Jack Holder's Restaurant &amp; Bar">
    </a>
    <div class="nav-links" id="navLinks">
{nav_html(current)}
    </div>
    <div class="nav-cta">
      <a class="btn btn-ghost" href="{PHONE_LINK}">Call</a>
      <a class="btn btn-primary" href="{ORDER}">Order Online</a>
      <button class="nav-toggle" id="navToggle" aria-label="Menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>

{body}

<section class="cta-band">
  <div class="narrow">
    <h2>Hungry now?</h2>
    <p>Start an order for pickup, or just walk in &mdash; we're open until 9.</p>
    <div class="cta-actions">
      <a class="btn btn-primary" href="{ORDER}">Order Online</a>
      <a class="btn btn-light" href="{PHONE_LINK}">Call {PHONE_DISPLAY}</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="{IMG}/cropped-Jack_Holders_Logo.png" alt="Jack Holder's Restaurant &amp; Bar">
        <p>Everyday eatery and family-friendly tavern in Willow Glen, San Jose. All-day breakfast and American comfort food.</p>
      </div>
      <div>
        <h4>Menus</h4>
        <a href="/jack-holders-demo/breakfast">Breakfast</a>
        <a href="/jack-holders-demo/lunch-dinner">Lunch &amp; Dinner</a>
        <a href="/jack-holders-demo/bar">Cocktails &amp; Bar</a>
      </div>
      <div>
        <h4>Order</h4>
        <a href="{ORDER}">Order Online</a>
        <a href="{GIFT}">Gift Cards</a>
        <a href="{PHONE_LINK}">Call for Large Parties</a>
      </div>
      <div>
        <h4>Visit</h4>
        <a href="/jack-holders-demo/visit">Hours &amp; Directions</a>
        <a href="/jack-holders-demo/about">Our Story</a>
        <a href="https://www.facebook.com/Jackholdersrandb/">Facebook</a>
        <a href="https://www.instagram.com/jackholdersrandb/">Instagram</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="yr">2026</span> Jack Holder's Restaurant &amp; Bar. All rights reserved.</span>
      <span class="gullstack-credit">Concept site built by <a href="https://gullstack.com">GullStack</a></span>
    </div>
  </div>
</footer>

<div class="mobile-bar">
  <a href="{PHONE_LINK}">Call</a>
  <a class="order" href="{ORDER}">Order Online</a>
</div>
{schema}
<script>
(function(){{
  document.getElementById('yr').textContent = new Date().getFullYear();

  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');
  toggle.addEventListener('click', function(){{
    var open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }});
  links.querySelectorAll('a').forEach(function(a){{
    a.addEventListener('click', function(){{
      links.classList.remove('open');
      toggle.setAttribute('aria-expanded','false');
    }});
  }});

  var now = new Date();
  var day = now.getDay();
  var closeHour = (day === 0) ? 20 : 21;
  var mins = now.getHours() * 60 + now.getMinutes();
  var isOpen = mins >= 7 * 60 && mins < closeHour * 60;
  var closeLabel = (day === 0) ? '8:00pm' : '9:00pm';

  var status = document.getElementById('open-status');
  var dot = document.querySelector('.dot-open');
  if (isOpen) {{
    status.textContent = 'Open now \\u00b7 until ' + closeLabel;
  }} else {{
    status.textContent = 'Closed \\u00b7 opens 7:00am';
    dot.style.background = '#C3922E';
    dot.style.boxShadow = '0 0 0 3px rgba(195,146,46,.2)';
  }}

  var row = document.querySelector('.hours-table tr[data-day="' + day + '"]');
  if (row) row.classList.add('today');
}})();
</script>

</body>
</html>
"""


def menu_groups(groups):
    out = []
    for name, note, items in groups:
        anchor = name.lower().replace("&amp;", "and").replace("'", "").replace(" ", "-")
        anchor = "".join(c for c in anchor if c.isalnum() or c == "-")
        out.append(f'        <div class="menu-group" id="{anchor}">')
        out.append(f"          <h2>{name}</h2>")
        if note:
            out.append(f'          <div class="note">{note}</div>')
        for item, desc in items:
            out.append(
                f'          <div class="item"><div class="name">{item}</div>'
                f'<div class="desc">{desc}</div></div>'
            )
        out.append("        </div>")
    return "\n".join(out)


def jump_nav(groups):
    out = ['<div class="jump"><div class="wrap"><div class="jump-inner">']
    for name, _, _ in groups:
        anchor = name.lower().replace("&amp;", "and").replace("'", "").replace(" ", "-")
        anchor = "".join(c for c in anchor if c.isalnum() or c == "-")
        out.append(f'  <a href="#{anchor}">{name}</a>')
    out.append("</div></div></div>")
    return "\n".join(out)


def page_head(eyebrow, h1, sub, image, crumb):
    return f"""<header class="page-head">
  <div class="page-head-img"><img src="{IMG}/{image}" alt=""></div>
  <div class="wrap page-head-inner">
    <div class="crumbs"><a href="/jack-holders-demo">Home</a> &nbsp;&rsaquo;&nbsp; {crumb}</div>
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p>{sub}</p>
  </div>
</header>"""


def menu_page(groups, eyebrow, h1, sub, image, crumb, foot_note, foot_cta, foot_href):
    return f"""{page_head(eyebrow, h1, sub, image, crumb)}

{jump_nav(groups)}

<section class="menu-section">
  <div class="wrap">
    <div class="menu-cols">
{menu_groups(groups)}
    </div>
    <div class="menu-foot">
      <p>{foot_note}</p>
      <a class="btn btn-primary" href="{foot_href}">{foot_cta}</a>
    </div>
  </div>
</section>"""


GALLERY_IMAGES = [
    ("french-toast-jack-holders-restaurant-bar-and-grill-willow-glen.jpg", "French toast with berries and whipped cream"),
    ("hamburger-jack-holders-restaurant-bar-and-grill-willow-glen-scaled.jpg", "Harris Ranch burger with fries"),
    ("eggs-benedict-jack-holders-restaurant-bar-and-grill-willow-glen.jpg", "Eggs benedict with hash browns"),
    ("chicken-tacos-jack-holders-restaurant-bar-and-grill-willow-glen.jpg", "Blackened salmon tacos with avocado and slaw"),
    ("omlette-jack-holders-restaurant-bar-and-grill-willow-glen.jpg", "Omelette soufflé with hash browns"),
    ("plate-of-pasta-with-garlic-bread-and-tomatoes-with-red-sauce.jpg", "Pasta with garlic bread and red sauce"),
    ("salad-jack-holders-restaurant-bar-and-grill-willow-glen.jpg", "Farm fresh salad"),
    ("syrup-dripping-onto-pancakes-with-with-butter.jpg", "Syrup dripping onto buttermilk pancakes"),
    ("sandwich-jack-holders-restaurant-bar-and-grill-willow-glen.jpg", "Signature sandwich with fries"),
    ("lemon-cocktail-jack-holders-willow-glen.jpg", "Lemon cocktail"),
]


def gallery():
    rows = []
    for src, alt in GALLERY_IMAGES:
        rows.append(f'    <img src="{IMG}/{src}" alt="{alt}">')
    for src, _ in GALLERY_IMAGES:
        rows.append(f'    <img src="{IMG}/{src}" alt="" aria-hidden="true">')
    return '<div class="gallery">\n  <div class="marquee">\n' + "\n".join(rows) + "\n  </div>\n</div>"


HOURS_ROWS = "\n".join(
    f'        <tr data-day="{d}"><td>{name}</td><td>{hrs}</td></tr>'
    for d, name, hrs in [
        (1, "Monday", "7:00am &ndash; 9:00pm"),
        (2, "Tuesday", "7:00am &ndash; 9:00pm"),
        (3, "Wednesday", "7:00am &ndash; 9:00pm"),
        (4, "Thursday", "7:00am &ndash; 9:00pm"),
        (5, "Friday", "7:00am &ndash; 9:00pm"),
        (6, "Saturday", "7:00am &ndash; 9:00pm"),
        (0, "Sunday", "7:00am &ndash; 8:00pm"),
    ]
)

RESTAURANT_SCHEMA = """
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Restaurant",
  "name":"Jack Holder's Restaurant & Bar",
  "url":"https://jackholders.com/",
  "image":"https://jackholders.com/wp-content/uploads/2023/07/best-restaurant-willow-glen-plates-of-food.webp",
  "description":"Family-owned everyday eatery and family-friendly tavern in Willow Glen, San Jose, serving all-day breakfast, American comfort food, 14 beers on tap and craft cocktails.",
  "telephone":"+1-408-613-2365",
  "servesCuisine":["American","Breakfast","Comfort Food"],
  "priceRange":"$$",
  "address":{
    "@type":"PostalAddress",
    "streetAddress":"3153 Meridian Avenue, Suite 20",
    "addressLocality":"San Jose",
    "addressRegion":"CA",
    "postalCode":"95124",
    "addressCountry":"US"
  },
  "areaServed":["Willow Glen","San Jose","Cambrian Park","Campbell","Los Gatos"],
  "openingHoursSpecification":[
    {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"07:00","closes":"21:00"},
    {"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"07:00","closes":"20:00"}
  ],
  "acceptsReservations":"False",
  "hasMenu":"https://order.toasttab.com/online/jackholders",
  "potentialAction":{
    "@type":"OrderAction",
    "target":{"@type":"EntryPoint","urlTemplate":"https://order.toasttab.com/online/jackholders","inLanguage":"en-US"},
    "deliveryMethod":"http://purl.org/goodrelations/v1#PickUp"
  },
  "sameAs":[
    "https://www.facebook.com/Jackholdersrandb/",
    "https://www.instagram.com/jackholdersrandb/"
  ]
}
</script>"""

FAQ_SCHEMA = """
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Do you serve breakfast all day?","acceptedAnswer":{"@type":"Answer","text":"Yes. Every breakfast item is available from open at 7am until close, including omelette souffles, benedicts, pancakes and crepes."}},
    {"@type":"Question","name":"What are Jack Holder's hours?","acceptedAnswer":{"@type":"Answer","text":"Open 7:00am to 9:00pm Monday through Saturday, and 7:00am to 8:00pm on Sunday, seven days a week."}},
    {"@type":"Question","name":"Can I order online for pickup?","acceptedAnswer":{"@type":"Answer","text":"Yes. Order online any time we're open, usually ready in about 20 minutes, or call (408) 613-2365."}},
    {"@type":"Question","name":"Do you take reservations or large parties?","acceptedAnswer":{"@type":"Answer","text":"Jack Holder's is walk-in, but larger groups, birthdays and team dinners can be arranged by calling (408) 613-2365."}},
    {"@type":"Question","name":"Do you sell gift cards?","acceptedAnswer":{"@type":"Answer","text":"Yes. Gift cards are available online in any amount and are delivered by email."}},
    {"@type":"Question","name":"Is there parking, and are kids welcome?","acceptedAnswer":{"@type":"Answer","text":"There is a free lot in front on Meridian Avenue. Jack Holder's is a family-friendly tavern with high chairs and a dog-friendly patio."}}
  ]
}
</script>"""


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

def build_home():
    body = f"""<header class="hero">
  <div class="hero-img">
    <img src="{IMG}/best-restaurant-willow-glen-plates-of-food.webp"
         alt="Overhead spread of French toast, eggs benedict, salmon tacos, Chinese chicken salad and cocktails at Jack Holder's">
  </div>
  <div class="hero-content">
    <div class="wrap">
      <span class="hero-tag">Willow Glen &middot; San Jose</span>
      <h1>Breakfast served <em>all day.</em> Every day.</h1>
      <p>A family-owned everyday eatery and family-friendly tavern. Pancakes at 7am, a burger and a cold draft at 7pm, and a patio that's happy to see you either way.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{ORDER}">Order Pickup</a>
        <a class="btn btn-light" href="/jack-holders-demo/breakfast">See the Menus</a>
      </div>
    </div>
  </div>
</header>

<div class="strip">
  <div class="wrap" style="padding:0">
    <div class="strip-grid">
      <a class="strip-item" href="{ORDER}">
        <span class="k">Order Online</span>
        <span class="v">Pickup, ready in about 20 minutes</span>
        <span class="arrow">START AN ORDER &rarr;</span>
      </a>
      <a class="strip-item" href="{GIFT}">
        <span class="k">Gift Cards</span>
        <span class="v">Delivered by email, any amount</span>
        <span class="arrow">BUY A CARD &rarr;</span>
      </a>
      <a class="strip-item" href="{PHONE_LINK}">
        <span class="k">Large Parties</span>
        <span class="v">Call ahead and we'll set the table</span>
        <span class="arrow">{PHONE_DISPLAY} &rarr;</span>
      </a>
      <a class="strip-item" href="/jack-holders-demo/visit">
        <span class="k">Find Us</span>
        <span class="v">3153 Meridian Ave, Ste 20</span>
        <span class="arrow">HOURS &amp; DIRECTIONS &rarr;</span>
      </a>
    </div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="eyebrow">The Menus</div>
    <h2 class="section-title">Everything, all day.</h2>
    <p class="lede">Breakfast doesn't stop at 11. Order any of it, any hour we're open.</p>

    <div class="menu-cards">
      <a class="menu-card" href="/jack-holders-demo/breakfast">
        <img src="{IMG}/french-toast-jack-holders-restaurant-bar-and-grill-willow-glen.jpg" alt="French toast with strawberries and whipped cream">
        <div class="body">
          <h3>Breakfast</h3>
          <p>Omelette souffl&eacute;s, benedicts, Swedish crepes, chicken fried steak and a griddle that never cools off. Served 7am to close.</p>
          <span class="go">See the breakfast menu &rarr;</span>
        </div>
      </a>
      <a class="menu-card" href="/jack-holders-demo/lunch-dinner">
        <img src="{IMG}/hamburger-jack-holders-restaurant-bar-and-grill-willow-glen-scaled.jpg" alt="Harris Ranch burger with fries">
        <div class="body">
          <h3>Lunch &amp; Dinner</h3>
          <p>Harris Ranch burgers, pecan-smoked ribs, prime rib dip, pasta jambalaya and six farm-fresh salads.</p>
          <span class="go">See lunch &amp; dinner &rarr;</span>
        </div>
      </a>
      <a class="menu-card" href="/jack-holders-demo/bar">
        <img src="{IMG}/cocktail-jack-holders-willow-glen.jpg" alt="Craft cocktail at the Jack Holder's bar">
        <div class="body">
          <h3>Cocktails &amp; Bar</h3>
          <p>Fourteen beers on tap, morning mimosas, craft cocktails and the bourbon list the sign out back is named for.</p>
          <span class="go">See the bar menu &rarr;</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="dark-feature">
  <div class="wrap split">
    <div>
      <div class="eyebrow">God Bless Bourbon</div>
      <h2 class="section-title">Fourteen taps and a patio that stays warm.</h2>
      <p>The tavern half of Jack Holder's runs from open to close. Cold drafts, craft cocktails, an honest bourbon list and a patio where nobody minds if you stay for the second half.</p>
      <div class="stat-row">
        <div class="stat"><div class="n">14</div><div class="l">Beers on tap</div></div>
        <div class="stat"><div class="n">7am</div><div class="l">Mimosas start</div></div>
        <div class="stat"><div class="n">9pm</div><div class="l">Last call, Mon&ndash;Sat</div></div>
      </div>
      <a class="btn btn-light" href="/jack-holders-demo/bar">See the bar menu</a>
    </div>
    <div class="photo-pair">
      <img src="{IMG}/cocktail-jack-holders-willow-glen.jpg" alt="Craft cocktail served at the Jack Holder's bar">
      <img src="{IMG}/bloody-mary-in-a-glass-with-bacon-olives-and-vegetables.jpg" alt="Bloody Mary garnished with bacon, olives and vegetables">
    </div>
  </div>
</section>

<section class="proof">
  <div class="wrap">
    <div class="eyebrow">The Neighborhood Verdict</div>
    <h2 class="section-title">Willow Glen keeps coming back.</h2>
    <p class="lede">Thousands of reviews across the platforms that matter &mdash; and a dining room that's full on a Tuesday.</p>
    <div class="proof-grid">
      <div class="proof-card">
        <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="score">4.4</div>
        <div class="src">Google reviews</div>
        <div class="cnt">1,100+ ratings</div>
      </div>
      <div class="proof-card">
        <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="score">4.4</div>
        <div class="src">Aggregated across platforms</div>
        <div class="cnt">2,900+ ratings</div>
      </div>
      <div class="proof-card">
        <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="score">750+</div>
        <div class="src">Yelp reviews</div>
        <div class="cnt">843 photos and counting</div>
      </div>
    </div>
  </div>
</section>

{gallery()}

<section>
  <div class="wrap split">
    <div class="split-copy">
      <div class="eyebrow">Our Story</div>
      <h2 class="section-title">The neighborhood's kitchen table.</h2>
      <p class="first">We're family-owned, we're on Meridian Ave, and we've spent years getting this menu exactly right.</p>
      <p>Jack Holder's isn't trying to be the newest thing in San Jose. We're the place you bring your parents on Sunday morning and your softball team on Thursday night.</p>
      <a class="btn btn-ghost" href="/jack-holders-demo/about" style="margin-top:12px">Read our story</a>
    </div>
    <div class="split-media">
      <img src="{IMG}/Jack-Holders-Photos_web-29.jpg" alt="The Jack Holder's Restaurant &amp; Bar sign on Meridian Avenue in Willow Glen">
      <div class="split-badge">
        <div class="n">7am</div>
        <div class="l">Doors open, seven days a week</div>
      </div>
    </div>
  </div>
</section>"""
    return page(
        "home",
        "Jack Holder's Restaurant &amp; Bar | All-Day Breakfast in Willow Glen, San Jose",
        "Family-owned everyday eatery and family-friendly tavern in Willow Glen. All-day breakfast, Harris Ranch burgers, 14 beers on tap and craft cocktails. Open 7am daily. Order online or call (408) 613-2365.",
        body,
        schema=RESTAURANT_SCHEMA,
        canonical="/",
    )


def build_breakfast():
    body = menu_page(
        BREAKFAST,
        "Served 7am to close",
        "The breakfast menu.",
        "Every item below is available from the minute we open until the minute we lock the door. Order a rib eye and eggs at 8pm &mdash; we won't blink.",
        "french-toast-jack-holders-restaurant-bar-and-grill-willow-glen.jpg",
        "Breakfast",
        "Live prices, add-ons and today's availability are on the ordering menu.",
        "View prices &amp; order",
        ORDER,
    )
    return page(
        "breakfast",
        "Breakfast Menu | Jack Holder's Restaurant &amp; Bar, Willow Glen",
        "All-day breakfast in Willow Glen: omelette souffles, eggs benedict, Swedish crepes, chicken fried steak and buttermilk pancakes. Served 7am to close, seven days a week.",
        body,
        canonical="/breakfast-menu/",
    )


def build_lunch():
    body = menu_page(
        LUNCH,
        "Served 11am to close",
        "Lunch &amp; dinner.",
        "Harris Ranch burgers, pecan-smoked ribs, steaks off the broiler and pasta that comes with garlic bread whether you asked or not.",
        "hamburger-jack-holders-restaurant-bar-and-grill-willow-glen-scaled.jpg",
        "Lunch &amp; Dinner",
        "Live prices, add-ons and today's availability are on the ordering menu.",
        "View prices &amp; order",
        ORDER,
    )
    return page(
        "lunch-dinner",
        "Lunch &amp; Dinner Menu | Jack Holder's Restaurant &amp; Bar, Willow Glen",
        "Harris Ranch burgers, pecan-smoked ribs, prime rib dip, pasta jambalaya, rib eye and New York steaks, and six farm-fresh salads in Willow Glen, San Jose.",
        body,
        canonical="/lunch-and-dinner-menu/",
    )


def build_bar():
    body = menu_page(
        BAR,
        "God Bless Bourbon",
        "The bar.",
        "Fourteen rotating taps, mimosas from 7am, craft cocktails and a bourbon list we take personally. Open every hour the kitchen is.",
        "bloody-mary-in-a-glass-with-bacon-olives-and-vegetables.jpg",
        "The Bar",
        "Full bar open until close. Happy hour on the patio is the neighborhood's worst-kept secret.",
        "Call the bar",
        PHONE_LINK,
    )
    return page(
        "bar",
        "Cocktails, Beer &amp; Bourbon | Jack Holder's Restaurant &amp; Bar, Willow Glen",
        "Fourteen beers on tap, morning mimosas, craft cocktails and the God Bless Bourbon list at Jack Holder's in Willow Glen, San Jose.",
        body,
        canonical="/drink-menu/",
    )


def build_about():
    body = f"""{page_head(
        "Since day one",
        "Family-owned, and it shows.",
        "Jack Holder's isn't trying to be the newest thing in San Jose. We're trying to be the one you keep coming back to.",
        "Jack-Holders-Photos_web-29.jpg",
        "Our Story",
    )}

<section>
  <div class="wrap split">
    <div class="split-copy">
      <div class="eyebrow">The Kitchen</div>
      <h2 class="section-title">A menu we've spent years getting right.</h2>
      <p class="first">Omelette souffl&eacute;s and Swedish crepes before noon. Harris Ranch burgers, pecan-smoked ribs and pasta jambalaya after. Fourteen beers on tap the whole time.</p>
      <p>Everything is made to order. The portions are honest. Nobody rushes you off the patio, and if you want breakfast at eight at night, that's between you and your conscience &mdash; the griddle's still hot.</p>
      <p>We're the place you bring your parents on Sunday morning and your softball team on Thursday night. That's not an accident. It's the whole point.</p>
      <a class="btn btn-ghost" href="/jack-holders-demo/breakfast" style="margin-top:12px">Browse the menu</a>
    </div>
    <div class="split-media">
      <img src="{IMG}/omlette-jack-holders-restaurant-bar-and-grill-willow-glen.jpg" alt="Omelette souffl&eacute; with hash browns at Jack Holder's">
    </div>
  </div>
</section>

<section class="dark-feature">
  <div class="wrap">
    <div class="eyebrow">What To Expect</div>
    <h2 class="section-title">Come as you are.</h2>
    <div class="stat-row" style="margin-top:44px">
      <div class="stat"><div class="n">7 days</div><div class="l">Open every week</div></div>
      <div class="stat"><div class="n">All day</div><div class="l">Breakfast never stops</div></div>
      <div class="stat"><div class="n">Free</div><div class="l">Lot parking out front</div></div>
    </div>
    <p style="max-width:58ch">Family friendly with high chairs, a dog-friendly patio, big tables for big groups, and a bar that'll pour you a mimosa at 7:02am without judgment.</p>
  </div>
</section>

<section class="faq">
  <div class="narrow">
    <div class="eyebrow">Good Questions</div>
    <h2 class="section-title" style="margin-bottom:36px">Before you come in.</h2>

    <details class="q" open>
      <summary>Do you serve breakfast all day?</summary>
      <p>Yes. Every breakfast item &mdash; omelette souffl&eacute;s, benedicts, pancakes, crepes, the whole list &mdash; is available from the moment we open at 7am until we close. You can order a rib eye and eggs at 8pm.</p>
    </details>
    <details class="q">
      <summary>What are your hours?</summary>
      <p>We're open 7:00am to 9:00pm Monday through Saturday, and 7:00am to 8:00pm on Sunday. Seven days a week.</p>
    </details>
    <details class="q">
      <summary>Can I order online for pickup?</summary>
      <p>Yes &mdash; order online any time we're open and it's usually ready in about 20 minutes. You can also call the restaurant directly at {PHONE_DISPLAY}.</p>
    </details>
    <details class="q">
      <summary>Do you take reservations or large parties?</summary>
      <p>We're a walk-in dining room, but we're glad to plan ahead for larger groups, birthdays and team dinners. Call us at {PHONE_DISPLAY} and we'll get the table set.</p>
    </details>
    <details class="q">
      <summary>Do you sell gift cards?</summary>
      <p>We do. Gift cards are available online in any amount and are delivered by email, so you can buy one five minutes before you need it.</p>
    </details>
    <details class="q">
      <summary>Is there parking, and are kids welcome?</summary>
      <p>There's a free lot right out front on Meridian. We're a family-friendly tavern &mdash; high chairs, a kids-welcome dining room and a patio that works for strollers and dogs alike.</p>
    </details>
    <details class="q">
      <summary>Do you have vegetarian and lighter options?</summary>
      <p>Plenty. The Healthy Choice breakfast section runs egg-white scrambles and a keto scramble, and lunch has a black bean burger, the vegetarian sandwich, flatbreads and six farm-fresh salads.</p>
    </details>
  </div>
</section>"""
    return page(
        "about",
        "Our Story | Jack Holder's Restaurant &amp; Bar, Willow Glen San Jose",
        "Family-owned everyday eatery and family-friendly tavern on Meridian Avenue in Willow Glen. All-day breakfast, American comfort food, full bar and a dog-friendly patio.",
        body,
        schema=FAQ_SCHEMA,
        canonical="/about-us/",
    )


def build_visit():
    body = f"""{page_head(
        "Willow Glen, San Jose",
        "Find us on Meridian.",
        "Free lot out front, open seven days a week from 7am, and a patio that's usually got a seat.",
        "best-restaurant-willow-glen-plates-of-food.webp",
        "Visit",
    )}

<section>
  <div class="wrap visit-grid">
    <div>
      <div class="eyebrow">Hours</div>
      <h2 class="section-title">Open every day.</h2>
      <table class="hours-table">
{HOURS_ROWS}
      </table>
      <div class="visit-detail">
        <div class="lbl">Address</div>
        <a href="{MAPS}">3153 Meridian Avenue, Suite 20<br>San Jose, CA 95124</a>
      </div>
      <div class="visit-detail">
        <div class="lbl">Phone</div>
        <a href="{PHONE_LINK}">{PHONE_DISPLAY}</a>
      </div>
      <div class="visit-detail">
        <div class="lbl">Good to know</div>
        <p>Free lot parking. Family friendly, high chairs available. Dog-friendly patio. Large parties welcome &mdash; call ahead.</p>
      </div>
      <a class="btn btn-primary" href="{MAPS}">Get directions</a>
    </div>
    <div>
      <iframe class="map-embed" loading="lazy" title="Map to Jack Holder's Restaurant &amp; Bar"
        src="https://www.google.com/maps?q=3153+Meridian+Ave+Ste+20,+San+Jose,+CA+95124&amp;output=embed"></iframe>
    </div>
  </div>
</section>

<div class="strip">
  <div class="wrap" style="padding:0">
    <div class="strip-grid">
      <a class="strip-item" href="{ORDER}">
        <span class="k">Order Online</span>
        <span class="v">Pickup, ready in about 20 minutes</span>
        <span class="arrow">START AN ORDER &rarr;</span>
      </a>
      <a class="strip-item" href="{GIFT}">
        <span class="k">Gift Cards</span>
        <span class="v">Delivered by email, any amount</span>
        <span class="arrow">BUY A CARD &rarr;</span>
      </a>
      <a class="strip-item" href="{PHONE_LINK}">
        <span class="k">Large Parties</span>
        <span class="v">Call ahead and we'll set the table</span>
        <span class="arrow">{PHONE_DISPLAY} &rarr;</span>
      </a>
      <a class="strip-item" href="https://www.instagram.com/jackholdersrandb/">
        <span class="k">Follow Along</span>
        <span class="v">Specials, events and what's on tap</span>
        <span class="arrow">INSTAGRAM &rarr;</span>
      </a>
    </div>
  </div>
</div>"""
    return page(
        "visit",
        "Hours, Location &amp; Directions | Jack Holder's Restaurant &amp; Bar",
        "Jack Holder's is at 3153 Meridian Avenue, Suite 20, San Jose CA 95124. Open 7am-9pm Monday-Saturday and 7am-8pm Sunday. Free parking, dog-friendly patio, (408) 613-2365.",
        body,
        schema=RESTAURANT_SCHEMA,
        canonical="/contact/",
    )


PAGES = {
    ROOT / "jack-holders-demo.html": build_home,
    OUT_DIR / "breakfast.html": build_breakfast,
    OUT_DIR / "lunch-dinner.html": build_lunch,
    OUT_DIR / "bar.html": build_bar,
    OUT_DIR / "about.html": build_about,
    OUT_DIR / "visit.html": build_visit,
}


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for path, fn in PAGES.items():
        path.write_text(fn(), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}  ({len(path.read_text(encoding='utf-8')):,} bytes)")


if __name__ == "__main__":
    main()
