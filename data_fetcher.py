
import requests
import random

API_KEY = "cd52d4f5c5924063a7af0070445d2a3b"

ATIVOS = [
    "BTC/USD", "ETH/USD", "BNB/USD", "XRP/USD", "ADA/USD", "DOGE/USD", "SOL/USD", "LTC/USD",
    "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "USD/CAD", "AUD/USD", "NZD/USD",
    "EUR/JPY", "EUR/GBP", "EUR/CHF", "GBP/JPY", "AUD/JPY", "NZD/JPY", "CAD/CHF", "CHF/JPY"
]

def consultar_api(endpoint, params):
    base_url = f"https://api.twelvedata.com/{endpoint}"
    params["apikey"] = API_KEY
    response = requests.get(base_url, params=params)
    return response.json()

def obter_dados():
    ativo = random.choice(ATIVOS)

    # Coleta candle
    ts_data = consultar_api("time_series", {
        "symbol": ativo,
        "interval": "1min",
        "outputsize": 5
    })

    try:
        ultimo = ts_data["values"][0]
        preco = float(ultimo["close"])
        volume = float(ultimo.get("volume", 0))
        variacao = (float(ultimo["close"]) - float(ultimo["open"])) / float(ultimo["open"]) * 100
    except:
        preco = 0
        volume = 0
        variacao = 0

    # Indicadores técnicos
    rsi_data = consultar_api("rsi", {"symbol": ativo, "interval": "1min", "time_period": 14})
    ema_data = consultar_api("ema", {"symbol": ativo, "interval": "1min", "time_period": 10})
    macd_data = consultar_api("macd", {"symbol": ativo, "interval": "1min"})

    try:
        rsi = float(rsi_data["values"][0]["rsi"])
    except:
        rsi = 0

    try:
        ema = float(ema_data["values"][0]["ema"])
    except:
        ema = 0

    try:
        macd = float(macd_data["values"][0]["macd"])
        signal = float(macd_data["values"][0]["signal"])
        macd_hist = macd - signal
    except:
        macd = signal = macd_hist = 0

    return {
        "ativo": ativo,
        "preco": round(preco, 4),
        "volume": round(volume, 2),
        "variacao": round(variacao, 2),
        "rsi": round(rsi, 2),
        "ema": round(ema, 4),
        "macd": round(macd, 4),
        "macd_hist": round(macd_hist, 4)
    }
