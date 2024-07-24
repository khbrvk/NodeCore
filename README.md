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

1. For coroutines version:
    ```sh
   from src.asyncio_concurrent import ConcurrentAsyncClass
   fetcher = ConcurrentAsyncClass(MAX_CONCURRENT, URL)
   fetcher.run()
    ```
    For threading version:
    ```sh
    from src.multithreading_concurrent import ConcurrentThreadsClass
    fetcher = ConcurrentThreadsClass(MAX_CONCURRENT, URL)
    fetcher.run()
    ```
2. Run:
   ```sh
    python main.py
    ```