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
.list {
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================
st.title("🧠 Manual Mental de Funil de Vendas")
st.caption(
    "Um manual visual para ensinar como funciona um funil baseado na mente real do público — "
    "e como escalar sem quebrar o processo."
)

st.divider()

# ==================================================
# ABAS
# ==================================================
tab_principio, tab_mente, tab_regua, tab_tofu, tab_mofu, tab_bofu, tab_mapa = st.tabs(
    [
        "🧠 Princípio",
        "🧠 Mente do Público",
        "📊 Régua",
        "🔹 TOFU",
        "🟡 MOFU",
        "🔴 BOFU",
        "🗺️ Mapa dos Criativos"
    ]
)

# ==================================================
# PRINCÍPIO
# ==================================================
with tab_principio:
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
    O fator decisivo é o <span class="tag">timing mental</span>.

    TOFU leve e escalável.  
    MOFU lógico e educativo.  
    BOFU forte, sem contaminar o funil.

    <br><br>
    👉 Isso é tráfego de escala, não de tentativa.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# MENTE DO PÚBLICO
# ==================================================
with tab_mente:
    st.markdown("""
    <div class="block">
    Antes de comprar, a pessoa passa por estágios mentais reais:

    Desconhecimento  
    Identificação do problema  
    Comparação e ceticismo  
    Confiança  
    Decisão

    <br>
    O Meta Ads só escala quando os anúncios acompanham essa progressão.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="block">
    <strong>Erro clássico de escala:</strong>

    Público aberto  
    Criativo de oferta  
    “Compre agora”  

    <br>
    ROAS cai.  
    CPM sobe.  
    Algoritmo perde sinal.

    <br>
    Isso acontece porque a mente ainda não está pronta.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# RÉGUA
# ==================================================
with tab_regua:
    st.markdown("""
    <div class="block">
    Classifique todo criativo pelo que ele exige da mente:

    ❓ Pede decisão ou curiosidade?  
    🧠 Explica o porquê ou só mostra que existe?  
    ⚠️ Reduz ou aumenta risco mental?  
    ⏱️ Quanto esforço cognitivo exige?

    <br>
    Essa régua define o nível do funil.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# TOFU
# ==================================================
with tab_tofu:
    st.markdown("## 🔹 TOFU — Primeiro Contato")
    st.markdown("<div class='block'><strong>Nível de consciência:</strong> “Isso existe?”</div>", unsafe_allow_html=True)

    st.markdown("### 🎬 Tipos de criativo TOFU")
    st.markdown("""
    <div class="block list">
    Uso rápido no dia a dia  
    Close sutil do produto  
    Rotina real  
    Identificação pessoal  
    Produto resolve sem ser protagonista
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔵 Criativos TOFU — FLEXLIVE")
    st.markdown("""
    <div class="block list">
    07 — Apresentação simples  
    17 — Uso durante atividade  
    24 — Rotina ativa  
    25 — Lista objetiva de benefícios  
    26 — Mensagens curtas  
    29 — Rotina simples (10s)
    </div>
    """, unsafe_allow_html=True)

    st.info("Função mental: apresentar sem exigir decisão.")

# ==================================================
# MOFU
# ==================================================
with tab_mofu:
    st.markdown("## 🟡 MOFU — Educação e Justificação")
    st.markdown("<div class='block'><strong>Nível de consciência:</strong> “Isso faz sentido?”</div>", unsafe_allow_html=True)

    st.markdown("### 🎬 Tipos de criativo MOFU")
    st.markdown("""
    <div class="block list">
    Educacional  
    Mecanismo  
    Comparação  
    Demonstração parcial
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🟡 Criativos MOFU — FLEXLIVE")
    st.markdown("""
    <div class="block list">
    02 — Anti-inflamatório vs natural  
    03 — Pesquisa + mecanismo  
    04 — Dor crônica  
    16 — Comparação com joelheira  
    22 — Profissional em pé  
    28 — Passo a passo  
    </div>
    """, unsafe_allow_html=True)

    st.info("Função mental: organizar raciocínio e reduzir ceticismo.")

# ==================================================
# BOFU
# ==================================================
with tab_bofu:
    st.markdown("## 🔴 BOFU — Decisão")
    st.markdown("<div class='block'><strong>Nível de consciência:</strong> “Posso confiar?”</div>", unsafe_allow_html=True)

    st.markdown("### 🎬 Tipos de criativo BOFU")
    st.markdown("""
    <div class="block list">
    Prova social  
    Antes e depois funcional  
    Autoridade  
    Oferta estruturada  
    Escassez legítima
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔴 Criativos BOFU — FLEXLIVE")
    st.markdown("""
    <div class="block list">
    13 — Benefícios + oferta  
    20 — Oferta direta  
    23 — Rotina + desconto  
    27 — Prova familiar  
    01 — História longa  
    09 — Dor extrema + garantia
    </div>
    """, unsafe_allow_html=True)

    st.warning("Se o BOFU precisa explicar demais, o MOFU falhou.")

# ==================================================
# MAPA FINAL
# ==================================================
with tab_mapa:
    st.markdown("""
    <div class="block">
    🔢 31 criativos organizados por função mental.

    TOFU apresenta.  
    MOFU explica.  
    BOFU confirma.

    <br>
    Escalar fora dessa ordem quebra o funil.
    </div>
    """, unsafe_allow_html=True)
