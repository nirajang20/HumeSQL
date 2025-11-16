# Prompting Tips

- Be explicit about filters: “last 5 orders from customers in Nepal”.
- Mention known entities: table/column hints help the model pick correct joins.
- State aggregations and ranges: “average order value per month in 2023”.
- Clarify sorting/limits: “order by signup_date desc limit 10”.
- Use clear units: “within the last 30 days”, “USD total”.

If results look off, tighten the prompt with table/column names you know exist.
