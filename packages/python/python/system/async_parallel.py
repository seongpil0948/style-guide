import asyncio
import time
from concurrent.futures import ProcessPoolExecutor
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        session.headers["User-Agent"] = "SNU IDS Lab (http://ids.snu.ac.kr/)"
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)



if __name__ == "__main__":
    sites = ['www.naver.com'] * 100000
    num_of_process = 5
    start_time = time.time()
    with ProcessPoolExecutor(num_of_process) as executor:
        for _ in range(num_of_process):
            executor.submit(asyncio.get_event_loop().run_until_complete(download_all_sites(sites[:20000])))

    duration = time.time() - start_time
    print(f"Total: {len(sites)} Downloaded {len(sites)} sites in {duration} seconds")