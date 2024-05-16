from some_code import my_func, my_other_func


def test_my_func():
    assert my_func() == 7  # should pass!


def test_my_other_func():
    assert my_other_func()[0, 0] == 1.0  # should fail!
