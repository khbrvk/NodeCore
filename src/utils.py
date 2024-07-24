import os


def check_directory(directory: str) -> None:
    """
    Функция для проверки существует ли директория.
    Создает директорию если та не существует.
    :param directory: название директории
    :return: None
    """

    if not os.path.isdir(directory):  # проверяем наличие директории
        os.mkdir(directory)  # создаем директорию если та не существует