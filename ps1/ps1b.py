# Problem Set 1 - Part B: Saving, with a raise

while True:
    while True:
        try:
            annual_salary = float(input("Enter your starting annual salary: "))
            if annual_salary > 0:
                break
            print("Please enter a valid salary!")
        except ValueError:
            print("Please enter a valid salary!")

    while True:
        try:
            portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
            if portion_saved > 0:
                break
            print("Please enter a valid portion!")
        except ValueError:
            print("Please enter a valid portion!")

    while True:
        try:
            total_cost = float(input("Enter the cost of your dream house: "))
            if total_cost > 0:
                break
            print("Please enter a valid cost!")
        except ValueError:
            print("Please enter a valid cost!")

    while True:
        try:
            semi_annual_rise = float(input("Enter the semi-annual raise, as a decimal: "))
            if semi_annual_rise >= 0:
                break
            print("Please enter a valid raise!")
        except ValueError:
            print("Please enter a valid raise!")
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


    cevap = input("Calculate again? (y,n): ")
    if      cevap.lower() == "y":
        continue
    elif    cevap.lower() == "n":
        break
    else  :
        print("Invalid choose!")
        continue