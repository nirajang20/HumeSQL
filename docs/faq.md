# FAQ

**Is this production-ready?**  
HumeSQL provides guardrails and uses parameterized execution, but you should review outputs, apply least-privilege DB access, and add your own auditing/limits for production environments.

**Which databases are supported?**  
MySQL and MariaDB via `mysql-connector-python`. Other engines would require additional adapters.

**Can I disable schema caching?**  
Yes: `cache_schema=False` in Python or `--no-cache-schema` via CLI. You can also call `refresh_schema_cache()` after schema changes.

**How do I select a different Gemini model?**  
Pass `model="gemini-1.5-pro-latest"` (Python) or `--model gemini-1.5-pro-latest` (CLI). Ensure your API key has access.

**How are API keys resolved?**  
Order: `api_key` argument > `HUMESQL_AI_KEY` > `HUMANSQL_AI_KEY` (legacy) > `GEMINI_API_KEY`.
