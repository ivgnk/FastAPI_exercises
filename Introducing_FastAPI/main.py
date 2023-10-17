#'''
#Знакомство с FastAPI
#https://pythonru.com/biblioteki/znakomstvo-s-fastapi
#
#Запуск
#C:\Python\Python311\Scripts\uvicorn.exe main:app --reload
#'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from main"}

