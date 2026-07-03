import streamlit as st
import json

st.title("⚡ Quiz de Revisão")

with open("questoes.json", "r", encoding="utf-8") as f:
    questoes = json.load(f)

if 'idx' not in st.session_state: st.session_state.idx = 0

idx = st.session_state.idx
q = questoes[idx]

st.write(f"Questão {idx + 1} de {len(questoes)}")
st.subheader(q["pergunta"])

if st.button("Ver Resposta"):
    st.info(q["resposta"])

col1, col2 = st.columns(2)
if col1.button("⬅️ Anterior") and idx > 0:
    st.session_state.idx -= 1
    st.rerun()
if col2.button("Próxima ➡️") and idx < len(questoes) - 1:
    st.session_state.idx += 1
    st.rerun()
