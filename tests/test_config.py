import pytest

from novacommerce.config import load_settings


def test_settings_load_without_exposing_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "test-model")

    settings = load_settings()

    assert settings.api_key == "test-key"
    assert settings.model == "test-model"
    assert "test-key" not in repr(settings)


def test_missing_api_key_is_rejected(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setenv("OPENAI_MODEL", "test-model")

    with pytest.raises(ValueError, match="OPENAI_API_KEY is missing"):
        load_settings()


def test_missing_model_is_rejected(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    with pytest.raises(ValueError, match="OPENAI_MODEL is missing"):
        load_settings()