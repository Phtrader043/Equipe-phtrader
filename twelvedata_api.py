
import requests

API_KEY = "cd52d4f5c5924063a7af0070445d2a3b"

def consultar_twelvedata(symbol):
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()
