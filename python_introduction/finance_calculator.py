#finance calculator
#declare a variable to prompt the user for their monthly income and expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#calculate monthly savings by subtracting monthly expenses from monthly income
monthly_savings = monthly_income - monthly_expenses

#Annual savings incorperating the 5% interest rate
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print results
print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is {int(projected_savings)}.")