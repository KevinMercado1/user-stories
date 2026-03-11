def calculate_total_sales(sales_data):
    
    grand_total = sum(item['subtotal'] for item in sales_data.values())
    return grand_total