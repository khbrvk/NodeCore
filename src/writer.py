import aiofiles
from src.utils import check_directory
import os
from dotenv import load_dotenv

load_dotenv()


class Writer:

    directory_name: str = os.getenv("DIRECTORY_NAME")  #  определяем атрибут класса в котором хранится директория для
    # сохранения файлов
    file_number: int = 1  #  определяем атрибут класса для подсчета скачанный файлов

    @classmethod
    def write_file_sync(cls, data: bytes) -> None:
        """
        Функция для записи данных в бинарном формате в .jpeg файл
        :param directory_name: название директории куда записать файл
        :param data:  данные файла в бинарном формате
        :return: None
        """
        check_directory(cls.directory_name)  # проверяем наличие директории
        file_name = f"{cls.directory_name}/image_{cls.file_number}.jpeg"  # определяем имя записываемого файла
        with open(file_name, 'wb') as file:  # открываем менеджер контекста для записи файла
            file.write(data)  # пишем файл
            print(f"File number {Writer.file_number} has been downloaded")  # выводим информацию на печать
            Writer.file_number += 1  # инкрементируем переменную когда файл запишется

    @classmethod
    async def write_file_async(cls, data: bytes) -> None:
        """
        Функция для асинхронной записи данных в бинарном формате в .jpeg файл
        :param directory_name: название директории для записи файла
        :param data: данные файла в бинарном формате
        :return: None
        """
        check_directory(Writer.directory_name)  # проверяем наличие директории
        file_name = f"{cls.directory_name}/image_{cls.file_number}.jpeg"  # определяем имя записываемого файла
        async with aiofiles.open(file_name, 'wb') as file:  # открываем асинхронный менеджер контекста для записи файла
            await file.write(data)  # отдаем контроль управления в событийный цикл и пишем файл
            print(f"File number {cls.file_number} has been downloaded")  # выводим информацию на печать
            cls.file_number += 1  # инкрементируем переменную когда файл запишется