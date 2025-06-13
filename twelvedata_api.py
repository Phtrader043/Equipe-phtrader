
import requests

API_KEY = "08665d12c4394cafad7e9a36f1bf3ba8"

def consultar_twelvedata(symbol):
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()
