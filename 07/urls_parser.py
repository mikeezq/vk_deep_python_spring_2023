import sys
import os
import asyncio
import aiohttp


COUNT = 0


async def fetch_url(url, sem):
    global COUNT

    async with aiohttp.ClientSession() as session:
        async with sem:
            async with session.get(url) as resp:
                COUNT += 1
                assert resp.status == 200


async def fetch_urls(args):
    try:
        coroutines_count = int(args[0])
    except ValueError:
        raise ValueError("First argument must be numeric")

    file = args[1]
    if not os.path.exists(file):
        raise FileNotFoundError(f"File {file} does not exists")

    sem = asyncio.Semaphore(coroutines_count)

    tasks = [
        asyncio.create_task(fetch_url(url.strip(), sem))
        for url in open(file, "r")
    ]
    await asyncio.gather(*tasks)
    return COUNT


if __name__ == "__main__":
    sys_args = sys.argv[1:]
    asyncio.run(fetch_urls(sys_args))
