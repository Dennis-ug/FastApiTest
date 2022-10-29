from fastapi import FastAPI
from routes.use_apis import user
from routes.payments import payments
from routes.media import media


app = FastAPI(debug=True,title='Holy Healing Ministries Internatinal')


app.include_router(user)
app.include_router(payments)
app.include_router(media)
# @app.get('/')
# def test():
#     return{}