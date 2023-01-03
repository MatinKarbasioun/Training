import time
import requests

def syncRequest(num):
    names = []
    with requests.session() as session:
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{num}'
        resp = session.get(pokemon_url) 
        pokemon = resp.json()
        names.append(pokemon)
        print(pokemon["name"])


def callSync():
    startTime = time.time()
    any(syncRequest(num) for num in range(1,151))
    endTime = time.time()

    print(f'sync Request Time is about {endTime-startTime}')




if __name__ == "__main__":
    callSync()