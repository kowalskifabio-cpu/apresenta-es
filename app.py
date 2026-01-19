import streamlit as st
from streamlit_option_menu import option_menu

# =========================================================
# EDITAR TÍTULOS AQUI
# =========================================================
TITULO_PRINCIPAL = "Proposta Marcenaria Status"
SUBTITULO = "Gestão Assistida e Melhoria de Processos"
CLIENTE = "Status Marcenaria"
# =========================================================

# Configuração da página
st.set_page_config(page_title=f"Labor Business | {CLIENTE}", layout="wide", page_icon="📊")

# Nome do arquivo de imagem conforme seu GitHub
NOME_IMAGEM = "tela inicial.png"

# CSS para visual profissional
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1 { color: #2c3e50; font-size: 42px; }
    .st-emotion-cache-1cv02ne { color: #ff9900; }
    .metric-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff9900;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Menu Lateral
with st.sidebar:
    try:
        st.image(NOME_IMAGEM, use_container_width=True)
    except:
        st.warning("Imagem não encontrada. Verifique o nome no GitHub.")
    
    st.divider()
    selected = option_menu(
        menu_title="Navegação",
        options=["Apresentação", "Escopo", "Cronograma", "Investimento", "Próximos Passos"],
        icons=["house", "briefcase", "calendar-range", "currency-dollar", "check-circle"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )

# --- CONTEÚDO ---

if selected == "Apresentação":
    st.title(TITULO_PRINCIPAL)
    st.subheader(f"{SUBTITULO} | Prazo: 5 Meses")
    
    try:
        st.image(NOME_IMAGEM, use_container_width=True)
    except:
        st.error(f"Erro ao carregar {NOME_IMAGEM}. Verifique se o nome no GitHub está idêntico.")
    
    st.markdown("### 🎯 Objetivo do Projeto")
    st.write(f"A Labor Business atuará na {CLIENTE} para estruturar processos e reduzir desperdícios.")

elif selected == "Escopo":
    st.header("🔍 Frentes de Atuação")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("1. Compras e Financeiro", expanded=True):
            st.write("* Política de 2 autorizações.")
            st.write("* Fluxo de caixa semanal.")
    with col2:
        with st.expander("2. Produção e Logística", expanded=True):
            st.write("* Programação semanal de produção.")
            st.write("* Controle de frota e entregas.")

elif selected == "Cronograma":
    st.header("📅 Cronograma Macro")
    meses = ["Mês 1: Diagnóstico", "Mês 2: Implantação", "Mês 3: Eficiência", "Mês 4: Logística", "Mês 5: Consolidação"]
    for m in meses:
        st.markdown(f"<div class='metric-card'>{m}</div>", unsafe_allow_html=True)

elif selected == "Investimento":
    st.header("💰 Investimento")
    c1, c2 = st.columns(2)
    c1.metric("Mensalidade", "R$ 21.450,00")
    c2.metric("Total (5 meses)", "R$ 107.250,00")

elif selected == "Próximos Passos":
    st.header("🚀 Como Iniciar")
    st.write("1. Aprovação | 2. Assinatura | 3. Kick-off | 4. Início Presencial")
    if st.button("Confirmar Interesse"):
        st.balloons()
