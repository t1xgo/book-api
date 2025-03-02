import uuid
from app.models import Book
from app.repositories import BookRepository
from app.schemas import BookSchema

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository
        self.schema = BookSchema()

    def get_all_books(self):
        return self.repository.get_all()

    def get_book(self, book_id: str):
        return self.repository.get_by_id(book_id)

    def create_book(self, data: dict):
        validated_data = self.schema.load(data)
        validated_data.id = str(uuid.uuid4())
        return self.repository.create(validated_data)

    def update_book(self, book_id: str, data: dict):
        validated_data = self.schema.load(data, partial=True)
        return self.repository.update(book_id, validated_data.title, validated_data.author, validated_data.read)

    def delete_book(self, book_id: str):
        return self.repository.delete(book_id)
