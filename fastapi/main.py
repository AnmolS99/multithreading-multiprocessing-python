from fastapi import FastAPI, Query
import asyncio


app = FastAPI()


@app.get("/currency/convert/")
async def convert(_from: str = Query(..., alias="from"), _to: str = Query(..., alias="to")):
    from_currency = _from.lower()
    to_currency = _to.lower()

    rate = await convert_currency_io_bound(from_currency, to_currency)
    return rate


async def convert_currency_io_bound(from_currency, to_currency):
    
    await asyncio.sleep(5) # awaiting while the DB uses 5 sec to respond

    if (from_currency == "usd" and to_currency == "gbp"):
        return 0.75
    elif (from_currency == "gbp" and to_currency == "usd"):
        return 1.33
    elif (from_currency == "usd" and to_currency == "eur"):
        return 0.86
    elif (from_currency == "eur" and to_currency == "usd"):
        return  1.16