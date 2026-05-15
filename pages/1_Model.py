import streamlit as st
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),".."))

try:
    from rag_model import response
except ImportError:
    
    def response(text):
        return "RAG Not Founded ⚠️ "
    
st.set_page_config(page_title="Aqua Bot",page_icon="🤖")
st.title("🤖 AquaBot")
st.caption("Assistant For Searching in DOCs")
st.write("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

user_input = st.chat_input("Ask Me Any Question")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking ....."):
        bot_reply = response(user_input)
    
    st.session_state.messages.append({"role": "assistant", "text": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

if st.session_state.messages:
    if st.sidebar.button("🗑️ Clear "):
        st.session_state.messages = []
        st.rerun()
