#!/usr/bin/env python3
import time, asyncio, aiohttp

# --- configuration ---
PAIRS = [("USD", "GBP"), ("GBP", "USD")]
BASE_URL = "http://localhost:8000/currency/convert"
# ----------------------

async def fetch(session, frm, to):
    url = f"{BASE_URL}?from={frm}&to={to}"
    start = time.perf_counter()
    async with session.get(url) as r:
        body = await r.text()  # expected to be a number
        duration = time.perf_counter() - start
        return frm, to, r.status, body, duration

async def main():
    print(f"Sending {len(PAIRS)} concurrent requests...")
    start_total = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, frm, to) for frm, to in PAIRS]
        for i, task in enumerate(asyncio.as_completed(tasks), 1):
            frm, to, status, body, dur = await task
            print(f"[{i}/{len(PAIRS)}] {frm}->{to} | resp={body} | status={status} | {dur:.4f}s")

    print(f"Total time: {time.perf_counter() - start_total:.4f}s")

if __name__ == "__main__":
    asyncio.run(main())