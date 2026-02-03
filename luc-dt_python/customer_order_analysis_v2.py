from typing import List, Dict, Tuple 
from collections import Counter 

# 1. Define constants or configuration at the top
TOP_N_CUSTOMERS = 3

def calculate_total_revenue(orders: List[Dict]) -> float:
    """Calculates the sum of (quantity * price) for all orders."""
    return sum(order['quantity'] * order['price'] for order in orders)

def get_most_frequent_customers(orders: List[Dict], n: int = 3) -> List[Tuple[str, int]]:
    """Identifies the top N customers by order count"""
    customer_ids = [order['customer_id'] for order in orders]
    # Using Counter is much more 'Pythonic' and efficient than a manual dictionary loop
    return Counter(customer_ids).most_common(n)

def run_pipeline(orders: List[Dict]):
    """Main execution flow for the data processing task."""
    print("--- Starting Order Analytics Pipeline ---")

    # Transformation Step
    revenue = calculate_total_revenue(orders)
    print(f"Total Revenue: ${revenue:,.2f}")

    # Aggregation Step 
    top_customers = get_most_frequent_customers(orders, n=TOP_N_CUSTOMERS)
    print(f"Top {TOP_N_CUSTOMERS} Frequent Customers: {top_customers}")

    print("--- Pipeline Completed Successfully ---")

if __name__ == "__main__":
    # Mock data - in a real DE scenario, this would be read from an API or Database
    orders_data = [
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
    run_pipeline(orders_data)