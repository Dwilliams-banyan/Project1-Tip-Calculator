# Creating a tip calculator that will ask for the cost of food,
# number of people splitting the bill, and if you want to leave a tip.
# It shall take your answer and give you the price of what you are expected to pay.
from custom_functions.tip_functions import total_with_tip, total_with_no_tip

# 'meal_calculation' is a function that returns the price to be displayed to the user.
def meal_calculation():
# 'sales_tax' is a variable that will hold the value of the sales for the bill amount
    sales_tax = float(10)
    customer_inputs = False
    while customer_inputs == False:
        try:
# 'food_price' is a variable that will hold the value of the cost of the meal.
            food_price = float(input('What is the price of your meal? '))
# 'customers' is a variable that will hold the value of who all was eating at the table.
            customers = float(input('Thank you, how many was at your table eating? Include yourself as well. '))
        except ValueError:
            print(f'I apologize but the information you provided was not efficient, let\'s do it again')
        else:
            customer_inputs = True


# 'tip_option' is a variable that will hold the value of rather a tip will be left of not.
    tip_option = input('Thank you again, would you like to leave a tip? ').upper()
    if tip_option == 'YES' or tip_option == 'YEAH' or tip_option == 'SURE':
# 'is_num' is a variable that will not change until the value of tip_option is given correctly
        is_num = False
        while is_num == False:
            try:
# 'tip_percent' is a variable that will hold the value of how much a tip the customer is willing to leave.
                tip_percent = float(input('What tip percentage would you like to leave?\nPlease do not add the percentage symbol (%) '))
            except ValueError:
                print('You did not enter a valid percentage, please try again.')
            else:
                is_num = True
# 'extra_tip' is a variable that will not change until the client does not want to leave an additional  tip.
                extra_tip = True
                while extra_tip is True:
# 'higher_tip_option' is a variable that will hold the value of rather a additional tip will be left of not.
                    higher_tip_option = input('Awesome, would you like to add to that tip? ').upper()
                    if higher_tip_option == 'YES' or higher_tip_option == 'YEAH' or higher_tip_option == 'SURE':
                        tip_percent = tip_percent + float(input('How much more would you like to leave? '))
                    else:
                        extra_tip = False
# 'total_with_tip' is a function imported that will take in four argument, run, and do the calacutalions if a tip will be added
# and return the total price and the price to be paid by each person if more than 1 person has eaten.
                print(
                    total_with_tip(food_price, sales_tax, customers, tip_percent)
                    )
    else:
# 'total_with_no_tip' is a function imported that will take in three argument, run and do the calacutalions if a tip will not be added,
# and return the total price and the price to be paid by each person if more than 1 person has eaten.
        print(
            total_with_no_tip(food_price, sales_tax, customers)
            )

# 'tip_calculator' is function that will ask the user for the price, the number of people eating,
# if a tip will be left, how much of a tip, if additional tips will be left, how much of additional tips,
# and if the user would like to do this again. 
def tip_calculator():
    done_eating = True
    while done_eating is True:
        meal_calculation()
        finished = input('Would you like to do this again? ').upper()
        if finished == 'YEAH' or finished == 'YUP' or finished == 'YES':
            meal_calculation()
        else:
            done_eating = False

# tip_calculator()