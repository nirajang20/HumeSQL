# Python API

## HumeSQL
```python
HumeSQL(
    db_config: dict,
    model: str = "gemini-2.5-flash",
    api_key: str | None = None,
    cache_schema: bool = True,
)
```

### Methods
`query(user_text: str, debug: bool = False) -> dict`
- Returns a dict with keys: `ok`, `error`, `sql`, `reasoning`, `limit_applied`, `rows`, `time_ms`, and `raw_ai_response` when `debug=True`.
- Applies guardrails: blocks dangerous SQL, adds `LIMIT 100` when missing on SELECT, rejects non-JSON AI output.

`refresh_schema_cache() -> None`
- Forces a reload of the database schema even when caching is enabled.

### Result shape
```json
{
  "ok": true,
  "error": null,
  "sql": "SELECT ...",
  "reasoning": "short explanation",
  "limit_applied": true,
  "rows": [ {"col": "val"} ],
  "time_ms": 123.45,
  "raw_ai_response": "..."   // present only with debug=True
}
```

### Example
```python
from humesql import HumeSQL

db = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "classicmodels",
    "port": 3306,
}

h = HumeSQL(db, model="gemini-2.5-flash")
res = h.query("top 5 customers from Nepal", debug=True)

if res["ok"]:
    print(res["sql"])
    print(res["rows"])
else:
    print("Error:", res["error"])
```
