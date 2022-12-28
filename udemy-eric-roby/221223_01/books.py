from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

books = {
    "book_1": {"author": "Author One", "title": "Title One"},
    "book_2": {"author": "Author Two", "title": "Title Two"},
    "book_3": {"author": "Author Three", "title": "Title Three"},
    "book_4": {"author": "Author Four", "title": "Title Four"},
    "book_5": {"author": "Author Five", "title": "Title Five"},
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = books.copy()
        del new_books[skip_book]
        return new_books
    return books


# create endpoint with path parameter
@app.get("/{book_name}")
async def read_book(book_name: str):
    return books[book_name]

@app.get("/query/")
async def read_book_query_param(book_name: Optional[str] = None):
    if book_name is None:
        return books

    return books[book_name] 


@app.get("/books/my_book")
async def read_favorite_book():
    return {"title": "My favorite book"}


@app.get("/books/{book_title}")
async def read_book_2(book_title: str):
    query = [books[k] for k in books.keys() if books[k]["title"] == book_title]
    if query is None:
        return None
    return query


# use enumeration with path parameter
@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"direction": direction_name, "subject": "up"}
    if direction_name == DirectionName.south:
        return {"direction": direction_name, "subject": "down"}
    if direction_name == DirectionName.east:
        return {"direction": direction_name, "subject": "right"}
    if direction_name == DirectionName.west:
        return {"direction": direction_name, "subject": "left"}


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0
    if len(books) > 0:
        # books is a dictionary
        for book in books:
            x = int(book.split("_")[-1])
            if x > current_book_id:
                current_book_id = x + 1

    books[f"book_{current_book_id}"] = {"title": book_title, "author": book_author}

    return books[f"book_{current_book_id}"]


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book = {"title": book_title, "author": book_author}
    books[book_name] = book
    return book


@app.delete("/{book_name}")
async def delete_book(book_name):
    del books[book_name]
    return f"OK! {book_name} was deleted."

@app.delete("/query/")
async def delete_book_query_param(book_name: str):
    del books[book_name]
    return f"OK from query param! {book_name} was deleted."

