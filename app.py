import streamlit as st
from fpdf import FPDF
from datetime import datetime

# IMPORTANTE: só usa OpenAI se tiver chave
try:
    from openai import OpenAI
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    usar_ia = True
except:
    usar_ia = False

st.set_page_config(page_title="EduCognitivo PRO", layout="wide")

st.title("🧠 EduCognitivo PRO")

# Sidebar
st.sidebar.header("👨‍🎓 Gestão")
turma = st.sidebar.text_input("Turma")
aluno = st.sidebar.text_input("Aluno")

# Domínio cognitivo
dominio = st.selectbox(
    "Domínio Cognitivo",
    ["Memorizar", "Compreender", "Aplicar", "Analisar", "Avaliar", "Criar"]
)

tema = st.text_input("Tema da atividade")

# Histórico
if "historico" not in st.session_state:
    st.session_state.historico = []

# IA ou fallback
def gerar_atividade(dominio, tema):
    if usar_ia:
        prompt = f"""
        Crie uma atividade educacional no nível {dominio}
        sobre o tema: {tema}.

        Inclua:
        - Enunciado
        - Orientações
        - Critérios de avaliação
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
    else:
        return f"""
        ATIVIDADE ({dominio})

        Tema: {tema}

        Desenvolva uma atividade relacionada ao tema,
        considerando o nível cognitivo {dominio}.
        """

# PDF
def gerar_pdf(texto):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for linha in texto.split("\n"):
        pdf.multi_cell(0, 8, linha)

    nome = f"atividade_{datetime.now().strftime('%H%M%S')}.pdf"
    pdf.output(nome)
    return nome

# Botão
if st.button("🚀 Gerar Atividade"):
    if not tema:
        st.warning("Digite um tema")
    else:
        resultado = gerar_atividade(dominio, tema)

        registro = {
            "turma": turma,
            "aluno": aluno,
            "tema": tema,
            "dominio": dominio,
            "conteudo": resultado
        }

        st.session_state.historico.append(registro)

        st.subheader("📄 Atividade Gerada")
        st.write(resultado)

        arquivo = gerar_pdf(resultado)
        with open(arquivo, "rb") as f:
            st.download_button("📥 Baixar PDF", f, file_name=arquivo)

# Histórico
st.divider()
st.subheader("📚 Histórico")

for item in reversed(st.session_state.historico):
    with st.expander(f"{item['tema']} - {item['dominio']}"):
        st.write(f"Turma: {item['turma']}")
        st.write(f"Aluno: {item['aluno']}")
        st.write(item["conteudo"])
