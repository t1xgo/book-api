from pydantic import BaseModel

class BookCreateRequest(BaseModel):
    title: str
    author: str
    read: bool = False

class BookUpdateRequest(BaseModel):
    title: str | None = None
    author: str | None = None
    read: bool | None = None

class BookResponse(BaseModel):
    id: str
    title: str
    author: str
    read: bool
