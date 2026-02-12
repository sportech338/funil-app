import streamlit as st
from dataclasses import dataclass
from typing import Dict, List, Tuple

st.set_page_config(page_title="Manual Mental de Funil", layout="wide")

# -----------------------------
# UTILIDADES
# -----------------------------
def clamp(n: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, n))

def pct(n: int, d: int) -> int:
    if d <= 0:
        return 0
    return int(round((n / d) * 100))

def score_to_label(score: int) -> str:
    if score >= 80:
        return "Excelente"
    if score >= 60:
        return "Bom"
    if score >= 40:
        return "Atenção"
    return "Crítico"

def stage_from_inputs(pede_decisao: bool, explica: bool, reduz_risco: bool, esforco: int, cta: str) -> str:
    # Heurística simples e prática
    if cta in ("Comprar agora", "Garantir o seu") or pede_decisao:
        return "BOFU"
    if explica or reduz_risco or esforco >= 3 or cta in ("Entenda como funciona", "Veja por que funciona"):
        return "MOFU"
    return "TOFU"

def contamination_risk(pede_decisao: bool, esforco: int, cta: str) -> int:
    risk = 0
    if pede_decisao:
        risk += 45
    if cta in ("Comprar agora", "Garantir o seu"):
        risk += 35
    if esforco >= 4:
        risk += 20
    return clamp(risk, 0, 100)

def mental_coherence_score(target_stage: str, predicted_stage: str, risk: int) -> int:
    score = 100
    if target_stage != predicted_stage:
        score -= 35
    score -= int(risk * 0.35)
    return clamp(score, 0, 100)

def recommendation(target_stage: str, predicted_stage: str, risk: int) -> Tuple[str, str]:
    if target_stage == predicted_stage and risk <= 35:
        return ("Escalar", "Coerência mental alta e risco baixo. Dá para ampliar com segurança.")
    if target_stage == "TOFU" and (predicted_stage in ("MOFU", "BOFU") or risk > 35):
        return ("Consertar antes de escalar", "Você está exigindo demais cedo. Alivie o esforço mental e suavize CTA.")
    if target_stage == "MOFU" and predicted_stage == "BOFU":
        return ("Ajustar", "Está pedindo decisão cedo. Troque CTA para aprofundamento e aumente lógica/mecanismo.")
    if target_stage == "BOFU" and predicted_stage in ("TOFU", "MOFU"):
        return ("Ajustar", "Está fraco para decisão. Falta prova, segurança e CTA de ação.")
    return ("Ajustar", "Há desalinhamento mental. Refaça o criativo para casar com o timing do público.")

@dataclass
class Creative:
    name: str
    target_stage: str
    cta: str
    pede_decisao: bool
    explica_porque: bool
    reduz_risco: bool
    esforco: int
    obs: str = ""

def ensure_state():
    if "mode" not in st.session_state:
        st.session_state.mode = "Guia"
    if "wizard_step" not in st.session_state:
        st.session_state.wizard_step = 0
    if "creatives" not in st.session_state:
        st.session_state.creatives: List[Creative] = []
    if "template" not in st.session_state:
        st.session_state.template = "TOFU"
    if "last_result" not in st.session_state:
        st.session_state.last_result = {}

ensure_state()

# -----------------------------
# HEADER
# -----------------------------
st.title("🧠 Manual Mental de Funil")
st.caption("Escala é coerência com a mente do comprador. O app te guia para decidir o que escalar, o que ajustar e o que evitar.")

# -----------------------------
# CONTROLES GERAIS
# -----------------------------
colA, colB, colC = st.columns([1.2, 1, 1])
with colA:
    st.session_state.mode = st.radio(
        "Modo",
        ["Guia", "Classificar Criativo", "Biblioteca", "Diagnóstico"],
        horizontal=True,
        index=["Guia", "Classificar Criativo", "Biblioteca", "Diagnóstico"].index(st.session_state.mode),
    )
with colB:
    st.session_state.template = st.selectbox(
        "Preset mental",
        ["TOFU", "MOFU", "BOFU"],
        index=["TOFU", "MOFU", "BOFU"].index(st.session_state.template),
    )
with colC:
    st.markdown("")

# -----------------------------
# PRESETS
# -----------------------------
PRESETS: Dict[str, Dict] = {
    "TOFU": {
        "cta": "Saiba mais",
        "pede_decisao": False,
        "explica": False,
        "reduz_risco": False,
        "esforco": 2,
        "hint": "Leve, rotina, curiosidade. Produto aparece sem argumentar."
    },
    "MOFU": {
        "cta": "Entenda como funciona",
        "pede_decisao": False,
        "explica": True,
        "reduz_risco": True,
        "esforco": 3,
        "hint": "Lógico, educativo, mecanismo, comparação implícita, micro prova."
    },
    "BOFU": {
        "cta": "Comprar agora",
        "pede_decisao": True,
        "explica": False,
        "reduz_risco": True,
        "esforco": 3,
        "hint": "Confirmação, prova, segurança, oferta clara. Sem explicar demais."
    },
}

