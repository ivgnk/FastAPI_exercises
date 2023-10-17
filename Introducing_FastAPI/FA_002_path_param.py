'''
Path-параметры
https://fastapi.tiangolo.com/ru/tutorial/path-params/
'''
# Запуск
# C:\Python\Python311\Scripts\uvicorn.exe FA_002:app --reload

from fastapi import FastAPI

app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}