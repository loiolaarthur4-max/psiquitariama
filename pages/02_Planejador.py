import streamlit as st
import json
import os

st.title("📅 Planejador de Estudos")

PROGRESS_FILE = "progresso.json"

# Carrega progresso
if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "r") as f:
        progresso = json.load(f)
else:
    progresso = {}

capitulos = ["Neuroanatomia", "Psicopatologia", "Farmacologia", "Transtornos de Humor"]

for cap in capitulos:
    progresso[cap] = st.checkbox(cap, value=progresso.get(cap, False))

with open(PROGRESS_FILE, "w") as f:
    json.dump(progresso, f)

st.progress(sum(progresso.values()) / len(capitulos))
