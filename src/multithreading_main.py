from concurrent.futures import ThreadPoolExecutor
import requests
import os


MAX_CONCURRENT: int = 10  # устанавливаем макисмальное количество тасок
URL: str = "https://loremflickr.com/320/240"  # определяем url ресурса
FILE_NUMBER: int = 1  # определяем переменную для подсчета скачанных файлов
DIRECTORY_NAME: str = "images2"


def check_directory(directory: str) -> None:
    """
    Функция для проверки существует ли директория.
    Создает директория если та не существует.
    :param directory:
    :return:
    """
    if not os.path.isdir(directory):  # проверяем наличие директории
        os.mkdir(directory)  # создаем директорию если та не существует


def write_file(data: bytes) -> None:
    global FILE_NUMBER  # объявляем что работать внутри функции будем с глобальной переменной
    file_name = f"{DIRECTORY_NAME}/image_{FILE_NUMBER}.jpeg"  # определяем имя записываемого файла
    with open(file_name, 'wb') as file:  # открываем менеджер контекста для записи файла
        file.write(data)  # пишем файл
        print(f"File number {FILE_NUMBER} has been downloaded")  # выводим информацию на печать
        FILE_NUMBER += 1  # инкрементируем переменную когда файл запишется


def get_content(url: str) -> None:
    response = requests.get(url)  # запрашиваем данные с ресурса
    write_file(response.content)  # пишем данные в файл


if __name__ == "__main__":
    check_directory(DIRECTORY_NAME)
    amount_of_files = int(input("Input the amount of files that should be downloaded: "))  # задаем количество файлов
    # для загрузки
    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT) as executor:
        urls = [URL for _ in range(amount_of_files)]
        executor.map(get_content, urls)
