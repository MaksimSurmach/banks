from fastapi import FastAPI
from dotenv import load_dotenv
from database import Database
import dataclass


app = FastAPI()


@app.on_event("startup")
async def startup():
    try:
        load_dotenv()
        global db
        db = Database()
    except Exception as e:
        print(e)
        raise e


@app.on_event("shutdown")
async def shutdown():
    db.close()


@app.get("/health", status_code=200)
async def health():
    return {"message": "ok"}


@app.get("/random", response_model=dataclass.Anek)
async def get_random_anek():
    return db.get_random_joke()
