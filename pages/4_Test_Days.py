import streamlit as st
import os

st.set_page_config(page_title="Visual Results", page_icon="📊", layout="wide")

GRAPHS = [
    {
        "file": "graphs/lux_5.png",
        "title": "Light Intensity (Lux)",
        "description": "Light intensity readings over time captured by the sensor. Shows how ambient illumination varies.",
        "tag": "Lux"
    },
    {
        "file": "graphs/distance_5.png",
        "title": "Distance Measurement (CM)",
        "description": "Distance sensor readings in centimetres, reflecting object proximity changes detected.",
        "tag": "Distance"
    },
    {
        "file": "graphs/temp_5.png",
        "title": "Temperature (°C)",
        "description": "Ambient temperature readings in Celsius recorded continuously throughout the monitoring period.",
        "tag": "Temperature"
    },
]

st.title("Visual Results")
st.caption(" CAP Project · Key graphs from the project ")
st.divider()

st.write("### Featured Graph")
main_graph = GRAPHS[0]
col_main_1, col_main_2 = st.columns([2, 1])

with col_main_1:
    if os.path.exists(main_graph["file"]):
        st.image(main_graph["file"], use_container_width=True)
    else:
        st.info(f"Main graph placeholder: {main_graph['file']}")

with col_main_2:
    st.subheader(main_graph["title"])
    st.info(f"Category: {main_graph['tag']}")
    st.write(main_graph["description"])

st.divider()
st.write("### Additional Metrics")
col1, col2 = st.columns(2)

for index, graph in enumerate(GRAPHS[1:]):
    target_col = col1 if index == 0 else col2
    with target_col:
        st.write(f"#### {graph['title']}")
        if os.path.exists(graph["file"]):
            st.image(graph["file"], use_container_width=True)
        else:
            st.warning(f"File {graph['file']} not found")
        st.caption(f"**{graph['tag']}**: {graph['description']}")

st.write("---")
st.info("© 2026 Aquagreen · CAP Project Visual Results</center>")
