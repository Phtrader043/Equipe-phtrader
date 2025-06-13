
import cohere

co = cohere.Client("0zIapnzQSu4BXmPPkFbL4A0E4HZG9wM6IotodQOn")

def analisar_tendencia(dados):
    texto = f"""Você é um analista financeiro experiente.
Aqui estão os dados mais recentes de um ativo de criptomoeda ou Forex:

Ativo: {dados['ativo']}
Preço atual: {dados['preco']}
Volume: {dados['volume']}
Variação percentual: {dados['variacao']}%
RSI (14): {dados['rsi']}
EMA (10): {dados['ema']}
MACD: {dados['macd']}
Histograma MACD: {dados['macd_hist']}

Com base nesses dados e indicadores técnicos, responda:
1. Você recomenda COMPRA ou VENDA?
2. Qual o nível de confiança dessa recomendação em porcentagem? (ex: 95%)
Responda diretamente, exemplo: "Compra - Confiança: 93%""""

    resposta = co.generate(
        prompt=texto,
        model="command",
        max_tokens=60,
        temperature=0.3
    )

    resultado = resposta.generations[0].text.strip().lower()
    if "compra" in resultado:
        tipo = "Compra"
    elif "venda" in resultado:
        tipo = "Venda"
    else:
        tipo = "Indefinido"

    confianca = "".join([c for c in resultado if c.isdigit()])
    if confianca:
        confianca = int(confianca)
        if confianca > 100:
            confianca = 100
    else:
        confianca = 50

    return {
        "tipo": tipo,
        "confianca": confianca
    }
