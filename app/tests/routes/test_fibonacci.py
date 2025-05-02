from fastapi.testclient import TestClient
from api.main import app
from app.database.models.fibonacci import FibonacciRequest, FibonacciDatabaseDB



client = TestClient(app)

class TestGetItems:
    def test_get_items(self) -> None:
        #Arrange None
        #Act
        response = client.get("fibonacci_email/")
        #Assert
        assert response.status_code ==200
        assert isinstance(response.json(),list)

class TestCreateItem:
    def test_create_item(self) -> None:
        #Arrange
        item_data: dict = {
  "hour": "16:02:22.803Z",
  "email": "jevojob@gmail.com.com",
  "subject": "string"
}
        #Act
        response = client.post("/fibonacci_email/",json=item_data)
        response_data = response.json()
        #Assert
        assert response.status_code == 201

