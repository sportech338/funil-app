import streamlit as st
from dataclasses import dataclass
from typing import Dict, List, Tuple

st.set_page_config(
    page_title="Manual Mental de Funil de Vendas",
    layout="wide"
)

# ==================================================
# FUNÇÕES UTILITÁRIAS (LÓGICA)
# ==================================================
def clamp(n: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, n))

def score_label(score: int) -> str:
    if score >= 80:
        return "Excelente"
    if score >= 60:
        return "Bom"
    if score >= 40:
        return "Atenção"
    return "Crítico"

def detectar_estagio(pede_decisao, explica, reduz_risco, esforco, cta):
    if pede_decisao or cta in ["Comprar agora", "Garantir o seu"]:
        return "BOFU"
    if explica or reduz_risco or esforco >= 3:
        return "MOFU"
    return "TOFU"

def risco_contaminacao(pede_decisao, esforco, cta):
    risco = 0
    if pede_decisao:
        risco += 40
    if cta in ["Comprar agora", "Garantir o seu"]:
        risco += 35
    if esforco >= 4:
        risco += 25
    return clamp(risco, 0, 100)

def coerencia_mental(planejado, detectado, risco):
    score = 100
    if planejado != detectado:
        score -= 35
    score -= int(risco * 0.3)
    return clamp(score, 0, 100)

def decisao_funil(planejado, detectado, risco):
    if planejado == detectado and risco <= 35:
        return "Escalar", "Criativo coerente com o estágio mental do público."
    if planejado == "TOFU" and detectado != "TOFU":
        return "Consertar", "Você está exigindo demais para um primeiro contato."
    if planejado == "MOFU" and detectado == "BOFU":
        return "Ajustar", "Está pedindo decisão antes de organizar o raciocínio."
    if planejado == "BOFU" and detectado != "BOFU":
        return "Ajustar", "Está fraco para decisão. Falta segurança."
    return "Ajustar", "Criativo desalinhado com o timing mental."

# ==================================================
# MODELOS DE DADOS
# ==================================================
@dataclass
class Creative:
    nome: str
    estagio_planejado: str
    cta: str
    pede_decisao: bool
    explica: bool
    reduz_risco: bool
    esforco: int
    obs: str = ""

# ==================================================
# ESTADO
# ==================================================
if "pagina" not in st.session_state:
    st.session_state.pagina = "Guia"
if "criativos" not in st.session_state:
    st.session_state.criativos: List[Creative] = []

# ==================================================
# CABEÇALHO
# ==================================================
st.title("🧠 Manual Mental de Funil de Vendas")
st.caption("Este app ensina como construir, analisar e escalar um funil de vendas baseado na mente real do comprador.")

# ==================================================
# NAVEGAÇÃO
# ==================================================
st.session_state.pagina = st.radio(
    "Escolha o que deseja aprender ou analisar:",
    ["Guia", "O que é TOFU, MOFU e BOFU", "Classificar Criativo", "Biblioteca", "Diagnóstico"],
    horizontal=True
)

# ==================================================
# GUIA – AULA BASE
# ==================================================
if st.session_state.pagina == "Guia":
    st.subheader("📘 Aula 1 — O que é um funil de vendas de verdade")

    st.markdown("""
    Um funil de vendas não é uma estrutura de campanhas.  
    Um funil de vendas é uma **sequência de estados mentais**.

    Antes de comprar, toda pessoa passa por cinco momentos:
    desconhecimento, identificação do problema, dúvida, confiança e decisão.

    O erro mais comum no tráfego pago é **tentar pular etapas**.
    """)

    st.warning("""
    Escalar não é:
    aumentar orçamento  
    duplicar conjunto  
    abrir público parecido  

    Escalar é ampliar algo que já está coerente com a mente do comprador.
    """)

    st.success("""
    Quando seus anúncios respeitam o timing mental, a escala vira consequência.
    """)

