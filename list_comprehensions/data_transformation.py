#!/usr/bin/python3

sales_data = [
    {"product": "laptop", "price": 999, "quantity": 2, "category": "electronics"},
    {"product": "book", "price": 15, "quantity": 5, "category": "education"},
    {"product": "phone", "price": 699, "quantity": 1, "category": "electronics"},
]

# 1. Get list of all product names
print([p["product"] for p in sales_data])

# 2. Calculate total revenue for each item (price * quantity)
print(sum(p["price"] * p["quantity"] for p in sales_data))

# 3. Filter electronics over $500
print([over for over in sales_data if over["category"] == "electronics" and over["price"] > 500])

# 4. Create price ranges: "cheap" (<50), "medium" (50-500), "expensive" (>500)
cheap = [c for c in sales_data if c["price"] < 50]
medium = [m for m in sales_data if m["price"] >= 50 and m["price"] <= 500]
expensive = [e for e in sales_data if e["price"] > 500]
