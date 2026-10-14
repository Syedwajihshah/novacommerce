import pytest
from pydantic import ValidationError
from novacommerce.schemas import LLMAnswer

def test_valid_response():
    payload = '{"answer":"Please provide the policy.","needs_more_information":true}'
    response = LLMAnswer.model_validate_json(payload)

    assert response.answer == "Please provide the policy."
    assert response.needs_more_information is True

def test_wrong_boolean_type_is_rejected():
    payload = '{"answer":"Yes.","needs_more_information":"false"}'

    with pytest.raises(ValidationError):
        LLMAnswer.model_validate_json(payload)