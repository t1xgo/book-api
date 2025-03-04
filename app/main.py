from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import get_db, create_tables
from app.schemas import BookCreateRequest, BookUpdateRequest, BookResponse
from app.repositories import BookRepository
from app.services import BookService

app = FastAPI(
    title="Books API",
    description="API for managing books",
    version="1.0.0",
    contact={"name": "Santiago Cano"},
    openapi_tags=[{"name": "Books", "description": "Books management"}]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()

@app.get("/books", response_model=list[BookResponse], tags=["Books"])
def get_books(db: Session = Depends(get_db)):
    service = BookService(BookRepository(db))
    return service.get_all_books()

@app.post("/books", response_model=BookResponse, tags=["Books"])
def create_book(book: BookCreateRequest, db: Session = Depends(get_db)):
    service = BookService(BookRepository(db))
    return service.create_book(book)

@app.put("/books/{book_id}", response_model=BookResponse, tags=["Books"])
def update_book(book_id: str, book: BookUpdateRequest, db: Session = Depends(get_db)):
    book_id = book_id.strip()
    service = BookService(BookRepository(db))
    updated_book = service.update_book(book_id, book)
    
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return updated_book

@app.delete("/books/{book_id}", tags=["Books"])
def delete_book(book_id: str, db: Session = Depends(get_db)):
    book_id = book_id.strip()
    service = BookService(BookRepository(db))
    if not service.get_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    
    service.delete_book(book_id)    
    return {"message": "Book deleted"}