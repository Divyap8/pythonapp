import requests

def test_root():
    """Test the root endpoint."""
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200
    assert 'Hello from Flask & Docker' in response.text

def test_hi():
    """Test the /hi endpoint."""
    response = requests.get('http://localhost:5000/hi')
    assert response.status_code == 200
    assert 'Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii from Flask & Docker' in response.text

if __name__ == "__main__":
    test_root()
    test_hi()
    print("All tests passed!")