# ==================================================
# AULA TOFU / MOFU / BOFU
# ==================================================
elif st.session_state.pagina == "O que é TOFU, MOFU e BOFU":
    st.subheader("📘 Aula 2 — TOFU, MOFU e BOFU explicados")

    tab1, tab2, tab3 = st.tabs(["TOFU", "MOFU", "BOFU"])

    with tab1:
        st.markdown("""
        TOFU é o primeiro contato.

        O público ainda não quer comprar.
        Ele só quer entender se aquilo existe e se pode ser relevante.

        O erro no TOFU é pedir decisão cedo demais.
        """)

        st.info("No TOFU, o produto aparece como parte da rotina, não como argumento de venda.")

    with tab2:
        st.markdown("""
        MOFU é organização mental.

        Aqui o público já está curioso, mas desconfiado.
        Ele quer lógica, comparação e explicação.

        MOFU não vende. MOFU faz sentido.
        """)

        st.info("MOFU existe para explicar o que o público já começou a suspeitar.")

    with tab3:
        st.markdown("""
        BOFU é decisão.

        A pessoa já entendeu tudo.
        O único medo agora é errar na escolha.

        BOFU não convence. BOFU confirma.
        """)

        st.info("BOFU não empurra a venda. Ele dá segurança para decidir.")

# ==================================================
# CLASSIFICADOR
# ==================================================
elif st.session_state.pagina == "Classificar Criativo":
    st.subheader("🧪 Classificador Mental de Criativos")

    nome = st.text_input("Nome do criativo")
    planejado = st.selectbox("Função planejada no funil", ["TOFU", "MOFU", "BOFU"])
    cta = st.selectbox("CTA", ["Saiba mais", "Entenda como funciona", "Comprar agora", "Garantir o seu"])
    pede_decisao = st.toggle("Pede decisão?")
    explica = st.toggle("Explica o porquê?")
    reduz_risco = st.toggle("Reduz risco mental?")
    esforco = st.slider("Esforço cognitivo", 1, 5)

    if nome:
        detectado = detectar_estagio(pede_decisao, explica, reduz_risco, esforco, cta)
        risco = risco_contaminacao(pede_decisao, esforco, cta)
        score = coerencia_mental(planejado, detectado, risco)
        acao, motivo = decisao_funil(planejado, detectado, risco)

        st.metric("Estágio detectado", detectado)
        st.metric("Risco mental", f"{risco}%")
        st.progress(score / 100)
        st.write(f"Coerência: {score}/100 — {score_label(score)}")

        if acao == "Escalar":
            st.success(motivo)
        else:
            st.warning(motivo)

        if st.button("Salvar criativo"):
            st.session_state.criativos.append(
                Creative(nome, planejado, cta, pede_decisao, explica, reduz_risco, esforco)
            )
            st.success("Criativo salvo.")

# ==================================================
# BIBLIOTECA
# ==================================================
elif st.session_state.pagina == "Biblioteca":
    st.subheader("📚 Biblioteca de Criativos")

    if not st.session_state.criativos:
        st.info("Nenhum criativo cadastrado ainda.")
    else:
        for c in st.session_state.criativos:
            with st.expander(c.nome):
                st.write(f"Planejado: {c.estagio_planejado}")
                st.write(f"CTA: {c.cta}")
                st.write(f"Esforço: {c.esforco}")

# ==================================================
# DIAGNÓSTICO
# ==================================================
elif st.session_state.pagina == "Diagnóstico":
    st.subheader("📈 Diagnóstico do Funil")

    if not st.session_state.criativos:
        st.info("Cadastre criativos para gerar diagnóstico.")
    else:
        total = len(st.session_state.criativos)
        st.metric("Total de criativos", total)

        st.success("""
        Use este diagnóstico para responder:
        Onde estou pedindo decisão cedo demais?
        Onde falta educação?
        Onde falta segurança?
        """)