# -----------------------------
# GUIA (WIZARD)
# -----------------------------
def page_guide():
    st.subheader("Guia mental")
    st.write("O app faz 3 perguntas e te dá uma decisão prática.")

    steps = ["Princípio", "Timing mental", "Regra de ouro", "Pronto"]
    st.progress(pct(st.session_state.wizard_step, len(steps) - 1))

    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        back = st.button("⬅️ Voltar", use_container_width=True, disabled=st.session_state.wizard_step == 0)
    with c2:
        next_ = st.button("Avançar ➡️", use_container_width=True, disabled=st.session_state.wizard_step == len(steps) - 1)
    with c3:
        reset = st.button("Reiniciar", use_container_width=True)

    if back:
        st.session_state.wizard_step = clamp(st.session_state.wizard_step - 1, 0, len(steps) - 1)
    if next_:
        st.session_state.wizard_step = clamp(st.session_state.wizard_step + 1, 0, len(steps) - 1)
    if reset:
        st.session_state.wizard_step = 0

    step = st.session_state.wizard_step

    st.divider()

    if step == 0:
        st.markdown("### Princípio central")
        st.info("Escala acontece quando você amplia algo que já está coerente com a mente do comprador.")
        st.markdown("### O que escala não é")
        st.warning("Aumentar orçamento, duplicar conjunto e abrir público aleatório não conserta falta de coerência mental.")
        st.markdown("### O que escala é")
        st.success("Ampliar um sistema de criativos que respeita o timing mental: TOFU desperta, MOFU organiza, BOFU confirma.")

    elif step == 1:
        st.markdown("### Timing mental real")
        st.info("A mente passa por estágios: desconhecimento → identificação → ceticismo → confiança → decisão.")
        st.markdown("### Tradução para tráfego")
        st.success("TOFU leve e escalável, MOFU lógico e educativo, BOFU forte sem contaminar o funil.")
        st.markdown("### Regra prática")
        st.warning("Se seu BOFU precisa explicar demais, o problema está no MOFU. Se seu ROAS cai ao escalar, o problema pode estar no TOFU.")

    elif step == 2:
        st.markdown("### Regra de ouro")
        st.info("O criativo deve exigir apenas o que a mente do público já está pronta para dar.")
        st.markdown("### Perguntas que mandam")
        st.success("O app vai usar essas perguntas para classificar criativos e prever risco de contaminação.")
        q1, q2 = st.columns(2)
        with q1:
            st.markdown("### Pergunta 1")
            st.write("Esse criativo pede decisão ou curiosidade?")
        with q2:
            st.markdown("### Pergunta 2")
            st.write("Ele reduz risco mental ou aumenta exigência?")
        st.markdown("### Pergunta 3")
        st.write("O CTA está alinhado com o estágio mental?")

    else:
        st.markdown("### Pronto")
        st.success("Agora vá em Classificar Criativo e use o preset TOFU/MOFU/BOFU. Depois salve na Biblioteca e rode o Diagnóstico.")
        st.caption("Se quiser, você pode cadastrar seus 31 criativos e deixar o app organizar tudo automaticamente.")

