import paho.mqtt.client as mqtt
import time
import random

# Configurações do broker MQTT
BROKER = "10.0.0.100"  # Altere para o IP do seu broker, se necessário
PORT = 1884
TOPICO_TEMPERATURA = "temperatura"
INTERVALO_ENVIO = 2  # Tempo em segundos entre envios

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

try:
    while True:
        temperatura = round(random.uniform(20.0, 30.0), 2) 
        client.publish(TOPICO_TEMPERATURA, temperatura)

        print(f"Publicado: {temperatura}°C no tópico {TOPICO_TEMPERATURA}")

        time.sleep(INTERVALO_ENVIO)
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
    client.disconnect()
