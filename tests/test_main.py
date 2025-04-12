from src.main import my_func
import pytest
import pytest_cov

@pytest.mark.parametrize('value1, value2, expected', [
    ([1, "Маша", 3.9, [], {}, 4, 5], int, 3),
    ([1, "Маша", 3.9, [], {}, 4, 5], str, 1),
    ([1, "Маша", 3.9, [], {}, 4, 5], float, 1)
])
def test_my_func(value1, value2, expected):
    assert my_func(value1, value2) == expected

# def test_my_func():
#     assert my_func([1, "Маша", 3.9, [], {}, 4, 5], int) == 3
#     assert my_func([1, "Маша", 3.9, [], {}, 4, 5], str) == 1
#     assert my_func([1, "Маша", 3.9, [], {}, 4, 5], float) == 1
#     assert my_func([1, "Маша", 3.9, [], {}, 4, 5], list) == 1
