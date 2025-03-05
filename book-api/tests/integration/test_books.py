def test_create_book(client):
    response = client.post("/books", json={"title": "1984", "author": "George Orwell"})
    
    assert response.status_code == 200
    data = response.json()
    
    assert "id" in data
    assert data["title"] == "1984"
    assert data["author"] == "George Orwell"
    assert data["read"] is False

def test_get_books(client):
    response = client.get("/books")
    
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) == 1
    assert data[0]["title"] == "1984"
    assert data[0]["author"] == "George Orwell"
    
def test_update_book(client):
    create_response = client.post("/books", json={"title": "The fire", "author": "Mr. Bean", "read": False})
    assert create_response.status_code == 200
    
    book_id = create_response.json()["id"]

    response = client.put(f"/books/{book_id}", json={"title": "The fire updated", "author": "Bean Bean", "read": True})
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["title"] == "The fire updated"
    assert data["author"] == "Bean Bean"
    assert data["read"] is True
    
def test_delete_book(client):
    create_response = client.post("/books", json={"title": "Tom Sawyer", "author": "Mr. Rolling Stones", "read": True})
    assert create_response.status_code == 200
    
    book_id = create_response.json()["id"]

    response = client.delete(f"/books/{book_id}")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["message"] == "Book deleted"

