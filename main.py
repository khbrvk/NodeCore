import os
from dotenv import load_dotenv
from src.asyncio_concurrent import ConcurrentAsyncClass
from src.multithreading_concurrent import ConcurrentThreadsClass

load_dotenv()

MAX_CONCURRENT: int = int(os.getenv('MAX_CONCURRENT'))  #  читаем переменную из конфигурационного файла
URL: str = os.getenv("URL")  #  читаем переменную из конфигурационного файла

fetcher = ConcurrentThreadsClass(MAX_CONCURRENT, URL)  #  создаем экземпляр требуемого класса
fetcher.run()  #  запускаем  скрипт
