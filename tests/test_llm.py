from unittest.mock import Mock

import pytest
import novacommerce.llm as llm

from novacommerce.config import Settings
from novacommerce.schemas import LLMAnswer


def test_generate_returns_validated_answer(monkeypatch):
    expected = LLMAnswer(
        answer="Yes.",
        needs_more_information=False
    )
    client = Mock()
    client.responses.parse.return_value = Mock(
        status="completed",
        output_parsed=expected
    )
    monkeypatch.setattr(llm, "OpenAI", Mock(return_value=client))

    provider = llm.OpenAIProvider(
        Settings(api_key="test-key", model="test-model")
    )
    result = provider.generate(
        "Use the supplied information.",
        "Does this order qualify?"
    )

    assert isinstance(result, LLMAnswer)
    assert result == expected


def test_empty_input_does_not_call_api(monkeypatch):
    client = Mock()
    monkeypatch.setattr(llm, "OpenAI", Mock(return_value=client))

    provider = llm.OpenAIProvider(
        Settings(api_key="test-key", model="test-model")
    )

    with pytest.raises(ValueError, match="Input text must not be empty"):
        provider.generate("Use the supplied information.", "   ")

    client.responses.parse.assert_not_called()