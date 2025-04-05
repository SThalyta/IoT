import asyncio
import random
from aiocoap import Context, Message, resource, CHANGED
import time

class TemperatureResource(resource.Resource):
    async def render_get(self, request):
        temperatura = round(random.uniform(20.0, 30.0), 2)
        print(f"Enviando temperatura: {temperatura}°C")
        time.sleep(5)
        return Message(payload=str(temperatura).encode('utf-8'))

class LampadaResource(resource.Resource):
    def __init__(self):
        super().__init__()
        self.lampada = "off"  # Estado inicial da lâmpada

    async def render_get(self, request):
        print(f"Enviando o estado atual da lâmpada: {self.lampada}")
        return Message(payload=self.lampada.encode('utf-8'))

    async def render_put(self, request):
        novo_estado = request.payload.decode('utf-8')  # Decodifica o estado enviado
        if novo_estado in ["on", "off"]:
            self.lampada = novo_estado  # Atualiza o estado da lâmpada (A atualização poderia ser com o on_change)
            print(f"Lâmpada alterada para: {self.lampada}")
            return Message(code=CHANGED, payload=f"{self.lampada}".encode('utf-8'))
        else:
            return Message(code=CHANGED, payload=f"Comando inválido, use 'on' ou 'off'.")

async def main():
    root = resource.Site()
    root.add_resource(('temperatura',), TemperatureResource())
    root.add_resource(('lampada',), LampadaResource())

    await Context.create_server_context(root, bind=('127.0.0.1', 5683))
    print("Servidor CoAP rodando na porta 5683...")
    await asyncio.get_running_loop().create_future()  # Mantém o servidor rodando

if __name__ == "__main__":
    asyncio.run(main())
