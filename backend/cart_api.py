from celery import Celery

app = Celery('cart', backend='redis://localhost:6379/2', broker = 'redis://localhost:6379/2')


from cart import CartManager

handler = CartManager("cart")

#@app.task
#def patch(message):
#    print(message)
#    return handler.login_check(message)

@app.task
def post(message):
    print(message)
    return handler.insert_book(message)


@app.task
def get(message):
    print(message)
    return handler.get_cart(message)


@app.task
def delete(message):
    print(message)
    return handler.delete_book(message)
