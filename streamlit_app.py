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
    padding: 1.25rem 1.3rem;
    margin-bottom: 1rem;
}

.title {
    font-size: 1.2rem;
    font-weight: 800;
    margin-bottom: 0.6rem;
}

.badge {
    display:inline-block;
    padding: 0.2rem 0.55rem;
    border-radius: 999px;
    border: 1px solid #1f2933;
    font-size: 0.82rem;
    color:#cbd5e1;
    margin-right: 0.4rem;
}

.muted { color: #9ca3af; font-size: 0.92rem; line-height: 1.35; }

.highlight {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    padding: 0.2rem 0.5rem;
    border-radius: 8px;
    font-weight: 700;
    display: inline-block;
}

hr {
    border: none;
    border-top: 1px solid #1f2933;
    margin: 0.85rem 0;
}

ul { margin-left: 1.2rem; }
li { margin-bottom: 0.28rem; }

.grid2 {
    display:grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.9rem;
}

.grid3 {
    display:grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0.9rem;
}

.kpi {
    background:#0b1220;
    border: 1px solid #1f2933;
    border-radius: 12px;
    padding: 0.85rem 1rem;
}

.kpi h4 { margin:0 0 0.25rem 0; font-size: 0.95rem; }
.kpi p { margin:0; color:#9ca3af; font-size:0.88rem; }

.tofu { border-left: 4px solid #3b82f6; }
.mofu { border-left: 4px solid #f59e0b; }
.bofu { border-left: 4px solid #ef4444; }

/* ============================
   FUNÇÃO COGNITIVA POR ETAPA
   ============================ */

/* TOFU — azul claro e limpo */
.card.tofu {
    border-left: 4px solid #3b82f6;
    background: linear-gradient(
        180deg,
        rgba(59,130,246,0.08),
        #0e1117 40%
    );
}

/* MOFU — amarelo sóbrio */
.card.mofu {
    border-left: 4px solid #f59e0b;
    background: linear-gradient(
        180deg,
        rgba(245,158,11,0.08),
        #0e1117 40%
    );
}

/* BOFU — vermelho discreto */
.card.bofu {
    border-left: 4px solid #ef4444;
    background: linear-gradient(
        180deg,
        rgba(239,68,68,0.08),
        #0e1117 40%
    );
}

.small { font-size: 0.9rem; }
</style>
""", unsafe_allow_html=True)

# ======================================================
# DADOS (CRIATIVOS)
# ======================================================
CREATIVES = {
    "TOFU PURO — DESCOBERTA": [
        ("07", "Apresentação simples do produto"),
        ("17", "Uso durante atividade"),
        ("24", "Rotina ativa"),
        ("25", "Lista objetiva de benefícios"),
        ("26", "Mensagens de impacto curtas"),
    ],
    "TOFU HÍBRIDO — DESCOBERTA + PROVA": [
        ("10", "Primeira experiência emocional"),
        ("11", "Alívio rápido (nota 8 → 2)"),
        ("12", "Antes/depois simples"),
        ("18", "Público 45+ (sem medo, sem oferta)"),
        ("29", "Rotina simples (10 segundos)"),
    ],
    "MOFU PURO — EDUCAÇÃO": [
        ("02", "Anti-inflamatório vs natural"),
        ("03", "Pesquisa + mecanismo + ingredientes"),
        ("04", "Dor crônica + terapia (sem desconto)"),
        ("16", "Comparação com joelheira"),
        ("22", "Profissional em pé o dia todo"),
        ("28", "Passo a passo (sem pressão)"),
    ],
    "MOFU — VALIDAÇÃO": [
        ("05", "Evolução em dias (sem urgência)"),
        ("06", "Antes/depois + segredo"),
        ("08", "Dor severa + alternativa à cirurgia"),
        ("15", "Caso real + validação profissional"),
        ("19", "Osso com osso + indicação técnica"),
        ("21", "Medicamentos vs adesivo"),
    ],
    "BOFU — DECISÃO": [
        ("13", "Benefícios claros + oferta"),
        ("20", "Oferta direta + urgência"),
        ("23", "Rotina 2 passos + desconto"),
        ("27", "Prova familiar + desconto"),
    ],
    "BOFU — DECISÃO | NARRATIVA LONGA": [
        ("01", "História longa + médico + cirurgia"),
        ("09", "Dor extrema + testemunho + garantia"),
    ],
    "BOFU — PROVA SOCIAL": [
        ("UGC", "Cliente (Diego)"),
        ("UGC", "Cliente (Idosa)"),
    ],
}

# ======================================================
# SIDEBAR — NAVEGAÇÃO
# ======================================================
st.sidebar.title("🧠 Manual (rápido)")
section = st.sidebar.radio(
    "Escolha:",
    [
        "⚡ Visão Rápida",
        "📘 Fundamentos",
        "🔵 TOFU",
        "🟡 MOFU",
        "🔴 BOFU",
        "🎥 Criativos (31)",
        "🩺 Diagnóstico",
    ]
)

# ======================================================
# HEADER
# ======================================================
st.title("🧠 Funil Mental de Vendas")
st.caption("Sem teoria desnecessária. Aprenda rápido e execute certo.")

# ======================================================
# COMPONENTE: CARD PADRÃO (DIDÁTICO)
# ======================================================
def card_stage(
    stage_name: str,
    stage_class: str,
    o_que_e: str,
    funcao_mental: str,
    objetivo_real: str,
    formato: str,
    estrutura: list,
    cta: str,
    tipos: list,
    metricas: list,
    papel: list,
    erros: list,
    frase: str,
):
    st.markdown(f"""
<div class="card {stage_class}">
<div class="title">{stage_name}</div>

<span class="badge">O que é</span>
<div class="small">{o_que_e}</div>

<hr>

<span class="badge">Função mental</span>
<div class="small"><b>{funcao_mental}</b></div>

<hr>

<span class="badge">Objetivo real</span>
<div class="small">{objetivo_real}</div>

<hr>

<span class="badge">Formato ideal</span>
<div class="small">{formato}</div>

<hr>

<span class="badge">Estrutura mental</span>
<ul>
{''.join([f"<li>{x}</li>" for x in estrutura])}
</ul>

<hr>

<span class="badge">CTA</span>
<div class="small"><b>{cta}</b></div>

<hr>

<div class="grid2">
  <div class="kpi">
    <h4>🎬 Tipos de criativo</h4>
    <ul>
      {''.join([f"<li>{x}</li>" for x in tipos])}
    </ul>
  </div>
  <div class="kpi">
    <h4>📊 Métricas-chave</h4>
    <ul>
      {''.join([f"<li>{x}</li>" for x in metricas])}
    </ul>
  </div>
</div>

<hr>

<div class="grid2">
  <div class="kpi">
    <h4>🧩 Papel na escala</h4>
    <ul>
      {''.join([f"<li>{x}</li>" for x in papel])}
    </ul>
  </div>
  <div class="kpi">
    <h4>🚫 Erros comuns</h4>
    <ul>
      {''.join([f"<li>{x}</li>" for x in erros])}
    </ul>
  </div>
</div>

<hr>

<span class="highlight">{frase}</span>
</div>
""", unsafe_allow_html=True)

# ======================================================
# ⚡ VISÃO RÁPIDA
# ======================================================
if section == "⚡ Visão Rápida":
    st.markdown("""
<div class="card">
<div class="title">⚡ Como escalar (em 15s)</div>
<ul>
<li><b>TOFU</b> = “Isso existe?”</li>
<li><b>MOFU</b> = “Isso faz sentido?”</li>
<li><b>BOFU</b> = “Posso confiar?”</li>
</ul>
</div>

<div class="card">
<div class="title">Regra de ouro</div>
<span class="highlight">Escala só funciona quando replica o processo mental real do público.</span>
</div>

<div class="card">
<div class="title">Erro mais comum</div>
<ul>
<li>Público aberto</li>
<li>Criativo de oferta</li>
<li>“Compre agora”</li>
<li>Aumenta orçamento → ROAS cai → CPM sobe → algoritmo perde sinal</li>
</ul>
<div class="muted">Isso acontece porque a mente ainda não está pronta.</div>
</div>

<div class="card">
<div class="title">Régua de consciência (classifique qualquer criativo)</div>
<ul>
<li>❓ Pede decisão ou curiosidade?</li>
<li>🧠 Explica “por quê” ou só mostra “que existe”?</li>
<li>⚠️ Aumenta ou reduz risco mental?</li>
<li>⏱️ Exige muito esforço cognitivo?</li>
</ul>
<hr>
<span class="highlight">TOFU desperta · MOFU organiza · BOFU confirma</span>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 📘 FUNDAMENTOS
# ======================================================
elif section == "📘 Fundamentos":
    col1, col2 = st.columns([1.1, 1])

    with col1:
        st.markdown("""
<div class="card">
<div class="title">🧠 Princípio central</div>
<ul>
<li><b>Escala não é:</b> aumentar orçamento, duplicar conjunto, abrir LAL aleatório</li>
<li><b>Escala é:</b> ampliar algo coerente com a mente do comprador</li>
</ul>
<hr>
<div class="title">Timing mental</div>
<ul>
<li>TOFU leve e escalável</li>
<li>MOFU lógico e educativo</li>
<li>BOFU forte, sem contaminar o funil</li>
</ul>
<span class="highlight">Tráfego de escala, não de tentativa.</span>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="card">
<div class="title">📐 Progressão psicológica real</div>
<ul>
<li>Desconhecimento</li>
<li>Identificação do problema</li>
<li>Comparação / ceticismo</li>
<li>Confiança</li>
<li>Decisão</li>
</ul>
<hr>
<span class="highlight">Meta Ads só escala quando os anúncios acompanham essa progressão.</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<div class="title">📏 Checklist binário (protege o funil)</div>
<div class="grid3">
  <div class="kpi tofu">
    <h4>🔵 TOFU — só é TOFU se:</h4>
    <ul>
      <li>Não pede compra</li>
      <li>Não fala de preço/desconto</li>
      <li>Produto aparece breve</li>
      <li>Dor aparece mais que solução</li>
      <li>CTA: “Saiba mais”</li>
    </ul>
    <p class="muted">Falhou em 1 item → não é TOFU.</p>
  </div>
  <div class="kpi mofu">
    <h4>🟡 MOFU — só é MOFU se:</h4>
    <ul>
      <li>Explica por que funciona</li>
      <li>Introduz mecanismo/lógica</li>
      <li>Reduz objeções silenciosas</li>
      <li>Não cria urgência</li>
      <li>CTA não é compra</li>
    </ul>
    <p class="muted">Se começa a vender → virou BOFU.</p>
  </div>
  <div class="kpi bofu">
    <h4>🔴 BOFU — só é BOFU se:</h4>
    <ul>
      <li>Assume que o usuário já entende</li>
      <li>Usa prova real</li>
      <li>Remove risco percebido</li>
      <li>CTA de ação</li>
    </ul>
    <p class="muted">Se precisa explicar demais → MOFU falhou.</p>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<div class="title">👁️ PageView (uso certo)</div>
<ul>
<li><b>Não é</b> intenção de compra</li>
<li><b>É</b> curiosidade estruturada</li>
<li><b>Uso correto:</b> PageView + vídeo/engajamento</li>
</ul>
<span class="highlight">PageView prepara. BOFU confirma.</span>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 🔵 TOFU
# ======================================================
elif section == "🔵 TOFU":

    # ---------- RESUMO FIXO (sempre visível) ----------
    st.markdown("""
<div class="card tofu">
<div class="title">🔵 TOFU — Primeiro Contato</div>

<b>Âncora mental:</b><br>
“Isso existe… e talvez seja pra mim.”

<hr>

<b>Objetivo:</b><br>
Gerar curiosidade sem exigir decisão.

<hr>

<b>CTA:</b> Saiba mais<br>
<b>Métricas:</b> ThruPlay · 50% vídeo · CPM

<hr>

<span class="highlight">
Produto aparece como parte da rotina, não como argumento de venda.
</span>
</div>
""", unsafe_allow_html=True)

    # ---------- ABAS INTERNAS ----------
    tab1, tab2, tab3, tab4 = st.tabs([
        "🧠 Essência",
        "🧱 Estrutura",
        "🎬 Criativos",
        "🚫 Erros & Papel"
    ])

    # ---------- ESSÊNCIA ----------
    with tab1:
        st.markdown("""
<div class="card">
<b>O que é:</b><br>
Apresentar o produto sem exigir decisão.<br>
<b>Não</b> é esconder o produto.

<hr>

<b>Estágio mental:</b><br>
Usuário ainda não quer comprar, mas já consegue:
<ul>
<li>Se enxergar no cenário</li>
<li>Reconhecer a dor</li>
<li>Aceitar que a solução existe</li>
</ul>
</div>
""", unsafe_allow_html=True)

    # ---------- ESTRUTURA ----------
    with tab2:
        st.markdown("""
<div class="card">
<b>Formato ideal:</b><br>
Vídeos curtos (até 20s)

<hr>

<b>Estrutura mental correta:</b>
<ol>
<li>Situação cotidiana real</li>
<li>Dor silenciosa (sem exagero)</li>
<li>Produto aparece como parte da rotina</li>
<li>Micro curiosidade</li>
<li>CTA leve</li>
</ol>

<hr>

<span class="highlight">
Meta: atenção qualificada (não venda).
</span>
</div>
""", unsafe_allow_html=True)

    # ---------- CRIATIVOS ----------
    with tab3:
        st.markdown("""
<div class="card">
<b>Tipos de criativo TOFU:</b>
<ul>
<li>Uso rápido no dia a dia</li>
<li>Close sutil do produto (sem explicar tudo)</li>
<li>Rotina real (trabalho, treino, deslocamento)</li>
<li>“Eu comecei a usar por causa disso…”</li>
<li>Situações onde o produto resolve sem ser protagonista</li>
</ul>
</div>
""", unsafe_allow_html=True)

    # ---------- ERROS & PAPEL ----------
    with tab4:
        st.markdown("""
<div class="card">
<b>Erros comuns:</b>
<ul>
<li>Mostrar demais (gera rejeição)</li>
<li>Esconder totalmente (perde qualificação)</li>
<li>Puxar oferta ou desconto cedo</li>
</ul>

<hr>

<b>Papel do TOFU na escala:</b>
<ul>
<li>Gera públicos quentes</li>
<li>Cria curiosos compradores</li>
<li>Planta dúvida nos céticos</li>
<li>Alimenta MOFU e BOFU</li>
<li>Mantém CPM baixo em escala</li>
</ul>
</div>
""", unsafe_allow_html=True)


# ======================================================
# 🟡 MOFU
# ======================================================
elif section == "🟡 MOFU":

    # ---------- RESUMO FIXO (sempre visível) ----------
    st.markdown("""
<div class="card mofu">
<div class="title">🟡 MOFU — Educação & Justificação</div>

<b>Âncora mental:</b><br>
“Ok… isso pode funcionar. Mas será que funciona pra mim?”

<hr>

<b>Objetivo:</b><br>
Organizar o raciocínio e reduzir ceticismo.

<hr>

<b>CTA:</b> Entenda como funciona<br>
<b>Métricas:</b> 50–75% vídeo · CTR · Tempo médio

<hr>

<span class="highlight">
MOFU não vende. MOFU faz sentido.
</span>
</div>
""", unsafe_allow_html=True)

    # ---------- ABAS INTERNAS ----------
    tab1, tab2, tab3, tab4 = st.tabs([
        "🧠 Essência",
        "🧱 Estrutura",
        "🎬 Criativos",
        "🚫 Erros & Papel"
    ])

    # ---------- ESSÊNCIA ----------
    with tab1:
        st.markdown("""
<div class="card">
<b>O que é:</b><br>
MOFU organiza o pensamento de quem já ficou curioso no TOFU.

<hr>

<b>Estágio mental:</b><br>
Aqui surgem:
<ul>
<li>Ceticismo</li>
<li>Comparação</li>
<li>Busca por lógica</li>
<li>Medo de errar na escolha</li>
</ul>

<hr>

<b>Papel central:</b><br>
Reduzir risco mental, não convencer.
</div>
""", unsafe_allow_html=True)

    # ---------- ESTRUTURA ----------
    with tab2:
        st.markdown("""
<div class="card">
<b>Formato ideal:</b><br>
Vídeos de 30 a 60 segundos

<hr>

<b>Estrutura mental correta:</b>
<ol>
<li>Reforço da dor já reconhecida</li>
<li>Introdução do mecanismo (o “por quê”)</li>
<li>Comparação implícita</li>
<li>Micro prova</li>
<li>CTA de aprofundamento</li>
</ol>

<hr>

<span class="highlight">
Meta: compreensão (não conversão).
</span>
</div>
""", unsafe_allow_html=True)

    # ---------- CRIATIVOS ----------
    with tab3:
        st.markdown("""
<div class="card">
<b>Tipos de criativo MOFU:</b>

<ul>
<li><b>Educacional (base):</b> dores, erros comuns, conceitos</li>
<li><b>Mecanismo:</b> o que acontece no corpo / no uso</li>
<li><b>Comparação:</b> tradicional × correto · errado × certo · genérico × técnico</li>
<li><b>Demonstração parcial:</b> close técnico + detalhe funcional + movimento real</li>
</ul>

<p class="muted">
📌 Mostre que existe engenharia.<br>
Não entregue o produto inteiro.
</p>
</div>
""", unsafe_allow_html=True)

    # ---------- ERROS & PAPEL ----------
    with tab4:
        st.markdown("""
<div class="card">
<b>Erros comuns:</b>
<ul>
<li>Virar oferta ou urgência</li>
<li>Explicar demais e cansar</li>
<li>Prometer em vez de justificar</li>
</ul>

<hr>

<b>Papel do MOFU na escala:</b>
<ul>
<li>Transforma curiosos em interessados</li>
<li>Filtra compradores reais</li>
<li>Prepara BOFU para converter barato</li>
<li>Reduz objeções no checkout</li>
<li>Aumenta LTV</li>
</ul>

<p class="muted">
Se o MOFU estiver fraco, o BOFU fica caro.
</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 🔴 BOFU
# ======================================================
elif section == "🔴 BOFU":

    # ---------- RESUMO FIXO (sempre visível) ----------
    st.markdown("""
<div class="card bofu">
<div class="title">🔴 BOFU — Decisão & Conversão</div>

<b>Âncora mental:</b><br>
“Eu já entendi. Agora só não quero errar.”

<hr>

<b>Objetivo:</b><br>
Dar segurança e facilitar a decisão.

<hr>

<b>CTA:</b> Comprar agora / Garantir o seu<br>
<b>Métricas:</b> CPA · ROAS · Taxa de conversão

<hr>

<span class="highlight">
BOFU não convence. Ele confirma.
</span>
</div>
""", unsafe_allow_html=True)

    # ---------- ABAS INTERNAS ----------
    tab1, tab2, tab3, tab4 = st.tabs([
        "🧠 Essência",
        "🧱 Estrutura",
        "🎬 Criativos",
        "🚫 Erros & Papel"
    ])

    # ---------- ESSÊNCIA ----------
    with tab1:
        st.markdown("""
<div class="card">
<b>O que é:</b><br>
BOFU não é persuasão.<br>
BOFU remove o último freio mental.

<hr>

<b>Estágio mental:</b><br>
Neste ponto, o usuário:
<ul>
<li>Já aceita o problema</li>
<li>Já acredita na solução</li>
<li>Já entende o mecanismo</li>
<li>Tem medo apenas da escolha</li>
</ul>

<hr>

<b>Papel central:</b><br>
Reduzir risco percebido — não explicar.
</div>
""", unsafe_allow_html=True)

    # ---------- ESTRUTURA ----------
    with tab2:
        st.markdown("""
<div class="card">
<b>Formato ideal:</b><br>
Vídeos de 15 a 40 segundos (curto e direto)

<hr>

<b>Estrutura mental correta:</b>
<ol>
<li>Confirmação do problema</li>
<li>Prova real (pessoas, uso, resultado)</li>
<li>Validação social ou técnica</li>
<li>Oferta clara</li>
<li>CTA de ação</li>
</ol>

<hr>

<span class="highlight">
Meta: eficiência (não volume).
</span>
</div>
""", unsafe_allow_html=True)

    # ---------- CRIATIVOS ----------
    with tab3:
        st.markdown("""
<div class="card">
<b>Tipos de criativo BOFU:</b>

<ul>
<li><b>Prova social:</b> depoimentos, UGC, prints (quando permitido)</li>
<li><b>Antes / Depois:</b> funcional, não estético<br>
<small>Movimento × limitação · segurança × instabilidade</small></li>
<li><b>Confiança & autoridade:</b> material, engenharia, diferenciais, bastidores</li>
<li><b>Oferta estruturada:</b> benefício principal, o que inclui, para quem é / não é</li>
<li><b>Escassez legítima:</b> lote, prazo real, bônus por tempo, demanda limitada</li>
</ul>

<p class="muted">
📌 Escassez falsa destrói BOFU.
</p>
</div>
""", unsafe_allow_html=True)

    # ---------- ERROS & PAPEL ----------
    with tab4:
        st.markdown("""
<div class="card">
<b>Erros comuns:</b>
<ul>
<li>Educar no BOFU (tarde demais)</li>
<li>Explicar mecanismo (MOFU falhou)</li>
<li>Escassez falsa ou forçada</li>
</ul>

<hr>

<b>Papel do BOFU na escala:</b>
<ul>
<li>Converte público já preparado</li>
<li>Protege margem</li>
<li>Estabiliza ROAS</li>
<li>Valida o funil inteiro</li>
</ul>

<p class="muted">
Se o BOFU estiver caro, o problema está antes.
</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# 🎥 CRIATIVOS (31)
# ======================================================
elif section == "🎥 Criativos (31)":
    st.markdown("""
<div class="card">
<div class="title">🎥 Biblioteca de criativos por função mental</div>
<div class="muted">
Aqui você não organiza por “número do vídeo”. Organiza por <b>efeito mental</b>.
</div>
</div>
""", unsafe_allow_html=True)

    stage_filter = st.selectbox(
        "Filtrar por etapa:",
        ["Todos", "TOFU", "MOFU", "BOFU"]
    )

    def show_group(title, items, note):
        st.markdown(f"""
<div class="card">
<div class="title">{title}</div>
<div class="muted">{note}</div>
<hr>
<ul>
{''.join([f"<li><b>{code}</b> — {desc}</li>" for code, desc in items])}
</ul>
</div>
""", unsafe_allow_html=True)

    if stage_filter in ["Todos", "TOFU"]:
        show_group(
            "🔵 TOFU PURO — DESCOBERTA",
            CREATIVES["TOFU PURO — DESCOBERTA"],
            "Função mental: apresentar o produto sem exigir decisão · Uso: escalar orçamento"
        )
        show_group(
            "🔁 TOFU HÍBRIDO — DESCOBERTA + PROVA",
            CREATIVES["TOFU HÍBRIDO — DESCOBERTA + PROVA"],
            "Função mental: descoberta qualificada + quebra leve de objeção · Uso: públicos de vídeo / segmentação 45+"
        )

    if stage_filter in ["Todos", "MOFU"]:
        show_group(
            "🟡 MOFU PURO — EDUCAÇÃO",
            CREATIVES["MOFU PURO — EDUCAÇÃO"],
            "Função mental: “ok, agora faz sentido” · Uso: escalar compreensão (não conversão)"
        )
        show_group(
            "🟠 MOFU — VALIDAÇÃO",
            CREATIVES["MOFU — VALIDAÇÃO"],
            "Função mental: “funciona para pessoas como eu” · Uso: remarketing + públicos quentes"
        )

    if stage_filter in ["Todos", "BOFU"]:
        show_group(
            "🔴 BOFU — DECISÃO",
            CREATIVES["BOFU — DECISÃO"],
            "Função mental: facilitar a decisão agora · Uso: conversão direta"
        )
        show_group(
            "🔴 BOFU — NARRATIVA LONGA",
            CREATIVES["BOFU — DECISÃO | NARRATIVA LONGA"],
            "Função mental: remover último freio emocional · Uso: RMK profundo (frequência baixa)"
        )
        show_group(
            "🧠 BOFU — PROVA SOCIAL",
            CREATIVES["BOFU — PROVA SOCIAL"],
            "Função mental: “outras pessoas como eu confiam” · Uso: fechamento e proteção de ROAS"
        )

# ======================================================
# 🩺 DIAGNÓSTICO
# ======================================================
elif section == "🩺 Diagnóstico":
    st.markdown("""
<div class="card">
<div class="title">🩺 Diagnóstico (rápido e útil)</div>
<div class="muted">Marque o sintoma. O app aponta o lugar provável do erro.</div>
</div>
""", unsafe_allow_html=True)

    colA, colB = st.columns(2)

    with colA:
        st.markdown("### Sintomas")
        s1 = st.checkbox("CPM subindo / alcance caro (mesmo sem mexer)")
        s2 = st.checkbox("ThruPlay / 50% vídeo fraco no frio")
        s3 = st.checkbox("CTR ok, mas a pessoa não evolui no funil")
        s4 = st.checkbox("BOFU caro (CPA alto) e você sente que precisa explicar muito")

    with colB:
        st.markdown("### Leitura provável")
        if s1 or s2:
            st.error("🔵 Provável TOFU errado: você está pedindo esforço cedo ou mostrando demais/menos.")
        if s3:
            st.warning("🟡 Provável MOFU fraco: falta lógica/mecanismo/justificativa.")
        if s4:
            st.error("🔴 BOFU está pagando a conta do que faltou antes (preparação mental).")
        if not (s1 or s2 or s3 or s4):
            st.success("✅ Sem sintomas marcados. Use a régua de consciência para auditar criativos.")

    st.markdown("""
<div class="card">
<div class="title">🪓 Critérios de corte por etapa (simples)</div>

<b>🔵 TOFU — cortar se:</b>
<ul>
<li>CPM sobe continuamente</li>
<li>ThruPlay / 50% vídeo abaixo da média do conjunto</li>
</ul>

<hr>

<b>🟡 MOFU — cortar se:</b>
<ul>
<li>50%–75% de vídeo baixo</li>
<li>Tempo médio fraco</li>
<li>CTR não melhora com frequência baixa</li>
</ul>

<hr>

<b>🔴 BOFU — cortar se:</b>
<ul>
<li>CPA acima do limite por vários dias</li>
<li>ROAS instável com frequência alta</li>
<li>Conversões concentradas em poucos dias</li>
</ul>

<hr>
<span class="highlight">Criativo ruim drena o funil inteiro.</span>
</div>
""", unsafe_allow_html=True)
