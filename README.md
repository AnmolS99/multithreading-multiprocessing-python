# Multithreading & Multiprocessing in Python

Short, focused repo that complements a blog post about multithreading and multiprocessing in Python.

## Prerequisites

-   Atleast Python 3.8
-   [uv](https://docs.astral.sh/uv/)

## Running the code

Add all necessary dependencies by running `uv sync`.

### Start a backend server

-   Django (sync):

    -   `cd django-webapp`
    -   For single-threaded: `python3 manage.py runserver --nothreading`
    -   For multi-threaded: `python3 manage.py runserver`

-   FastAPI (async):

    -   `cd fastapi`
    -   `fastapi dev main.py`

-   Gunicorn (sync multiprocessing):
    -   `cd django-webapp`
    -   `gunicorn --workers 2 --threads 1 banksite.wsgi:application`

### Send concurrent calls to the server

From repo root: `python3 benchmark.py`.

## Figures

Figures explaining multithreading, multiprocessing and asynchronous execution are available in the `/img` folder. These were drawn in Excalidraw.
