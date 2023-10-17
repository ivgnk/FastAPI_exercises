'''
2022_Создание веб-API Python с помощью FastAPI ч1.pdf, Глава 2

2022 Как работать с curl в Windows https://habr.com/ru/companies/ruvds/articles/699226/
'''
from fastapi import FastAPI

from todo import todo_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World ___ "
    }


app.include_router(todo_router)


