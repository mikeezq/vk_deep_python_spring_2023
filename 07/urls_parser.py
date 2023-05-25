import os
import asyncio
import argparse
import aiofiles
import aiohttp


async def fetch_url(url, sem):
    async with aiohttp.ClientSession() as session:
        async with sem:
            async with session.get(url) as resp:
                assert resp.status == 200
                response_text = await resp.text()
                return response_text


async def fetch_urls(args):
    file = args.file
    if not os.path.exists(file):
        raise FileNotFoundError(f"File {file} does not exists")

    sem = asyncio.Semaphore(args.c)

    tasks = []
    async with aiofiles.open(file, "r") as f:
        async for line in f:
            url = line.strip()
            task = asyncio.create_task(fetch_url(url, sem))
            tasks.append(task)
            if len(tasks) >= args.c:
                await asyncio.gather(*tasks)
                tasks = []

    if tasks:
        await asyncio.gather(*tasks)


def parse_args():
    args = argparse.ArgumentParser()

    args.add_argument("-c", type=int, default=5, help="Number of concurrent requests")
    args.add_argument("file", metavar="FILENAME")

    return args.parse_args()


if __name__ == "__main__":
    args = parse_args()
    asyncio.run(fetch_urls(args))
