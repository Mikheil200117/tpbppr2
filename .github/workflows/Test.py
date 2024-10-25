def test_addition():
    assert 2 + 2 == 4
    
def test_even_number():
    assert is_even(4) == True

def test_odd_number():
    assert is_even(3) == False

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
        
def test_even_number():
    assert is_even(4) == True

def test_odd_number():
    assert is_even(3) == False

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
#1
#2
