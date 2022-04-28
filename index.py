# Feito por ItzMaxxi

from pypresence import Presence
import time
import os
from config import id

# Define o tamanho da janela do terminal
window = 'mode 90,19'
os.system(window)

os.system('cls')

# config pro script rodar
tempo = int(time.time())
client_id = id

# RPC
RPC = Presence(client_id)
RPC.connect()
while True: #quando conectar...
      RPC.update(state='Um texto simples...',
           details="Como um outro texto qualquer",
           large_image="nome da img",
           large_text="texto da img",
           small_image="img pequena nome",
           small_text="texto da img pequena",
           comecar=tempo,
           buttons=[{"label": "GitHub", "url": "https://github.com/ItzMaxxi"}]) #remove se você não quer ter o botão