from celery import Celery

app = Celery('orders', backend='redis://localhost:6379/5', broker = 'redis://localhost:6379/6')


from comment import CommentManager

handler = CommentManager("order")

#@app.task
#def patch(message):
#    print(message)
#    return handler.login_check(message)

@app.task
def post(message):
    print(message)
    return handler.generate_comment(message)


@app.task
def get(message):
    print(message)
    return handler.get_comments(message)