# -----------------------------
# CLASSIFICAR CRIATIVO
# -----------------------------
def page_classify():
    st.subheader("Classificar criativo")
    preset = PRESETS[st.session_state.template]

    left, right = st.columns([1.1, 1])

    with left:
        st.markdown("### Dados do criativo")
        name = st.text_input("Nome do criativo", value="", placeholder="Ex: 29 — Rotina simples (10s)")
        target_stage = st.radio("Qual a função mental planejada?", ["TOFU", "MOFU", "BOFU"], horizontal=True, index=["TOFU","MOFU","BOFU"].index(st.session_state.template))

        cta = st.selectbox(
            "CTA",
            ["Saiba mais", "Entenda como funciona", "Veja por que funciona", "Comprar agora", "Garantir o seu"],
            index=["Saiba mais","Entenda como funciona","Veja por que funciona","Comprar agora","Garantir o seu"].index(preset["cta"])
            if preset["cta"] in ["Saiba mais","Entenda como funciona","Veja por que funciona","Comprar agora","Garantir o seu"]
            else 0
        )

        pede_decisao = st.toggle("O criativo pede decisão?", value=preset["pede_decisao"])
        explica = st.toggle("Explica o porquê (mecanismo/lógica)?", value=preset["explica"])
        reduz_risco = st.toggle("Reduz risco mental (prova, segurança, validação)?", value=preset["reduz_risco"])
        esforco = st.slider("Esforço cognitivo", 1, 5, value=preset["esforco"])

        obs = st.text_area("Observações", value="", placeholder="Ex: foco em detalhe técnico, close, comparação implícita")

        st.caption(f"Preset {st.session_state.template}: {preset['hint']}")

    with right:
        st.markdown("### Resultado")
        predicted = stage_from_inputs(pede_decisao, explica, reduz_risco, esforco, cta)
        risk = contamination_risk(pede_decisao, esforco, cta)
        score = mental_coherence_score(target_stage, predicted, risk)
        action, why = recommendation(target_stage, predicted, risk)

        k1, k2, k3 = st.columns(3)
        k1.metric("Função planejada", target_stage)
        k2.metric("Função detectada", predicted)
        k3.metric("Risco de contaminação", f"{risk}%")

        st.progress(score / 100)
        st.write(f"Coerência mental: {score}/100 ({score_to_label(score)})")

        if action == "Escalar":
            st.success(f"Decisão: {action}")
        elif action == "Consertar antes de escalar":
            st.error(f"Decisão: {action}")
        else:
            st.warning(f"Decisão: {action}")

        st.write(why)

        st.markdown("### Ajuste rápido")
        if target_stage == "TOFU":
            st.info("Alivie: diminua esforço, troque CTA para Saiba mais, remova pedido de decisão, aumente rotina e curiosidade.")
        elif target_stage == "MOFU":
            st.info("Organize: mecanismo claro, comparação implícita, micro prova, CTA de aprofundamento, sem oferta.")
        else:
            st.info("Confirme: prova social, validação técnica, garantia, oferta clara e CTA de ação. Evite explicar demais.")

        save = st.button("Salvar na Biblioteca", use_container_width=True, disabled=(name.strip() == ""))
        if save:
            st.session_state.creatives.append(
                Creative(
                    name=name.strip(),
                    target_stage=target_stage,
                    cta=cta,
                    pede_decisao=pede_decisao,
                    explica_porque=explica,
                    reduz_risco=reduz_risco,
                    esforco=esforco,
                    obs=obs.strip(),
                )
            )
            st.success("Criativo salvo.")

# -----------------------------
# BIBLIOTECA
# -----------------------------
def page_library():
    st.subheader("Biblioteca de criativos")
    st.caption("Aqui você cadastra, organiza e limpa sua base. O diagnóstico usa esta biblioteca.")

    if len(st.session_state.creatives) == 0:
        st.info("Nenhum criativo cadastrado ainda. Vá em Classificar Criativo e salve alguns.")
        return

    cols = st.columns([1.4, 1, 1, 1, 1])
    with cols[0]:
        search = st.text_input("Buscar", value="", placeholder="Digite parte do nome")
    with cols[1]:
        filt = st.selectbox("Filtrar", ["Todos", "TOFU", "MOFU", "BOFU"])
    with cols[2]:
        sort = st.selectbox("Ordenar", ["Recente", "Nome", "Estágio"])
    with cols[3]:
        if st.button("Limpar tudo", use_container_width=True):
            st.session_state.creatives = []
            st.success("Biblioteca limpa.")
            return
    with cols[4]:
        st.markdown("")

    items = st.session_state.creatives[:]

    if search.strip():
        s = search.strip().lower()
        items = [x for x in items if s in x.name.lower()]

    if filt != "Todos":
        items = [x for x in items if x.target_stage == filt]

    if sort == "Nome":
        items.sort(key=lambda x: x.name.lower())
    elif sort == "Estágio":
        order = {"TOFU": 0, "MOFU": 1, "BOFU": 2}
        items.sort(key=lambda x: (order.get(x.target_stage, 9), x.name.lower()))
    else:
        items = list(reversed(items))

    for idx, c in enumerate(items):
        predicted = stage_from_inputs(c.pede_decisao, c.explica_porque, c.reduz_risco, c.esforco, c.cta)
        risk = contamination_risk(c.pede_decisao, c.esforco, c.cta)
        score = mental_coherence_score(c.target_stage, predicted, risk)
        action, _ = recommendation(c.target_stage, predicted, risk)

        with st.expander(f"{c.name}  |  planejado: {c.target_stage}  |  detectado: {predicted}  |  coerência: {score}/100"):
            a, b, d, e = st.columns(4)
            a.metric("CTA", c.cta)
            b.metric("Esforço", str(c.esforco))
            d.metric("Risco", f"{risk}%")
            e.metric("Decisão", action)

            st.write("Sinais")
            s1, s2, s3 = st.columns(3)
            s1.write("Pede decisão" if c.pede_decisao else "Não pede decisão")
            s2.write("Explica porquê" if c.explica_porque else "Não explica porquê")
            s3.write("Reduz risco" if c.reduz_risco else "Não reduz risco")

            if c.obs:
                st.write("Obs")
                st.write(c.obs)

