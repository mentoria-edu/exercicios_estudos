import pytest
from src.menu import  _choose_field_to_search, select_search_contact, menu_loop, unique_choose_loop

QUIT_OPTION = 'q'
KEEP_LOOP = 'keep'


def test_choose_field_to_search_invalid_options(monkeypatch, caplog):
    input_value= ['x', 'banana', '8', '3']

    monkeypatch.setattr("builtins.input", lambda _: input_value.pop(0))

    with caplog.at_level('WARNING'):
        _choose_field_to_search()
        
        assert caplog.text.count("Invalid option") == 3


@pytest.mark.parametrize("input_field, expected_field, search_input, expected_value", [
    ('1', 'name', 'Rodrigo', 'Rodrigo'),
    ('2', 'phone', '123456789', '123456789'),
    ('3', 'email', 'test@example.com', 'test@example.com'),    
])
def test_select_search_contact_expected_value(monkeypatch, input_field, expected_field, search_input, expected_value):
    inputs = [input_field, search_input]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))

    field, value = select_search_contact()

    assert field == expected_field
    assert value == expected_value


def test_menu_loop_breaks(monkeypatch):
    menu_iterations = 0

    def mock_input(prompt):

        nonlocal menu_iterations

        menu_iterations += 1

        if menu_iterations == 3:
            return QUIT_OPTION

        return '1'
    
    monkeypatch.setattr('builtins.input', mock_input)

    @menu_loop()
    def mock_function(choice):
        return 'continue'
    
    mock_function()
        
    assert menu_iterations == 3
 