from unittest.mock import MagicMock
from app.services import BookService
from app.models import Book
from app.schemas import BookCreateRequest

def test_create_book():
    mock_repo = MagicMock()
    service = BookService(mock_repo)

    book_request = BookCreateRequest(title="Test Book", author="Alan Brito", read=False)

    expected_book = Book(id="123", **book_request.model_dump())  
    mock_repo.create.return_value = expected_book

    created_book = service.create_book(book_request)

    mock_repo.create.assert_called_once()

    assert created_book.id == "123"
    assert created_book.title == "Test Book"
    assert created_book.author == "Alan Brito"
    assert created_book.read is False
    
def test_update_book():
    mock_repo = MagicMock()
    service = BookService(mock_repo)

    book_id = "123"
    book_request = BookCreateRequest(title="Updated Book", author="Alan Brito", read=True)

    expected_book = Book(id=book_id, **book_request.model_dump())
    mock_repo.update.return_value = expected_book

    updated_book = service.update_book(book_id, book_request)

    mock_repo.update.assert_called_once()

    assert updated_book.id == "123"
    assert updated_book.title == "Updated Book"
    assert updated_book.author == "Alan Brito"
    assert updated_book.read is True

def test_delete_book():
    mock_repo = MagicMock()
    service = BookService(mock_repo)

    book_id = "123"

    service.delete_book(book_id)

    mock_repo.delete.assert_called_once_with(book_id)

def test_get_all_books():
    mock_repo = MagicMock()
    service = BookService(mock_repo)

    mock_repo.get_all.return_value = []

    books = service.get_all_books()

    mock_repo.get_all.assert_called_once()

    assert books == []
