import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Data Explorer", page_icon="📈", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=DM+Sans:wght@300;400;500&display=swap');
:root {
    --aqua:#2ec4b6;--aqua-dark:#1a8f84;--aqua-light:#a8ede8;
    --aqua-glow:rgba(46,196,182,0.13);--bg:#04191a;--surface:#071f20;
    --surface2:#0a2829;--border:rgba(46,196,182,0.2);--text:#d6f5f3;--muted:#6ab8b3;
}
html,body,[class*="css"],.stApp{background-color:var(--bg)!important;color:var(--text)!important;font-family:'DM Sans',sans-serif;}
#MainMenu,footer,header{visibility:hidden;}
.block-container{padding:2rem 2.5rem 4rem!important;max-width:1350px;}
section[data-testid="stSidebar"]{background:var(--bg)!important;border-right:1px solid var(--border)!important;}

.page-header{text-align:center;padding:2.5rem 0 2rem;position:relative;}
.page-header::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:500px;height:150px;background:radial-gradient(ellipse,var(--aqua-glow) 0%,transparent 70%);pointer-events:none;}
.page-title{font-family:'Cormorant Garamond',serif;font-size:clamp(2.2rem,5vw,4rem);font-weight:300;letter-spacing:0.18em;text-transform:uppercase;background:linear-gradient(135deg,var(--aqua-light),var(--aqua),var(--aqua-dark));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin:0;line-height:1.1;}
.page-sub{font-size:0.72rem;letter-spacing:0.35em;text-transform:uppercase;color:var(--muted);margin-top:0.6rem;opacity:0.8;}
.page-divider{width:60px;height:1.5px;background:linear-gradient(90deg,transparent,var(--aqua),transparent);margin:1.2rem auto 0;}

.section-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:1.6rem 1.8rem;margin-bottom:1.8rem;position:relative;overflow:hidden;}
.section-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--aqua-dark),var(--aqua),transparent);}
.section-num{font-family:'Cormorant Garamond',serif;font-size:3.5rem;font-weight:300;color:rgba(46,196,182,0.08);position:absolute;top:0.3rem;right:1.2rem;line-height:1;pointer-events:none;user-select:none;}
.section-title{font-size:0.68rem;letter-spacing:0.3em;text-transform:uppercase;color:var(--aqua);margin:0 0 0.3rem;}
.section-heading{font-family:'Cormorant Garamond',serif;font-size:1.55rem;font-weight:400;color:var(--text);margin:0 0 1.3rem;}

