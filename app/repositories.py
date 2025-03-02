from sqlalchemy.orm import Session
from app.models import Book

class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Book).all()

    def get_by_id(self, book_id: str):
        return self.db.query(Book).filter(Book.id == book_id).first()

    def create(self, book: Book):
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book
    
    def update(self, book: Book):
        self.db.merge(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def delete(self, book_id: str):
        book = self.get_by_id(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
