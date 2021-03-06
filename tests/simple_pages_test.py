"""This tests the homepage"""

def test_request_main_menu_links(client):
    """This tests the main menu links in HTML files"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data
def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data

def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_request_welcome(client):
    """This makes the welcome page"""
    response = client.get("/welcome")
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_request_page_not_found(client):
    """This makes the 404 page"""
    response = client.get("/404")
    assert response.status_code == 404
