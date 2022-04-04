import requests
from fastapi import FastAPI
from pydantic import BaseModel

from app import settings


class UrlToPing(BaseModel):
    url: str


app = FastAPI()


@app.post("/ping")
async def ping(url_to_ping: UrlToPing):
    response = requests.get(url_to_ping.url,
                            verify=settings.VERIFY_SSL_CERT,
                            timeout=settings.GET_REQUEST_TIMEOUT_SECONDS)
    return {
        'status_code': response.status_code,
        'elapsed_in_seconds': response.elapsed,
        'body_as_text': response.text
    }


@app.get("/info")
async def info():
    return {"Receiver": "Cisco is the best!"}
