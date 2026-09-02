# Function to calculate the total for a single item type
def calculate_item_total(price, quantity):
    total = price * quantity
    return total

# Function to calculate sales tax
def calculate_tax(subtotal, tax_rate):
    tax_amount = subtotal * tax_rate
    return tax_amount

# Function to generate and print the full bill
def print_receipt(customer_name, items_list, tax_rate=0.08):
    print("\n" + "="*40)
    print(f"      ART SUPPLY SHOP - INVOICE")
    print("="*40)
    print(f"Customer: {customer_name}")
    print("-"*40)
    print(f"{'Item':<18}{'Qty':<6}{'Price':<8}{'Total':<8}")
    print("-"*40)
    
    subtotal = 0
    
    # Loop through items, call calculation function, and print rows
    for item in items_list:
        name = item["name"]
        price = item["price"]
        qty = item["quantity"]
        
        # Function Call with Arguments and Returned Value
        item_total = calculate_item_total(price, qty)
        subtotal += item_total
        
        print(f"{name:<18}{qty:<6}${price:<7.2f}${item_total:<7.2f}")
        
    # Function Call to calculate tax
    tax = calculate_tax(subtotal, tax_rate)
    grand_total = subtotal + tax
    
    print("-"*40)
    print(f"{'Subtotal:':<32}${subtotal:.2f}")
    print(f"{'Tax (' + str(tax_rate*100) + '%):':<32}${tax:.2f}")
    print("="*40)
    print(f"{'GRAND TOTAL:':<32}${grand_total:.2f}")
    print("="*40)
    print("        Thank you for your order!\n")

# --- MAIN PROGRAM EXECUTION ---

# 1. Define customer data
customer = "Alice Smith"

# 2. Define the shopping cart list of dictionaries
cart = [
    {"name": "Sketchbook A4", "price": 12.50, "quantity": 2},
    {"name": "Acrylic Paint Set", "price": 24.99, "quantity": 1},
    {"name": "Paintbrushes (Pack)", "price": 8.75, "quantity": 3},
    {"name": "Graphite Pencils", "price": 5.20, "quantity": 2}
]

# 3. Call the main function to write the full bill
print_receipt(customer, cart, tax_rate=0.08)

