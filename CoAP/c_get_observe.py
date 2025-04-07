import asyncio
from aiocoap import *

async def main():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri="coap://127.0.0.1/temperatura", observe=0) #tag do observe incluida

    pr = protocol.request(request)

    r = await pr.response
    print("First response: %s\n%r" % (r, r.payload))

    async for r in pr.observation:
        print("Next result: %s\n%r" % (r, r.payload))
        temperatura = float(r.payload.decode('utf-8'))
        if temperatura == 24.2: # condição para parar de observar
            pr.observation.cancel()
            break

    print("Loop encerrado")
    await asyncio.sleep(2) # aguarda 2 segundos

if __name__ == "__main__":
    asyncio.run(main())
