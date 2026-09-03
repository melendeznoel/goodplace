"""Unit tests for generator helpers."""

from app.generator import generate
from app.config import LLM_MODEL


class TestGenerate:
    def test_generate_builds_prompt_and_returns_model_response(self, monkeypatch):
        captured = {}

        def fake_chat(*, model, messages):
            captured["model"] = model
            captured["messages"] = messages
            return {"message": {"content": "Mocked answer"}}

        monkeypatch.setattr("app.generator.ollama.chat", fake_chat)

        result = generate("What is the summary?", ["First chunk", "Second chunk"])

        assert result == "Mocked answer"
        assert captured["model"] == LLM_MODEL
        assert len(captured["messages"]) == 1
        assert captured["messages"][0]["role"] == "user"
        assert "First chunk\n\nSecond chunk" in captured["messages"][0]["content"]
        assert "What is the summary?" in captured["messages"][0]["content"]
