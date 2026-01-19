import streamlit as st
from streamlit_option_menu import option_menu

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Proposta Status Marcenaria | Labor Business", layout="wide", page_icon="📊")

# --- ESTILIZAÇÃO CSS (Cores Labor Business) ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stApp { max-width: 1100px; margin: 0 auto; }
    .titulo-capa { color: #2c3e50; font-size: 42px; font-weight: bold; line-height: 1.2; }
    .sub-capa { color: #ff9900; font-size: 22px; font-weight: 500; margin-bottom: 30px; }
    .secao-header { color: #2c3e50; border-bottom: 2px solid #ff9900; padding-bottom: 5px; margin-top: 30px; margin-bottom: 20px; font-size: 28px; font-weight: bold; }
    .sub-secao-header { color: #ff9900; font-size: 20px; font-weight: bold; margin-top: 15px; }
    .card-cronograma { background-color: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 5px solid #ff9900; margin-bottom: 15px; }
    .entrega-box { background-color: #e8f5e9; padding: 10px; border-radius: 5px; border: 1px solid #c8e6c9; color: #2e7d32; font-weight: 500; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- MENU LATERAL ---
with st.sidebar:
    try:
        st.image("tela inicial.png", use_container_width=True)
    except:
        st.error("Imagem 'tela inicial.png' não encontrada.")
    
    selected = option_menu(
        menu_title="Conteúdo da Proposta",
        options=["Apresentação", "Escopo Detalhado", "Metodologia", "Cronograma Macro", "Metas e Condições", "Investimento"],
        icons=["house", "list-check", "gear", "calendar-event", "shield-check", "cash-coin"],
        menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#ff9900"}}
    )
    st.divider()
    st.write("**Proponente:** Labor Business")
    st.write("**Cliente:** Status Marcenaria")

# --- CONTEÚDO DAS PÁGINAS ---

if selected == "Apresentação":
    st.markdown('<p class="titulo-capa">Gestão Assistida e Melhoria de Processos – 5 Meses</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-capa">Proposta Comercial: Status Marcenaria</p>', unsafe_allow_html=True)
    
    st.image("tela inicial.png", use_container_width=True)
    
    st.markdown('<div class="secao-header">1) Objetivo do Projeto</div>', unsafe_allow_html=True)
    st.write("A Labor Business atuará na Status Marcenaria durante 5 meses, por meio de um modelo de gestão assistida presencial, com o objetivo de estruturar e consolidar os processos essenciais, garantindo:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("* Organização e padronização dos setores críticos")
        st.markdown("* Redução de desperdícios (material, retrabalho, horas improdutivas)")
        st.markdown("* Agilidade em compras e controle de fornecedores")
        st.markdown("* Controle e auditoria de prestadores terceirizados")
        st.markdown("* Melhoria da previsibilidade financeira e fluxo de caixa")
    with col2:
        st.markdown("* Evolução de produtividade e previsibilidade na produção")
        st.markdown("* Redução de atrasos e melhoria do cumprimento de prazos")
        st.markdown("* Fortalecimento da comunicação entre departamentos")
        st.markdown("* Formação de um ambiente sustentável para continuidade por um gerente interno.")
    
    st.info("Este projeto une diagnóstico + implantação prática + consolidação, com disciplina e governança operacional.")

elif selected == "Escopo Detalhado":
    st.markdown('<div class="secao-header">2) Escopo do Trabalho (Frentes de Atuação)</div>', unsafe_allow_html=True)
    
    # 2.1 Compras
    st.markdown('<div class="sub-secao-header">2.1 Compras (gargalos, desperdícios, agilidade e base de fornecedores)</div>', unsafe_allow_html=True)
    st.markdown("* Mapeamento e redesenho do fluxo de compras")
    st.markdown("* Implantação/ajuste de política de compras e padronização de solicitações")
    st.markdown("* Atualização constante da base de fornecedores com critérios mínimos")
    st.markdown("* Controle de compras emergenciais e correção de causas")
    st.markdown('<div class="entrega-box">Entregas: processo padronizado + base “viva” de fornecedores + rotina semanal de pendências.</div>', unsafe_allow_html=True)

    # 2.2 Terceirizados
    st.markdown('<div class="sub-secao-header">2.2 Gestão de Prestadores Terceirizados (processos, auditorias e base de contratação)</div>', unsafe_allow_html=True)
    st.markdown("* Padronização do processo de contratação e critérios de avaliação")
    st.markdown("* Auditoria por entrega e controle de qualidade/prazo")
    st.markdown("* Redução de retrabalho e desperdícios em terceirizações")
    st.markdown('<div class="entrega-box">Entregas: base de prestadores + modelo de avaliação + checklists de controle.</div>', unsafe_allow_html=True)

    # 2.3 Financeiro
    st.markdown('<div class="sub-secao-header">2.3 Gestão Financeira (fluxo de caixa, pagamentos, recebimentos e melhorias)</div>', unsafe_allow_html=True)
    st.markdown("* Estruturação do fluxo de caixa e previsibilidade semanal")
    st.markdown("* Calendário financeiro (priorização e organização)")
    st.markdown("* Redução de “vazamentos” e compras fora do planejamento")
    st.markdown("* Identificação de oportunidades: renegociações e melhorias no contas a pagar/receber")
    st.markdown("* Orientação sobre investimentos (quando houver excedente)")
    st.markdown('<div class="entrega-box">Entregas: rotina de fechamento semanal e entrega de relatório gerencial dentro do prazo.</div>', unsafe_allow_html=True)

    # 2.4 Produção
    st.markdown('<div class="sub-secao-header">2.4 Produção (desperdícios, prazos, organização e fluxo de processos)</div>', unsafe_allow_html=True)
    st.markdown("* Diagnóstico de gargalos e perdas por processo")
    st.markdown("* Implementação de programação semanal e controle diário")
    st.markdown("* Ajustes na organização, priorização e padronização das rotinas")
    st.markdown("* Integração entre compras, produção e logística")
    st.markdown('<div class="entrega-box">Entregas: rotina de produção estruturada + redução de atrasos e retrabalho.</div>', unsafe_allow_html=True)

    # 2.5 Aprovação
    st.markdown('<div class="sub-secao-header">2.5 Aprovação de Compras com Duas Autorizações</div>', unsafe_allow_html=True)
    st.markdown("* Implantação/ajuste do modelo com duas etapas")
    st.markdown("* Definição de faixas de valor, alçadas e exceções")
    st.markdown("* Registro mínimo para rastreabilidade")
    st.markdown('<div class="entrega-box">Entregas: processo implantado, comunicado e auditável.</div>', unsafe_allow_html=True)

    # 2.6 Logística
    st.markdown('<div class="sub-secao-header">2.6 Logística (frota, custos, organização e melhoria)</div>', unsafe_allow_html=True)
    st.markdown("* Diagnóstico de custos logísticos e pontos de desperdício")
    st.markdown("* Organização de roteiros e agenda de entregas")
    st.markdown("* Controle de frota (manutenção, consumo, indicadores)")
    st.markdown("* Avaliação de eficiência (frota própria x terceirização)")
    st.markdown('<div class="entrega-box">Entregas: rotina logística organizada + medidas de redução de custo e atraso.</div>', unsafe_allow_html=True)

elif selected == "Metodologia":
    st.markdown('<div class="secao-header">3) Metodologia de Execução</div>', unsafe_allow_html=True)
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.write("✔️ **Presencial:** 3 dias/semana (seg/qua/sex)")
        st.write("✔️ **Acompanhamento:** Prático, dentro da operação")
        st.write("✔️ **Implantação:** Rotinas e padronização")
    with col_m2:
        st.write("✔️ **Reuniões:** Curtas, frequentes e orientadas a resultado")
        st.write("✔️ **Gestão:** Indicadores simples, consistentes e úteis")

elif selected == "Cronograma Macro":
    st.markdown('<div class="secao-header">4) Cronograma Macro – 5 Meses</div>', unsafe_allow_html=True)
    
    # Mês 1
    with st.container():
        st.markdown('<div class="card-cronograma"><strong>MÊS 1 — Diagnóstico profundo + estabilização</strong><br>Objetivo: parar o sangramento operacional e trazer visibilidade.</div>', unsafe_allow_html=True)
        st.markdown("- Diagnóstico por área com mapeamento de gargalos e desperdícios\n- Organização das rotinas mínimas (compras, financeiro e produção)\n- Implantação inicial do fluxo de caixa e prioridades de pagamentos\n- Ajustes emergenciais de comunicação entre setores")
        st.markdown('<div class="entrega-box">Entregas Mês 1: Diagnóstico + plano tático de ação + Primeiros fluxos rodando.</div>', unsafe_allow_html=True)
    
    # Mês 2
    with st.container():
        st.markdown('<div class="card-cronograma"><strong>MÊS 2 — Implantação dos processos e regras</strong><br>Objetivo: colocar disciplina no dia a dia e reduzir improviso.</div>', unsafe_allow_html=True)
        st.markdown("- Implantação completa do processo de compras\n- Base de fornecedores estruturada e atualizável\n- Regra de aprovação de compras com 2 autorizações\n- Rotina de produção com programação semanal\n- Financeiro com previsão e calendário de compromissos")
        st.markdown('<div class="entrega-box">Entregas Mês 2: Compras funcionando com padrão + Rotina financeira e produtiva estabilizadas.</div>', unsafe_allow_html=True)

    # Mês 3
    with st.container():
        st.markdown('<div class="card-cronograma"><strong>MÊS 3 — Eficiência e redução real de desperdícios</strong><br>Objetivo: atacar desperdício que está escondido e caro.</div>', unsafe_allow_html=True)
        st.markdown("- Auditoria de prestadores e melhoria do processo de terceirização\n- Redução de retrabalho, falhas e custos indiretos\n- Ajustes finos no planejamento de produção e integração com compras\n- Controle de gastos recorrentes e negociação com fornecedores")
        st.markdown('<div class="entrega-box">Entregas Mês 3: Queda no volume de retrabalho + Melhoria perceptível na previsibilidade.</div>', unsafe_allow_html=True)

    # Mês 4
    with st.container():
        st.markdown('<div class="card-cronograma"><strong>MÊS 4 — Logística e performance por prazos (foco em entrega)</strong><br>Objetivo: reduzir custo por entrega e eliminar atrasos.</div>', unsafe_allow_html=True)
        st.markdown("- Revisão de custos logísticos e padrões de entrega\n- Organização de frota/agenda, manutenção e consumo\n- Padronização de checklists de saída e entrega\n- Ajuste geral do fluxo (produção → expedição → entrega)")
        st.markdown('<div class="entrega-box">Entregas Mês 4: Logística operando com controle + Redução de "correções emergenciais".</div>', unsafe_allow_html=True)

    # Mês 5
    with st.container():
        st.markdown('<div class="card-cronograma"><strong>MÊS 5 — Consolidação e continuidade</strong><br>Objetivo: deixar uma empresa “gerenciável” sem depender da consultoria.</div>', unsafe_allow_html=True)
        st.markdown("- Consolidação final dos processos implantados\n- Treinamento dos responsáveis internos\n- Implantação do painel mínimo de indicadores\n- Definição de rotinas e responsabilidades fixas\n- Plano de continuidade para 90 dias pós-projeto")
        st.markdown('<div class="entrega-box">Entregas Mês 5: Operação sustentável + Modelo de gestão simples com disciplina.</div>', unsafe_allow_html=True)

elif selected == "Metas e Condições":
    st.markdown('<div class="secao-header">5) Critérios de Sucesso (Metas do Projeto)</div>', unsafe_allow_html=True)
    st.write("O sucesso será medido por entregas e melhorias reais, acompanhadas semanalmente:")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown("**Governança e Controle:**")
        st.markdown("- Processos críticos implantados e funcionando\n- Base de fornecedores/prestadores estruturada\n- Aprovação com 2 autorizações operando\n- Comunicação padronizada")
    with col_s2:
        st.markdown("**Operacionais e Financeiros:**")
        st.markdown("- Redução de compras emergenciais\n- Melhoria no cumprimento de prazos\n- Redução de desperdício e retrabalho\n- Fluxo de caixa com controle semanal")

    st.markdown('<div class="secao-header">6) Dependências da Contratante</div>', unsafe_allow_html=True)
    st.warning("Para os resultados acontecerem, a Status deve garantir: disponibilidade de lideranças, acesso a dados, adesão ao fluxo de aprovação e disciplina nas rotinas.")

    st.markdown('<div class="secao-header">7) Limites do Escopo</div>', unsafe_allow_html=True)
    st.markdown("**Incluído:** Diagnóstico, implantação, criação de controles e gestão assistida.")
    st.markdown("**Não incluído:** Garantia de resultado sem adesão da equipe, auditoria contábil/fiscal e rotinas de RH.")

elif selected == "Investimento":
    st.markdown('<div class="secao-header">8) Investimento e Condições Comerciais</div>', unsafe_allow_html=True)
    
    col_i1, col_i2, col_i3 = st.columns(3)
    col_i1.metric("Investimento Mensal", "R$ 21.450,00")
    col_i2.metric("Prazo Total", "5 Meses")
    
    st.markdown("""
    * **Formato:** seg/qua/sex – 09h às 17h
    * **Pagamento:** Mensal mediante nota fiscal
    * **Vencimento:** Todo dia 05
    """)

    st.markdown('<div class="secao-header">9) Próximos Passos</div>', unsafe_allow_html=True)
    st.write("1. Aprovação da proposta | 2. Assinatura do contrato | 3. Reunião de kick-off | 4. Início das atividades")

    st.markdown('<div class="secao-header">10) Encerramento</div>', unsafe_allow_html=True)
    st.write("A Labor Business se compromete a atuar com foco em controle, eficiência e previsibilidade, preparando a empresa para sustentação com liderança interna.")
    st.button("Aceitar e Iniciar Projeto")

# --- RODAPÉ ---
st.divider()
st.caption("Labor Business - Inteligência em Gestão e Resultados")
