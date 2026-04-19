import streamlit as st
import base64
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(page_title="Project Analysis", page_icon="📊", layout="wide")

def img_to_b64(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    suffix = p.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(suffix, "jpeg")
    return f"data:image/{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

GRAPHS = [
    {"file": "graphs/all_graphs.png", "title": "Data 6 hrs ", "description": "Data during the working of the prototype 6 hrs", "tag": "Overview"},
    {"file": "graphs/distance`.png", "title": "Graph Title 2", "description": "Short description of what this graph shows.", "tag": "Performance"},
    {"file": "graphs/lux.png", "title": "Graph Title 3", "description": "Short description of what this graph shows.", "tag": "Comparison"},
    {"file": "graphs/temp.png", "title": "Graph Title 4", "description": "Short description of what this graph shows.", "tag": "Trends"},
    {"file": "graphs/ultra_div.png", "title": "Graph Title 5", "description": "Short description of what this graph shows.", "tag": "Distribution"},
    {"file": "graphs/temp_div.png", "title": "Graph Title 6", "description": "Short description of what this graph shows.", "tag": "Analysis"},
    {"file": "graphs/lux_div.png", "title": "Graph Title 7", "description": "Short description of what this graph shows.", "tag": "Results"},
    {"file": "graphs/temp_with_dist.png", "title": "Graph Title 8", "description": "Short description of what this graph shows.", "tag": "Summary"},
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=DM+Sans:wght@300;400;500&display=swap');
:root {
    --aqua:#2ec4b6;--aqua-dark:#1a8f84;--aqua-light:#a8ede8;
    --aqua-glow:rgba(46,196,182,0.15);--bg:#04191a;--surface:#071f20;
    --border:rgba(46,196,182,0.2);--text:#d6f5f3;--muted:#6ab8b3;
}
html,body,[class*="css"],.stApp{background-color:var(--bg)!important;color:var(--text)!important;font-family:'DM Sans',sans-serif;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:2rem 2.5rem 4rem!important;max-width:1300px;}
section[data-testid="stSidebar"]{background:var(--bg)!important;border-right:1px solid var(--border)!important;}
.page-header{text-align:center;padding:2.5rem 0 2rem;position:relative;}
.page-header::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:500px;height:150px;background:radial-gradient(ellipse,var(--aqua-glow) 0%,transparent 70%);pointer-events:none;}
.page-title{font-family:'Cormorant Garamond',serif;font-size:clamp(2.2rem,5vw,4rem);font-weight:300;letter-spacing:0.18em;text-transform:uppercase;background:linear-gradient(135deg,var(--aqua-light),var(--aqua),var(--aqua-dark));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin:0;line-height:1.1;}
.page-sub{font-size:0.72rem;letter-spacing:0.35em;text-transform:uppercase;color:var(--muted);margin-top:0.6rem;opacity:0.8;}
.page-divider{width:60px;height:1.5px;background:linear-gradient(90deg,transparent,var(--aqua),transparent);margin:1.2rem auto 0;}
.stats-bar{display:flex;justify-content:center;gap:3rem;padding:1rem 0 2rem;border-bottom:1px solid var(--border);margin-bottom:2rem;}
.stat-item{text-align:center;}
.stat-num{font-family:'Cormorant Garamond',serif;font-size:1.8rem;font-weight:600;color:var(--aqua);line-height:1;}
.stat-label{font-size:0.65rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--muted);margin-top:0.3rem;opacity:0.7;}
.section-label{font-size:0.68rem;letter-spacing:0.4em;text-transform:uppercase;color:var(--aqua);margin-bottom:1rem;display:flex;align-items:center;gap:1rem;}
.section-label::after{content:'';flex:1;height:1px;background:var(--border);}
.page-footer{text-align:center;margin-top:2rem;font-size:0.7rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--muted);opacity:0.4;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <p class="page-sub">✦ &nbsp; CAP Project &nbsp; ✦</p>
    <h1 class="page-title">Data Analysis</h1>
    <div class="page-divider"></div>
    <p class="page-sub">Visual insights from the project</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="stats-bar">
    <div class="stat-item"><div class="stat-num">{len(GRAPHS)}</div><div class="stat-label">Total Graphs</div></div>
    <div class="stat-item"><div class="stat-num">{len(set(g['tag'] for g in GRAPHS))}</div><div class="stat-label">Categories</div></div>
    <div class="stat-item"><div class="stat-num">2</div><div class="stat-label">Source Documents</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="section-label">Project Graphs</p>', unsafe_allow_html=True)

cards_html = ""
modals_html = ""

