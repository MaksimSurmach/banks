import datetime
from pydantic import BaseModel


class Anek(BaseModel):
    text: str
    date: datetime.datetime
    viewers_tg: int
    forwards_tg: int


class AnekList(BaseModel):
    aneks: list[Anek]


class RequestData(BaseModel):
    user_name: str
    days: int
