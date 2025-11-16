# CLI

HumeSQL ships a `humesql` command for quick, one-off natural language queries.

## Basic example
```bash
humesql "last 5 customers from Nepal" \
  -H localhost -u root -p "" -d classicmodels --port 3306 \
  --api-key "$HUMESQL_AI_KEY" --model gemini-2.5-flash --debug
```

## Arguments
- `query` (positional): natural language prompt.
- `-H, --host`: database host (required).
- `-u, --user`: database user (required).
- `-p, --password`: database password (default: empty).
- `-d, --database`: database name (required).
- `--port`: database port (default: 3306).
- `--api-key`: Gemini API key; overrides env vars.
- `--model`: Gemini model (default: `gemini-2.5-flash`).
- `--no-cache-schema`: disable schema caching.
- `--debug`: include the raw AI response in JSON output.

Exit code `0` on success, `1` on error.

## Output
Printed as JSON and matches the Python API shape. On errors, `ok` is `false` and `error` contains details.
