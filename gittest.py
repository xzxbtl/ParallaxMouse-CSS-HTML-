import datetime
import asyncio


async def time_screen():
    while True:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%y %m %d %H %M')
        if current_time != datetime.datetime(2024, 1, 29, 22, 40):
            await asyncio.sleep(60)
            print(f"Текущее время: {formatted_time}")

asyncio.run(time_screen())


