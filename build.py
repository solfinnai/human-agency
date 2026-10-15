# Static site generator: python3 build.py -> writes HTML into ./public
# Content: desks/services/copy below; niche taxonomy in data/niches.json (from the Oct 15 2026 research).
import os, html, json
from collections import OrderedDict
E=html.escape
DESKS = [
 ("Webtoon, Comic & Manga Creators","✒️","Webtoon Originals and CANVAS creators, mangaka, comic artists, writers, colorists and letterers. We grow readerships, land publishing and platform deals, and take your IP to screen without taking it from you."),
 ("Cosplayers","🧵","Costume and prop makers, con guests and photo-shoot talent. Guest bookings, brand campaigns, prints and merch."),
 ("Voice Actors","🎙️","Dub, anime, game, audio-drama and VTuber voices. Casting submissions and brand reads, with union-aware deal handling."),
 ("Indie VTubers","🦊","Independent virtual talent. Sponsorships, collabs and merch, with transparent payouts and none of the corporate lock-in."),
 ("Anime & Gaming Creators","🎮","AnimeTubers, reviewers, streamers, editors and gaming personalities who move the fandom every week."),
]
SERV = [
 ("Talent Management","Career strategy, scheduling, negotiation support and day-to-day representation from people who know the fandom."),
 ("Brand-Deals Desk","Fandom-native sponsorship packages that brands can buy and audiences actually like: integrations, campaigns, con activations."),
 ("Licensing & Adaptation Desk","Publishing, merch, games and animation licensing for creator-owned IP. Film and TV deals run through our licensed partner agency."),
 ("Events & Conventions","Con guest bookings, panels, signings, meet-and-greets and live performances."),
 ("Merch","Design, production partners and storefront launches for prints, figures, apparel and more."),
]
DIFF = [
 ("You keep your IP","Your characters, comics and channels stay yours. We license and grow them; we never take ownership."),
 ("Transparent payouts","Clear statements, on-time payments and visibility into every deal. Talent should never chase their own money."),
 ("Fandom-native brand packages","Campaigns built by fans for fans, so sponsors feel at home in anime, webtoon, cosplay and VTuber spaces."),
]
D=json.load(open("data/niches.json"))
CL=OrderedDict()
for n in sorted(D["niches"],key=lambda n:-n["fit"]): CL.setdefault(n["cluster"],[]).append(n)
NAV=[("index.html","Home"),("talent.html","Talent"),("roster.html","Roster"),("services.html","Services"),("about.html","About"),("apply.html","Apply / Contact")]
def page(fn,title,body):
    nav="".join(f'<a href="{h}"{" class=active" if h==fn else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Human Agency</title><meta name="description" content="Human Agency is the talent agency for fandom: the people behind the panels and the stars around them.">
<link rel="stylesheet" href="styles.css"></head><body>
<header class="nav"><a class="logo" href="index.html">HUMAN<span>AGENCY</span></a><nav>{nav}</nav></header>
<main>{body}</main>
<footer><p>© 2026 Human Agency · The talent agency for fandom</p><p><a href="apply.html">Join the roster</a> · <a href="mailto:hello@humanagency.example">hello@humanagency.example</a></p></footer>
</body></html>'''
desk_cards="".join(f'<div class="card"><div class="ico">{i}</div><h3>{E(n)}</h3><p>{d}</p></div>' for n,i,d in DESKS)
serv="".join(f'<div class="card"><h3>{n}</h3><p>{d}</p></div>' for n,d in SERV)
diff="".join(f'<div class="card"><h3>{n}</h3><p>{d}</p></div>' for n,d in DIFF)
def niches(full):
    out=[]
    for c,ns in CL.items():
        if full:
            items="".join(f'<details><summary>{E(n["niche"])}{" <span class=badge>Flagship</span>" if n["cluster"]=="Fandom & pop culture" else ""}</summary><p>{E(" · ".join(n["roles"]))}</p></details>' for n in ns)
            out.append(f'<div class="cluster"><h3>{E(c)}</h3>{items}</div>')
        else:
            out.append(f'<div class="card"><h3>{E(c)}</h3><p>{E(", ".join(n["niche"] for n in ns))}</p></div>')
    return "".join(out)
uni=OrderedDict()
for g,r in D["universal"]: uni.setdefault(g,[]).append(r)
uni_html="".join(f'<div class="card"><h3>{E(g)}</h3><p>{E(" · ".join(rs))}</p></div>' for g,rs in uni.items())
P={}
P["index.html"]=("Home",f'''<section class="hero"><p class="tag">The talent agency for fandom</p><h1>The people behind the <em>panels</em>,<br>and the stars around them.</h1>
<p class="lead">Human Agency represents webtoon, comic and manga creators, cosplayers, voice actors, indie VTubers and anime &amp; gaming creators, and turns their audiences and IP into careers.</p>
<div class="btns"><a class="btn" href="apply.html">Apply as talent</a><a class="btn ghost" href="services.html">Work with our talent</a></div></section>
<section><h2>Our core desks</h2><div class="grid">{desk_cards}</div></section>
<section><h2>Why Human Agency</h2><div class="grid">{diff}</div></section>
<section><h2>What we do</h2><div class="grid">{serv}</div></section>
<section><h2>Niches we're building</h2><p class="lead">Fandom is our flagship. We're building desks across every niche where audiences gather.</p><div class="grid">{niches(False)}</div><p><a href="talent.html#niches">See every niche and role →</a></p></section>
<section class="cta"><h2>Brands, studios, publishers and cons</h2><p>Tell us what you need and we'll put together a fandom-native package.</p><a class="btn" href="apply.html#brand">Start a booking</a></section>''')
P["talent.html"]=("Talent Categories",f'''<section><h1>Talent we represent</h1><p class="lead">Year one, we're focused on five fandom desks.</p><div class="grid">{desk_cards}</div></section>
<section id="niches"><h2>Niches we're building</h2><p class="lead">Fandom is the flagship, and Human Agency is built for every niche. Tap a niche to see its roles.</p><div class="clusters">{niches(True)}</div></section>
<section><h2>Roles in every niche</h2><div class="grid">{uni_html}</div></section>''')
ro="".join(f'<div class="card talent"><div class="avatar">{i}</div><h3>Talent Name</h3><p class="muted">{E(n)}</p><p>Profile coming soon.</p></div>' for n,i,_ in DESKS for _ in (0,1))
P["roster.html"]=("Roster",f'<section><h1>Roster</h1><p class="lead">Our signed talent will appear here. <span class="badge">Placeholder</span></p><div class="grid">{ro}</div></section>')
P["services.html"]=("Services",f'''<section><h1>Services</h1><p class="lead">Management, brand deals, licensing and adaptation, events and merch, all built around creator-owned IP.</p><div class="grid">{serv}</div></section>
<section><h2>How we work</h2><div class="grid">{diff}</div></section><section class="cta"><a class="btn" href="apply.html#brand">Request a proposal</a></section>''')
P["about.html"]=("About",'''<section class="narrow"><h1>About Human Agency</h1><p class="lead">The talent agency for fandom.</p>
<p>Anime, webtoons, comics, cosplay and VTubing are global culture, yet most of the people who make that culture have no representation. Big agencies chase mainstream celebrities, and platforms don't advocate for individual creators. Human Agency represents the people behind the panels and the stars around them, and turns their audiences and IP into lasting careers.</p>
<h2>What we stand for</h2><ul><li><b>You keep your IP.</b> We license and grow your work. We never take ownership of it.</li><li><b>Transparent payouts.</b> Clear statements and on-time payments, every time.</li><li><b>Fandom-native.</b> We build brand packages that feel at home in the community.</li></ul>
<h2>Where we're going</h2><p>We're starting with five fandom desks and building toward every niche where audiences gather, from gaming and music to film, fitness and travel. Screen deals are handled through a licensed partner agency.</p></section>''')
opts="".join(f"<option>{E(n)}</option>" for n,_,_ in DESKS)+"".join(f"<option>{E(n['niche'])}</option>" for ns in CL.values() for n in ns if n['cluster']!='Fandom & pop culture')
P["apply.html"]=("Apply / Contact",f'''<section class="narrow"><h1>Apply or get in touch</h1><p class="lead">No account needed. Submitting opens your email app with the details pre-filled.</p>
<form id="f"><div class="seg"><label><input type="radio" name="type" value="Talent application" checked> I'm talent</label><label id="brand"><input type="radio" name="type" value="Brand / booking inquiry"> I'm a brand / studio / event</label></div>
<label>Name<input name="name" required></label><label>Email<input name="email" type="email" required></label>
<label>Desk / niche<select name="category">{opts}<option>Other</option></select></label>
<label>Links (portfolio, socials, channel)<input name="links" placeholder="https://"></label>
<label>Message<textarea name="msg" rows="5"></textarea></label><button class="btn" type="submit">Send</button></form></section>
<script>document.getElementById('f').onsubmit=e=>{{e.preventDefault();const d=new FormData(e.target);const s=`${{d.get('type')}}: ${{d.get('name')}}`;const b=[...d.entries()].map(([k,v])=>k+': '+v).join('\\n');location.href='mailto:hello@humanagency.example?subject='+encodeURIComponent(s)+'&body='+encodeURIComponent(b);}};</script>''')
os.makedirs("public",exist_ok=True)
for fn,(t,b) in P.items(): open(f"public/{fn}","w").write(page(fn,t,b))
