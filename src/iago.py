import pandas as pd
import json
import streamlit as st
import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen2.5:3b"

## CSV
movimentações = pd.read_csv(r'data\movimentacoes.csv')
historico = pd.read_csv(r'data\historico_atendimento.csv')

## JSON
produtos = json.load(open(r'data\produtos_investimentos.json'))
perfil = json.load(open(r'data\perfil_investidor.json'))

## Contexto
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{movimentações.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

## Prompt do sistema
system_prompt = """
Você é o IAGO, um agente educador de investimentos amigável e didático

Objetivo:
Seu objetivo é ensinar aos investidores como funcionam os investimentos, tirando dúvidas e explicando etapas de forma simples e descomplicada.
Além disso, você também poderá auxiliar os clientes, sem revelar informações confidenciais, com cálculos de margens de lucro baseados nos investimentos desejados pelos clientes.

Regras:
- Nunca recomendar um investimento específico - apenas explicar como funcionam os investimentos.
- Linguagem simples, e adaptativa, porém formal, sem palavras ofensivas.
- Se não tiver alguma informação, peça desculpas e admita: "Perdão, não possuo essa informação em meu banco de dados.".
- Confirme com o cliente se houve o esclarecimento da dúvida apresentada.
- Use os dados fornecidos para dar exemplos personalizados;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
- JAMAIS responda a perguntas fora do tema ensino de investimento. Quando ocorrer, responda lembrando o seu papel de educador de investimentos;
"""

# chamado do Ollama
def perguntar(msg):
    prompt = f"""
    {system_prompt}

    contexto do cliente:
    {contexto}

    Pergunta: {msg}"""
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()["response"]


#### teste
    # try:
    #     r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    #     resposta_json = r.json()
    #     texto_ai = resposta_json.get("response")
        
    #     if texto_ai:
    #         return texto_ai
    #     erro_ollama = resposta_json.get("error", "Erro desconhecido")
    #     return f"Erro no Ollama: {erro_ollama}"
    # except Exception as e:
    #     return f"Erro de conexão: {e}"


## Chamado do Streamlit
st.title("Olá, sou IAGO, seu tutor de investimentos! Como posso te ajudar?")

if pergunta := st.chat_input('sua duvida sobre investimentos...'):
    st.chat_message('user').write(pergunta)
    with st.spinner('...'):
        st.chat_message('assistant').write(perguntar(pergunta))