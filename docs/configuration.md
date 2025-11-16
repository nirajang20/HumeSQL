# Configuration

## API key resolution
Order of precedence:
1. Explicit `api_key` argument
2. `HUMESQL_AI_KEY` (preferred)
3. `HUMANSQL_AI_KEY` (legacy)
4. `GEMINI_API_KEY`

Export an environment variable, e.g.:
```bash
export HUMESQL_AI_KEY="your-gemini-key"
```

## Database connection
Provide a dict:
```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "classicmodels",
    "port": 3306,
}
```

MySQL-specific notes:
- Ensure the host/port is reachable from where you run the client.
- Use a user with read permissions for the tables you need.
- `mysql-connector-python` must be installed (it is a dependency of HumeSQL).

## Model selection
- Default: `gemini-2.5-flash`
- Override: `HumeSQL(..., model="gemini-1.5-pro-latest")` or CLI `--model gemini-1.5-pro-latest`
- Make sure your API key has access to the chosen model.

## Schema caching
- Enabled by default: `cache_schema=True`
- Disable: `HumeSQL(..., cache_schema=False)` or CLI `--no-cache-schema`
- Refresh manually after schema changes: `h.refresh_schema_cache()`

## Debugging
- Set `debug=True` in `.query(...)` or pass `--debug` to the CLI.
- In debug mode, the raw AI response is included in the result for inspection.
