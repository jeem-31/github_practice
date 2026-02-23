# test_app.py
from app import greet

def test_greet():
    # This checks if our function actually returns what we expect
    assert greet("Future Coder") == "Hello, Future Coder! You've just updated your code."