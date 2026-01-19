import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página e visual
st.set_page_config(page_title="Labor Business | Proposta Status Marcenaria", layout="wide", page_icon="📊")

# CSS para cores da Labor Business (Laranja e Cinza Profissional)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stSidebar { background-color: #f1f3f6; }
    h1, h2, h3 { color: #2c3e50; }
    .st-emotion-cache-1cv02ne { color: #ff9900; } /* Cor de destaque */
    .metric-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff9900;
    }
    </style>
""", unsafe_allow_html=True)

# Menu Lateral Personalizado
with st.sidebar:
    st.image("tela inicial.jpg", use_container_width=True)
    st.divider()
    selected = option_menu(
        menu_title="Proposta Comercial",
        options=["Apresentação", "Escopo", "Cronograma", "Investimento", "Próximos Passos"],
        icons=["house", "briefcase", "calendar-range", "currency-dollar", "check-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#f1f3f6"},
            "nav-link-selected": {"background-color": "#ff9900"},
        }
    )

# --- Lógica de Navegação ---

if selected == "Apresentação":
    st.title("Gestão Assistida e Melhoria de Processos")
    st.subheader("Cliente: Status Marcenaria | Prazo: 5 Meses")
    
    st.image("tela inicial.jpg", use_container_width=True)
    
    st.markdown("### 🎯 Objetivo do Projeto")
    st.write("""
    A **Labor Business** atuará na Status Marcenaria com o objetivo de estruturar e consolidar os processos essenciais, 
    garantindo organização, redução de desperdícios e previsibilidade financeira.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Foco:** Diagnóstico + Implantação Prática + Consolidação.")
    with col2:
        st.success("**Meta Final:** Formação de um ambiente sustentável para um gerente interno.")

elif selected == "Escopo":
    st.header("🔍 Frentes de Atuação")
    
    with st.expander("1. Compras e Fornecedores", expanded=True):
        st.write("* Mapeamento de fluxo e política de aprovação (2 autorizações).")
        st.write("* Atualização de base de fornecedores e redução de compras emergenciais.")
        
    with st.expander("2. Gestão Financeira"):
        st.write("* Fluxo de caixa com previsibilidade semanal.")
        st.write("* Calendário financeiro e identificação de 'vazamentos'.")
        
    with st.expander("3. Produção e Logística"):
        st.write("* Programação semanal e redução de atrasos/retrabalho.")
        st.write("* Controle de frota, manutenção e eficiência de entregas.")

elif selected == "Cronograma":
    st.header("📅 Cronograma Macro – 5 Meses")
    
    timeline = {
        "Mês 1": "Diagnóstico profundo e 'estancar o sangramento' operacional.",
        "Mês 2": "Implantação de processos (Compras, Financeiro, Produção).",
        "Mês 3": "Eficiência e redução real de desperdícios e retrabalho.",
        "Mês 4": "Foco em Logística, performance de entrega e redução de custos.",
        "Mês 5": "Consolidação, treinamento de equipe e plano de continuidade."
    }
    
    for mes, acao in timeline.items():
        st.markdown(f"""
        <div class="metric-card">
            <strong>{mes}:</strong> {acao}
        </div><br>
        """, unsafe_allow_html=True)

elif selected == "Investimento":
    st.header("💰 Investimento e Condições")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Mensalidade", "R$ 21.450,00")
    c2.metric("Prazo", "5 Meses")
    c3.metric("Total", "R$ 107.250,00")
    
    st.markdown("""
    ---
    * **Formato:** Presencial 3x por semana (Seg/Qua/Sex) das 09h às 17h.
    * **Pagamento:** Mensal mediante NF (Vencimento dia 05).
    """)

elif selected == "Próximos Passos":
    st.header("🚀 Próximos Passos para Início")
    st.write("Para iniciarmos a transformação na Status Marcenaria:")
    st.markdown("""
    1. ✅ Aprovação desta proposta
    2. ✍️ Assinatura do contrato de prestação de serviços
    3. 📅 Reunião de Kick-off com as lideranças
    4. 🏁 Início das atividades presenciais
    """)
    
    if st.button("Solicitar Contato para Início"):
        st.balloons()
        st.success("Notificação enviada! Entraremos em contato para formalização.")
