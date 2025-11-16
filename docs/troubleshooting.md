# Troubleshooting

- **API key not valid**  
  Confirm `HUMESQL_AI_KEY` (or `--api-key`) and ensure the key has access to your chosen Gemini model.

- **Model not found (404)**  
  Use a supported model, e.g., `--model gemini-2.5-flash`.

- **Database connection errors**  
  Check host/port/user/password and make sure MySQL/MariaDB is reachable.

- **Malformed JSON from model**  
  Rerun with `debug=True` (or `--debug`) to see `raw_ai_response`. The JSON sanitizer helps, but non-JSON output will be rejected.

- **Schema changes not reflected**  
  Call `refresh_schema_cache()` or disable schema caching with `cache_schema=False` / `--no-cache-schema`.
