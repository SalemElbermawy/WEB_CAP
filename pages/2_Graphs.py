import streamlit as st
import os

st.set_page_config(page_title="Project Analysis", page_icon="📊", layout="wide")

GRAPHS = [
    {"file": "graphs/all_graphs.png", "title": "Data 6 hrs", "description": "Data during the working of the prototype 6 hrs", "tag": "Overview"},
    {"file": "graphs/distance.png", "title": "Graph Title 2", "description": "Short description of what this graph shows.", "tag": "Performance"},
    {"file": "graphs/lux.png", "title": "Graph Title 3", "description": "Short description of what this graph shows.", "tag": "Comparison"},
    {"file": "graphs/temp.png", "title": "Graph Title 4", "description": "Short description of what this graph shows.", "tag": "Trends"},
    {"file": "graphs/ultra_div.png", "title": "Graph Title 5", "description": "Short description of what this graph shows.", "tag": "Distribution"},
    {"file": "graphs/temp_div.png", "title": "Graph Title 6", "description": "Short description of what this graph shows.", "tag": "Analysis"},
    {"file": "graphs/lux_div.png", "title": "Graph Title 7", "description": "Short description of what this graph shows.", "tag": "Results"},
    {"file": "graphs/temp_with_dist.png", "title": "Graph Title 8", "description": "Short description of what this graph shows.", "tag": "Summary"},
]

st.title("Data Analysis")
st.caption("CAP Project · Visual insights from the project ")
st.write("---")

col_stat1, col_stat2, col_stat3 = st.columns(3)
with col_stat1:
    st.metric(label="Total Graphs", value=len(GRAPHS))
with col_stat2:
    st.metric(label="Categories", value=len(set(g['tag'] for g in GRAPHS)))
with col_stat3:
    st.metric(label="Source Documents", value="2")

st.write("---")
st.subheader("Project Graphs")

cols = st.columns(2, gap="large")

for index, graph in enumerate(GRAPHS):
    current_col = cols[index % 2]
    
    with current_col:
        st.write(f"### {graph['title']}")
        st.caption(f"Category: {graph['tag']}")
        
        if os.path.exists(graph["file"]):
            st.image(graph["file"], use_container_width=True)
        else:
            st.warning(f"Image not found: {graph['file']}")
            
        st.write(graph["description"])
        st.write("---")

st.write(" ")
st.info("© 2026 Aquagreen · CAP Project Analysis")
