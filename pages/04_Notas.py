import streamlit as st
import json
import os

st.title("📝 Meus Blocos de Notas")

# Carrega ou cria o arquivo de notas
if not os.path.exists("notas.json"):
    with open("notas.json", "w") as f: json.dump({}, f)

with open("notas.json", "r") as f:
    notas = json.load(f)

# Criar novo bloco
titulo = st.text_input("Nome do novo bloco de notas:")
if st.button("Criar Bloco") and titulo:
    notas[titulo] = ""
    with open("notas.json", "w") as f: json.dump(notas, f)
    st.rerun()

# Editar notas
if notas:
    bloco = st.selectbox("Escolha seu bloco:", list(notas.keys()))
    conteudo = st.text_area("Anote aqui:", value=notas[bloco], height=300)
    
    if st.button("Salvar Alterações"):
        notas[bloco] = conteudo
        with open("notas.json", "w") as f: json.dump(notas, f)
        st.success("Nota salva com sucesso!")
