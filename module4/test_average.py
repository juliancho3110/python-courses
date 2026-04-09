def calculate_average(values):
    """Returns the average of a list of numbers. Returns 0 if empty."""
    if not values:
        return 0
    return sum(values) / len(values)

def test_normalcase():
    assert calculate_average([4.0, 2.0]) == 3.0 #pruebas unitarias 

def test_singlevalue():
    assert calculate_average([3.5]) == 3.5

def test_emptylist():
    assert calculate_average([]) == 0

def test_allzeros():
    assert calculate_average([0, 0, 0]) == 0