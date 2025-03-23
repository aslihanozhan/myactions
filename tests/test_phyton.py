# tests/test_math.py
def test_addition():
    assert 1 + 1 == 2

def test_exception():
    try:
        raise ValueError("Sample error")
    except ValueError as e:
        assert str(e) == "Sample error"
