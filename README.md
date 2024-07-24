# NodeCore

Module allows you to get X amount of files with N amount of courutines/threads

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/khbrvk/NodeCore.git
    ```

2. Navigate to the project directory:
    ```sh
    cd NodeCore
    ```

3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Create your .env file and set the variables:
    ```sh
    MAX_CONCURRENT=
    URL=
    DIRECTORY_NAME=
   
   MAX_CONCURRENT - limit of tasks/threads
   URL - web path to image
   DIRECTORY_NAME - save files directory
   
   Example:
   
   MAX_CONCURRENT=10
   URL=https://loremflickr.com/320/240
   DIRECTORY_NAME=images
    ```

## Usage
1. Import modules:
    ```sh
   import os
   from dotenv import load_dotenv
   from src.asyncio_concurrent import ConcurrentAsyncClass
   from src.multithreading_concurrent import ConcurrentThreadsClass

   load_dotenv()
   ```
2. Import variables:
    ```sh
    MAX_CONCURRENT: int = int(os.getenv('MAX_CONCURRENT'))
    URL: str = os.getenv("URL")
3. For coroutines version:
    ```sh
   fetcher = ConcurrentAsyncClass(MAX_CONCURRENT, URL)
   fetcher.run()
    ```
    For threading version:
    ```sh
    fetcher = ConcurrentThreadsClass(MAX_CONCURRENT, URL)
    fetcher.run()
    ```
4. Run:
   ```sh
    python main.py
    ```