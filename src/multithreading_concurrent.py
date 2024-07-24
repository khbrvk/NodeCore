from concurrent.futures import ThreadPoolExecutor
import requests

from src.writer import Writer


class ConcurrentThreadsClass:

    def __init__(self, max_concurrent: int, url: str, ):
        self.max_concurrent = max_concurrent  # инициализируем макисмальное количество потоков
        self.url = url  # инициализируем ресурс

    def _get_content(self, url) -> None:
        """
        Функция для получения контента с какого либо веб ресурса
        :param url: ссылка на ресурс
        :return: None
        """
        response = requests.get(url)  # запрашиваем данные с ресурса
        Writer.write_file_sync(response.content)  # пишем файл

    def run(self):
        amount_of_files = int(input("Input the amount of files that should be downloaded: "))  # задаем количество файлов
        # для загрузки
        with ThreadPoolExecutor(max_workers=self.max_concurrent) as executor:  # определяем экземпляр класса
            # ThreadPoolExecutor в контекстном менеджере с установкой макс. количества потоков
            urls = [self.url for _ in range(amount_of_files)]  #  создаем список ресурсов для скачивания картинок
            executor.map(self._get_content, urls) #  запускаем потоки
