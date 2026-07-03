import streamlit as st
import os

st.title("📚 Biblioteca de Psiquiatria")

content_dir = "content"
if not os.path.exists(content_dir):
    os.makedirs(content_dir)

files = sorted([f for f in os.listdir(content_dir) if f.endswith(".md")])

if files:
    selected_file = st.selectbox("Escolha um capítulo para estudar:", files)
    with open(os.path.join(content_dir, selected_file), "r", encoding="utf-8") as f:
        st.markdown(f.read())
else:
    st.info("Ainda não há arquivos na pasta 'content'. Coloque seus capítulos lá!")
