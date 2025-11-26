from a import sub

def test_pos():
    assert sub(10,5) == 5

def test_neg():
    assert sub(5, 10) == -5

def test_zero():
    assert sub(5,0) == 0        