import asyncio
from aiocoap import Context, Message, PUT

async def main():
    context = await Context.create_client_context()

    payload = b"off" 
    request = Message(code=PUT, payload=payload, uri="coap://127.0.0.1/lampada")

    response = await context.request(request).response

    print(f"Agora o estado da lampada é: {response.payload.decode('utf-8')}")

if __name__ == "__main__":
    asyncio.run(main())