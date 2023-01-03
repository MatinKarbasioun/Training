import asyncRequests
import syncRequests


import asyncio

async def asyncRun(*args):
    await asyncio.gather(asyncRequests.asyncReqeust())

if __name__ == "__main__":
    syncRequests.syncRequest()
    asyncio.run(asyncRun())
