from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")

books = []
next_book_id = 1


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


@app.get("/health")
def health_check():
    # TODO: Return a JSON object that confirms the API is running.
    pass


@app.get("/books")
def list_books():
    # TODO: Return all books.
    pass


@app.post("/books", status_code=201)
def create_book(book: BookInput):
    # TODO: Assign a unique ID, save the book, and return it.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the matching book or raise HTTPException with status 404.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Update the matching book or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the matching book or raise HTTPException with status 404.
    pass
