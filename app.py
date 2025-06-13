
import streamlit as st
from signal_engine import gerar_sinal
from utils import agora_brasilia
import pandas as pd

st.set_page_config(layout="wide", page_title="Indicador GPT 1.0")

st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://i.imgur.com/Nn7eAvk.jpg');
            background-size: cover;
        }
        .titulo {
            font-size: 40px;
            color: white;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="titulo">Indicador GPT 1.0 - Cripto & Forex</div>', unsafe_allow_html=True)
st.write("Horário de Brasília:", agora_brasilia().strftime("%H:%M:%S"))

if st.button("🔍 Gerar Sinal"):
    sinal = gerar_sinal()
    st.success("Sinal gerado com sucesso!")
    st.json(sinal)

    if "historico" not in st.session_state:
        st.session_state["historico"] = []

    st.session_state["historico"].insert(0, sinal)

st.markdown("## Histórico de Sinais")
if "historico" in st.session_state:
    df = pd.DataFrame(st.session_state["historico"])
    st.dataframe(df)
