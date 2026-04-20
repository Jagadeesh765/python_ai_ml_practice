#RAISE PROPER EXCEPTIONS WHEN INVALID ID IS PASSED
from fastapi import FastAPI,HTTPException
app = FastAPI()
books={
    1:"Python",
    2:"FASTAPI"
}
@app.get("/books/{book_id}")
def get_books(book_id:int):
    if book_id not in books:
        raise HTTPException(status_code=404,detail="book not found")
    return {"book":books[book_id]}
#######ALL ERROR MESSAGES
from fastapi import FastAPI, HTTPException, status, Form, Header, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Sample data
books = {1: "Python", 2: "FastAPI"}

# Reusable error
def not_found():
    return HTTPException(status_code=404, detail="Item not found")

# Custom exception
class NegativeNumberException(Exception):
    pass

# Custom handler
@app.exception_handler(NegativeNumberException)
async def handler(request: Request, exc: NegativeNumberException):
    return JSONResponse(
        status_code=400,
        content={"message": "Negative ID is not allowed"}
    )

# Get book
@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id < 0:
        raise NegativeNumberException()
    if book_id not in books:
        raise not_found()
    return {"book": books[book_id]}

# Create book
@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: str = Form(...)):
    new_id = len(books) + 1
    books[new_id] = book
    return {"id": new_id, "book": book}

# Secure API
@app.get("/secure-data")
def secure(token: str = Header(None)):
    if token != "secret123":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "Access granted"}