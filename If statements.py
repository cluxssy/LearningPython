
Price = 1000000
is_good_credit = input("Does your credit score meet the minimum requirements? (True/False)")


if is_good_credit == "True":
    down_payment = 0.1 * Price
    print(" Your credit score is good and to buy the house, u need to put down a 10% down payment.")
    print(f" Your down payment is calculated to be= {down_payment} ")
    print(" Thank You")
elif is_good_credit == "False":
    down_payment = 0.2 * Price
    print(" Your credit score is lower than the required score,u need to put down a 20% Down payment to buy the house.")
    print(f" Your down payment is calculated to be= {down_payment} ")
    print(" Thank You")
else:
    raise ValueError('Write either True or False')
