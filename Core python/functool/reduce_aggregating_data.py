from functools import reduce

transactions = [
    {'category': 'Food', 'amount': 15.75},
    {'category': 'Books', 'amount': 25.50},
    {'category': 'Food', 'amount': 45.00},
    {'category': 'Clothing', 'amount': 100.00},
    {'category': 'Books', 'amount': 10.00},
    {'category': 'Food', 'amount': 5.25}
]

def aggregate_amount(acc, transactions):
    amount = transactions['amount']
    category = transactions['category']

    if category in acc:
        acc[category] += amount
    else:
        acc[category] = amount
    
    return acc

category_total = reduce(aggregate_amount, transactions, {})
print(category_total)