# -----------------------------
# DIAGNÓSTICO
# -----------------------------
def aggregate(creatives: List[Creative]) -> Dict[str, Dict[str, int]]:
    out = {
        "TOFU": {"count": 0, "good": 0, "bad": 0, "risk_sum": 0, "score_sum": 0},
        "MOFU": {"count": 0, "good": 0, "bad": 0, "risk_sum": 0, "score_sum": 0},
        "BOFU": {"count": 0, "good": 0, "bad": 0, "risk_sum": 0, "score_sum": 0},
    }

    for c in creatives:
        predicted = stage_from_inputs(c.pede_decisao, c.explica_porque, c.reduz_risco, c.esforco, c.cta)
        risk = contamination_risk(c.pede_decisao, c.esforco, c.cta)
        score = mental_coherence_score(c.target_stage, predicted, risk)
        out[c.target_stage]["count"] += 1
        out[c.target_stage]["risk_sum"] += risk
        out[c.target_stage]["score_sum"] += score
        if score >= 60 and risk <= 45:
            out[c.target_stage]["good"] += 1
        else:
            out[c.target_stage]["bad"] += 1

    return out

def page_diagnosis():
    st.subheader("Diagnóstico de escala")
    st.caption("O diagnóstico usa sua Biblioteca e te diz onde a escala vai quebrar antes de você gastar.")

    if len(st.session_state.creatives) == 0:
        st.info("Cadastre alguns criativos na Biblioteca para gerar diagnóstico.")
        return

    agg = aggregate(st.session_state.creatives)

    c1, c2, c3 = st.columns(3)
    for col, stage in zip([c1, c2, c3], ["TOFU", "MOFU", "BOFU"]):
        data = agg[stage]
        count = data["count"]
        avg_risk = int(round(data["risk_sum"] / count)) if count else 0
        avg_score = int(round(data["score_sum"] / count)) if count else 0

        with col:
            st.markdown(f"### {stage}")
            st.metric("Criativos", str(count))
            st.metric("Coerência média", f"{avg_score}/100")
            st.metric("Risco médio", f"{avg_risk}%")
            st.progress(avg_score / 100)

    st.divider()

    # Diagnóstico global
    total = len(st.session_state.creatives)
    avg_risk_total = int(round(sum(agg[s]["risk_sum"] for s in agg) / total))
    avg_score_total = int(round(sum(agg[s]["score_sum"] for s in agg) / total))

    st.markdown("### Placar do funil")
    d1, d2, d3, d4 = st.columns(4)
    d1.metric("Total", str(total))
    d2.metric("Coerência geral", f"{avg_score_total}/100")
    d3.metric("Risco geral", f"{avg_risk_total}%")
    d4.metric("Status", score_to_label(avg_score_total))

    if avg_score_total >= 70 and avg_risk_total <= 40:
        st.success("Funil mentalmente escalável. A escala tende a ser consequência.")
    elif avg_score_total >= 55:
        st.warning("Escala possível, mas com vazamentos. Ajuste os pontos críticos antes de ampliar orçamento.")
    else:
        st.error("Escalar agora tende a virar tentativa. Falta coerência mental entre TOFU/MOFU/BOFU.")

    st.divider()

    st.markdown("### Ação prática agora")
    tips = []
    if agg["TOFU"]["bad"] > agg["TOFU"]["good"]:
        tips.append("Seu TOFU está pesado. Reduza esforço e remova decisão. Objetivo é curiosidade e identificação.")
    if agg["MOFU"]["bad"] > agg["MOFU"]["good"]:
        tips.append("Seu MOFU está fraco ou virando BOFU. Coloque mecanismo, comparação implícita e CTA de aprofundamento.")
    if agg["BOFU"]["bad"] > agg["BOFU"]["good"]:
        tips.append("Seu BOFU está inseguro. Adicione prova social, validação, garantia e CTA de ação. Sem explicar demais.")
    if avg_risk_total > 45:
        tips.append("Risco alto de contaminação. Você está pedindo decisão cedo demais em partes do funil.")

    if not tips:
        tips.append("Seu funil está bem alinhado. Próximo passo é ampliar o que está consistente e alimentar públicos com TOFU.")

    for t in tips:
        st.info(t)

# -----------------------------
# ROTEADOR
# -----------------------------
if st.session_state.mode == "Guia":
    page_guide()
elif st.session_state.mode == "Classificar Criativo":
    page_classify()
elif st.session_state.mode == "Biblioteca":
    page_library()
else:
    page_diagnosis()
