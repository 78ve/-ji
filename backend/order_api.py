from celery import Celery

app = Celery('orders', backend='redis://localhost:6379/4', broker = 'redis://localhost:6379/4')


from order import OrderManager

handler = OrderManager("order")

#@app.task
#def patch(message):
#    print(message)
#    return handler.login_check(message)

@app.task
def post(message):
    print(message)
    return handler.generate_order(message)


@app.task
def get(message):
    print(message)
    return handler.get_order_details(message)


@app.task
def put(message):
    print(message)
    return handler.update_order_status(message)

@app.task
def patch(message):
    print(message)
    return handler.delete_order(message)
