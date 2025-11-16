# HumeSQL

HumeSQL converts natural language into safe SQL, executes it against your MySQL/MariaDB database, and returns JSON rows. It introspects your schema, prompts Gemini to craft SQL, applies guardrails, executes, and responds with the SQL, reasoning, and results.

## Why HumeSQL?
- Ask questions in plain English; get SQL and JSON back.
- Safe by default: blocks destructive SQL, limits large queries, only touches your schema.
- Works with MySQL/MariaDB using `mysql-connector-python`.
- Python API and CLI with schema caching and debug output.

## Quick start
```bash
pip install humesql
export HUMESQL_AI_KEY="your-gemini-key"
```

```python
from humesql import HumeSQL

db = {"host":"localhost","user":"root","password":"","database":"classicmodels","port":3306}
h = HumeSQL(db, model="gemini-2.5-flash")
print(h.query("last 5 customers from Nepal", debug=True))
```

Continue to [Getting Started](getting-started.md) for setup details.
