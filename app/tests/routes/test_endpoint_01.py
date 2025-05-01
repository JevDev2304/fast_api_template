from fastapi.testclient import TestClient
from api.main import app
from database.models.item import Item



client = TestClient(app)

class TestGetItems:
    def test_get_items(self) -> None:
        #Arrange None
        #Act
        response = client.get("/endpoint_01/")
        #Assert
        assert response.status_code ==200
        assert isinstance(response.json(),list)

class TestCreateItem:
    def test_create_item(self) -> None:
        #Arrange
        item_data: dict = {
            "id":1,
            "name": "New Item",
            "description": "A description for the new item"
        }
        #Act
        response = client.post("/endpoint_01/",json=item_data)
        response_data = response.json()
        #Assert
        assert response.status_code == 201
        for key,value in item_data.items():
            assert key in response_data
            assert response_data[key] == value

    def test_create_item_invalid_data(self) -> None:
        #Arrange
        item_data: dict = {
            "id":1
        }
        #Act
        response = client.post("/endpoint_01/",json=item_data)
        #Assert
        assert response.status_code == 422

    def test_create_item_without_body(self) -> None:
        #Arrange None
        #Act
        response = client.post("/endpoint_01/")
        #Assert
        assert response.status_code == 422
    def test_create_item_bad_body_types(self) -> None:
        #Arrange
        item_data: dict = {
            "id":"Hola",
            "name": 3,
            "description": ""
        }
        #Act
        response = client.post("/endpoint_01/", json=item_data)
        #Assert
        assert response.status_code == 422




