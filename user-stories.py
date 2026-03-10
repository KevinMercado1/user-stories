def sales_report():

    sales_data = {}
    keep_going = True

    while keep_going:
        print("\n--- Sales Report ---")
        product_name = input("Enter product name (or 'done' to finish): ")

        try:
            quantity_sold = int(input(f"Enter quantity of {product_name} sold: "))
            price_per_unit = float(input(f"Enter price per unit of {product_name}: "))

            if product_name in sales_data:
                sales_data[product_name]['quantity'] += quantity_sold
                sales_data[product_name]['subtotal'] += (quantity_sold * price_per_unit)

            else:
                sales_data[product_name] = {
                    'quantity': quantity_sold,
                    'subtotal': quantity_sold * price_per_unit
                }

        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.")
            continue

        choice = input("Do you want to add another product? (yes/no): ").lower()
        if choice != 'yes':
            keep_going = False

    return sales_data

def calculate_total_sales(sales_data):
    grand_total = sum(item['subtotal'] for item in sales_data.values())
    return grand_total

def generate_final_report(sales_data):
    print("========================================")
    print("       DAILY SALES SUMMARY              ")
    print("========================================")
    
    for product, data in sales_data.items():
        print(f"{product}: Quantity Sold: {data['quantity']}, Subtotal: ${data['subtotal']:.2f}")
    total_sales = calculate_total_sales(sales_data)
    print(f"\nTotal Sales: ${total_sales:.2f}")

    print("========================================")

def main():

    all_sales_data = sales_report()
    
    if not all_sales_data:
        print("No sales data entered.")
        return
    
    total = calculate_total_sales(all_sales_data)

    generate_final_report(all_sales_data)

if __name__ == "__main__":
    main()