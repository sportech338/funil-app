import streamlit as st

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(
    page_title="Manual Mental de Funil de Vendas",
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
    padding: 1.6rem;
    margin-bottom: 1.4rem;
}

.title {
    font-size: 1.3rem;
    font-weight: 800;
    margin-bottom: 0.6rem;
}

.muted { color: #9ca3af; font-size: 0.95rem; }

.highlight {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    padding: 0.15rem 0.45rem;
    border-radius: 6px;
    font-weight: 600;
}

.micro {
    margin-top: 1.4rem;
    padding: 0.8rem 1rem;
    border-left: 4px solid;
    background: #0b1220;
    border-radius: 10px;
}

.micro-title { font-weight: 800; font-size: 1.05rem; }
.micro-desc { color: #9ca3af; font-size: 0.9rem; }

.micro.tofu { border-color: #3b82f6; }
.micro.mofu { border-color: #f59e0b; }
.micro.bofu { border-color: #ef4444; }

hr {
    border: none;
    border-top: 1px solid #1f2933;
    margin: 1rem 0;
}

ul { margin-left: 1.2rem; }
li { margin-bottom: 0.35rem; }
</style>
""", unsafe_allow_html=True)

# ======================================================
# HEADER
# ======================================================
st.title("🧠 Manual Mental de Funil de Vendas")
st.caption("Escala não é tráfego. É psicologia aplicada.")

# ======================================================
# PRINCÍPIO CENTRAL
# ======================================================
st.markdown("""
<div class="card">
<div class="title">🧠 Princípio Central</div>

O fluxo de escala só funciona quando replica o
<span class="highlight">processo mental real do público</span>.

<hr>

<b>Escala não é:</b>
<ul>
<li>Aumentar orçamento</li>
<li>Duplicar conjunto</li>
<li>Abrir LAL aleatório</li>
</ul>

<b>Escala é ampliar algo que já está coerente com a mente do comprador.</b>

<hr>

<b>Timing mental correto:</b>
<ul>
<li>TOFU leve e escalável</li>
<li>MOFU lógico e educativo</li>
<li>BOFU forte, sem contaminar o funil</li>
</ul>

<b>👉 Isso é tráfego de escala, não de tentativa.</b>
</div>
""", unsafe_allow_html=True)

# ======================================================
# COMO A MENTE FUNCIONA
# ======================================================
st.markdown("""
<div class="card">
<div class="title">1️⃣ Como a mente do público funciona</div>

<ul>
<li>Desconhecimento</li>
<li>Identificação do problema</li>
<li>Comparação / ceticismo</li>
<li>Confiança</li>
<li>Decisão</li>
</ul>

<p class="highlight">
O Meta Ads só escala quando seus anúncios acompanham essa progressão.
</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# ERRO MAIS COMUM
# ======================================================
st.markdown("""
<div class="card">
<div class="title">2️⃣ O erro mais comum na escala</div>

<ul>
<li>Público aberto</li>
<li>Criativo de oferta</li>
<li>“Compre agora”</li>
<li>Aumenta orçamento</li>
<li>ROAS cai</li>
<li>CPM sobe</li>
<li>Algoritmo perde sinal</li>
</ul>

<p class="highlight">
Isso acontece porque a mente ainda não está pronta.
</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# RÉGUA DE CONSCIÊNCIA
# ======================================================
st.markdown("""
<div class="card">
<div class="title">3️⃣ Régua de Consciência</div>

<ul>
<li>❓ Pede decisão ou curiosidade?</li>
<li>🧠 Explica o “por quê” ou só mostra que existe?</li>
<li>⚠️ Aumenta ou reduz risco mental?</li>
<li>⏱️ Quanto esforço cognitivo exige?</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ======================================================
# TOFU
# ======================================================
with st.expander("🔹 ETAPA 1 — TOFU (Primeiro Contato)", expanded=True):
    st.markdown("""
<div class="card">

<div class="micro tofu">
<div class="micro-title">🔵 TOFU — DESCOBERTA (Puro)</div>
<div class="micro-desc">Primeiro contato · CPM baixo · escala longa</div>
</div>

<ul>
<li>Apresentação simples</li>
<li>Produto aparece sem explicação</li>
<li>Zero argumento de venda</li>
</ul>

<div class="micro tofu">
<div class="micro-title">🔵 TOFU — IDENTIFICAÇÃO</div>
<div class="micro-desc">Reconhecimento da dor · espelhamento</div>
</div>

<ul>
<li>Rotina real</li>
<li>Dor silenciosa</li>
<li>Produto como detalhe</li>
</ul>

<div class="micro tofu">
<div class="micro-title">🔵 TOFU — CURIOSIDADE ATIVA</div>
<div class="micro-desc">Aceitação da solução · abertura cognitiva</div>
</div>

<ul>
<li>Uso rápido</li>
<li>Close sutil</li>
<li>“Eu comecei a usar por causa disso…”</li>
</ul>

<b>CTA:</b> <span class="highlight">Saiba mais</span>

<hr>

<b>Métricas:</b> ThruPlay · 50% vídeo · CPM saudável
</div>
""", unsafe_allow_html=True)

# ======================================================
# MOFU
# ======================================================
with st.expander("🟡 ETAPA 2 — MOFU (Educação + Justificação)"):
    st.markdown("""
<div class="card">

<div class="micro mofu">
<div class="micro-title">🟡 MOFU — EDUCAÇÃO</div>
<div class="micro-desc">Organiza o raciocínio · reduz ceticismo</div>
</div>

<ul>
<li>Educacional</li>
<li>Mecanismo</li>
<li>Comparação lógica</li>
</ul>

<div class="micro mofu">
<div class="micro-title">🟠 MOFU — VALIDAÇÃO | PRÉ-DECISÃO</div>
<div class="micro-desc">Reduz medo de errar · prepara BOFU</div>
</div>

<ul>
<li>Casos reais</li>
<li>Antes/depois funcional</li>
<li>Validação profissional</li>
</ul>

<b>CTA:</b> <span class="highlight">Entenda como funciona</span>

<hr>

<b>Métricas:</b> 50–75% vídeo · CTR · Tempo médio
</div>
""", unsafe_allow_html=True)

# ======================================================
# BOFU
# ======================================================
with st.expander("🔴 ETAPA 3 — BOFU (Decisão + Conversão)"):
    st.markdown("""
<div class="card">

<div class="micro bofu">
<div class="micro-title">🔴 BOFU — DECISÃO</div>
<div class="micro-desc">Conversão direta · eficiência</div>
</div>

<ul>
<li>Oferta clara</li>
<li>Benefício principal</li>
<li>CTA direto</li>
</ul>

<div class="micro bofu">
<div class="micro-title">🧠 BOFU — PROVA SOCIAL</div>
<div class="micro-desc">Confiança final</div>
</div>

<ul>
<li>UGC</li>
<li>Depoimentos</li>
<li>Pessoas comuns</li>
</ul>

<div class="micro bofu">
<div class="micro-title">🔴 BOFU — NARRATIVA LONGA</div>
<div class="micro-desc">Remove último freio emocional</div>
</div>

<ul>
<li>História longa</li>
<li>Testemunho</li>
<li>Garantia</li>
</ul>

<b>CTA:</b> <span class="highlight">Comprar agora</span>

<hr>

<b>Métricas:</b> CPA · ROAS · Conversão
</div>
""", unsafe_allow_html=True)

# ======================================================
# RESUMO FINAL
# ======================================================
st.markdown("""
<div class="card">
<div class="title">🔥 Resumo Final</div>

<ul>
<li><b>TOFU:</b> Isso existe?</li>
<li><b>MOFU:</b> Isso faz sentido?</li>
<li><b>BOFU:</b> Posso confiar?</li>
</ul>

<p class="highlight">
Quando o anúncio respeita a mente, a escala vira consequência.
</p>
</div>
""", unsafe_allow_html=True)
