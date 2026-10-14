import json
import sys
from unittest.mock import Mock

import novacommerce.llm as llm

from novacommerce.cli import main
from novacommerce.schemas import LLMAnswer


def test_cli_prints_json_and_closes_client(monkeypatch, capsys):
    expected = LLMAnswer(
        answer="Please provide the refund policy.",
        needs_more_information=True
    )
    client = Mock()
    client.responses.parse.return_value = Mock(
        status="completed",
        output_parsed=expected
    )
    monkeypatch.setattr(llm, "OpenAI", Mock(return_value=client))
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "test-model")
    monkeypatch.setattr(
        sys,
        "argv",
        ["novacommerce", "Does this order qualify for a refund?"]
    )

    main()

    output = capsys.readouterr().out
    assert json.loads(output) == expected.model_dump()
    assert client.close.call_count == 1