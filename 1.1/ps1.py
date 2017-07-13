def main():
    print ("Enter the oustanding balance on your credit card.")
    balance = input()
    balance = float(balance)

    print ("Enter the annual credit card interest rate as a decimal.")
    annual_rate = input()
    annual_rate = float(annual_rate)

    print ("Enter the minimum monthly payment rate as a decimal.")
    minimum_rate = input()
    minimum_rate = float(minimum_rate)

    total_amount_paid = 0

    for month in range (1,13):

        minimum_payment = minimum_rate*balance
        interest_paid = annual_rate/12*balance
        principal_paid = minimum_payment-interest_paid
        balance = balance-principal_paid

        total_amount_paid = total_amount_paid + minimum_payment

        print ("Month "+str(month))
        print ("Minimum monthly payment: $"+str(round(minimum_payment,2)))
        print ("Principal paid: $"+str(round(principal_paid,2)))
        print ("Remaining balance: $"+str(round(balance,2)))

    print ("RESULT")
    print ("Total amount paid: $"+str(round(total_amount_paid,2)))
    print ("Remaining balance: $"+str(round(balance,2)))

main()
