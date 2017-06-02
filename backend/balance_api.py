from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379/3', broker = 'redis://localhost:6379/3')


from balance import BalanceManager

handler = BalanceManager("balance")

#@app.task
#def patch(message):
#    print(message)
#    return handler.login_check(message)

@app.task
def post(message):
    print(message)
    return handler.top_up(message)


@app.task
def get(message):
    print(message)
    return handler.get_balance(message)


@app.task
def put(message):
    print(message)
    return handler.withdraw(message)
