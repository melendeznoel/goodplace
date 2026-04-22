# goodplace RAG with Ollama

## install uv

irm https://astral.sh/uv/install.ps1 | iex

uv --version

## install python

uv python install 3.13

uv python pin 3.13

uv sync

## Setup
ollama pull llama3
ollama pull nomic-embed-text

## Run
uv run python main.py

uv run pytest

uv run rag

uv run ingest