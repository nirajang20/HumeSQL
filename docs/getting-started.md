# Getting Started

## Requirements
- Python 3.9+
- MySQL/MariaDB reachable from your environment
- Gemini API key with access to your desired model

## Installation
PyPI:
```bash
pip install humesql
```

From source (editable):
```bash
pip install -e .
```

## Configure credentials
### AI key order
1. Explicit `api_key` argument  
2. `HUMESQL_AI_KEY` (preferred)  
3. `HUMANSQL_AI_KEY` (legacy)  
4. `GEMINI_API_KEY`

Set an environment variable:
```bash
export HUMESQL_AI_KEY="your-gemini-key"
```

### Database config
Pass a dict to the client:
```python
db = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "classicmodels",
    "port": 3306,
}
```

## First query (Python)
```python
from humesql import HumeSQL

h = HumeSQL(db_config=db, model="gemini-2.5-flash")
res = h.query("show me the last 5 users from Nepal", debug=True)
print(res)
```

## First query (CLI)
```bash
humesql "last 5 customers from Nepal" \
  -H localhost -u root -p "" -d classicmodels --port 3306 \
  --api-key "$HUMESQL_AI_KEY" --model gemini-2.5-flash --debug
```

Exit code `0` on success, `1` on errors.
