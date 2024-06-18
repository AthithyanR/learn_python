from fastapi import FastAPI
from pydantic import BaseModel, Field
import csv

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    is_alive: bool

class Movie(BaseModel):
    title: str = Field(..., alias="Title")
    year: int = Field(..., alias="Year")
    rating: float = Field(..., alias="Rating")

users = [
    User(name="athi", age=25, is_alive=True)
]

movies = []

with open("./movies.csv", mode='r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        movie = Movie(**row)
        movies.append(movie)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users():
    return users

@app.get("/movies")
def get_movies():
    return movies;