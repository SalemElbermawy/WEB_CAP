import streamlit as st
import base64
from pathlib import Path

# ── Page config ───────────────────────────────────────────────
st.set_page_config(page_title="Our Team", page_icon="💧", layout="wide")

# ── Helper: local image → base64 data URI ─────────────────────
def img_to_b64(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    suffix = p.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(suffix, "jpeg")
    data = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/{mime};base64,{data}"

def resolve(src: str) -> str:
    """Accept a local path or a URL."""
    if src.startswith("http://") or src.startswith("https://"):
        return src
    return img_to_b64(src)

# ── CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --aqua:       #2ec4b6;
    --aqua-dark:  #1a8f84;
    --aqua-light: #a8ede8;
    --aqua-glow:  rgba(46,196,182,0.18);
    --bg:         #04191a;
    --border:     rgba(46,196,182,0.25);
    --text:       #d6f5f3;
    --muted:      #6ab8b3;
}
html, body, [class*="css"], .stApp {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem !important; max-width: 1200px; }

/* Hero */
.hero-wrapper { text-align: center; padding: 3rem 0 1.5rem; position: relative; }
.hero-wrapper::before {
    content: '';
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%,-50%);
    width: 600px; height: 180px;
    background: radial-gradient(ellipse, var(--aqua-glow) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3rem,7vw,5.5rem);
    font-weight: 300;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    background: linear-gradient(135deg, var(--aqua-light) 0%, var(--aqua) 50%, var(--aqua-dark) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0; line-height: 1.1;
}
.hero-sub { font-size: 0.85rem; letter-spacing: 0.35em; text-transform: uppercase; color: var(--muted); margin-top: 0.6rem; }
.hero-divider { width: 80px; height: 2px; background: linear-gradient(90deg, transparent, var(--aqua), transparent); margin: 1.4rem auto; }

/* Banner */
.banner-frame {
    border-radius: 16px; overflow: hidden;
    border: 1px solid var(--border);
    box-shadow: 0 0 0 1px var(--border), 0 20px 80px rgba(0,0,0,0.7), 0 0 60px var(--aqua-glow);
    margin: 1.5rem 0 3rem; position: relative;
}
.banner-frame img { width: 100%; height: 420px; object-fit: cover; display: block; transition: transform 0.6s ease; }
.banner-frame:hover img { transform: scale(1.02); }
.banner-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(to bottom, transparent 55%, rgba(4,25,26,0.85) 100%);
}

/* Section label */
.section-label {
    font-size: 0.72rem; letter-spacing: 0.4em; text-transform: uppercase;
    color: var(--aqua); margin-bottom: 1.5rem;
    display: flex; align-items: center; gap: 1rem;
}
.section-label::after { content: ''; flex: 1; height: 1px; background: var(--border); }

/* Member card */
.member-card {
    background: linear-gradient(145deg, rgba(7,31,32,0.95), rgba(10,40,42,0.9));
    border: 1px solid var(--border); border-radius: 14px; overflow: hidden;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    position: relative;
}
.member-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, var(--aqua-dark), var(--aqua), var(--aqua-light));
    opacity: 0; transition: opacity 0.3s;
}
.member-card:hover { transform: translateY(-6px); box-shadow: 0 24px 60px rgba(0,0,0,0.5), 0 0 30px var(--aqua-glow); border-color: var(--aqua); }
.member-card:hover::before { opacity: 1; }

.member-img-wrap { width: 100%; padding-top: 100%; position: relative; overflow: hidden; background: #0a2829; }
.member-img-wrap img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease; }
.member-card:hover .member-img-wrap img { transform: scale(1.07); }
.member-img-overlay { position: absolute; inset: 0; background: linear-gradient(to bottom, transparent 50%, rgba(4,25,26,0.8) 100%); }
.no-img { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 3rem; background: linear-gradient(135deg, #0a2829, #071f20); }

.member-info { padding: 1rem 1rem 1.3rem; }
.member-name { font-family: 'Cormorant Garamond', serif; font-size: 1.25rem; font-weight: 600; color: var(--text); margin: 0 0 0.2rem; letter-spacing: 0.04em; }
.member-role { font-size: 0.72rem; letter-spacing: 0.22em; text-transform: uppercase; color: var(--aqua); margin: 0; }
.member-badge { display: inline-block; width: 28px; height: 2px; background: var(--aqua); margin: 0.6rem auto 0; border-radius: 2px; opacity: 0.7; }

.footer { text-align: center; margin-top: 4rem; font-size: 0.75rem; letter-spacing: 0.2em; color: var(--muted); text-transform: uppercase; opacity: 0.6; }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
#  ✏️  EDIT HERE — put your file names or URLs
# ══════════════════════════════════════════════════════════════

HERO_IMAGE = "salem3.jpg"        # ← your big image (same folder as this script)

TEAM_MEMBERS = [
    {"name": "Anas Hessen",   "role": "Team Lead",   "image": "salem.jpg"},
    {"name": "Mohamed Shawky",   "role": "Developer",   "image": "shawky.jpg"},
    {"name": "Mohamed Hamdy", "role": "Designer",    "image": "hamdy.jpg"},
    {"name": "Salem Elbermawy",  "role": "Researcher",  "image": "salem.jpg"},
]

# ══════════════════════════════════════════════════════════════

# Hero title
st.markdown("""
<div class="hero-wrapper">
    <p class="hero-sub">✦ &nbsp; Welcome to &nbsp; ✦</p>
    <h1 class="hero-title">Aquagreen</h1>
    <div class="hero-divider"></div>
    <p class="hero-sub">Crafting tomorrow&rsquo;s solutions</p>
</div>
""", unsafe_allow_html=True)

# Banner
hero_src = resolve(HERO_IMAGE)
if hero_src:
    st.markdown(f"""
    <div class="banner-frame">
        <img src="{hero_src}" alt="Team banner">
        <div class="banner-overlay"></div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning(f"⚠️ Image '{HERO_IMAGE}' not found — place it in the same folder as this script.")

# Team grid
st.markdown('<p class="section-label">Meet the Team</p>', unsafe_allow_html=True)
cols = st.columns(4, gap="large")

for col, member in zip(cols, TEAM_MEMBERS):
    src = resolve(member["image"])
    img_html = f'<img src="{src}" alt="{member["name"]}">' if src else '<div class="no-img">👤</div>'
    with col:
        st.markdown(f"""
        <div class="member-card">
            <div class="member-img-wrap">
                {img_html}
                <div class="member-img-overlay"></div>
            </div>
            <div class="member-info">
                <p class="member-name">{member['name']}</p>
                <p class="member-role">{member['role']}</p>
                <div class="member-badge"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="footer"> © 2026 Aquagreen STEM 6th October </div>', unsafe_allow_html=True)
