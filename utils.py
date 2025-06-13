
from datetime import datetime, timedelta
import pytz

def agora_brasilia():
    fuso = pytz.timezone("America/Sao_Paulo")
    return datetime.now(fuso)

def adicionar_minutos(dt, minutos):
    return dt + timedelta(minutes=minutos)
