import asyncio
from aiocoap import Context, Message, PUT
import argparse

async def main(payload):
    context = await Context.create_client_context()
    
    request = Message(code=PUT, payload=payload.encode('utf-8'), uri="coap://127.0.0.1/lampada")

    response = await context.request(request).response

    print(f"Agora o estado da lampada é: {response.payload.decode('utf-8')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", required= True, help='Estado da lâmpada')

    args = parser.parse_args()

    asyncio.run(main(args.payload))