for i, graph in enumerate(GRAPHS):
    src = img_to_b64(graph["file"])
    if src:
        card_img  = f'<img src="{src}" alt="{graph["title"]}" style="width:100%;height:220px;object-fit:contain;display:block;padding:12px;transition:transform 0.4s ease;">'
        modal_img = f'<img src="{src}" alt="{graph["title"]}" style="max-width:100%;max-height:68vh;object-fit:contain;border-radius:8px;display:block;">'
    else:
        card_img  = f'<div style="width:100%;height:220px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:#6ab8b3;opacity:0.35;"><div style="font-size:2rem;">📊</div><div style="font-size:0.68rem;letter-spacing:0.15em;text-transform:uppercase;">{graph["file"]}</div></div>'
        modal_img = f'<div style="color:#6ab8b3;opacity:0.4;text-align:center;padding:3rem;font-size:0.8rem;letter-spacing:0.15em;text-transform:uppercase;">Image not found: {graph["file"]}</div>'

    cards_html += f"""
    <div onclick="openModal({i})" style="background:#071f20;border:1px solid rgba(46,196,182,0.2);border-radius:16px;overflow:hidden;cursor:pointer;position:relative;transition:transform 0.3s,box-shadow 0.3s,border-color 0.3s;"
         onmouseover="this.style.transform='translateY(-5px)';this.style.boxShadow='0 20px 60px rgba(0,0,0,0.6),0 0 30px rgba(46,196,182,0.15)';this.style.borderColor='rgba(46,196,182,0.5)';this.querySelector('.hint').style.opacity='1';"
         onmouseout="this.style.transform='';this.style.boxShadow='';this.style.borderColor='rgba(46,196,182,0.2)';this.querySelector('.hint').style.opacity='0';">
        <div style="background:#0a2829;overflow:hidden;">{card_img}</div>
        <div style="padding:12px 14px 14px;border-top:1px solid rgba(46,196,182,0.2);">
            <span style="font-size:0.58rem;letter-spacing:0.18em;text-transform:uppercase;color:#2ec4b6;background:rgba(46,196,182,0.08);border:1px solid rgba(46,196,182,0.2);border-radius:20px;padding:2px 10px;display:inline-block;margin-bottom:6px;">{graph["tag"]}</span>
            <p style="font-size:0.88rem;font-weight:500;color:#d6f5f3;margin:0 0 4px;line-height:1.3;">{graph["title"]}</p>
            <p style="font-size:0.74rem;color:#6ab8b3;margin:0;line-height:1.6;opacity:0.8;">{graph["description"]}</p>
        </div>
        <span class="hint" style="position:absolute;bottom:10px;right:10px;font-size:0.58rem;letter-spacing:0.12em;text-transform:uppercase;color:#2ec4b6;opacity:0;transition:opacity 0.25s;background:rgba(4,25,26,0.9);padding:3px 8px;border-radius:6px;border:1px solid rgba(46,196,182,0.2);pointer-events:none;">Click to zoom</span>
    </div>"""

    modals_html += f"""
    <div id="modal-{i}" onclick="closeModal(event,{i})" style="display:none;position:fixed;inset:0;background:rgba(2,10,11,0.93);z-index:9999;align-items:center;justify-content:center;backdrop-filter:blur(10px);">
        <div style="background:#071f20;border:1px solid rgba(46,196,182,0.45);border-radius:20px;max-width:90vw;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 40px 120px rgba(0,0,0,0.8);animation:zoomIn 0.25s ease;position:relative;">
            <div style="position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#1a8f84,#2ec4b6,#a8ede8);"></div>
            <div style="background:#0a2829;display:flex;align-items:center;justify-content:center;padding:24px 24px 16px;">{modal_img}</div>
            <div style="padding:14px 18px;border-top:1px solid rgba(46,196,182,0.2);display:flex;align-items:center;justify-content:space-between;gap:12px;">
                <div>
                    <span style="font-size:0.58rem;letter-spacing:0.18em;text-transform:uppercase;color:#2ec4b6;background:rgba(46,196,182,0.08);border:1px solid rgba(46,196,182,0.2);border-radius:20px;padding:2px 10px;display:inline-block;margin-bottom:5px;">{graph["tag"]}</span>
                    <p style="font-size:1rem;font-weight:500;color:#d6f5f3;margin:0 0 3px;">{graph["title"]}</p>
                    <p style="font-size:0.77rem;color:#6ab8b3;margin:0;opacity:0.75;">{graph["description"]}</p>
                </div>
                <button onclick="document.getElementById('modal-{i}').style.display='none';document.body.style.overflow='';"
                        style="width:36px;height:36px;border-radius:10px;border:1px solid rgba(46,196,182,0.25);background:#0a2829;color:#d6f5f3;font-size:1rem;cursor:pointer;flex-shrink:0;display:flex;align-items:center;justify-content:center;">✕</button>
            </div>
        </div>
    </div>"""

full_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: transparent; font-family: 'DM Sans', sans-serif; }}
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&display=swap');
  @keyframes zoomIn {{
    from {{ transform: scale(0.82); opacity: 0; }}
    to   {{ transform: scale(1);    opacity: 1; }}
  }}
  .grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; padding: 4px; }}
</style>
</head>
<body>
  <div class="grid">{cards_html}</div>
  {modals_html}
<script>
  function openModal(i) {{
    var m = document.getElementById('modal-' + i);
    m.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }}
  function closeModal(e, i) {{
    if (e.target === document.getElementById('modal-' + i)) {{
      document.getElementById('modal-' + i).style.display = 'none';
      document.body.style.overflow = '';
    }}
  }}
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') {{
      document.querySelectorAll('[id^="modal-"]').forEach(function(m) {{
        m.style.display = 'none';
      }});
      document.body.style.overflow = '';
    }}
  }});
</script>
</body>
</html>
"""

components.html(full_html, height=1100, scrolling=True)

st.markdown('<div class="page-footer">© 2026 Aquagreen · CAP Project Analysis</div>', unsafe_allow_html=True)