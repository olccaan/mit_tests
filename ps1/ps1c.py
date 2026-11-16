# Problem Set 1 - Part C: Finding the right amount to save away

while True:
    total_dream_house_cost = 1000000
    portion_down_payment = 0.25
    necessary_months = 36
    r = 0.04
    semi_annual_raise = .07
    while True:
        try:
            starting_salary = float(input("Enter the starting salary: "))
            break
        except ValueError:
            print("Please enter a valid salary!")
            
    down_payment = portion_down_payment * total_dream_house_cost

    low = 0
    high = 10000
    guess = (low + high) // 2

    current_savings = 0
    steps = 0

    while abs(current_savings - down_payment) > 100 and high - low > 1 : 
        current_savings = 0 
        annual_salary = starting_salary
        portion_saved = guess / 10000
        for months in range(1, necessary_months+1):
            monthly_salary = annual_salary / 12
            current_savings = current_savings * (1 + (r/12))
            current_savings = current_savings + monthly_salary * portion_saved
            if months % 6 == 0 :
                annual_salary = annual_salary * ( 1 + semi_annual_raise) 

        steps += 1

        if current_savings - down_payment < -100:
            low = guess
        elif current_savings-down_payment > 100:
            high = guess
        guess = (low + high) // 2

    if abs(current_savings - down_payment) > 100:
        print("It's not possible to pay the down payment in three years. ")
    else:
        print("Best savings rate:", portion_saved)
        print("Steps in bisection search: ", steps)



    cevap = input("Calculate again? (y,n): ")
    if      cevap.lower() == "y":
        continue
    elif    cevap.lower() == "n":
        break
    else  :
        print("Invalid choose!")
        continue