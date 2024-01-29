import datetime
import asyncio
from random import randint

async def time_screen():
    while True:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%y %m %d %H %M')
        if current_time != datetime.datetime(2024, 1, 29, 22, 40):
            await asyncio.sleep(60)
            print(f"Текущее время: {formatted_time}")

asyncio.run(time_screen())

def random():
    number = float(input("Введите число от 1 до 10 : "))
    if not isinstance(number, float):
        raise ValueError("Должно быть вещественное число")
    random_number = randint(1, 10)
    count = 0
    while number != random_number:
        number = float(input('Укажите новый номер: '))
        count += 1
    print(f"Успешно, количество попыток : {count}")


random()

