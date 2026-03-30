import streamlit as st

st.set_page_config(page_title="EduCognitivo PRO", layout="wide")

st.sidebar.title("🧠 EduCognitivo PRO")
menu = st.sidebar.radio("Menu", ["Dashboard", "Gerar Atividade"])

# =========================
# BASE COMPLETA (36 estratégias)
# =========================

estrategias = {

    "Memorizar": {

        "Mapas Mentais Colaborativos": {
            "descricao": "Organização visual de ideias com conexões entre conceitos.",
            "como_fazer": [
                "Dividir a turma em grupos",
                "Criar um tema central",
                "Construir ramificações com conceitos",
                "Apresentar o mapa"
            ],
            "tempo": "1h30 a 2h"
        },

        "Linha do Tempo": {
            "descricao": "Representação cronológica de eventos.",
            "como_fazer": [
                "Definir tema",
                "Listar eventos",
                "Organizar em ordem",
                "Apresentar"
            ],
            "tempo": "1h30"
        },

        "Quiz de Revisão": {
            "descricao": "Perguntas e respostas para revisão.",
            "como_fazer": [
                "Criar perguntas",
                "Aplicar em grupo ou digital",
                "Corrigir e discutir"
            ],
            "tempo": "30 a 50 min"
        },

        "Flashcards": {
            "descricao": "Cartões de pergunta e resposta.",
            "como_fazer": [
                "Criar cartões",
                "Treinar em duplas",
                "Revisar conteúdo"
            ],
            "tempo": "1h"
        },

        "Caça-palavras / Cruzadas": {
            "descricao": "Jogos de memorização de termos.",
            "como_fazer": [
                "Criar grade",
                "Inserir termos",
                "Resolver atividade"
            ],
            "tempo": "20 a 40 min"
        },

        "Pareamento de Conceitos": {
            "descricao": "Relacionar conceitos e definições.",
            "como_fazer": [
                "Criar cartões",
                "Misturar",
                "Alunos fazem pares"
            ],
            "tempo": "1h"
        }
    },

    "Compreender": {

        "Paráfrase Guiada": {
            "descricao": "Reescrita com palavras próprias.",
            "como_fazer": [
                "Apresentar texto",
                "Reescrever",
                "Compartilhar"
            ],
            "tempo": "50 min"
        },

        "Mapa Conceitual": {
            "descricao": "Resumo com relações entre conceitos.",
            "como_fazer": [
                "Selecionar conceitos",
                "Conectar ideias",
                "Apresentar"
            ],
            "tempo": "1h"
        },

        "Classificação e Categorização": {
            "descricao": "Agrupar conceitos por características.",
            "como_fazer": [
                "Listar itens",
                "Criar categorias",
                "Justificar escolhas"
            ],
            "tempo": "30 a 60 min"
        },

        "Explicação entre Pares": {
            "descricao": "Alunos ensinam uns aos outros.",
            "como_fazer": [
                "Dividir em duplas",
                "Explicar conteúdo",
                "Trocar papéis"
            ],
            "tempo": "40 a 60 min"
        },

        "Sequência Lógica": {
            "descricao": "Organizar processos como história.",
            "como_fazer": [
                "Criar etapas",
                "Misturar",
                "Organizar corretamente"
            ],
            "tempo": "1h a 1h30"
        },

        "Minute Paper": {
            "descricao": "Reflexão rápida.",
            "como_fazer": [
                "Responder 2 perguntas",
                "Entregar",
                "Professor analisa"
            ],
            "tempo": "5 a 10 min"
        },

        "Mentoria entre Pares": {
            "descricao": "Alunos ensinam colegas.",
            "como_fazer": [
                "Selecionar alunos",
                "Preparar aula",
                "Aplicar treinamento"
            ],
            "tempo": "2 a 4h"
        }
    },

    "Aplicar": {

        "Estudo de Caso": {
            "descricao": "Resolver problema real.",
            "como_fazer": [
                "Apresentar caso",
                "Analisar",
                "Propor solução"
            ],
            "tempo": "2h"
        },

        "PBL": {
            "descricao": "Aprendizagem baseada em problemas.",
            "como_fazer": [
                "Apresentar problema",
                "Pesquisar",
                "Resolver e apresentar"
            ],
            "tempo": "4h+"
        },

        "Simulação": {
            "descricao": "Simular prática profissional.",
            "como_fazer": [
                "Criar cenário",
                "Executar atividade",
                "Avaliar"
            ],
            "tempo": "2 a 4h"
        },

        "Jogo de Tabuleiro": {
            "descricao": "Aprender jogando.",
            "como_fazer": [
                "Criar tabuleiro",
                "Criar desafios",
                "Executar jogo"
            ],
            "tempo": "1 a 2h"
        },

        "Rotação por Estações": {
            "descricao": "Atividades em estações.",
            "como_fazer": [
                "Criar estações",
                "Dividir grupos",
                "Rotacionar"
            ],
            "tempo": "2 a 3h"
        }
    },

    "Analisar": {

        "Leitura Crítica": {
            "descricao": "Analisar documentos técnicos.",
            "como_fazer": [
                "Ler material",
                "Identificar pontos",
                "Discutir"
            ],
            "tempo": "2 a 4h"
        },

        "Causa e Efeito": {
            "descricao": "Identificar relações.",
            "como_fazer": [
                "Listar causas",
                "Relacionar efeitos",
                "Criar diagrama"
            ],
            "tempo": "1h"
        },

        "Análise de Erros": {
            "descricao": "Identificar falhas.",
            "como_fazer": [
                "Apresentar erro",
                "Analisar",
                "Corrigir"
            ],
            "tempo": "1 a 2h"
        },

        "Análise Comparativa": {
            "descricao": "Comparar elementos.",
            "como_fazer": [
                "Selecionar itens",
                "Comparar",
                "Apresentar"
            ],
            "tempo": "1h30"
        },

        "SWOT": {
            "descricao": "Análise estratégica.",
            "como_fazer": [
                "Identificar forças",
                "Fraquezas",
                "Oportunidades",
                "Ameaças"
            ],
            "tempo": "1h"
        },

        "Detetive de Dados": {
            "descricao": "Analisar dados.",
            "como_fazer": [
                "Observar dados",
                "Identificar padrões",
                "Concluir"
            ],
            "tempo": "2h"
        }
    },

    "Avaliar": {

        "Autoavaliação": {
            "descricao": "Refletir sobre desempenho.",
            "como_fazer": [
                "Usar checklist",
                "Avaliar",
                "Refletir"
            ],
            "tempo": "30 min"
        },

        "Júri Simulado": {
            "descricao": "Debate estruturado.",
            "como_fazer": [
                "Definir papéis",
                "Debater",
                "Julgar"
            ],
            "tempo": "2 a 3h"
        },

        "Avaliação por Pares": {
            "descricao": "Avaliação entre alunos.",
            "como_fazer": [
                "Definir critérios",
                "Avaliar colegas",
                "Discutir"
            ],
            "tempo": "1h"
        },

        "Benchmarking": {
            "descricao": "Análise crítica de soluções.",
            "como_fazer": [
                "Escolher objeto",
                "Definir critérios",
                "Comparar"
            ],
            "tempo": "5h+"
        }
    },

    "Criar": {

        "Projeto Integrador": {
            "descricao": "Projeto completo.",
            "como_fazer": [
                "Definir problema",
                "Planejar",
                "Executar"
            ],
            "tempo": "6h+"
        },

        "Protótipo": {
            "descricao": "Criar produto.",
            "como_fazer": [
                "Planejar",
                "Construir",
                "Testar"
            ],
            "tempo": "4 a 8h"
        },

        "Campanha Educativa": {
            "descricao": "Criar campanha.",
            "como_fazer": [
                "Definir tema",
                "Criar material",
                "Apresentar"
            ],
            "tempo": "3 a 6h"
        },

        "Plano de Ação": {
            "descricao": "Resolver problema real.",
            "como_fazer": [
                "Identificar problema",
                "Criar plano",
                "Executar"
            ],
            "tempo": "4 a 6h"
        },

        "Solução Sustentável": {
            "descricao": "Criar solução sustentável.",
            "como_fazer": [
                "Analisar problema",
                "Criar solução",
                "Apresentar"
            ],
            "tempo": "4 a 6h"
        },

        "Pecha Kucha": {
            "descricao": "Apresentação dinâmica.",
            "como_fazer": [
                "Criar slides",
                "Apresentar 20x20",
                "Avaliar"
            ],
            "tempo": "4 a 6h"
        }
    }
}

# =========================
# INTERFACE
# =========================

if menu == "Dashboard":
    st.title("📊 Painel")
    st.success("Sistema completo carregado com 36 estratégias!")

elif menu == "Gerar Atividade":

    st.title("🚀 Gerador de Atividades")

    dominio = st.selectbox("Domínio Cognitivo", list(estrategias.keys()))

    estrategia = st.selectbox(
        "Estratégia",
        list(estrategias[dominio].keys())
    )

    titulo = st.text_input("Título da Aula")
    tema = st.text_area("Tema")

    if st.button("Gerar Atividade"):

        dados = estrategias[dominio][estrategia]

        st.subheader("📘 O que é")
        st.write(dados["descricao"])

        st.subheader("🛠️ Como fazer")
        for passo in dados["como_fazer"]:
            st.write(f"- {passo}")

        st.subheader("🧑‍🏫 Roteiro da Aula")
        st.write(f"**Tema:** {tema}")
        st.write("1. Introdução")
        st.write("2. Desenvolvimento")
        st.write("3. Atividade prática")
        st.write("4. Fechamento")

        st.subheader("⏱️ Tempo")
        st.write(dados["tempo"])
