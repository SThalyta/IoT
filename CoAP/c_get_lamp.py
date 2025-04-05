import asyncio
from aiocoap import Context, Message, GET

async def get_lamp():
    protocol = await Context.create_client_context()
    request = Message(code=GET, uri="coap://127.0.0.1/lampada")
    
    try:
        response = await protocol.request(request).response
        print(f"Estado da lampada: {response.payload.decode('utf-8')}")
    except Exception as e:
        print(f"Erro o estado da lampada: {e}")

if __name__ == "__main__":
    asyncio.run(get_lamp())