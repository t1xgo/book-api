from app.models import Book
from app.repositories import BookRepository
from app.schemas import BookCreateRequest, BookUpdateRequest

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_all_books(self):
        return self.repository.get_all()

    def get_book(self, book_id: str):
        return self.repository.get_by_id(book_id)

    def create_book(self, data: BookCreateRequest):
        new_book = Book(**data.model_dump())
        return self.repository.create(new_book)

    def update_book(self, book_id: str, data: BookUpdateRequest):
        existing_book = self.repository.get_by_id(book_id)
        if not existing_book:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(existing_book, key, value)

        return self.repository.update(existing_book)

    def delete_book(self, book_id: str):
        return self.repository.delete(book_id)
