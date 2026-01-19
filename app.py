import streamlit as st
from streamlit_option_menu import option_menu

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Labor Business | Status Marcenaria", layout="wide", page_icon="📊")

# --- ESTILO CSS PERSONALIZADO ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stApp { max-width: 1200px; margin: 0 auto; }
    .titulo-principal { color: #2c3e50; font-size: 38px; font-weight: bold; margin-bottom: 0px; }
    .sub-titulo { color: #ff9900; font-size: 20px; font-weight: 600; margin-bottom: 20px; }
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 6px solid #ff9900;
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    .entrega-texto { color: #1e8449; font-weight: bold; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# --- MENU LATERAL ---
with st.sidebar:
    try:
        st.image("tela inicial.png", use_container_width=True)
    except:
        st.error("Imagem 'tela inicial.png' não encontrada no GitHub.")
    
    st.markdown("### Navegação")
    selected = option_menu(
        menu_title=None,
        options=["Início", "Escopo Detalhado", "Cronograma 5 Meses", "Metas e Sucesso", "Investimento"],
        icons=["house", "list-check", "calendar3", "trophy", "cash-coin"],
        menu_icon="cast", default_index=0,
        styles={
            "nav-link-selected": {"background-color": "#ff9900"},
        }
    )
    st.divider()
    st.caption("Proponente: Labor Business")
    st.caption("Cliente: Status Marcenaria")

# --- LÓGICA DE CONTEÚDO ---

if selected == "Início":
    st.markdown('<p class="titulo-principal">Proposta Marcenaria Status</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-titulo">Gestão Compartilhada Assistida e Melhoria de Processos</p>', unsafe_allow_html=True)
    
    st.image("tela inicial.png", use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎯 Contexto e Objetivo")
        st.write("""
        A Labor Business atuará por 5 meses focada em organização operacional, 
        fortalecimento de rotinas e governança prática. 
        O foco é aumentar previsibilidade e reduzir perdas.
        """)
    with col2:
        st.markdown("### 📋 Formato de Trabalho")
        st.info("""
        - **Presencial:** 3 dias/semana (Seg, Qua, Sex)
        - **Horário:** 09h às 17h
        - **Modelo:** Gerência temporária (Obrigação de meio)
        """)

elif selected == "Escopo Detalhado":
    st.header("🔍 Frentes de Atuação (Escopo)")
    
    tab1, tab2, tab3 = st.tabs(["Compras e Terceirizados", "Financeiro e Produção", "Logística e Aprovação"])
    
    with tab1:
        st.markdown("#### 🛒 2.1 Compras")
        st.write("- Mapeamento de fluxo, política de compras e controle de urgências.")
        st.markdown('<p class="entrega-texto">Entrega: Processo padronizado e base de fornecedores.</p>', unsafe_allow_html=True)
        
        st.markdown("#### 🤝 2.2 Gestão de Terceirizados")
        st.write("- Padronização de contratação, auditoria por entrega e redução de retrabalho.")
        st.markdown('<p class="entrega-texto">Entrega: Checklists e critérios de avaliação.</p>', unsafe_allow_html=True)

    with tab2:
        st.markdown("#### 💰 2.3 Gestão Financeira")
        st.write("- Fluxo de caixa projetado, calendário de pagamentos e redução de 'vazamentos'.")
        st.markdown('<p class="entrega-texto">Entrega: Visão projetada e rotina de fechamento.</p>', unsafe_allow_html=True)
        
        st.markdown("#### 🏗️ 2.4 Produção")
        st.write("- Diagnóstico de gargalos, programação semanal e integração com estoque.")
        st.markdown('<p class="entrega-texto">Entrega: Rotina organizada e redução de atrasos.</p>', unsafe_allow_html=True)

    with tab3:
        st.markdown("#### 🛡️ 2.5 Aprovação de Compras (2 Alçadas)")
        st.write("- Definição de faixas de valor e rastreabilidade total.")
        
        st.markdown("#### 🚛 2.6 Logística")
        st.write("- Controle de frota, roteiros de entrega e avaliação de custos.")
        st.markdown('<p class="entrega-texto">Entrega: Redução de falhas e custos operacionais.</p>', unsafe_allow_html=True)

elif selected == "Cronograma 5 Meses":
    st.header("📅 Cronograma Macro e Marcos")
    
    cronograma = [
        ("MÊS 1", "Diagnóstico e Estabilização", "Estancar sangramento e rotinas mínimas."),
        ("MÊS 2", "Implantação de Regras", "Fluxo de compras e aprovação com 2 autorizações."),
        ("MÊS 3", "Eficiência e Perdas", "Auditoria de terceiros e redução de retrabalho."),
        ("MÊS 4", "Logística e Performance", "Organização de frota e checklists de expedição."),
        ("MÊS 5", "Consolidação", "Treinamento interno e painel de indicadores.")
    ]
    
    for mes, titulo, desc in cronograma:
        with st.container():
            st.markdown(f"""
            <div class="card">
                <strong>{mes} - {titulo}</strong><br>
                {desc}
            </div>
            """, unsafe_allow_html=True)

elif selected == "Metas e Sucesso":
    st.header("🏆 Critérios de Sucesso e Dependências")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("O que mediremos:")
        st.write("✅ Processos críticos operando.")
        st.write("✅ Redução de compras emergenciais.")
        st.write("✅ Melhoria nos prazos de entrega.")
        st.write("✅ Fluxo de caixa semanal estável.")
    with col_b:
        st.subheader("Responsabilidades Status:")
        st.warning("""
        - Decisões rápidas da liderança.
        - Acesso total a dados financeiros/produção.
        - Adesão rigorosa aos novos fluxos.
        """)

elif selected == "Investimento":
    st.header("💳 Investimento e Próximos Passos")
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Mensalidade", "R$ 21.450,00")
        st.write("**Prazo Inicial:** 5 meses")
    with c2:
        st.metric("Total Estimado", "R$ 107.250,00")
        st.write("**Vencimento:** Dia 25")

    st.markdown("""
    ### 🚀 Próximos Passos
    1. Aprovação desta proposta.
    2. Assinatura do contrato.
    3. Reunião de Kick-off.
    4. Início das atividades presenciais.
    """)
    
    if st.button("Aceitar Proposta e Solicitar Contato"):
        st.balloons()
        st.success("Excelente! A equipe Labor Business será notificada.")

# --- RODAPÉ ---
st.divider()
st.caption("Labor Business - Gestão voltada para eficiência e previsibilidade.")
