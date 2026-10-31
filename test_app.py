
from app import add_numbers


def test_add_numbers():
    assert add_numbers(10, 20) == 30
    assert add_numbers(5, 5) == 10
    assert add_numbers(-2, 2) == 0


if __name__ == "__main__":
    test_add_numbers()
    print("All tests passed!")
