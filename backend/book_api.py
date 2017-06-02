from celery import Celery

app = Celery('books', backend='redis://localhost:6379/1', broker = 'redis://localhost:6379/1')

import time

from book import BooksManager

handler = BooksManager("book")

@app.task
def post(message):
    print(message)
    return handler.get_all_books(message)

@app.task
def patch(message):
    print(message)
    return handler.get_book(message)


#@app.task
#def delete(message):
#    print(message)
#    return handler.delete(message)


@app.task
def put(message):
    print(message)
    time.sleep(1)
    return handler.get_popular(message)
