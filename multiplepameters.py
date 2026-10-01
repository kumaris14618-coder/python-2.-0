def calculate_total(price,tax_rate,discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total:${final_price}")

calculate_total(100,0.08,10)