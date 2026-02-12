import streamlit as st

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(
    page_title="Manual Mental de Funil de Vendas",
    layout="wide",
)

# ======================================================
# ESTILO VISUAL (CSS)
# ======================================================
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
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.6rem;
}

.muted {
    color: #9ca3af;
    font-size: 0.95rem;
}

.highlight {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    padding: 0.15rem 0.45rem;
    border-radius: 6px;
    font-weight: 600;
}

hr {
    border: none;
    border-top: 1px solid #1f2933;
    margin: 1rem 0;
}

ul {
    margin-left: 1.2rem;
}

li {
    margin-bottom: 0.4rem;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# TÍTULO PRINCIPAL
# ======================================================
st.title("🧠 Manual Mental de Funil de Vendas")
st.caption("Tráfego de escala não replica anúncios. Replica a mente do comprador.")

# ======================================================
# PRINCÍPIO CENTRAL
# ======================================================
st.markdown("""
<div class="card">
  <div class="title">🧠 Princípio Central</div>

  <p>
    O fluxo de escala só funciona quando replica o
    <span class="highlight">processo mental real do público</span>.
  </p>

  <p class="muted">
    Escala não é aumentar orçamento, duplicar conjuntos ou abrir públicos aleatórios.<br>
    Escala é ampliar algo que já está coerente com a mente do comprador.
  </p>

  <hr>

  <b>Timing mental correto:</b>
  <ul>
    <li>TOFU — leve e escalável</li>
    <li>MOFU — lógico e educativo</li>
    <li>BOFU — forte, sem contaminar o funil</li>
  </ul>

  <p><b>👉 Isso é tráfego de escala, não de tentativa.</b></p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# ERRO MAIS COMUM
# ======================================================
st.markdown("""
<div class="card">
  <div class="title">🚨 O erro mais comum na “escala”</div>

  <p>Tentar escalar BOFU direto para público frio:</p>

  <ul>
    <li>Público aberto</li>
    <li>Criativo de oferta</li>
    <li>“Compre agora”</li>
    <li>Aumenta orçamento</li>
    <li>ROAS cai • CPM sobe • Algoritmo perde sinal</li>
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
  <div class="title">🧩 Régua de Consciência</div>

  <ul>
    <li>❓ O criativo pede decisão ou curiosidade?</li>
    <li>🧠 Ele explica o “por quê” ou apenas mostra que existe?</li>
    <li>⚠️ Ele aumenta ou reduz risco mental?</li>
    <li>⏱️ Quanto esforço cognitivo exige?</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# ======================================================
# TOFU
# ======================================================
with st.expander("🔹 ETAPA 1 — TOFU (Primeiro Contato)"):
    st.markdown("""
    <div class="card">
      <b>Estágio mental:</b><br>
      “Isso existe… talvez seja pra mim.”

      <hr>

      <b>Objetivo real:</b><br>
      Criar identificação com a rotina diária, enquanto o produto aparece
      de forma breve, natural e sem exigir decisão.

      <hr>

      <b>Formato ideal:</b>
      <ul>
        <li>Vídeos curtos — até 20s</li>
        <li>Situação cotidiana real</li>
        <li>Dor silenciosa (sem exagero)</li>
        <li>Produto como parte da rotina</li>
        <li>Micro curiosidade</li>
        <li>CTA leve</li>
      </ul>

      <p class="highlight">CTA recomendado: “Saiba mais”</p>

      <p class="muted">
        Métricas-chave: ThruPlay • 50% de vídeo • CPM saudável
      </p>

      <p><b>Frase do manual:</b><br>
      “No TOFU, o produto aparece como parte da rotina, não como argumento de venda.”
      </p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# MOFU
# ======================================================
with st.expander("🟡 ETAPA 2 — MOFU (Educação + Justificação)"):
    st.markdown("""
    <div class="card">
      <b>Estágio mental:</b><br>
      “Ok… isso pode funcionar. Mas será que funciona pra mim?”

      <hr>

      <b>Objetivo real:</b><br>
      Justificar racionalmente a solução, reduzindo risco mental
      sem pedir compra.

      <hr>

      <b>Formato ideal:</b>
      <ul>
        <li>Vídeos de 30 a 60s</li>
        <li>Explicação do mecanismo</li>
        <li>Comparação implícita</li>
        <li>Micro prova</li>
        <li>CTA de aprofundamento</li>
      </ul>

      <p class="highlight">
        CTA recomendado: “Entenda como funciona”
      </p>

      <p class="muted">
        Métricas-chave: 50–75% de vídeo • CTR • Tempo médio
      </p>

      <p><b>Frase do manual:</b><br>
      “MOFU existe para explicar o que o público já começou a suspeitar.”
      </p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# BOFU
# ======================================================
with st.expander("🔴 ETAPA 3 — BOFU (Decisão + Conversão)"):
    st.markdown("""
    <div class="card">
      <b>Estágio mental:</b><br>
      “Eu já entendi. Agora só não quero errar.”

      <hr>

      <b>Objetivo real:</b><br>
      Facilitar a decisão reduzindo medo, risco percebido
      e insegurança pós-compra.

      <hr>

      <b>Formato ideal:</b>
      <ul>
        <li>Vídeos de 15 a 40s</li>
        <li>Prova real e social</li>
        <li>Validação técnica</li>
        <li>Oferta clara</li>
        <li>CTA direto</li>
      </ul>

      <p class="highlight">
        CTA recomendado: “Comprar agora”
      </p>

      <p class="muted">
        Métricas-chave: CPA • ROAS • Taxa de conversão
      </p>

      <p><b>Frase do manual:</b><br>
      “BOFU não empurra a venda. Ele dá segurança para decidir.”
      </p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# RESUMO FINAL
# ======================================================
st.markdown("""
<div class="card">
  <div class="title">🔥 Resumo Final — Mente do Público</div>

  <ul>
    <li><b>TOFU:</b> “Isso existe?”</li>
    <li><b>MOFU:</b> “Isso faz sentido?”</li>
    <li><b>BOFU:</b> “Posso confiar?”</li>
  </ul>

  <p class="highlight">
    Quando seus anúncios seguem esse raciocínio, a escala deixa de ser tentativa
    e vira consequência.
  </p>
</div>
""", unsafe_allow_html=True)
