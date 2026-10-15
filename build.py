# Static site generator: python3 build.py -> writes HTML into ./public
import os, html
CATS = [
 ("Manga & Comic Artists","✒️","Line art, inking, full-page sequential storytelling for print and digital."),
 ("Webtoon Creators","📱","Vertical-scroll series creators, colorists and background artists."),
 ("Illustrators","🎨","Key visuals, covers, character design, splash art and merch art."),
 ("Writers & Scriptwriters","📖","Original stories, adaptations, light novels and comic scripts."),
 ("Animators","🎞️","2D/3D animation, motion graphics, openings and promo clips."),
 ("Voice Actors","🎙️","Dubbing, VTuber voices, games, audio dramas and ads."),
 ("VTubers","🦊","Virtual talent with rigged avatars, lore and loyal communities."),
 ("Streamers","🎮","Live creators on Twitch, YouTube, Kick and beyond."),
 ("Content Creators","🎬","YouTube, TikTok and Shorts creators covering anime & comics culture."),
 ("Influencers","✨","Social-first tastemakers who move fandoms."),
 ("Cosplayers","🧵","Costume artists, prop makers, con guests and photo-shoot talent."),
 ("Models","📸","Fashion, editorial and anime-collab campaign models."),
 ("Actors","🎭","Live-action adaptation talent, stage and screen."),
 ("Celebrities","🌟","Mainstream stars crossing into anime, gaming and comics."),
 ("Musicians & Singers","🎵","Anisong artists, composers, producers and J/K-pop crossover."),
 ("Dancers & Performers","💃","Idol-style performers, choreographers and event acts."),
 ("Game & Esports Talent","🕹️","Pro players, casters and gaming personalities."),
 ("Podcasters & Critics","🎧","Hosts, reviewers and community voices."),
 ("Photographers & Directors","🎥","Cosplay photographers, MV and promo directors."),
 ("Translators & Localizers","🌐","Manga/webtoon translation, lettering and subtitling."),
]
SERV = [
 ("Brand Deals & Sponsorships","Matchmaking with brands, negotiation, contracts and campaign delivery."),
 ("Licensing & IP","Protect, license and expand original characters, comics and webtoons."),
 ("Events & Conventions","Con guest bookings, panels, signings, live performances and tours."),
 ("Talent Management","Career strategy, scheduling, contracts and day-to-day representation."),
 ("Publishing & Adaptation","Pitching to publishers, platforms and studios for print, anime and live-action."),
 ("Merch & Commerce","Merch design, production partners and storefront launches."),
]
NAV=[("index.html","Home"),("talent.html","Talent"),("roster.html","Roster"),("services.html","Services"),("about.html","About"),("apply.html","Apply / Contact")]
def page(fn,title,body):
    nav="".join(f'<a href="{h}"{" class=active" if h==fn else ""}>{t}</a>' for h,t in NAV)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Human Agency</title><meta name="description" content="Human Agency — talent representation for anime, webtoons, comics and the creators, streamers and stars around them.">
