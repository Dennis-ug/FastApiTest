from fastapi import FastAPI
from routes.use_apis import user


app = FastAPI()


app.include_router(user)
