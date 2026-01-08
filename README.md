# MCP × LangChain × Mistral — Known Integration Failure

This repository exists **solely to reproduce and document a known failing integration**
between:

- LangChain agents
- MCP tools (via `langchain-mcp-adapters`)
- Mistral models

The failure occurs during **`agent.ainvoke()`** when using MCP-provided tools.

---

## Purpose

- Provide a **minimal, reproducible integration test**
- Keep CI green while the bug exists
- Serve as a **regression guard** once the issue is fixed

The test is intentionally marked as **`xfail(strict=True)`**.

---

## Test Overview

- Async integration test
- Uses a local MCP time server (`mcp-server-time`)
- Creates a LangChain agent with MCP tools
- Fails at `agent.ainvoke(...)`

Location:

```path
tests/integration/test_mcp_mistral_agent_known_failure.py
```

---

## Requirements

- Python 3.10+
- [`uv`](https://github.com/astral-sh/uv)
- Mistral API credentials
- MCP tooling available on PATH

### Environment

Create a `.env` file:

```env
MISTRAL_API_KEY=your_key_here
```

---

## Setup

Install dependencies:

```bash
uv sync
```

---

## Running the Test

```bash
uv run pytest tests/integration -v
```

Expected result:

- ✅ Test suite passes
- ⚠️ Test is reported as **XFAIL (expected failure)**

Example:

```error
XFAIL tests/integration/test_mcp_mistral_agent_known_failure.py
```

---

## Notes

- This is **not** a unit test.
- This test intentionally depends on:

  - `uvx`
  - `mcp-server-time`
  - live Mistral API access

- Do **not** remove `xfail` until the underlying issue is resolved.

When the test unexpectedly passes, `strict=True` will cause CI to fail,
signaling that the bug may have been fixed.

---

## Next Steps

- Capture and pin the exact exception signature
- Remove `xfail` once the integration works
- Convert into a passing regression test
