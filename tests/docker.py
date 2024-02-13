import requests
import time
def wait_for_service(url, timeout=30):
    start_time = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Service is up!")
                break
        except requests.ConnectionError:
            pass
        if time.time() - start_time > timeout:
            raise Exception("Timeout waiting for service")
        time.sleep(1)

# Example usage


def test_app_response():

    wait_for_service("http://localhost:8000/services/")
    response = requests.get("http://localhost:8000/services/")
    assert response.status_code == 200

    wait_for_service("http://localhost:8000/services/Diseño Web")
    response = requests.get("http://localhost:8000/services/Diseño Web")
    assert response.status_code == 200