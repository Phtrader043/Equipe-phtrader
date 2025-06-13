import cohere

co = cohere.Client("6UJatkMXui5NU3oNaoSAgAAUDVrI7Va7VddNbFUo")

def analisar_tendencia(dados):
    prompt = (
        f"Você é um analista financeiro experiente.\n"
        f"Aqui estão os dados mais recentes de um ativo de criptomoeda ou Forex:\n\n"
        f"Ativo: {dados['ativo']}\n"
        f"Preço atual: {dados['preco']}\n"
        f"Volume: {dados['volume']}\n"
        f"Variação percentual: {dados['variacao']}%\n"
        f"RSI (14): {dados['rsi']}\n"
        f"EMA (10): {dados['ema']}\n"
        f"MACD: {dados['macd']}\n"
        f"Histograma MACD: {dados['macd_hist']}\n\n"
        f"Com base nesses dados e indicadores técnicos, responda:\n"
        f"1. Você recomenda COMPRA ou VENDA?\n"
        f"2. Qual o nível de confiança dessa recomendação em porcentagem? (ex: 95%)\n"
        f"Responda diretamente, exemplo: 'Compra - Confiança: 93%'"
    )

    resposta = co.generate(
        prompt=prompt,
        model="command",
        max_tokens=60,
        temperature=0.3
    )

    texto = resposta.generations[0].text.strip().lower()

    if "compra" in texto:
        tipo = "Compra"
    elif "venda" in texto:
        tipo = "Venda"
    else:
        tipo = "Indefinido"

    numeros = [int(s) for s in texto.split() if s.isdigit()]
    confianca = max(numeros) if numeros else 50
    if confianca > 100:
        confianca = 100

    return {
        "tipo": tipo,
        "confianca": confianca
    }
