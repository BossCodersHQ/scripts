""" Calculate the cost savings at different levels of rent. Idea came from the 30% rule for rent. Wanted to see how much I can save if I reduce my rent. """
NUM_MONTHS = 12

if __name__ == "__main__":
    print("Cost savings at different levels of rent")

    net_salary = float(input("Enter your net salary (after tax and tithe): "))
    curr_rent = float(input("Enter the current rent amount you want to compare against: "))
    offset = float(input(
        "Enter any additional costs you expect during the move (e.g., moving costs, overlap in rent etc).\n"
        "Note: This amount will be divided by 12 to get a monthly offset: "
    ))

    monthly_offset = offset / NUM_MONTHS
    curr_rent_percentage = (curr_rent/net_salary) * 100
    print(f"Current Rent as a Percentage: {curr_rent_percentage:.2f}%")

    for i in range(15, 50, 5):
        cost_of_rent = net_salary * (i/100)
        savings_per_month = (curr_rent - cost_of_rent) - monthly_offset
        total_savings = savings_per_month * NUM_MONTHS
        print(f"Rent as a Percentage of Net Salary: {i}%, Rent: £{cost_of_rent:.2f}, Savings per Month: £{savings_per_month:.2f}, Total Savings per year: £{total_savings:.2f}")
