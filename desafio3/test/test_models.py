import pytest
from src.model import _placeholder_template

def test_placeholder_template():
    """Tests if the function generates correct placeholders.

    This test checks that the _placeholder_template function
     correctly creates a sequence of “?” separated by commas.

    The test uses a tuple with 3 column names and expects the function
    to return "?,?,?" as the placeholder string.

    Raises:
        AssertionError: If the function doesn't return the expected
            placeholder format.
    """
    columns = ("id", "name", "email")
    result = _placeholder_template(columns)
    assert result == "?,?,?"