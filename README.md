# goodplace

goodplace is a small retrieval-augmented generation (RAG) project built around Ollama. It ingests a local text file, splits it into chunks, embeds those chunks, stores them in an in-memory vector store, and uses the retrieved context to answer questions.

## What it does

- Loads source text from `data/data.txt`
- Chunks the text into 300-character segments
- Generates embeddings with `nomic-embed-text`
- Retrieves the top 3 matching chunks for a query
- Generates answers with `llama3`
- Exposes both an interactive CLI and a small Flask API

## Requirements

- Python 3.13+
- `uv`
- Ollama running locally
- The following Ollama models pulled locally:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

## Install

If `uv` is not installed yet, follow the instructions at https://docs.astral.sh/uv/.

Then install the project dependencies:

```bash
uv python install 3.13
uv python pin 3.13
uv sync
```

## Run the CLI

The CLI entry point is `main.py`. It ingests `data/data.txt` on startup and then opens an interactive prompt.

```bash
uv run python main.py
```

Example session:

```text
Ask a question: What is this document about?

Answer:
: ...model response...
```

Use `Ctrl+C` to exit.

## Run ingestion only

If you only want to build the in-memory vector store from the default data file, run:

```bash
uv run python -m scripts.ingest
```

This executes `scripts/ingest.py` and prints `Ingestion complete.` when finished.

## Run the API

The Flask API is defined in `app/api.py`.

```bash
uv run python -m app.api
```

The server listens on port `5000` and exposes:

- `POST /ship`

Request body:

```json
{
	"context": "Tell me about the source text"
}
```

The handler validates the payload, forwards `context` to the talking service, and returns a JSON response.

## Run tests

```bash
uv run pytest
```

Current tests cover the generator prompt assembly and the talking service behavior in `tests/test_generator.py` and `tests/services/test_talking_service.py`.

## Project layout

```text
app/
	api.py            Flask API
	chunker.py        Text chunking logic
	embeddings.py     Ollama embedding calls
	generator.py      Ollama answer generation
	rag_pipeline.py   Ingest + retrieve + generate orchestration
	retriever.py      Top-k retrieval
	vector_store.py   In-memory cosine similarity search
data/
	data.txt          Default source document
scripts/
	ingest.py         Standalone ingestion script
tests/
	...               Unit tests
```

## Notes

- The vector store is in memory, so data is rebuilt on each process start.
- The current `pyproject.toml` does not register console scripts, so use the `uv run python ...` commands above rather than `uv run rag` or `uv run ingest`.