"""
Simple usage example for HumeSQL.

Run with:  python example.py
"""

from humesql import HumeSQL

# Your DB credentials here
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "classicmodels",
    "port": 3306,
}

# Make sure you exported HUMESQL_AI_KEY (or GEMINI_API_KEY) before running.
# For example (macOS / Linux):
#   export GEMINI_API_KEY="your-secret-key"

h = HumeSQL(db_config, model="gemini-2.5-flash")

if __name__ == "__main__":
    user_query = "Show me the customers who are up from USA"
    res = h.query(user_query, debug=True)

    if res["ok"]:
        print("✅ SQL used:")
        print(res["sql"])
        print("\n🧠 Reasoning:")
        print(res["reasoning"])
        print("\n📊 Rows:")
        for row in res["rows"]:
            print(row)
    else:
        print("❌ Error:", res["error"])
        if "raw_ai_response" in res:
            print("\nRaw AI response:", res["raw_ai_response"])
