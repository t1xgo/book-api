from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, create_tables
from app.schemas import BookSchema
from app.repositories import BookRepository
from app.services import BookService

app = FastAPI(
    title="Books API",
    description="API for managing books",
    version="1.0.0",
    contact={
        "name": "Santiago Cano",
    },
    openapi_tags=[
        {"name": "Books", "description": "Books management"},
    ]
)

create_tables()
book_schema = BookSchema()
books_schema = BookSchema(many=True)

@app.get("/books", tags=["Books"])
def get_books(db: Session = Depends(get_db)):
    repository = BookRepository(db)
    service = BookService(repository)
    books = service.get_all_books()
    return books_schema.dump(books)

@app.post("/books", tags=["Books"])
def create_book(book: dict, db: Session = Depends(get_db)):
    repository = BookRepository(db)
    service = BookService(repository)
    new_book = service.create_book(book_schema.load(book))
    return book_schema.dump(new_book)

@app.put("/books/{book_id}", tags=["Books"])
def update_book(book_id: str, book: dict, db: Session = Depends(get_db)):
    repository = BookRepository(db)
    service = BookService(repository)
    updated_book = service.update_book(book_id, book_schema.load(book, partial=True))
    
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book_schema.dump(updated_book)

@app.delete("/books/{book_id}", tags=["Books"])
def delete_book(book_id: str, db: Session = Depends(get_db)):
    repository = BookRepository(db)
    service = BookService(repository)
    if not service.delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    
    return {"message": "Book deleted"}
