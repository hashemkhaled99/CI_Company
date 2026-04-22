from trying.good_logic import calculate_things

def test_calculate_things_success():
    assert calculate_things(7, 7) is True

def test_calculate_things_failure():
    assert calculate_things(1, 1) is False