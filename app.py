import streamlit as st

st.set_page_config(page_title="EduCognitivo PRO", layout="wide")

st.title("🧠 EduCognitivo PRO")

# Estrutura real
estrategias = {
    "Memorizar": {
        "Mapas Mentais Colaborativos": {
            "descricao": "Organização visual de ideias com conexões entre conceitos.",
            "como_fazer": [
                "Dividir a turma em grupos",
                "Escolher um tema central",
                "Criar ramificações com conceitos",
                "Apresentar o mapa"
            ],
            "tempo": "1h30"
        },
        "Linha do Tempo": {
            "descricao": "Representação cronológica de eventos.",
            "como_fazer": [
                "Definir tema",
                "Listar eventos importantes",
                "Organizar em ordem",
                "Apresentar resultados"
            ],
            "tempo": "1h"
        }
    }
}

# Seleção
dominio = st.selectbox("Domínio Cognitivo", list(estrategias.keys()))

estrategia = st.selectbox(
    "Estratégia",
    list(estrategias[dominio].keys())
)

titulo = st.text_input("Título da Aula")
tema = st.text_area("Tema")

if st.button("🚀 Gerar Atividade"):

    dados = estrategias[dominio][estrategia]

    st.subheader("📘 O que é")
    st.write(dados["descricao"])

    st.subheader("🛠️ Como fazer")
    for passo in dados["como_fazer"]:
        st.write(f"- {passo}")

    st.subheader("🧑‍🏫 Roteiro da Aula")
    st.write(f"Tema: {tema}")
    st.write("1. Introdução")
    st.write("2. Desenvolvimento")
    st.write("3. Atividade prática")
    st.write("4. Fechamento")

    st.subheader("⏱️ Tempo estimado")
    st.write(dados["tempo"])
   
