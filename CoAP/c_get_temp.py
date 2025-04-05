import asyncio
from aiocoap import Context, Message, GET

async def get_temperature():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri="coap://127.0.0.1/temperatura")
    
    try:
        response = await protocol.request(request).response
        print(f"Temperatura recebida: {response.payload.decode('utf-8')}°C")
    except Exception as e:
        print(f"Erro ao buscar temperatura: {e}")

if __name__ == "__main__":
    asyncio.run(get_temperature())