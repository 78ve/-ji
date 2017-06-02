from celery import Celery

app = Celery('account', backend='redis://localhost:6379/0', broker = 'redis://localhost:6379/0')


from account import AccountsManager

handler = AccountsManager("user")

@app.task
def patch(message):
    print(message)
    return handler.login_check(message)

@app.task
def get(message):
    print(message)
    return handler.get_all_users(message)

@app.task
def post(message):
    print(message)
    return handler.create(message)


@app.task
def delete(message):
    print(message)
    return handler.delete(message)


@app.task
def put(message):
    print(message)
    return handler.update(message)
