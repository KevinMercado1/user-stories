from calculate import calculate_total_sales

def sales_report():
    sales_data = {}
    choice = 'yes'
    
    while choice == 'yes':
        product = input("Enter product name: ")
        try:
            quantity = int(input(f"Enter quantity of {product} sold: "))
            price = float(input(f"Enter price per unit of {product}: "))
            sales_data[product] = {
                'quantity': quantity,
                'subtotal': quantity * price
            }

            choice = input("Do you want to add another product? (yes/no): ").lower()
            
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.")
            continue
            
    return sales_data

def generate_final_report(sales_data):
    print("========================================")
    print("           DAILY SALES SUMMARY          ")
    print("========================================")
    
    for product, data in sales_data.items():
        print(f"{product}: Quantity Sold: {data['quantity']}, Subtotal: ${data['subtotal']:.2f}")
    
    total_sales = calculate_total_sales(sales_data)
    print(f"\nTotal Sales: ${total_sales:.2f}")
    print("========================================")