NUM_MONTHS = 12

if __name__ == "__main__":
    print("Cost savings at different levels of rent")

    net_salary = input("Enter your net salary (after tax,tithe): ")
    curr_rent = input("Enter your current rent: ")
    curr_rent_percentage = (curr_rent/net_salary) * 100
    print(f"Current Rent as a Percentage: {curr_rent_percentage:.2f}%")

    for i in range(20, 50, 5):
        cost_of_rent = 5117 * (i/100)
        savings_per_month = (curr_rent - cost_of_rent)
        total_savings = savings_per_month * NUM_MONTHS
        print(f"Rent as a Percentage: {i}%, Rent: £{cost_of_rent:.2f}, Savings per Month: £{savings_per_month:.2f}, Total Savings: £{total_savings:.2f}")
