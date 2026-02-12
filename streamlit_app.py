import streamlit as st

st.set_page_config(
    page_title="Manual Mental de Funil de Vendas",
    layout="wide"
)

# ==================================================
# ESTILO VISUAL CLEAN
# ==================================================
st.markdown("""
<style>
body {
    color: #e5e7eb;
}
.card {
    background: #0e1117;
    border: 1px solid #1f2933;
    border-radius: 14px;
    padding: 1.6rem;
    margin-bottom: 1.4rem;
}
.title {
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 0.6rem;
}
.muted {
    color: #9ca3af;
}
.highlight {
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
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
st.caption("Todo o conteúdo original organizado apenas em um layout limpo, visual e fácil de consumir.")
st.divider()

# ==================================================
# ABAS
# ==================================================
tabs = st.tabs([
    "🧠 Princípio Central",
    "🧠 Mente do Público",
    "📊 Régua de Consciência",
    "🔹 TOFU",
    "🟡 MOFU",
    "🔴 BOFU",
    "🔥 Resumo + Criativos"
])

# ==================================================
# PRINCÍPIO CENTRAL
# ==================================================
with tabs[0]:
    st.markdown("""
    <div class="card">
    <div class="title">🧠 PRINCÍPIO CENTRAL</div>

    O fluxo de escala só funciona quando replica o processo mental real do público alvo.

    <br><br>
    Escala não é:
    <div class="list">
    aumentar orçamento<br>
    duplicar conjunto<br>
    abrir LAL aleatório
    </div>

    <br>
    Escala é ampliar algo que já está coerente com a mente do comprador.

    <br><br>
    O mais importante é o <span class="highlight">timing mental</span>:

    <br><br>
    TOFU leve e escalável<br>
    MOFU lógico e educativo<br>
    BOFU forte, sem contaminar o funil

    <br><br>
    👉 Isso é tráfego de escala, não de tentativa.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# MENTE DO PÚBLICO
# ==================================================
with tabs[1]:
    st.markdown("""
    <div class="card">
    <div class="title">1️⃣ COMO A MENTE DO PÚBLICO FUNCIONA (REALIDADE)</div>

    Antes de comprar, a pessoa passa por estágios mentais, não por funis bonitos no PowerPoint:

    <div class="list">
    Desconhecimento<br>
    Identificação do problema<br>
    Comparação / ceticismo<br>
    Confiança<br>
    Decisão
    </div>

    <br>
    👉 O Meta Ads só escala quando seus anúncios acompanham essa progressão.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <div class="title">2️⃣ O ERRO MAIS COMUM NA “ESCALA”</div>

    🚨 Tentar escalar BOFU direto para público frio.

    <br><br>
    Exemplo clássico:

    <div class="list">
    Público aberto<br>
    Criativo de oferta<br>
    “Compre agora”<br>
    Aumenta orçamento
    </div>

    <br>
    ROAS cai<br>
    CPM sobe<br>
    Algoritmo perde sinal

    <br><br>
    👉 Isso acontece porque a mente ainda não está pronta.
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# RÉGUA DE CONSCIÊNCIA
# ==================================================
with tabs[2]:
    st.markdown("""
    <div class="card">
    <div class="title">3️⃣ RÉGUA DE CONSCIÊNCIA</div>

    Classifique cada criativo com base em:

    <div class="list">
    ❓ Esse vídeo pede decisão ou curiosidade?<br>
    🧠 Ele explica “por quê” ou apenas mostra “que existe”?<br>
    ⚠️ Ele aumenta ou reduz risco mental?<br>
    ⏱️ Quanto esforço cognitivo exige?
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# TOFU
# ==================================================
with tabs[3]:
    st.markdown("""
    <div class="card">
    <div class="title">🔹 ETAPA 1 — TOFU (PRIMEIRO CONTATO)</div>

    TOFU não é esconder o produto.<br>
    TOFU é apresentar o produto sem exigir decisão.

    <br><br>
    <strong>Estágio mental do público</strong><br>
    “Isso existe… e talvez seja pra mim.”

    <br><br>
    Aqui o usuário ainda não quer comprar, mas já consegue:
    <div class="list">
    se enxergar no cenário<br>
    reconhecer a dor<br>
    aceitar a existência da solução
    </div>

    <br>
    <strong>OBJETIVO REAL DO TOFU</strong><br>
    Criar identificação com a rotina diária, enquanto o produto aparece de forma breve, natural e não invasiva.

    <br><br>
    <strong>FORMATO IDEAL DE CRIATIVO</strong><br>
    Vídeos curtos — até 20 segundos<br>
    Situação cotidiana real<br>
    Dor silenciosa (sem exagero)<br>
    Produto aparece como parte da rotina<br>
    Micro curiosidade<br>
    CTA leve

    <br><br>
    CTA recomendado: “Saiba mais”
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# MOFU
# ==================================================
with tabs[4]:
    st.markdown("""
    <div class="card">
    <div class="title">🔹 ETAPA 2 — MOFU (EDUCAÇÃO + JUSTIFICAÇÃO)</div>

    MOFU não vende.<br>
    MOFU faz sentido.

    <br><br>
    <strong>Estágio mental do público</strong><br>
    “Ok… isso pode funcionar. Mas será que funciona pra mim?”

    <br><br>
    <strong>OBJETIVO REAL DO MOFU</strong><br>
    Justificar racionalmente a solução, sem pedir compra.

    <br><br>
    <strong>FORMATO IDEAL DE CRIATIVO</strong><br>
    Vídeos de 30 a 60 segundos<br>
    Reforço da dor já reconhecida<br>
    Introdução do mecanismo<br>
    Comparação implícita<br>
    Micro prova<br>
    CTA de aprofundamento
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# BOFU
# ==================================================
with tabs[5]:
    st.markdown("""
    <div class="card">
    <div class="title">🔹 ETAPA 3 — BOFU (DECISÃO + CONVERSÃO)</div>

    BOFU não é persuasão.<br>
    BOFU é confirmação.

    <br><br>
    <strong>Estágio mental do público</strong><br>
    “Eu já entendi. Agora só não quero errar.”

    <br><br>
    <strong>OBJETIVO REAL DO BOFU</strong><br>
    Facilitar a decisão reduzindo risco percebido, medo de arrependimento,
    dúvida de qualidade e insegurança pós-compra.

    <br><br>
    <strong>FORMATO IDEAL DE CRIATIVO</strong><br>
    Vídeos de 15 a 40 segundos<br>
    Confirmação do problema<br>
    Prova real<br>
    Validação social ou técnica<br>
    Oferta clara<br>
    CTA de ação
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# RESUMO + CRIATIVOS
# ==================================================
with tabs[6]:
    st.markdown("""
    <div class="card">
    <div class="title">🔥 RESUMO FINAL DO FUNIL</div>

    TOFU: “Isso existe?”<br>
    MOFU: “Isso faz sentido?”<br>
    BOFU: “Posso confiar?”

    <br><br>
    Quando seus anúncios seguem esse raciocínio,
    a escala deixa de ser tentativa e vira consequência.

    <br><br>
    🔢 31 criativos organizados por função mental.
    </div>
    """, unsafe_allow_html=True)
