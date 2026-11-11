from app import add

def test_small_numbers():
    assert add(2, 3) == 5

def test_larger_numbers():
    assert add(10, 5) == 15