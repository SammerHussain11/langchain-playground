# Structured Output with LangChain

This module demonstrates how to extract consistent, schema-validated JSON from natural language reviews using `with_structured_output(...)` in LangChain.

It includes four approaches:

- Raw JSON Schema
- Pydantic model schema
- Python `TypedDict` schema
- Hugging Face chat model + structured output

## Files

- `structured-output/with_structured_output_json.py`
- `structured-output/with_structured_output_pydantic.py`
- `structured-output/with_structured_output_typeddict.py`
- `structured-output/with_structured_output_llama.py`

## What These Examples Do

Each script:

1. Defines a schema for a product-review extraction task
2. Wraps an LLM with `with_structured_output(...)`
3. Invokes the model on the same sample Samsung Galaxy S24 Ultra review
4. Prints structured output containing fields like themes, summary, sentiment, pros, cons, and reviewer name

## Prerequisites

- Python 3.10+
- A virtual environment
- API access for at least one provider:
  - OpenAI (for JSON, Pydantic, and TypedDict examples)
  - Hugging Face Inference (for Llama/TinyLlama example)

## Install

From repository root:

```bash
pip install langchain langchain-openai langchain-huggingface pydantic python-dotenv
```

If you use a local `requirements.txt`, make sure the packages above are included.

## Environment Variables

Create or update `.env` in the repository root:

```env
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

Notes:

- `OPENAI_API_KEY` is required for:
  - `with_structured_output_json.py`
  - `with_structured_output_pydantic.py`
  - `with_structured_output_typeddict.py`
- `HUGGINGFACEHUB_API_TOKEN` is required for:
  - `with_structured_output_llama.py`

## Run Examples

From repository root:

```bash
python structured-output/with_structured_output_json.py
python structured-output/with_structured_output_pydantic.py
python structured-output/with_structured_output_typeddict.py
python structured-output/with_structured_output_llama.py
```

## Comparison Guide

- `with_structured_output_json.py`
  - Best when you need explicit JSON Schema control or external schema compatibility.
- `with_structured_output_pydantic.py`
  - Best developer ergonomics, validation, and type-safe Python objects.
- `with_structured_output_typeddict.py`
  - Lightweight typing with minimal runtime model overhead.
- `with_structured_output_llama.py`
  - Demonstrates provider flexibility using a Hugging Face model backend.

## Current Schema Shape

All examples target a review extraction object with:

- `key_themes` (list of strings, required)
- `summary` (string, required)
- `sentiment` (restricted label)
- `pros` (optional list)
- `cons` (optional list)
- `name` (optional string)

## Troubleshooting

- Authentication errors:
  - Verify `.env` keys and confirm `load_dotenv()` can read the file.
- Import errors:
  - Reinstall dependencies in the active virtual environment.
- Model response validation failures:
  - Tighten field descriptions or simplify enum labels.
- Hugging Face latency/timeouts:
  - Try a smaller prompt or a more reliable hosted model.

## Suggested Improvements

- Normalize sentiment labels (`pos`/`neg` vs `positive`/`negative`) across all files.
- Add a shared schema module to avoid drift between examples.
- Add a small test suite that validates output keys and value types.
