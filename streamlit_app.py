import streamlit as st

st.set_page_config(
    page_title="Manual Mental de Funil de Vendas",
    layout="wide"
)

# ==================================================
# ESTILO VISUAL
# ==================================================
st.markdown("""
<style>
.block {
    padding: 1.8rem;
    border-radius: 16px;
    background: #0e1117;
    border: 1px solid #1f2933;
    margin-bottom: 1.6rem;
}
.small {
    color: #9ca3af;
    font-size: 0.95rem;
}
.tag {
    display: inline-block;
    padding: 0.3rem 0.7rem;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 600;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================
st.title("🧠 Manual Mental de Funil de Vendas")
st.caption(
    "Um guia visual e didático para entender como a mente do público funciona — "
    "e como escalar sem quebrar o funil."
)

st.divider()

# ==================================================
# ABAS PRINCIPAIS
# ==================================================
tab_principio, tab_mente, tab_regua, tab_tofu, tab_mofu, tab_bofu, tab_resumo = st.tabs(
    [
        "🧠 Princípio",
        "🧠 Mente do Público",
        "📊 Régua de Consciência",
        "🔹 TOFU",
        "🟡 MOFU",
        "🔴 BOFU",
        "🔥 Resumo"
    ]
)

# ==================================================
# PRINCÍPIO CENTRAL
# ==================================================
with tab_principio:
    st.markdown("## 🧠 Princípio Central")

    st.markdown("""
    <div class="block">
    O fluxo de escala só funciona quando replica o processo mental real do público-alvo.

    Escala não é aumentar orçamento.  
    Escala não é duplicar conjunto.  
    Escala não é abrir LAL aleatório.

    <br>

    <strong>Escala é ampliar algo que já está coerente com a mente do comprador.</strong>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    O fator mais importante da escala é o <span class="tag">timing mental</span>.

    TOFU precisa ser leve e escalável.  
    MOFU precisa ser lógico e educativo.  
    BOFU precisa ser forte, sem contaminar o funil.

    <br><br>
    👉 Isso é tráfego de escala. Não é tráfego de tentativa.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# MENTE DO PÚBLICO
# ==================================================
with tab_mente:
    st.markdown("## 🧠 Como a Mente do Público Funciona (Realidade)")

    st.markdown("""
    <div class="block">
    Antes de comprar, a pessoa não passa por funis bonitos no PowerPoint.

    Ela passa por <strong>estágios mentais reais</strong>:

    Desconhecimento  
    Identificação do problema  
    Comparação e ceticismo  
    Confiança  
    Decisão

    <br><br>
    👉 O Meta Ads só escala quando os anúncios acompanham essa progressão.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    <strong>Erro clássico de escala:</strong>

    Público aberto  
    Criativo de oferta  
    “Compre agora”  
    Orçamento aumentado  

    <br>

    ROAS cai.  
    CPM sobe.  
    O algoritmo perde sinal.

    <br>
    Isso acontece porque a mente ainda não está pronta.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# RÉGUA DE CONSCIÊNCIA
# ==================================================
with tab_regua:
    st.markdown("## 📊 Régua de Consciência")

    st.markdown("""
    <div class="block">
    Todo criativo deve ser analisado pelo que ele exige da mente.

    Perguntas essenciais:

    Esse vídeo pede decisão ou curiosidade?  
    Ele explica o porquê ou apenas mostra que existe?  
    Ele reduz ou aumenta o risco mental?  
    Quanto esforço cognitivo exige?

    <br>
    Essa régua define se o criativo pertence ao TOFU, MOFU ou BOFU.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# TOFU
# ==================================================
with tab_tofu:
    st.markdown("## 🔹 TOFU — Primeiro Contato")

    with st.expander("🧠 Estágio mental do público"):
        st.write("""
        “Isso existe… e talvez seja pra mim.”

        O usuário ainda não quer comprar.  
        Mas já consegue se enxergar no cenário, reconhecer a dor  
        e aceitar a existência da solução.
        """)

    with st.expander("🎯 Objetivo real do TOFU"):
        st.write("""
        Criar identificação com a rotina diária.

        O produto aparece de forma breve, natural e não invasiva.

        Mostrar demais gera rejeição.  
        Esconder demais perde sinal.  

        O equilíbrio é o que escala.
        """)

    with st.expander("📹 Formato ideal de criativo"):
        st.write("""
        Vídeos até 20 segundos.  
        Situação cotidiana real.  
        Dor silenciosa, sem exagero.  
        Produto como parte da rotina.  
        Micro curiosidade.  
        CTA leve.
        """)

    with st.expander("📊 Métricas-chave"):
        st.write("""
        ThruPlay  
        50% de vídeo  
        CPM saudável  

        Essas métricas medem atenção qualificada, não venda.
        """)

    st.info("No TOFU, o produto aparece como parte da rotina, não como argumento de venda.")

# ==================================================
# MOFU
# ==================================================
with tab_mofu:
    st.markdown("## 🟡 MOFU — Educação e Justificação")

    with st.expander("🧠 Estágio mental do público"):
        st.write("""
        “Ok… isso pode funcionar.  
        Mas será que funciona pra mim?”

        Aqui surgem ceticismo, comparação e busca por lógica.
        """)

    with st.expander("🎯 Objetivo real do MOFU"):
        st.write("""
        Justificar racionalmente a solução sem pedir compra.

        Explicar o porquê.  
        Mostrar o como, sem entregar tudo.  
        Reduzir objeções silenciosas.
        """)

    with st.expander("📹 Formato ideal de criativo"):
        st.write("""
        Vídeos de 30 a 60 segundos.

        Reforço da dor.  
        Introdução do mecanismo.  
        Comparação implícita.  
        Micro prova.  
        CTA de aprofundamento.
        """)

    st.info("MOFU existe para explicar o que o público já começou a suspeitar.")

# ==================================================
# BOFU
# ==================================================
with tab_bofu:
    st.markdown("## 🔴 BOFU — Decisão e Conversão")

    with st.expander("🧠 Estágio mental do público"):
        st.write("""
        “Eu já entendi.  
        Agora só não quero errar.”

        O medo aqui é apenas da escolha.
        """)

    with st.expander("🎯 Objetivo real do BOFU"):
        st.write("""
        Facilitar a decisão reduzindo:

        Risco percebido  
        Medo de arrependimento  
        Dúvida de qualidade  
        Insegurança pós-compra
        """)

    with st.expander("📹 Formato ideal de criativo"):
        st.write("""
        Vídeos de 15 a 40 segundos.

        Confirmação do problema.  
        Prova real.  
        Validação social ou técnica.  
        Oferta clara.  
        CTA de ação.
        """)

    st.warning("Se o BOFU precisa explicar demais, o MOFU falhou.")
    st.info("BOFU não empurra a venda. Ele dá segurança para decidir.")

# ==================================================
# RESUMO FINAL
# ==================================================
with tab_resumo:
    st.markdown("## 🔥 Resumo Final — Mente do Público")

    st.markdown("""
    <div class="block">
    TOFU responde: “Isso existe?”  
    MOFU responde: “Isso faz sentido?”  
    BOFU responde: “Posso confiar?”

    <br>
    Quando seus anúncios seguem esse raciocínio,  
    a escala deixa de ser tentativa e vira consequência.
    </div>
    """, unsafe_allow_html=True)
