import streamlit as st

# --------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="Manual Mental de Funil",
    layout="wide"
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("🧠 Manual Mental de Funil")
menu = st.sidebar.radio(
    "Navegação",
    [
        "Introdução",
        "Mente do Público",
        "Régua de Consciência",
        "TOFU — Descoberta",
        "MOFU — Educação",
        "BOFU — Decisão",
        "Classificador de Criativos",
        "Diagnóstico de Escala"
    ]
)

# --------------------------------------------------
# INTRODUÇÃO
# --------------------------------------------------
if menu == "Introdução":
    st.title("🧠 Manual Mental de Funil de Vendas")

    st.markdown("""
    ### PRINCÍPIO CENTRAL

    O fluxo de escala só funciona quando **replica o processo mental real do público-alvo**.

    **Escala NÃO é:**
    - aumentar orçamento  
    - duplicar conjunto  
    - abrir LAL aleatório  

    **Escala É:**
    > Ampliar algo que já está coerente com a mente do comprador.
    """)

    st.success("👉 Isso é tráfego de escala. Não tráfego de tentativa.")

# --------------------------------------------------
# MENTE DO PÚBLICO
# --------------------------------------------------
elif menu == "Mente do Público":
    st.title("🧠 Como a Mente do Público Funciona")

    st.markdown("""
    Antes de comprar, a pessoa não segue funis bonitos.
    Ela passa por **estágios mentais reais**:

    1. Desconhecimento  
    2. Identificação do problema  
    3. Comparação / Ceticismo  
    4. Confiança  
    5. Decisão  

    👉 O Meta Ads só escala quando seus anúncios **acompanham essa progressão**.
    """)

    st.info("Funil é consequência da mente. Não o contrário.")

# --------------------------------------------------
# RÉGUA DE CONSCIÊNCIA
# --------------------------------------------------
elif menu == "Régua de Consciência":
    st.title("📊 Régua de Consciência do Criativo")

    st.markdown("Responda com honestidade:")

    pede_decisao = st.checkbox("❓ Esse criativo pede decisão?")
    explica = st.checkbox("🧠 Ele explica o porquê?")
    reduz_risco = st.checkbox("⚠️ Ele reduz risco mental?")
    esforco = st.slider("⏱️ Esforço cognitivo exigido", 1, 5)

    st.markdown("### Diagnóstico Mental")

    if pede_decisao and esforco >= 4:
        st.error("🚨 Criativo exige decisão cedo demais → quebra escala.")
    elif not pede_decisao and explica and reduz_risco:
        st.success("✅ Criativo coerente com MOFU.")
    elif not pede_decisao and esforco <= 2:
        st.success("✅ Criativo leve → ideal para TOFU.")
    else:
        st.warning("⚠️ Criativo desalinhado. Reavaliar estágio mental.")

# --------------------------------------------------
# TOFU
# --------------------------------------------------
elif menu == "TOFU — Descoberta":
    st.title("🔹 TOFU — Primeiro Contato")

    st.markdown("""
    **Estágio mental do público:**
    > “Isso existe… talvez seja pra mim.”

    **Objetivo real do TOFU:**
    Criar identificação com a rotina **sem exigir decisão**.
    """)

    st.markdown("""
    **Formato ideal:**
    - Vídeos até 20s  
    - Situação cotidiana real  
    - Produto aparece de forma sutil  
    - Micro curiosidade  
    """)

    st.success("No TOFU, o produto aparece como parte da rotina, não como argumento de venda.")

    st.markdown("### Métricas-chave")
    st.metric("Foco", "Atenção Qualificada")
    st.metric("KPIs", "ThruPlay • 50% Vídeo • CPM")

# --------------------------------------------------
# MOFU
# --------------------------------------------------
elif menu == "MOFU — Educação":
    st.title("🟡 MOFU — Educação e Justificação")

    st.markdown("""
    **Estágio mental:**
    > “Ok… isso pode funcionar. Mas será que funciona pra mim?”

    **Função do MOFU:**
    - Organizar o raciocínio  
    - Reduzir ceticismo  
    - Explicar o mecanismo  
    """)

    st.markdown("""
    **Tipos de criativo:**
    - Educacional  
    - Mecanismo  
    - Comparação  
    - Demonstração parcial  
    """)

    st.success("MOFU existe para explicar o que o público já começou a suspeitar.")

    st.markdown("### Métricas-chave")
    st.metric("KPIs", "50–75% Vídeo • CTR • Tempo Médio")

# --------------------------------------------------
# BOFU
# --------------------------------------------------
elif menu == "BOFU — Decisão":
    st.title("🔴 BOFU — Decisão")

    st.markdown("""
    **Estágio mental:**
    > “Eu já entendi. Só não quero errar.”

    **BOFU não persuade. BOFU confirma.**
    """)

    st.markdown("""
    **Função do BOFU:**
    - Reduzir medo  
    - Passar segurança  
    - Facilitar a decisão  
    """)

    st.warning("Se o BOFU precisa explicar demais, o problema está no MOFU.")

    st.success("BOFU não empurra a venda. Ele dá segurança para decidir.")

    st.markdown("### Métricas-chave")
    st.metric("KPIs", "CPA • ROAS • Conversão • AOV")

# --------------------------------------------------
# CLASSIFICADOR DE CRIATIVOS
# --------------------------------------------------
elif menu == "Classificador de Criativos":
    st.title("🧪 Classificador Mental de Criativos")

    estagio = st.selectbox(
        "Estágio mental do público:",
        ["Frio / Descoberta", "Curioso / Avaliando", "Pronto para decidir"]
    )

    cta = st.selectbox(
        "CTA do criativo:",
        ["Saiba mais", "Entenda como funciona", "Comprar agora"]
    )

    if estagio == "Frio / Descoberta" and cta == "Comprar agora":
        st.error("🚨 BOFU em público frio → quebra total de escala.")
    elif estagio == "Curioso / Avaliando" and cta == "Entenda como funciona":
        st.success("✅ MOFU bem alinhado com o timing mental.")
    elif estagio == "Pronto para decidir" and cta == "Comprar agora":
        st.success("🔥 BOFU correto → foco em eficiência.")
    else:
        st.warning("⚠️ CTA desalinhado com o estágio mental.")

# --------------------------------------------------
# DIAGNÓSTICO DE ESCALA
# --------------------------------------------------
elif menu == "Diagnóstico de Escala":
    st.title("📈 Diagnóstico de Escala do Funil")

    tofu_ok = st.checkbox("TOFU gera curiosidade e identificação?")
    mofu_ok = st.checkbox("MOFU reduz objeções e organiza o raciocínio?")
    bofu_ok = st.checkbox("BOFU converte sem explicar demais?")

    if tofu_ok and mofu_ok and bofu_ok:
        st.success("🔥 Funil mentalmente escalável. Escalar orçamento faz sentido.")
    else:
        st.error("🚨 Funil desalinhado. Escalar agora gera desperdício.")

    st.markdown("""
    ### Lembrete final:
    **TOFU desperta**  
    **MOFU organiza**  
    **BOFU confirma**
    """)
