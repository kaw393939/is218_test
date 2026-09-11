"""Test suite for the add() function.

Demonstrates comprehensive testing practices:
- Basic functionality testing
- Edge case testing (zero values)
- Negative number handling
"""

from app import add


def test_add_basic():
    """Test basic addition: 2 + 3 = 5
    
    This is the fundamental test case that proves the add() function works
    for basic arithmetic operations with positive integers.
    """
    assert add(2, 3) == 5


def test_add_with_zero():
    """Test edge case: adding zero preserves the other value.
    
    This tests an important edge case: add(0, 5) should equal 5.
    Zero is a boundary value that can reveal issues in some implementations.
    """
    assert add(0, 5) == 5


def test_add_negative_numbers():
    """Test handling of negative integers: -2 + 3 = 1
    
    This tests that the function correctly handles negative numbers,
    which is essential for any arithmetic operation to be considered robust.
    """
    assert add(-2, 3) == 1
