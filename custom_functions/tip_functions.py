# A function called 'total_with_tip' that will take in four argument, run, and do the calacutalions if a tip will be added
# and return the total price and the price to be paid by each person if more than 1 person has eaten.
def total_with_tip(price, tax, client, tip):

    tax_price = round(((tax / 100) * price), 2)
    tip_price = round(((tip / 100) * price), 2)
    total = price + tax_price + tip_price

    if client == 1:
        final_price = f'Total bill: ${total}'
    else:
        final_price = f'Total bill: ${total}\nEach person should pay ${round(total / client, 2)}'

    return final_price

# A function called 'total_with_no_tip' that will take in three argument, run and do the calacutalions if a tip will not be added,
# and return the total price and the price to be paid by each person if more than 1 person has eaten.
def total_with_no_tip(price, tax, client):

    total = round(price + ((tax / 100) * price), 2)
    if client == 1:
        final_price = f'Total bill: ${total}'
    else:
        final_price = f'Total bill: ${total}\nEach person should pay ${round(total / client, 2)}'
    return final_price
    