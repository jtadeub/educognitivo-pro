import streamlit as st
from database import salvar_atividade, listar_atividades

st.set_page_config(page_title="EduCognitivo PRO", layout="wide")

st.sidebar.title("🧠 EduCognitivo PRO")
menu = st.sidebar.radio("Menu", ["Dashboard", "Gerar", "Histórico"])

if menu == "Dashboard":
    st.title("Painel Geral")
    st.info("Sistema funcionando!")

elif menu == "Gerar":
    st.title("Gerar Atividade")
    titulo = st.text_input("Título")
    tema = st.text_area("Tema")
    estrategia = st.text_input("Estratégia")

    if st.button("Gerar"):
        resultado = f"Atividade gerada para {titulo} - {tema} usando {estrategia}"
        st.write(resultado)
        salvar_atividade(titulo, tema, estrategia, resultado)

elif menu == "Histórico":
    st.title("Histórico")
    dados = listar_atividades()
    for d in dados:
        st.write(d)
