import streamlit as st

st.set_page_config(page_title="EduCognitivo PRO", layout="wide")

st.title("🧠 EduCognitivo PRO")

# Seleção do domínio cognitivo
dominio = st.selectbox(
    "Domínio Cognitivo",
    ["Memorizar", "Compreender", "Aplicar", "Analisar", "Avaliar", "Criar"]
)

# Campos principais
titulo = st.text_input("Título da Aula")
tema = st.text_input("Tema")

st.divider()

# Função para gerar atividade
def gerar_atividade(dominio, tema):
    atividades = {
        "Memorizar": f"Liste os principais conceitos sobre {tema}.",
        "Compreender": f"Explique com suas palavras o tema: {tema}.",
        "Aplicar": f"Resolva um problema prático envolvendo {tema}.",
        "Analisar": f"Compare diferentes abordagens sobre {tema}.",
        "Avaliar": f"Defenda um ponto de vista sobre {tema}.",
        "Criar": f"Desenvolva um projeto ou solução inovadora sobre {tema}."
    }
    return atividades.get(dominio, "")

# Botão gerar
if st.button("🚀 Gerar Atividade"):
    if tema == "":
        st.warning("Digite um tema primeiro!")
    else:
        atividade = gerar_atividade(dominio, tema)

        st.subheader("📌 Atividade Gerada")
        st.success(atividade)

        st.subheader("📝 Orientações ao Aluno")
        st.info(f"""
        • Leia atentamente a proposta  
        • Organize suas ideias  
        • Utilize exemplos práticos  
        • Revise antes de entregar  
        """)

        st.subheader("📊 Critérios de Avaliação")
        st.write(f"""
        ✔ Clareza na resposta  
        ✔ Coerência com o tema  
        ✔ Profundidade de análise  
        ✔ Organização das ideias  
        """)

st.divider()

# Extra: mapas mentais
with st.expander("🧩 Mapas Mentais Colaborativos"):
    st.write(f"""
    Crie um mapa mental sobre **{tema if tema else "o tema escolhido"}** contendo:

    • Conceitos principais  
    • Relações entre ideias  
    • Exemplos práticos  
    • Aplicações no mundo real  
    """)

st.divider()

st.caption("Desenvolvido para uso educacional 🚀")
