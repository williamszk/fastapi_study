from fastapi import FastAPI

app = FastAPI()

books = {
    "book_1": {"author": "Author One", "title": "Title One"},
    "book_2": {"author": "Author Two", "title": "Title Two"},
    "book_3": {"author": "Author Three", "title": "Title Three"},
    "book_4": {"author": "Author Four", "title": "Title Four"},
    "book_5": {"author": "Author Five", "title": "Title Five"},
}


@app.get("/")
async def read_all_books():
    return books


@app.get("/books/my_book")
async def read_favorite_book():
    return {"title":"My favorite book"}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    query = [books[k] for k in books.keys() if books[k]["title"] == book_title]
    if query is None:
        return None
    return query
