def add_numbers(a, b):
    """A simple function to test coverage."""
    return a + b

def test_add_numbers():
    assert add_numbers(1, 2) == 3

# 🚨 UNTESTED LOGIC BELOW
# This will lower your coverage percentage because these lines are never called.
def complex_business_logic(x):
    if x > 100:
        return "Large"
    elif x > 50:
        return "Medium"
    else:
        for i in range(x):
            print(f"Counting {i}")
        return "Small"