import streamlit as st
import base64
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="Project Graphs", page_icon="📊", layout="wide")

def img_to_b64(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    suffix = p.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(suffix, "jpeg")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

GRAPHS = [
    {
        "file":        "graphs/lux_5.png",
        "title":       "Light Intensity (Lux)",
        "description": "Light intensity readings over time captured by the sensor. Shows how ambient illumination varies across the observation period.",
        "tag":         "Lux",
        "accent":      "#2ec4b6",
    },
    {
        "file":        "graphs/distance_5.png",
        "title":       "Distance Measurement (CM)",
        "description": "Distance sensor readings in centimetres, reflecting object proximity changes detected by the system over the session.",
        "tag":         "Distance",
        "accent":      "#5dd6cd",
    },
    {
        "file":        "graphs/temp_5.png",
        "title":       "Temperature (°C)",
        "description": "Ambient temperature readings in Celsius recorded continuously by the system sensor throughout the monitoring period.",
        "tag":         "Temperature",
        "accent":      "#a8ede8",
    },
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=DM+Sans:wght@300;400;500&display=swap');
:root{
    --aqua:#2ec4b6;--aqua-dark:#1a8f84;--aqua-light:#a8ede8;
    --aqua-glow:rgba(46,196,182,0.14);--bg:#04191a;--surface:#071f20;
    --surface2:#0a2829;--border:rgba(46,196,182,0.2);--text:#d6f5f3;--muted:#6ab8b3;
}
html,body,[class*="css"],.stApp{background-color:var(--bg)!important;color:var(--text)!important;font-family:'DM Sans',sans-serif;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:2rem 2.5rem 4rem!important;max-width:1280px;}
section[data-testid="stSidebar"]{background:var(--bg)!important;border-right:1px solid var(--border)!important;}
.page-header{text-align:center;padding:2.5rem 0 2.2rem;position:relative;}
.page-header::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:500px;height:150px;background:radial-gradient(ellipse,var(--aqua-glow) 0%,transparent 70%);pointer-events:none;}
.page-title{font-family:'Cormorant Garamond',serif;font-size:clamp(2.2rem,5vw,4rem);font-weight:300;letter-spacing:0.18em;text-transform:uppercase;background:linear-gradient(135deg,var(--aqua-light),var(--aqua),var(--aqua-dark));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin:0;line-height:1.1;}
.page-sub{font-size:0.72rem;letter-spacing:0.35em;text-transform:uppercase;color:var(--muted);margin-top:0.6rem;opacity:0.8;}
.page-divider{width:60px;height:1.5px;background:linear-gradient(90deg,transparent,var(--aqua),transparent);margin:1.2rem auto 0;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <p class="page-sub">✦ &nbsp; CAP Project &nbsp; ✦</p>
    <h1 class="page-title">Visual Results</h1>
    <div class="page-divider"></div>
    <p class="page-sub">Key graphs from the project</p>
</div>
""", unsafe_allow_html=True)

g0, g1, g2 = GRAPHS[0], GRAPHS[1], GRAPHS[2]
src0 = img_to_b64(g0["file"])
src1 = img_to_b64(g1["file"])
src2 = img_to_b64(g2["file"])

def card_img_html(src, name, height):
    if src:
        return f'<img src="{src}" alt="{name}" style="width:100%;height:{height}px;object-fit:contain;display:block;padding:18px;transition:transform 0.5s ease;">'
    return f'<div style="width:100%;height:{height}px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:#6ab8b3;opacity:0.28;"><div style="font-size:2.5rem;">📊</div><div style="font-size:0.65rem;letter-spacing:0.15em;text-transform:uppercase;">{name}</div></div>'

def modal_img_html(src, name):
    if src:
        return f'<img src="{src}" alt="{name}" style="max-width:88vw;max-height:72vh;object-fit:contain;border-radius:8px;display:block;">'
    return f'<div style="color:#6ab8b3;opacity:0.32;padding:4rem 2rem;text-align:center;font-size:0.78rem;letter-spacing:0.15em;text-transform:uppercase;">Image not found:<br>{name}</div>'

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&family=DM+Sans:wght@300;400;500&display=swap');
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: transparent; font-family: 'DM Sans', sans-serif; }}

  @keyframes zoomIn {{ from {{ transform: scale(0.86); opacity: 0; }} to {{ transform: scale(1); opacity: 1; }} }}
  @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}

  .wrap {{ padding: 4px; display: flex; flex-direction: column; gap: 18px; }}

  .card-main {{
    background: #071f20; border: 1px solid rgba(46,196,182,0.22);
    border-radius: 20px; overflow: hidden; cursor: pointer; position: relative;
    transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
  }}
  .card-main::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2.5px;
    background: linear-gradient(90deg, #1a8f84, #2ec4b6, #a8ede8, #2ec4b6); opacity: 0.9;
  }}
  .card-main:hover {{
    transform: translateY(-5px);
    box-shadow: 0 28px 80px rgba(0,0,0,0.65), 0 0 50px rgba(46,196,182,0.18);
    border-color: rgba(46,196,182,0.55);
  }}
  .card-main:hover .img-zoom {{ transform: scale(1.025); }}
  .img-main {{ width: 100%; background: #0a2829; overflow: hidden; }}
  .img-zoom {{ transition: transform 0.5s ease; display: block; }}
  .footer-main {{
    padding: 16px 22px 18px; border-top: 1px solid rgba(46,196,182,0.15);
    display: flex; align-items: center; justify-content: space-between; gap: 16px;
    background: linear-gradient(90deg, rgba(7,31,32,0.98), rgba(10,40,42,0.95));
  }}
  .meta {{ flex: 1; }}
  .tag {{
    font-size: 0.58rem; letter-spacing: 0.2em; text-transform: uppercase;
    border-radius: 20px; padding: 3px 11px; display: inline-block; margin-bottom: 6px;
  }}
  .title-main {{ font-family: 'Cormorant Garamond', serif; font-size: 1.35rem; font-weight: 600; color: #d6f5f3; margin: 0 0 5px; }}
  .desc {{ font-size: 0.77rem; color: #6ab8b3; line-height: 1.65; margin: 0; opacity: 0.82; }}
  .zoom-badge {{
    font-size: 0.62rem; letter-spacing: 0.14em; text-transform: uppercase;
    color: #2ec4b6; background: rgba(4,25,26,0.9); border: 1px solid rgba(46,196,182,0.25);
    border-radius: 8px; padding: 6px 13px; white-space: nowrap; opacity: 0;
    transition: opacity 0.25s; pointer-events: none; flex-shrink: 0;
  }}
  .card-main:hover .zoom-badge {{ opacity: 1; }}

  .row-bottom {{ display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }}
  .card-small {{
    background: #071f20; border: 1px solid rgba(46,196,182,0.18);
    border-radius: 16px; overflow: hidden; cursor: pointer; position: relative;
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
  }}
  .card-small::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, #1a8f84, #2ec4b6, transparent);
    opacity: 0; transition: opacity 0.3s;
  }}
  .card-small:hover {{
    transform: translateY(-5px);
    box-shadow: 0 20px 55px rgba(0,0,0,0.6), 0 0 30px rgba(46,196,182,0.14);
    border-color: rgba(46,196,182,0.48);
  }}
  .card-small:hover::before {{ opacity: 1; }}
  .card-small:hover .img-zoom {{ transform: scale(1.04); }}
  .card-small:hover .zoom-sm {{ opacity: 1; }}
  .img-small {{ width: 100%; background: #0a2829; overflow: hidden; }}
  .footer-small {{
    padding: 12px 16px 38px; border-top: 1px solid rgba(46,196,182,0.12);
    background: rgba(7,31,32,0.96); position: relative;
  }}
  .tag-sm {{
    font-size: 0.56rem; letter-spacing: 0.18em; text-transform: uppercase;
    border-radius: 20px; padding: 2px 9px; display: inline-block; margin-bottom: 5px;
  }}
  .title-sm {{ font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; font-weight: 600; color: #d6f5f3; margin: 0 0 4px; }}
  .desc-sm {{ font-size: 0.73rem; color: #6ab8b3; line-height: 1.6; margin: 0; opacity: 0.78; }}
  .zoom-sm {{
    position: absolute; bottom: 10px; right: 12px;
    font-size: 0.56rem; letter-spacing: 0.12em; text-transform: uppercase;
    color: #2ec4b6; background: rgba(4,25,26,0.9); border: 1px solid rgba(46,196,182,0.22);
    border-radius: 6px; padding: 3px 8px; opacity: 0; transition: opacity 0.22s; pointer-events: none;
  }}

  .modal-overlay {{
    display: none; position: fixed; inset: 0;
    background: rgba(2,8,9,0.94); z-index: 99999;
    align-items: center; justify-content: center;
    backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
  }}
  .modal-overlay.active {{ display: flex; animation: fadeIn 0.2s ease; }}
  .modal-box {{
    background: #071f20; border: 1px solid rgba(46,196,182,0.45);
    border-radius: 20px; max-width: 92vw; overflow: hidden;
    display: flex; flex-direction: column;
    box-shadow: 0 50px 140px rgba(0,0,0,0.88), 0 0 80px rgba(46,196,182,0.12);
    animation: zoomIn 0.22s ease; position: relative;
  }}
  .modal-box::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2.5px;
    background: linear-gradient(90deg, #0d5e58, #1a8f84, #2ec4b6, #a8ede8);
  }}
  .modal-img-area {{
    background: #0a2829; display: flex; align-items: center;
    justify-content: center; padding: 28px;
  }}
  .modal-footer {{
    padding: 14px 20px; border-top: 1px solid rgba(46,196,182,0.18);
    display: flex; align-items: center; justify-content: space-between; gap: 14px;
  }}
  .modal-meta {{ flex: 1; }}
  .modal-tag {{
    font-size: 0.56rem; letter-spacing: 0.18em; text-transform: uppercase;
    background: rgba(46,196,182,0.08); border: 1px solid rgba(46,196,182,0.2);
    border-radius: 20px; padding: 2px 10px; display: inline-block; margin-bottom: 5px;
  }}
  .modal-title {{ font-family: 'Cormorant Garamond', serif; font-size: 1.15rem; font-weight: 600; color: #d6f5f3; margin: 0 0 3px; }}
  .modal-desc {{ font-size: 0.75rem; color: #6ab8b3; margin: 0; opacity: 0.75; line-height: 1.6; }}
  .close-btn {{
    width: 38px; height: 38px; border-radius: 10px;
    border: 1px solid rgba(46,196,182,0.28); background: #0a2829;
    color: #d6f5f3; font-size: 1.05rem; cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0; transition: border-color 0.18s, background 0.18s;
  }}
  .close-btn:hover {{ border-color: #2ec4b6; background: rgba(46,196,182,0.1); color: #2ec4b6; }}
</style>
</head>
<body>
<div class="wrap">

  <!-- TOP BIG CARD -->
  <div class="card-main" onclick="showModal(0)">
    <div class="img-main">{card_img_html(src0, g0["file"], 460)}</div>
    <div class="footer-main">
      <div class="meta">
        <span class="tag" style="color:{g0['accent']};border:1px solid {g0['accent']}55;background:{g0['accent']}18;">{g0["tag"]}</span>
        <p class="title-main">{g0["title"]}</p>
        <p class="desc">{g0["description"]}</p>
      </div>
      <span class="zoom-badge">🔍 Click to zoom</span>
    </div>
  </div>

  <!-- BOTTOM ROW -->
  <div class="row-bottom">
    <div class="card-small" onclick="showModal(1)">
      <div class="img-small">{card_img_html(src1, g1["file"], 280)}</div>
      <div class="footer-small">
        <span class="tag-sm" style="color:{g1['accent']};border:1px solid {g1['accent']}55;background:{g1['accent']}18;">{g1["tag"]}</span>
        <p class="title-sm">{g1["title"]}</p>
        <p class="desc-sm">{g1["description"]}</p>
        <span class="zoom-sm">🔍 Zoom</span>
      </div>
    </div>
    <div class="card-small" onclick="showModal(2)">
      <div class="img-small">{card_img_html(src2, g2["file"], 280)}</div>
      <div class="footer-small">
        <span class="tag-sm" style="color:{g2['accent']};border:1px solid {g2['accent']}55;background:{g2['accent']}18;">{g2["tag"]}</span>
        <p class="title-sm">{g2["title"]}</p>
        <p class="desc-sm">{g2["description"]}</p>
        <span class="zoom-sm">🔍 Zoom</span>
      </div>
    </div>
  </div>

</div>

<!-- MODAL 0 -->
<div id="modal-0" class="modal-overlay" onclick="bgClose(event, 0)">
  <div class="modal-box">
    <div class="modal-img-area">{modal_img_html(src0, g0["file"])}</div>
    <div class="modal-footer">
      <div class="modal-meta">
        <span class="modal-tag" style="color:{g0['accent']};">{g0["tag"]}</span>
        <p class="modal-title">{g0["title"]}</p>
        <p class="modal-desc">{g0["description"]}</p>
      </div>
      <button class="close-btn" onclick="hideModal(0)">✕</button>
    </div>
  </div>
</div>

<!-- MODAL 1 -->
<div id="modal-1" class="modal-overlay" onclick="bgClose(event, 1)">
  <div class="modal-box">
    <div class="modal-img-area">{modal_img_html(src1, g1["file"])}</div>
    <div class="modal-footer">
      <div class="modal-meta">
        <span class="modal-tag" style="color:{g1['accent']};">{g1["tag"]}</span>
        <p class="modal-title">{g1["title"]}</p>
        <p class="modal-desc">{g1["description"]}</p>
      </div>
      <button class="close-btn" onclick="hideModal(1)">✕</button>
    </div>
  </div>
</div>

<!-- MODAL 2 -->
<div id="modal-2" class="modal-overlay" onclick="bgClose(event, 2)">
  <div class="modal-box">
    <div class="modal-img-area">{modal_img_html(src2, g2["file"])}</div>
    <div class="modal-footer">
      <div class="modal-meta">
        <span class="modal-tag" style="color:{g2['accent']};">{g2["tag"]}</span>
        <p class="modal-title">{g2["title"]}</p>
        <p class="modal-desc">{g2["description"]}</p>
      </div>
      <button class="close-btn" onclick="hideModal(2)">✕</button>
    </div>
  </div>
</div>

<script>
  function showModal(i) {{
    document.getElementById('modal-' + i).classList.add('active');
  }}
  function hideModal(i) {{
    document.getElementById('modal-' + i).classList.remove('active');
  }}
  function bgClose(e, i) {{
    if (e.target === document.getElementById('modal-' + i)) {{
      hideModal(i);
    }}
  }}
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') {{
      [0, 1, 2].forEach(function(i) {{ hideModal(i); }});
    }}
  }});
</script>
</body>
</html>
"""

st.markdown("""
<div style="font-size:0.68rem;letter-spacing:0.4em;text-transform:uppercase;color:#2ec4b6;
margin-bottom:1.2rem;display:flex;align-items:center;gap:1rem;">
Project Graphs
<span style="flex:1;height:1px;background:rgba(46,196,182,0.2);display:block;"></span>
</div>
""", unsafe_allow_html=True)

components.html(html, height=980, scrolling=False)

st.markdown("""
<div style="text-align:center;margin-top:1.5rem;font-size:0.68rem;letter-spacing:0.2em;
text-transform:uppercase;color:#6ab8b3;opacity:0.35;">
© 2025 Aquagreen · CAP Project Visual Results
</div>
""", unsafe_allow_html=True)