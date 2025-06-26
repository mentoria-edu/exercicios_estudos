import pytest
from src.menu import get_field_search, get_search_contact, menu_loop


def test_menu_loop_breaks():
    menu_iterations = 0
    
    @menu_loop
    def mock_function():

        nonlocal menu_iterations

        menu_iterations += 1

        if menu_iterations == 3:
            return '9'
        
        return 'continue'
    
    result = mock_function()

    assert result == '9'
    assert menu_iterations == 3


@pytest.mark.parametrize("input_value, expected", [
    ('1', 'name'),
    ('2', 'phone'),
    ('3', 'email'),
])
def test_get_field_searches_expected_output(monkeypatch, input_value, expected):
    monkeypatch.setattr("builtins.input", lambda _: input_value)

    result = get_field_search()

    assert result == expected


def test_get_field_searches_invalid_options(monkeypatch, caplog):
    input_value= ['x', 'banana', '8', '3']

    monkeypatch.setattr("builtins.input", lambda _: input_value.pop(0))

    with caplog.at_level('WARNING'):
        get_field_search()
        
        assert caplog.text.count("Invalid option") == 3


def test_get_search_contact_value_no_space(monkeypatch):
    inputs = ['1', '  Rodrigo  ']

    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    field, value = get_search_contact()

    assert field == 'name'
    assert value == 'Rodrigo'
 