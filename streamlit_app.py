import streamlit as st

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(
    page_title="Funil Mental",
    page_icon="🧠",
    layout="wide",
)

# ======================================================
# CSS GLOBAL
# ======================================================
st.markdown("""
<style>
body { color: #e5e7eb; }

.card {
    background: #0e1117;
    border: 1px solid #1f2933;
    border-radius: 14px;
    padding: 1.4rem;
    margin-bottom: 1.2rem;
}

.title {
    font-size: 1.25rem;
    font-weight: 800;
    margin-bottom: 0.6rem;
}

.muted { color: #9ca3af; font-size: 0.9rem; }

.highlight {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    padding: 0.2rem 0.45rem;
    border-radius: 6px;
    font-weight: 600;
    display: inline-block;
}

hr {
    border: none;
    border-top: 1px solid #1f2933;
    margin: 0.8rem 0;
}

ul { margin-left: 1.2rem; }
li { margin-bottom: 0.3rem; }
</style>
""", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================
st.sidebar.title("🧠 Navegação")

section = st.sidebar.radio(
    "O que você quer aprender agora?",
    [
        "⚡ Visão Rápida",
        "🔵 TOFU",
        "🟡 MOFU",
        "🔴 BOFU",
        "🩺 Diagnóstico"
    ]
)

# ======================================================
# HEADER
# ======================================================
st.title("🧠 Funil Mental de Vendas")
st.caption("Aprenda rápido. Execute certo. Escale com segurança.")

# ======================================================
# ⚡ VISÃO RÁPIDA
# ======================================================
if section == "⚡ Visão Rápida":

    st.markdown("""
<div class="card">
<b>Regra de ouro:</b><br>
Escala só acontece quando o anúncio respeita o estágio mental do público.
</div>

<div class="card">
<ul>
<li><b>TOFU</b> → gerar curiosidade</li>
<li><b>MOFU</b> → gerar lógica</li>
<li><b>BOFU</b> → gerar segurança</li>
</ul>
</div>

<div class="card">
<b>Erro mais comum:</b><br>
Tentar vender para quem ainda não entendeu.
</div>

<div class="card">
<span class="highlight">
Se precisa explicar, não é BOFU.<br>
Se precisa convencer, o MOFU falhou.<br>
Se precisa vender cedo, o TOFU está errado.
</span>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 🔵 TOFU
# ======================================================
elif section == "🔵 TOFU":

    st.markdown("""
<div class="card">
<div class="title">🔵 TOFU — DESCOBERTA</div>

<b>O que é:</b><br>
Primeiro contato. Nenhuma decisão.

<hr>

<b>Função mental:</b><br>
“Isso existe… talvez seja pra mim.”

<hr>

<b>Pode:</b>
<ul>
<li>Rotina real</li>
<li>Dor silenciosa</li>
<li>Produto aparecendo rápido</li>
</ul>

<b>Não pode:</b>
<ul>
<li>Preço</li>
<li>Desconto</li>
<li>Depoimento longo</li>
</ul>

<hr>

<b>CTA:</b> Saiba mais<br>
<b>Métrica:</b> ThruPlay · 50% vídeo · CPM

<hr>

<span class="highlight">
Produto aparece como parte da rotina, não como argumento de venda.
</span>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 🟡 MOFU
# ======================================================
elif section == "🟡 MOFU":

    st.markdown("""
<div class="card">
<div class="title">🟡 MOFU — EDUCAÇÃO</div>

<b>O que é:</b><br>
Organização mental. Lógica.

<hr>

<b>Função mental:</b><br>
“Isso faz sentido pra mim?”

<hr>

<b>Pode:</b>
<ul>
<li>Explicar por que funciona</li>
<li>Mostrar mecanismo</li>
<li>Comparar soluções</li>
</ul>

<b>Não pode:</b>
<ul>
<li>Urgência</li>
<li>Desconto</li>
<li>Pedir compra</li>
</ul>

<hr>

<b>CTA:</b> Entenda como funciona<br>
<b>Métrica:</b> 50–75% vídeo · CTR

<hr>

<span class="highlight">
MOFU existe para explicar o que o público já começou a suspeitar.
</span>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 🔴 BOFU
# ======================================================
elif section == "🔴 BOFU":

    st.markdown("""
<div class="card">
<div class="title">🔴 BOFU — DECISÃO</div>

<b>O que é:</b><br>
Confirmação. Escolha.

<hr>

<b>Função mental:</b><br>
“Já entendi, só não quero errar.”

<hr>

<b>Pode:</b>
<ul>
<li>Prova social</li>
<li>Oferta clara</li>
<li>Garantia</li>
</ul>

<b>Não pode:</b>
<ul>
<li>Explicar mecanismo</li>
<li>Educar</li>
<li>Alongar demais</li>
</ul>

<hr>

<b>CTA:</b> Comprar agora<br>
<b>Métrica:</b> CPA · ROAS

<hr>

<span class="highlight">
BOFU não empurra a venda. Ele dá segurança para decidir.
</span>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 🩺 DIAGNÓSTICO
# ======================================================
elif section == "🩺 Diagnóstico":

    st.markdown("""
<div class="card">
<div class="title">🩺 Onde está o problema?</div>
</div>
""", unsafe_allow_html=True)

    cpm = st.checkbox("CPM alto")
    ctr = st.checkbox("CTR bom, CPA ruim")
    rmk = st.checkbox("CPA alto no remarketing")

    if cpm:
        st.error("❌ Problema de TOFU → público não preparado")
    if ctr:
        st.warning("⚠️ MOFU fraco → entendimento insuficiente")
    if rmk:
        st.error("❌ BOFU não gera segurança")
    if not (cpm or ctr or rmk):
        st.success("🚀 Funil mentalmente alinhado. Escalar é seguro.")

    st.markdown("""
<div class="card">
<b>Regra prática:</b><br>
O problema quase nunca é BOFU.<br>
Normalmente é falha de preparação mental antes.
</div>
""", unsafe_allow_html=True)
