import asyncio
import datetime as dt
import random

import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

loop = asyncio.get_event_loop()

async def test_function(data=0):
    data += random.randint(0, 100)
    print(dt.datetime.now(), data)
    return data

test_scheduler = AsyncIOScheduler()

test_scheduler.add_job(
    test_function,
    id="TestJob",
    trigger=IntervalTrigger(
        seconds=1,
        start_date=dt.datetime.now(tz=pytz.UTC)
    )
)

test_scheduler.start()

loop.run_until_complete(asyncio.sleep(60))
