import streamlit as st

st.title("🧠 Resumo Executivo do Funil")

st.markdown("""
Este funil não é sobre anúncios.  
É sobre **acompanhar o processo mental real do comprador**.
""")

st.divider()

st.subheader("🔹 TOFU — Despertar")
st.markdown("""
**Pergunta mental:**  
> “Isso existe?”

**Função:**  
Despertar curiosidade e identificação, sem exigir decisão.

**Erro fatal:**  
Forçar venda cedo demais.
""")

st.subheader("🟡 MOFU — Organizar")
st.markdown("""
**Pergunta mental:**  
> “Isso faz sentido pra mim?”

**Função:**  
Organizar o raciocínio, explicar o porquê e reduzir ceticismo.

**Erro fatal:**  
Prometer demais ou vender cedo.
""")

st.subheader("🔴 BOFU — Confirmar")
st.markdown("""
**Pergunta mental:**  
> “Posso confiar?”

**Função:**  
Remover medo e facilitar a decisão.

**Erro fatal:**  
Usar BOFU em público que ainda não entendeu.
""")

st.divider()

st.success("""
📌 REGRA DE OURO  
Se o criativo não responde claramente a uma dessas perguntas,
ele não deve ser escalado.
""")
