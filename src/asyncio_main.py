import aiohttp
import asyncio
import aiofiles

from src.utils import check_directory

import os
from dotenv import load_dotenv

load_dotenv()

MAX_CONCURRENT: int = int(os.getenv('MAX_CONCURRENT'))  # устанавливаем макисмальное количество тасок
URL: str = os.getenv("URL")  # определяем url ресурса
FILE_NUMBER: int = int(os.getenv("FILE_NUMBER"))  # определяем переменную для подсчета скачанных файлов
DIRECTORY_NAME: str = os.getenv("DIRECTORY_NAME")


async def write_file_async(data: bytes) -> None:
    """
    Функция для асинхронной записи данных в бинарном формате в .jpeg файл
    :param data: данные файла в бинарном формате
    :return: None
    """

    global FILE_NUMBER  # объявляем что работать внутри функции будем с глобальной переменной
    file_name = f"{DIRECTORY_NAME}/image_{FILE_NUMBER}.jpeg"  # определяем имя записываемого файла
    async with aiofiles.open(file_name, 'wb') as file:  # открываем асинхронный менеджер контекста для записи файла
        await file.write(data)  # отдаем контроль управления в событийный цикл и пишем файл
        print(f"File number {FILE_NUMBER} has been downloaded")  # выводим информацию на печать
        FILE_NUMBER += 1  # инкрементируем переменную когда файл запишется


async def get_content(session: aiohttp.ClientSession, url: str) -> None:
    """
    Функция для получения контента с какого либо веб ресурса
    :param session: экземпляр класса ClientSession
    :param url: ссылка на ресурс
    :return: None
    """

    async with session.get(url=url) as response:  # определяем менеджер контекста для работы в сесии
        data = await response.content.read()  # отдаем контроль управления пока не получим данные с ресурса
        await write_file_async(data)  # вызываем асинхронную функцию для записи файла


async def main(amount_of_files: int = 5):
    """
    Событийный цикл для выполнения тасок (загрузка картинок)
    :param amount_of_files: количество загружаемых файлов
    :return: None
    """

    tasks = []  # определяем контейнер в котором будем хранить наши таски
    connector = aiohttp.TCPConnector(limit=MAX_CONCURRENT)  # определяем экземпляр класса TCPConnector чтобы
     # установить предельное значение обрабатываемых тасок
    async with aiohttp.ClientSession(connector=connector) as session:  # определяем сессию чтобы затем
         # передать ее в функцию и работать в рамкох одной сессии не тратя ресурсы на ее создание каждый раз
        for _ in range(amount_of_files):
            task = asyncio.create_task(get_content(session=session, url=URL))  # создаем таску
            tasks.append(task)  # добавляем таску в контейнер

        await asyncio.gather(*tasks)  # распаковываем контейнер и запускаем несколько тасок


if __name__ == "__main__":
    check_directory(DIRECTORY_NAME)  # проверяем наличие директории
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # требуется для ОС Windows чтобы
     # корректно завершать корутины
    amount_of_files = int(input("Input the amount of files that should be downloaded: "))  # задаем количество файлов
     # для загрузки
    asyncio.run(main(amount_of_files=amount_of_files))  # запускаем событийный цикл
