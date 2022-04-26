"""This tests the homepage"""

def test_homepage(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
