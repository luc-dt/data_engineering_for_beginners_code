# let's create a function to create an age_bucket for our customer data
customer_data = [
    {'name': 'customer_1', 'id': 1, 'age': 100},
    {'name': 'customer_2', 'id': 2, 'age': 42},
    {'name': 'customer_3', 'id': 3, 'age': 25},
    {'name': 'customer_4', 'id': 4, 'age': 19},
]

def get_age_bucket(customer):
    customer_age = customer['age']
    if customer_age > 85:
        return '85+'
    elif customer_age > 50:
        return '50_85'
    elif customer_age > 30:
        return '30_50'
    else:
        return '0_30'

for customer in customer_data:
    print(customer['age'], get_age_bucket(customer))