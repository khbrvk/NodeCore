import aiohttp
import asyncio

from src.writer import Writer


class ConcurrentAsyncClass:

    def __init__(self, max_concurrent: int, url: str, ):
        self.max_concurrent = max_concurrent #
        self.url = url

    async def get_content(self, session: aiohttp.ClientSession, url: str) -> None:
        """
        Функция для получения контента с какого либо веб ресурса
        :param session: экземпляр класса ClientSession
        :param url: ссылка на ресурс
        :return: None
        """

        async with session.get(url=url) as response:  # определяем менеджер контекста для работы в сесии
            data = await response.content.read()  # отдаем контроль управления пока не получим данные с ресурса
            await Writer.write_file_async(data) # вызываем асинхронную функцию для записи файла

    async def event_loop(self, amount_of_files: int = 5,):
        """
        Событийный цикл для выполнения тасок (загрузка картинок)
        :param amount_of_files: количество загружаемых файлов
        :return: None
        """

        tasks = []  # определяем контейнер в котором будем хранить наши таски
        connector = aiohttp.TCPConnector(limit=self.max_concurrent)  # определяем экземпляр класса TCPConnector чтобы
         # установить предельное значение обрабатываемых тасок
        async with aiohttp.ClientSession(connector=connector) as session:  # определяем сессию чтобы затем
             # передать ее в функцию и работать в рамкох одной сессии не тратя ресурсы на ее создание каждый раз
            for _ in range(amount_of_files):
                task = asyncio.create_task(self.get_content(session=session, url=self.url))  # создаем таску
                tasks.append(task)  # добавляем таску в контейнер

            await asyncio.gather(*tasks)  # распаковываем контейнер и запускаем несколько тасок

    def run(self):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # требуется для ОС Windows чтобы
         # корректно завершать корутины
        amount_of_files = int(input("Input the amount of files that should be downloaded: "))  # задаем количество файлов
         # для загрузки
        asyncio.run(self.event_loop(amount_of_files=amount_of_files))  # запускаем событийный цикл
