import streamlit as st

st.set_page_config(page_title="AQUA GREEN",page_icon="💧")

st.title("Aquagreen 💧")
st.subheader("We Are The Future Solution")
st.write("---")

try:
    st.image("cap.jpg",use_container_width=True,caption="AquaGreen")
except:
    st.warning("Not Founded ⚠️")
    
st.write("Team Members")

team=[
    {"name": "Mohamed Hamdy", "role": "Team Lead", "image": "hamdy.jpg"},
    {"name": "Mohamed Shawky", "role": "Hardware Implementer", "image": "shawky.jpg"},
    {"name": "Anas Hessen", "role": "Designer", "image": "anas.jpg"},
    {"name": "Salem Elbermawy", "role": "Data Analyst", "image": "salem.jpg"},    
]

cols=st.columns(4)

for index,member in enumerate(team):
    with cols[index]:
        try: 
            st.image(member["image"],use_column_width=True)
            
        except:
            st.write("Not Founded ⚠️")

        member_ol=member["name"]
        st.markdown("** " + member_ol + " **")
        st.caption(member["role"])
        
st.write("---")
st.info("© 2026 Aquagreen STEM 6th October")
