#!/usr/bin/env python3

import json
import random
import shutil
from pathlib import Path
from datetime import datetime

# =========================================================
# CONFIG
# =========================================================

SITE_NAME = "Crossout Wasteland HQ"

DOMAIN = "https://YOURUSERNAME.github.io/crossout"

AFFILIATE_URL = "https://convert.ctypy.com/aff_c?offer_id=29178&aff_id=21885"

YEAR = datetime.now().year

# =========================================================
# SEO KEYWORDS
# =========================================================

KEYWORDS = [
    "crossout best builds",
    "crossout beginner guide",
    "crossout best weapons",
    "crossout pvp guide",
    "crossout factions explained",
    "crossout best cabins",
    "crossout crafting guide",
    "crossout vehicle builds",
    "crossout free to play",
    "crossout tips and tricks"
]

# =========================================================
# PAGES
# =========================================================

PAGES = [
    {
        "slug": "index",
        "title": "Crossout Beginner Guide & Best Builds",
        "keyword": "crossout beginner guide",
        "description": "Learn the best Crossout builds, weapons, cabins, and PvP strategies."
    },
    {
        "slug": "best-weapons",
        "title": "Best Crossout Weapons",
        "keyword": "crossout best weapons",
        "description": "Discover the strongest weapons in Crossout for PvP and PvE."
    },
    {
        "slug": "best-builds",
        "title": "Best Crossout Vehicle Builds",
        "keyword": "crossout best builds",
        "description": "Top Crossout vehicle builds for speed, armor, and firepower."
    },
    {
        "slug": "factions",
        "title": "Crossout Factions Guide",
        "keyword": "crossout factions explained",
        "description": "Learn all Crossout factions and unlock powerful gear."
    },
    {
        "slug": "crafting",
        "title": "Crossout Crafting Guide",
        "keyword": "crossout crafting guide",
        "description": "Master crafting, farming, and resource management in Crossout."
    },
    {
        "slug": "pvp",
        "title": "Crossout PvP Guide",
        "keyword": "crossout pvp guide",
        "description": "Win more PvP battles with advanced Crossout combat tactics."
    },
    {
        "slug": "cabins",
        "title": "Best Crossout Cabins",
        "keyword": "crossout best cabins",
        "description": "The best cabins for tank, speed, and hybrid builds."
    },
    {
        "slug": "tips",
        "title": "Crossout Tips & Tricks",
        "keyword": "crossout tips and tricks",
        "description": "Advanced Crossout gameplay tips to improve faster."
    },
]

# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).parent
DIST = BASE_DIR / "dist"
ASSETS = DIST / "assets"

if DIST.exists():
    shutil.rmtree(DIST)

DIST.mkdir()
ASSETS.mkdir()

# =========================================================
# CSS
# =========================================================

CSS = """
body{
    background:#0d0d0d;
    color:#ddd;
    font-family:Arial,sans-serif;
    margin:0;
    line-height:1.7;
}

header{
    background:#151515;
    padding:20px;
    border-bottom:3px solid #ff6600;
    position:sticky;
    top:0;
    z-index:999;
}

.logo{
    font-size:2rem;
    color:#ff6600;
    font-weight:bold;
}

nav{
    margin-top:15px;
}

nav a{
    color:#ccc;
    text-decoration:none;
    margin-right:15px;
    font-weight:bold;
}

nav a:hover{
    color:#ff6600;
}

.hero{
    padding:100px 20px;
    text-align:center;
    background:#1a1a1a;
}

.hero h1{
    font-size:3rem;
    color:#ff6600;
}

.container{
    width:92%;
    max-width:1200px;
    margin:auto;
    padding:40px 0;
}

.card{
    background:#181818;
    padding:30px;
    border-radius:10px;
    border:1px solid #333;
    margin-bottom:30px;
}

.cta{
    display:inline-block;
    background:#ff6600;
    color:white;
    padding:14px 28px;
    border-radius:5px;
    text-decoration:none;
    font-weight:bold;
    margin-top:20px;
}

.cta:hover{
    background:#ff8533;
}

.related a{
    display:block;
    color:#ff6600;
    margin-bottom:10px;
}

footer{
    background:#111;
    padding:40px;
    text-align:center;
    border-top:3px solid #ff6600;
}
"""

(ASSETS / "style.css").write_text(CSS)

