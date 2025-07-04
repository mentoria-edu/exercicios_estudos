import pytest
from src.validator import infinite_try, confirm_data

CONTACT_TEST = ("contact_test", "11999999999", "email@email.com")

def test_infinite_try_success_after_failures(mocker):
    mock_function = mocker.Mock()
    mock_function.side_effect = [ValueError("Message error"), "Success"]
    
    decorated_function = infinite_try(mock_function)
    result = decorated_function("teste")
    
    assert result == "Success"
    assert mock_function.call_count == 2


@pytest.mark.parametrize(
    "data, input_value, output_value",
    [
     (CONTACT_TEST, "", CONTACT_TEST),
     (CONTACT_TEST, "y", CONTACT_TEST),
     (CONTACT_TEST, "n", None),
    ]
)
def test_confirm_data(data, input_value, output_value):
    result_data = confirm_data(data, input_value)

    assert result_data == output_value