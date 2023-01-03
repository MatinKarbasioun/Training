import time
import aiohttp
import asyncio

async def asyncReqeust(num):

    names = []
    async with aiohttp.ClientSession() as session:
        
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{num}'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            names.append(pokemon)

            print(pokemon["name"])

    
async def callAsync():
    startTime = time.time()
    await asyncio.gather(*(asyncReqeust(num) for num in range(1,151)))
    endTime = time.time()
    print(f'async Request Time is about {endTime-startTime}')

if __name__ == "__main__":
    asyncio.run(callAsync())