# Grocery queue: Each customer has a name and a cart of items with quantities
billing_queue = [
    {
        "name": "Alice", 
        "cart": [{"item": "apple", "price": 2.0, "qty": 6}, {"item": "milk", "price": 3.5, "qty": 1}]
    },
    {
        "name": "Bob", 
        "cart": [{"item": "bread", "price": 2.5, "qty": 2}]
    }
]

# Outer Loop: Process each customer in the queue
for customer in billing_queue:
    print(f"Billing for {customer['name']}:")
    total_bill = 0
    
    # Inner Loop: Process each item in the current customer's cart
    for item in customer['cart']:
        item_total = item['price'] * item['qty']
        
        # Nested IF: Apply bulk discount if they buy more than 5 of an item
        if item['qty'] > 5:
            item_total *= 0.90  # 10% off
            print(f"  - {item['item']}: Buy 5+ deal applied!")
        elif item['item'] == "milk":
            item_total -= 0.50  # Flat discount on milk
            print(f"  - {item['item']}: Dairy coupon applied!")
            
        total_bill += item_total
        print(f"    {item['qty']}x {item['item']} = ${item_total:.2f}")
        
    print(f"Total Bill for {customer['name']}: ${total_bill:.2f}\n")