div[data-testid="stFileUploader"]{background:var(--surface2)!important;border:1.5px dashed rgba(46,196,182,0.3)!important;border-radius:14px!important;}
div[data-testid="stFileUploader"]:hover{border-color:var(--aqua)!important;}
div[data-testid="stFileUploader"] label p{color:var(--muted)!important;}
div[data-testid="stFileUploader"] button{background:var(--aqua-dark)!important;color:#fff!important;border:none!important;border-radius:8px!important;}

div[data-testid="stMultiSelect"] > div > div{background:var(--surface2)!important;border:1px solid var(--border)!important;border-radius:10px!important;}
div[data-testid="stMultiSelect"] span[data-baseweb="tag"]{background:rgba(46,196,182,0.12)!important;border:1px solid rgba(46,196,182,0.3)!important;color:var(--aqua)!important;border-radius:6px!important;}
div[data-testid="stSelectbox"] > div > div{background:var(--surface2)!important;border:1px solid var(--border)!important;border-radius:10px!important;color:var(--text)!important;}

div[data-testid="stSlider"] > div{padding:0.2rem 0.4rem!important;}
div[data-testid="stSlider"] [data-testid="stTickBar"]{color:var(--muted)!important;}
div[data-testid="stSlider"] > div > div > div{background:var(--aqua-dark)!important;}

div[data-testid="stDataFrame"]{border:1px solid var(--border)!important;border-radius:12px!important;overflow:hidden!important;}
div[data-testid="stDataFrame"] thead tr th{background:var(--surface)!important;color:var(--aqua)!important;font-size:0.72rem!important;letter-spacing:0.1em!important;text-transform:uppercase!important;border-bottom:1px solid var(--border)!important;padding:10px 12px!important;}
div[data-testid="stDataFrame"] tbody tr td{color:var(--text)!important;font-size:0.82rem!important;border-bottom:1px solid rgba(46,196,182,0.06)!important;}
div[data-testid="stDataFrame"] tbody tr:hover td{background:rgba(46,196,182,0.04)!important;}

div[data-testid="stRadio"] > div{display:flex;gap:0.8rem;flex-wrap:wrap;}
div[data-testid="stRadio"] label{background:var(--surface2)!important;border:1px solid var(--border)!important;border-radius:8px!important;padding:0.4rem 1rem!important;cursor:pointer!important;transition:all 0.2s!important;color:var(--muted)!important;font-size:0.82rem!important;}
div[data-testid="stRadio"] label:has(input:checked){border-color:var(--aqua)!important;color:var(--aqua)!important;background:rgba(46,196,182,0.08)!important;}

div[data-testid="stButton"] > button{background:linear-gradient(135deg,var(--aqua-dark),var(--aqua))!important;color:#04191a!important;border:none!important;border-radius:10px!important;font-weight:500!important;font-size:0.88rem!important;padding:0.65rem 2rem!important;transition:opacity 0.2s!important;}
div[data-testid="stButton"] > button:hover{opacity:0.85!important;}

.stat-row{display:flex;gap:0.9rem;margin-bottom:1.3rem;flex-wrap:wrap;}
.stat-pill{background:var(--surface2);border:1px solid var(--border);border-radius:10px;padding:0.6rem 1.1rem;text-align:center;flex:1;min-width:90px;}
.stat-pill-num{font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:600;color:var(--aqua);line-height:1;}
.stat-pill-label{font-size:0.6rem;letter-spacing:0.15em;text-transform:uppercase;color:var(--muted);opacity:0.7;margin-top:3px;}

.info-box{background:rgba(46,196,182,0.05);border:1px solid rgba(46,196,182,0.18);border-radius:10px;padding:0.7rem 1rem;margin-bottom:0.8rem;display:flex;align-items:center;gap:0.6rem;font-size:0.78rem;color:var(--muted);}
.ctrl-label{font-size:0.68rem;letter-spacing:0.25em;text-transform:uppercase;color:var(--aqua);margin-bottom:0.4rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-header">
    <p class="page-sub">✦ &nbsp; CAP Project &nbsp; ✦</p>
    <h1 class="page-title">Data Explorer</h1>
    <div class="page-divider"></div>
    <p class="page-sub">Upload · Slice · Visualize</p>
</div>
""", unsafe_allow_html=True)

if "df_raw" not in st.session_state:
    st.session_state.df_raw = None


st.markdown("""
<div class="section-card">
    <div class="section-num">01</div>
    <p class="section-title">Step One</p>
    <h2 class="section-heading">Upload Your CSV File</h2>
</div>
""", unsafe_allow_html=True)

uploaded = st.file_uploader("", type=["csv"], label_visibility="collapsed")

if uploaded:
    try:
        df_raw = pd.read_csv(uploaded)

        for col in df_raw.columns:
            if "timestamp" in col.lower() or "time" in col.lower() or "date" in col.lower():
                try:
                    df_raw[col] = pd.to_datetime(df_raw[col])
                except:
                    pass

        st.session_state.df_raw = df_raw
        st.success(f"✓  Loaded **{uploaded.name}** — {df_raw.shape[0]:,} rows × {df_raw.shape[1]} columns")
    except Exception as e:
        st.error(f"Could not read file: {e}")

if st.session_state.df_raw is None:
    st.markdown('<div class="info-box">⬆ &nbsp; Upload a CSV file above to continue.</div>', unsafe_allow_html=True)
    st.stop()

df_raw = st.session_state.df_raw


datetime_cols = [c for c in df_raw.columns if pd.api.types.is_datetime64_any_dtype(df_raw[c])]
numeric_cols  = [c for c in df_raw.columns if pd.api.types.is_numeric_dtype(df_raw[c])]
all_cols      = list(df_raw.columns)
total_rows    = len(df_raw)


st.markdown("""
<div class="section-card">
    <div class="section-num">02</div>
    <p class="section-title">Step Two</p>
    <h2 class="section-heading">Slice & Preview Data</h2>
</div>
""", unsafe_allow_html=True)

num_rows_raw = df_raw.shape[0]
num_cols_raw = df_raw.shape[1]
num_numeric  = len(numeric_cols)
missing      = int(df_raw.isnull().sum().sum())

st.markdown(f"""
<div class="stat-row">
    <div class="stat-pill"><div class="stat-pill-num">{num_rows_raw:,}</div><div class="stat-pill-label">Total Rows</div></div>
    <div class="stat-pill"><div class="stat-pill-num">{num_cols_raw}</div><div class="stat-pill-label">Columns</div></div>
    <div class="stat-pill"><div class="stat-pill-num">{num_numeric}</div><div class="stat-pill-label">Numeric</div></div>
    <div class="stat-pill"><div class="stat-pill-num">{len(datetime_cols)}</div><div class="stat-pill-label">Datetime</div></div>
    <div class="stat-pill"><div class="stat-pill-num">{missing}</div><div class="stat-pill-label">Missing</div></div>
</div>
""", unsafe_allow_html=True)

sl_col1, sl_col2 = st.columns(2)

with sl_col1:
    st.markdown('<p class="ctrl-label">Row Range</p>', unsafe_allow_html=True)
    row_range = st.slider(
        "", 0, total_rows - 1, (0, min(199, total_rows - 1)),
        key="row_slider", label_visibility="collapsed"
    )

with sl_col2:
    st.markdown('<p class="ctrl-label">Select Columns to Display</p>', unsafe_allow_html=True)
    selected_cols = st.multiselect(
        "", options=all_cols,
        default=all_cols[:min(6, len(all_cols))],
        key="col_select", label_visibility="collapsed"
    )

if not selected_cols:
    st.markdown('<div class="info-box">ℹ &nbsp; Select at least one column above.</div>', unsafe_allow_html=True)
else:
    df_slice = df_raw.iloc[row_range[0]:row_range[1] + 1][selected_cols].copy()

    for col in df_slice.columns:
        if pd.api.types.is_datetime64_any_dtype(df_slice[col]):
            df_slice[col] = df_slice[col].dt.strftime("%H:%M:%S")

    st.markdown(f'<p style="font-size:0.7rem;color:var(--muted);opacity:0.6;margin-bottom:0.5rem;">Showing rows {row_range[0]} → {row_range[1]}  ·  {len(df_slice):,} rows  ·  {len(selected_cols)} columns</p>', unsafe_allow_html=True)
    st.dataframe(df_slice, use_container_width=True, height=340)


st.markdown("""
<div class="section-card">
    <div class="section-num">03</div>
    <p class="section-title">Step Three</p>
    <h2 class="section-heading">Visualize Feature Relationships</h2>
</div>
""", unsafe_allow_html=True)

if len(numeric_cols) < 1:
    st.markdown('<div class="info-box">⚠ &nbsp; No numeric columns found in your data.</div>', unsafe_allow_html=True)
    st.stop()

time_axis_options = datetime_cols + numeric_cols
value_axis_options = numeric_cols

v1, v2, v3, v4 = st.columns([2, 2, 2, 1])

with v1:
    st.markdown('<p class="ctrl-label">X Axis</p>', unsafe_allow_html=True)
    x_col = st.selectbox("", options=time_axis_options, index=0, key="x_col", label_visibility="collapsed")

with v2:
    st.markdown('<p class="ctrl-label">Y Axis</p>', unsafe_allow_html=True)
    y_options = [c for c in value_axis_options if c != x_col]
    y_col = st.selectbox("", options=y_options, index=0, key="y_col", label_visibility="collapsed")

with v3:
    st.markdown('<p class="ctrl-label">Color by (optional)</p>', unsafe_allow_html=True)
    color_col = st.selectbox("", options=["None"] + all_cols, index=0, key="color_col", label_visibility="collapsed")

with v4:
    st.markdown('<p class="ctrl-label">Plot Type</p>', unsafe_allow_html=True)
    plot_type = st.radio("", ["Scatter", "Line"], key="plot_type", label_visibility="collapsed")

st.markdown('<p class="ctrl-label" style="margin-top:0.8rem;">Row Range for Plot</p>', unsafe_allow_html=True)
plot_range = st.slider(
    "", 0, total_rows - 1, (0, min(499, total_rows - 1)),
    key="plot_slider", label_visibility="collapsed"
)

st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)

if st.button("  ▶  Generate Plot  "):

    cols_needed = [x_col, y_col]
    if color_col != "None":
        cols_needed.append(color_col)

    df_plot = df_raw.iloc[plot_range[0]:plot_range[1] + 1][cols_needed].copy().dropna(subset=[x_col, y_col])

    is_datetime_x = pd.api.types.is_datetime64_any_dtype(df_plot[x_col])

    if is_datetime_x:
        df_plot["__time__"] = df_plot[x_col].dt.strftime("%H:%M:%S")
        df_plot["__sort__"] = df_plot[x_col]
        df_plot = df_plot.sort_values("__sort__")
        x_use   = "__time__"
        x_label = f"{x_col} (HH:MM:SS)"
    else:
        df_plot = df_plot.sort_values(x_col)
        x_use   = x_col
        x_label = x_col

    color_arg = None if color_col == "None" else color_col

    PALETTE = ["#2ec4b6","#a8ede8","#5dd6cd","#1a8f84","#7fffd4","#3cbfb5","#0d5e58","#e0f7f5"]

    layout_cfg = dict(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(10,40,42,0.55)",
        font=dict(family="DM Sans", color="#d6f5f3", size=12),
        height=520,
        margin=dict(l=55, r=30, t=60, b=60),
        xaxis=dict(
            title=dict(text=x_label, font=dict(color="#6ab8b3", size=11)),
            gridcolor="rgba(46,196,182,0.09)",
            linecolor="rgba(46,196,182,0.22)",
            tickfont=dict(color="#6ab8b3", size=10),
            showgrid=True,
        ),
        yaxis=dict(
            title=dict(text=y_col, font=dict(color="#6ab8b3", size=11)),
            gridcolor="rgba(46,196,182,0.09)",
            linecolor="rgba(46,196,182,0.22)",
            tickfont=dict(color="#6ab8b3", size=10),
            showgrid=True,
        ),
        legend=dict(
            bgcolor="rgba(7,31,32,0.85)",
            bordercolor="rgba(46,196,182,0.2)",
            borderwidth=1,
            font=dict(color="#d6f5f3", size=11),
        ),
        title=dict(
            text=f"<b>{x_label}</b>  ×  <b>{y_col}</b>",
            font=dict(family="Cormorant Garamond", size=21, color="#a8ede8"),
            x=0.03,
        ),
        hoverlabel=dict(
            bgcolor="#071f20",
            bordercolor="rgba(46,196,182,0.4)",
            font=dict(color="#d6f5f3", family="DM Sans", size=12),
        ),
    )

    if plot_type == "Scatter":
        if is_datetime_x:
            df_plot = df_plot.sort_values("__sort__")
        fig = px.scatter(
            df_plot, x=x_use, y=y_col,
            color=color_arg,
            color_discrete_sequence=PALETTE,
            labels={x_use: x_label, y_col: y_col},
            opacity=0.85,
        )
        fig.update_traces(marker=dict(size=7, line=dict(width=0.6, color="rgba(46,196,182,0.35)")))

    else:
        fig = px.line(
            df_plot, x=x_use, y=y_col,
            color=color_arg,
            color_discrete_sequence=PALETTE,
            labels={x_use: x_label, y_col: y_col},
        )
        fig.update_traces(line=dict(width=2.2))
        fig.add_traces(
            px.scatter(df_plot, x=x_use, y=y_col, color=color_arg,
                       color_discrete_sequence=PALETTE, opacity=0.6).data
        )
        for trace in fig.data[len(fig.data)//2:]:
            trace.marker.size = 4
            trace.showlegend = False

    fig.update_layout(**layout_cfg)

    if is_datetime_x:
        tick_vals = df_plot["__time__"].iloc[::max(1, len(df_plot)//10)].tolist()
        fig.update_xaxes(tickvals=tick_vals, tickangle=-35)

    st.plotly_chart(fig, use_container_width=True)

    s1, s2, s3, s4 = st.columns(4)
    corr_val = df_plot[y_col].corr(df_plot[x_use] if not is_datetime_x else df_plot["__sort__"].astype("int64"))
    with s1:
        st.markdown(f'<div class="stat-pill"><div class="stat-pill-num">{df_plot[y_col].min():.3g}</div><div class="stat-pill-label">{y_col} Min</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown(f'<div class="stat-pill"><div class="stat-pill-num">{df_plot[y_col].max():.3g}</div><div class="stat-pill-label">{y_col} Max</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown(f'<div class="stat-pill"><div class="stat-pill-num">{df_plot[y_col].mean():.3g}</div><div class="stat-pill-label">{y_col} Mean</div></div>', unsafe_allow_html=True)
    with s4:
        st.markdown(f'<div class="stat-pill"><div class="stat-pill-num">{corr_val:.3f}</div><div class="stat-pill-label">Correlation</div></div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center;margin-top:3rem;font-size:0.68rem;letter-spacing:0.2em;text-transform:uppercase;color:#6ab8b3;opacity:0.35;">© 2026 Aquagreen · CAP Project Data Explorer</div>', unsafe_allow_html=True)