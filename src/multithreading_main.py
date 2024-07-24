from concurrent.futures import ThreadPoolExecutor
import requests

from src.utils import check_directory

import os
from dotenv import load_dotenv

load_dotenv()


MAX_CONCURRENT: int = int(os.getenv('MAX_CONCURRENT'))  # устанавливаем макисмальное количество тасок
URL: str = os.getenv("URL")  # определяем url ресурса
FILE_NUMBER: int = int(os.getenv("FILE_NUMBER"))  # определяем переменную для подсчета скачанных файлов
DIRECTORY_NAME: str = os.getenv("DIRECTORY_NAME")


def write_file_sync(data: bytes) -> None:
    """
    Функция для записи данных в бинарном формате в .jpeg файл
    :param data: данные файла в бинарном формате
    :return: None
    """

    global FILE_NUMBER  # объявляем что работать внутри функции будем с глобальной переменной
    file_name = f"{DIRECTORY_NAME}/image_{FILE_NUMBER}.jpeg"  # определяем имя записываемого файла
    with open(file_name, 'wb') as file:  # открываем менеджер контекста для записи файла
        file.write(data)  # пишем файл
        print(f"File number {FILE_NUMBER} has been downloaded")  # выводим информацию на печать
        FILE_NUMBER += 1  # инкрементируем переменную когда файл запишется


def get_content(url: str) -> None:
    """
    Функция для получения контента с какого либо веб ресурса
    :param url: ссылка на ресурс
    :return: None
    """

    response = requests.get(url)  # запрашиваем данные с ресурса
    write_file_sync(response.content)  # пишем данные в файл


if __name__ == "__main__":
    check_directory(DIRECTORY_NAME)  # проверяем наличие директории
    amount_of_files = int(input("Input the amount of files that should be downloaded: "))  # задаем количество файлов
    # для загрузки
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT) as executor:  # определяем экземпляр класса
        # ThreadPoolExecutor в контекстном менеджере
        urls = [URL for _ in range(amount_of_files)]  #  создаем список ресурсов для скачивания картинок
        executor.map(get_content, urls) #  запускаем потоки
