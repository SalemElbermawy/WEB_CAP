import streamlit as st
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from rag_model import response

# ── Page config ───────────────────────────────────────────────
st.set_page_config(page_title="AquaBot", page_icon="🤖", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --aqua:        #2ec4b6;
    --aqua-dark:   #1a8f84;
    --aqua-light:  #a8ede8;
    --aqua-glow:   rgba(46,196,182,0.15);
    --bg:          #04191a;
    --surface2:    #0a2829;
    --border:      rgba(46,196,182,0.22);
    --text:        #d6f5f3;
    --muted:       #6ab8b3;
}

html, body, [class*="css"], .stApp {
    background-color: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2rem 3rem !important; max-width: 820px; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--bg) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }

/* ── Top bar ── */
.topbar {
    text-align: center;
    padding: 2rem 0 1.5rem;
    position: relative;
    margin-bottom: 1rem;
}
.topbar::before {
    content: '';
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%,-50%);
    width: 400px; height: 120px;
    background: radial-gradient(ellipse, var(--aqua-glow) 0%, transparent 70%);
    pointer-events: none;
}
.topbar-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    font-weight: 300;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    background: linear-gradient(135deg, var(--aqua-light), var(--aqua), var(--aqua-dark));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}
.topbar-sub {
    font-size: 0.68rem;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 0.4rem;
}
.topbar-line {
    width: 50px; height: 1.5px;
    background: linear-gradient(90deg, transparent, var(--aqua), transparent);
    margin: 0.8rem auto 0;
}

/* ── Messages ── */
.chat-wrap {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 0.5rem 0 1.5rem;
}
.msg-row { display: flex; align-items: flex-end; gap: 0.7rem; }
.msg-row.user { flex-direction: row-reverse; }
.msg-row.bot  { flex-direction: row; }

.avatar {
    width: 34px; height: 34px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; flex-shrink: 0;
    border: 1px solid var(--border);
}
.avatar.bot  { background: var(--surface2); color: var(--aqua); }
.avatar.user { background: var(--aqua-dark); color: #fff; }

.bubble {
    max-width: 74%;
    padding: 0.8rem 1.1rem;
    border-radius: 16px;
    font-size: 0.92rem;
    line-height: 1.7;
    word-break: break-word;
    position: relative;
}
.bubble.bot {
    background: rgba(10,40,42,0.95);
    border: 1px solid var(--border);
    border-bottom-left-radius: 4px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.35);
}
.bubble.bot::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, var(--aqua-dark), var(--aqua));
    border-radius: 16px 16px 0 0;
    opacity: 0.6;
}
.bubble.user {
    background: rgba(46,196,182,0.1);
    border: 1px solid rgba(46,196,182,0.3);
    border-bottom-right-radius: 4px;
}

/* ── Empty state ── */
.empty-state { text-align: center; padding: 3rem 1rem; color: var(--muted); }
.empty-icon  { font-size: 2.8rem; margin-bottom: 1rem; opacity: 0.45; }
.empty-text  { font-size: 0.83rem; letter-spacing: 0.08em; line-height: 1.9; }

/* ── Input styling ── */
div[data-testid="stTextInput"] input {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
    padding: 0.75rem 1.1rem !important;
    caret-color: var(--aqua) !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: var(--aqua) !important;
    box-shadow: 0 0 0 3px var(--aqua-glow) !important;
    outline: none !important;
}
div[data-testid="stTextInput"] input::placeholder {
    color: var(--muted) !important;
    opacity: 0.6;
}

/* Send button */
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, var(--aqua-dark), var(--aqua)) !important;
    color: #04191a !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.06em !important;
    padding: 0.7rem 1.4rem !important;
    transition: opacity 0.2s !important;
    white-space: nowrap !important;
    width: 100% !important;
}
div[data-testid="stFormSubmitButton"] button:hover { opacity: 0.85 !important; }

/* Clear button */
div[data-testid="stButton"] > button {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    color: var(--muted) !important;
    border-radius: 8px !important;
    font-size: 0.75rem !important;
    padding: 0.4rem 0.9rem !important;
    transition: border-color 0.2s, color 0.2s !important;
}
div[data-testid="stButton"] > button:hover {
    border-color: var(--aqua) !important;
    color: var(--aqua) !important;
}

.input-divider {
    height: 1px;
    background: var(--border);
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []


st.markdown("""
<div class="topbar">
    <h1 class="topbar-title">AquaBot</h1>
    <p class="topbar-sub">RAG · Document Assistant</p>
    <div class="topbar-line"></div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)

with st.form("chat_form", clear_on_submit=True):
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            label="",
            placeholder="Ask a question about your documents…",
            label_visibility="collapsed"
        )
    with col2:
        submitted = st.form_submit_button("Send ➤")

st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)


if submitted and user_input.strip():
    st.session_state.messages.append({"role": "user", "text": user_input.strip()})
    with st.spinner("Thinking…"):
        bot_reply = response(user_input.strip())
    st.session_state.messages.append({"role": "bot", "text": bot_reply})
    st.rerun()

if not st.session_state.messages:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">💬</div>
        <p class="empty-text">
            Ask me anything about your documents.<br>
            I'll find the most relevant context for you.
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

    html = '<div class="chat-wrap">'
    for msg in st.session_state.messages:
        role = msg["role"]
        text = msg["text"].replace("\n", "<br>")
        av   = "🤖" if role == "bot" else "🧑"
        html += f"""
        <div class="msg-row {role}">
            <div class="avatar {role}">{av}</div>
            <div class="bubble {role}">{text}</div>
        </div>"""
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)