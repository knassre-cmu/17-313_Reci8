import pytest
from app.fib import fibonacci

@pytest.mark.parametrize(
    "n, answer", [
        pytest.param(0, 0, id="0"),
        pytest.param(1, 1, id="1"),
        pytest.param(2, 1, id="2"),
        pytest.param(3, 2, id="3"),
        pytest.param(4, 3, id="4"),
        pytest.param(5, 5, id="5"),
        pytest.param(6, 8, id="6"),
        pytest.param(7, 13, id="7"),
        pytest.param(8, 21, id="8"),
        pytest.param(9, 34, id="9"),
    ]
)
def test_fibonacci_valid(n, answer):
    """Verify that fibonacci returns the correct answer for certain non-negative
       integer tests"""
    assert(fibonacci(n) == answer)


@pytest.mark.parametrize(
    "n", 
    [
        pytest.param(-1, id="-1"),
        pytest.param(-24, id="-24"),
        pytest.param(None, id="none"),
        pytest.param("3", id="string"),
        pytest.param(10.0, id="float"),
    ]
)
@pytest.mark.paramtrize
def test_fibonacci_invalid(n):
    """Verify that fibonacci raises an exception when the input is negative or
       the wrong type."""
    try:
        assert(fibonacci(n))
        raise AssertionError("Should have raised an exception error")
    except ValueError as e:
        assert(str(e) == "Invalid input")