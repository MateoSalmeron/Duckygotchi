from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    description="This is a simple app to take care of a duck",
    title="Duckygotchy",
    docs_url="/"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


import json

@app.get("/duck")
def get_duck():
    return "hello duck"

if __name__ == '__main__':
  uvicorn.run("main:app",reload=True)


