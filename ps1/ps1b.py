# Problem Set 1 - Part B: Saving, with a raise

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_rise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
r = 0.04
current_savings = 0
months = 0

down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    current_savings = current_savings + current_savings * r / 12
    current_savings = current_savings + annual_salary / 12 * portion_saved
    months = months + 1
    if months % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_rise)

print("Number of months:", months)