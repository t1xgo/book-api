from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from app.models import Book

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True

class BookUpdateSchema(BookSchema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    read = fields.Bool()