# =========================================================
# NAVIGATION
# =========================================================

def nav():

    html = []

    for p in PAGES:

        filename = (
            "index.html"
            if p["slug"] == "index"
            else f"{p['slug']}.html"
        )

        html.append(f'<a href="{filename}">{p["title"]}</a>')

    return "\n".join(html)

# =========================================================
# RELATED LINKS
# =========================================================

def related_links(current_slug):

    links = []

    for p in PAGES:

        if p["slug"] == current_slug:
            continue

        filename = (
            "index.html"
            if p["slug"] == "index"
            else f"{p['slug']}.html"
        )

        links.append(
            f'<a href="{filename}">{p["title"]}</a>'
        )

    random.shuffle(links)

    return "\n".join(links[:5])

# =========================================================
# HTML TEMPLATE
# =========================================================

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">

<title>{title}</title>

<meta name="description" content="{description}">
<meta name="keywords" content="{keyword}">

<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="assets/style.css">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">

<script type="application/ld+json">
{schema}
</script>

</head>

<body>

<header>

<div class="logo">
{site_name}
</div>

<nav>
{navigation}
</nav>

</header>

<section class="hero">

<h1>{title}</h1>

<p>
{description}
</p>

<a class="cta" href="{affiliate}">
Play Crossout Free
</a>

</section>

<section class="container">

<div class="card">

<h2>{keyword}</h2>

<p>
Crossout is one of the most competitive post-apocalyptic vehicle combat MMOs available today.
Players can build fully customized war machines using armor, cabins, weapons, boosters, drones, and advanced movement systems.
</p>

<p>
Whether you enjoy PvP arena combat, raids, crafting, or faction grinding, Crossout delivers deep progression and endless build combinations.
</p>

<p>
This guide covers advanced gameplay strategies, beginner tips, build optimization, crafting systems, and faction progression.
</p>

<a class="cta" href="{affiliate}">
Start Playing Crossout
</a>

</div>

<div class="card">

<h2>Why Players Love Crossout</h2>

<ul>
<li>Deep vehicle customization</li>
<li>Fast-paced PvP combat</li>
<li>Unique faction technology</li>
<li>Huge weapon variety</li>
<li>Free-to-play progression</li>
<li>Massive build creativity</li>
</ul>

</div>

<div class="card related">

<h2>Related Guides</h2>

{related}

</div>

</section>

<footer>

<p>
© {year} {site_name}
</p>

<p>
Built for Crossout fans and wasteland warriors.
</p>

<a class="cta" href="{affiliate}">
Join Crossout Now
</a>

</footer>

</body>
</html>
"""

# =========================================================
# GENERATE PAGES
# =========================================================

for page in PAGES:

    filename = (
        "index.html"
        if page["slug"] == "index"
        else f"{page['slug']}.html"
    )

    canonical = (
        DOMAIN + "/"
        if page["slug"] == "index"
        else f"{DOMAIN}/{page['slug']}.html"
    )

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": page["title"],
        "description": page["description"]
    }, indent=2)

    html = TEMPLATE.format(
        title=page["title"],
        description=page["description"],
        keyword=page["keyword"],
        canonical=canonical,
        navigation=nav(),
        affiliate=AFFILIATE_URL,
        related=related_links(page["slug"]),
        schema=schema,
        site_name=SITE_NAME,
        year=YEAR
    )

    (DIST / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# SITEMAP
# =========================================================

urls = []

for page in PAGES:

    if page["slug"] == "index":
        loc = DOMAIN + "/"
    else:
        loc = f"{DOMAIN}/{page['slug']}.html"

    urls.append(f"""
<url>
<loc>{loc}</loc>
</url>
""")

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

{''.join(urls)}

</urlset>
"""

(DIST / "sitemap.xml").write_text(sitemap)

# =========================================================
# ROBOTS
# =========================================================

robots = f"""
User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""

(DIST / "robots.txt").write_text(robots)

# =========================================================
# CONFIG EXPORT
# =========================================================

with open(DIST / "site.json", "w") as f:
    json.dump(PAGES, f, indent=2)

print("====================================")
print("CROSSOUT MONEY SITE GENERATED")
print("====================================")
print(f"Pages: {len(PAGES)}")
print(f"Output: {DIST}")
print("Ready for GitHub Pages deployment")