<link rel="stylesheet" href="styles.css"></head><body>
<header class="nav"><a class="logo" href="index.html">HUMAN<span>AGENCY</span></a><nav>{nav}</nav></header>
<main>{body}</main>
<footer><p>© 2026 Human Agency · Talent for anime, webtoons & comics</p><p><a href="apply.html">Join the roster</a> · <a href="mailto:hello@humanagency.example">hello@humanagency.example</a></p></footer>
</body></html>'''
cards="".join(f'<div class="card"><div class="ico">{i}</div><h3>{html.escape(n)}</h3><p>{d}</p></div>' for n,i,d in CATS)
serv="".join(f'<div class="card"><h3>{n}</h3><p>{d}</p></div>' for n,d in SERV)
P={}
P["index.html"]=("Home",f'''<section class="hero"><p class="tag">Anime · Webtoons · Comics · Creators</p><h1>We represent the people<br>behind the <em>panels</em>.</h1>
<p class="lead">Human Agency is a talent agency for the artists, creators, streamers and stars shaping anime, webtoon and comic culture.</p>
<div class="btns"><a class="btn" href="apply.html">Apply as talent</a><a class="btn ghost" href="services.html">Work with our talent</a></div></section>
<section><h2>Who we represent</h2><div class="grid">{cards[:0]}{"".join(f'<a class="chip" href="talent.html">{i} {n}</a>' for n,i,_ in CATS)}</div></section>
<section><h2>What we do</h2><div class="grid">{serv}</div></section>
<section class="cta"><h2>Brands, studios, publishers and cons —</h2><p>tell us what you need and we'll match you with the right talent.</p><a class="btn" href="apply.html#brand">Start a booking</a></section>''')
P["talent.html"]=("Talent Categories",f'<section><h1>Talent categories</h1><p class="lead">Every corner of the fandom, under one roof.</p><div class="grid">{cards}</div></section>')
ro="".join(f'<div class="card talent"><div class="avatar">{i}</div><h3>Talent Name</h3><p class="muted">{n}</p><p>Profile coming soon.</p></div>' for n,i,_ in CATS[:12])
P["roster.html"]=("Roster",f'<section><h1>Roster</h1><p class="lead">Our signed talent will appear here. <span class="badge">Placeholder</span></p><div class="grid">{ro}</div></section>')
P["services.html"]=("Services",f'<section><h1>Services</h1><p class="lead">Full-stack representation for creative talent and the brands who want to work with them.</p><div class="grid">{serv}</div></section><section class="cta"><a class="btn" href="apply.html#brand">Request a proposal</a></section>')
P["about.html"]=("About",'''<section class="narrow"><h1>About Human Agency</h1><p class="lead">Built by fans, run like an agency.</p>
<p>Anime, webtoons and comics have become global culture — but the people who make and carry that culture are often unrepresented. Human Agency exists to change that: we sign, protect and grow creative talent, from the illustrator drawing tonight's chapter to the voice actor, cosplayer, streamer or celebrity bringing it to life.</p>
<h2>Our values</h2><ul><li><b>Creators first.</b> Fair deals, transparent splits, creator-owned IP.</li><li><b>Fandom fluent.</b> We know the culture because we live in it.</li><li><b>Global by default.</b> Japan, Korea, the Americas, Europe and SEA.</li></ul></section>''')
opts="".join(f"<option>{html.escape(n)}</option>" for n,_,_ in CATS)
P["apply.html"]=("Apply / Contact",f'''<section class="narrow"><h1>Apply or get in touch</h1><p class="lead">No account needed. Submitting opens your email app with the details pre-filled.</p>
<form id="f"><div class="seg"><label><input type="radio" name="type" value="Talent application" checked> I'm talent</label><label id="brand"><input type="radio" name="type" value="Brand / booking inquiry"> I'm a brand / studio / event</label></div>
<label>Name<input name="name" required></label><label>Email<input name="email" type="email" required></label>
<label>Category<select name="category">{opts}<option>Other</option></select></label>
<label>Links (portfolio, socials, channel)<input name="links" placeholder="https://"></label>
<label>Message<textarea name="msg" rows="5"></textarea></label><button class="btn" type="submit">Send</button></form></section>
<script>document.getElementById('f').onsubmit=e=>{{e.preventDefault();const d=new FormData(e.target);const s=`${{d.get('type')}}: ${{d.get('name')}}`;const b=[...d.entries()].map(([k,v])=>k+': '+v).join('\\n');location.href='mailto:hello@humanagency.example?subject='+encodeURIComponent(s)+'&body='+encodeURIComponent(b);}};</script>''')
os.makedirs("public",exist_ok=True)
for fn,(t,b) in P.items(): open(f"public/{fn}","w").write(page(fn,t,b))
