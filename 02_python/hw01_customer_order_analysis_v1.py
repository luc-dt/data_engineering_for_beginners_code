orders = [
    {"customer_id": "C001", "product": "laptop", "quantity": 2, "price": 1200.00},
    {"customer_id": "C002", "product": "mouse", "quantity": 1, "price": 25.99},
    {"customer_id": "C001", "product": "keyboard", "quantity": 1, "price": 89.50},
    {"customer_id": "C003", "product": "monitor", "quantity": 1, "price": 299.99},
    {"customer_id": "C002", "product": "laptop", "quantity": 1, "price": 1200.00},
    {"customer_id": "C004", "product": "headphones", "quantity": 3, "price": 79.99},
    {"customer_id": "C001", "product": "webcam", "quantity": 1, "price": 45.00},
    {"customer_id": "C003", "product": "mouse", "quantity": 2, "price": 25.99},
    {"customer_id": "C002", "product": "speaker", "quantity": 1, "price": 150.00},
    {"customer_id": "C005", "product": "tablet", "quantity": 1, "price": 399.99}
]

print("Calculate the total revenue:\n")
total_revenue = 0
for order in orders:
    total_revenue += order['quantity'] * order['price']
    order['revenue'] = round(total_revenue,2)
    print(order)

print(f'\nTotal revenue is {round(total_revenue, 2)}')

print("Top 3 the most frequent customer\n")
customer_count = {}

for order in orders:
    if order['customer_id'] in customer_count:
        customer_count[order['customer_id']] += 1
    else:
        customer_count[order['customer_id']] = 1

sorted_order_customer = sorted(customer_count.items(), key=lambda item: item[1], reverse=True)
print(f"Top 3 the most frequent customer: {sorted_order_customer[: 3]}")