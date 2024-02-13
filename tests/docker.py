import requests
import time

def test_app_response():
    time.sleep(10)

    response = requests.get("http://localhost:8000/services/")
    assert response.status_code == 200

    response = requests.get("http://localhost:8000/services/{name}")
    assert response.status_code == 200