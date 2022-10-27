from fastapi import FastAPI
from routes.use_apis import user


app = FastAPI(debug=True)


# app.include_router(user)
