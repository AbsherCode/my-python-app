"""Tests for utility functions."""

import pytest
from src.myapp.utils import add, multiply, format_name

def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    """Test multiplication function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_format_name():
    """Test name formatting function."""
    assert format_name("john", "doe") == "John Doe"
    assert format_name("JANE", "SMITH") == "Jane Smith"
