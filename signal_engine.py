
from data_fetcher import obter_dados
from cohere_analysis import analisar_tendencia
from utils import agora_brasilia, adicionar_minutos

CONFIANCA_MINIMA = 90  # filtro de risco

def gerar_sinal():
    tentativa = 0
    while tentativa < 5:
        dados = obter_dados()
        decisao = analisar_tendencia(dados)
        confianca = int(decisao["confianca"])

        if confianca >= CONFIANCA_MINIMA:
            agora = agora_brasilia()
            entrada = adicionar_minutos(agora, 2).strftime("%H:%M")
            saida = adicionar_minutos(agora, 7).strftime("%H:%M")

            return {
                "Ativo": dados["ativo"],
                "Tipo": decisao["tipo"],
                "Entrada": entrada,
                "Saída": saida,
                "Tendência": f"{confianca}%"
            }

        tentativa += 1

    return {
        "Ativo": "Nenhum",
        "Tipo": "Sem sinal",
        "Entrada": "-",
        "Saída": "-",
        "Tendência": "Sinal descartado por baixo risco"
    }
