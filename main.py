from calculate import calculate_total_sales
from user_stories import generate_final_report, sales_report 

if __name__ == "__main__":
    all_sales_data = sales_report()

    if all_sales_data:
        generate_final_report(all_sales_data)
    else:
        print("No sales data entered.")