# main file

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello World"}


books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"id": 2, "title": "Neuromancer", "author": "William Gibson", "year": 1984},
    {"id": 3, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 4, "title": "Foundation", "author": "Isaac Asimov", "year": 1951},
]

class Book(BaseModel):
    title: str
    author: str
    year: int

def find_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books")
def get_books(author: str | None = None):
    if author:
        return [book for book in books if author.lower() in book["author"].lower()]
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    return find_book(book_id)


@app.post("/books", status_code=201)
def create_book(book: Book):
    new_id = max((b["id"] for b in books), default=0) + 1
    new_book = {'id': new_id, 'title': book.title, 'author': book.author, 'year': book.year}
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def replace_book(book_id: int, book: Book):
    existing = find_book(book_id)
    existing['title'] = book.title
    existing['author'] = book.author
    existing['year'] = book.year
    return existing


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    existing = find_book(book_id)
    books.remove(existing)


# client file
from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

books = get_json(f"{BASE}/books")
# print(books)


new_book = {"title": "Snow Crash", "author": "Neal Stephenson", "year": 1992}
response = requests.post(f"{BASE}/books", json=new_book, timeout=5)
print(response.status_code, response.json())

get_json(f"{BASE}/books/99")