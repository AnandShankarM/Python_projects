#Mini project - 11
def atm_session():
    Main_balance = 10000
    withdraw_amount = 0

    withdrawal = input("Do you want to withdraw amount from your account 'y' or 'n'? ").lower()

    if withdrawal != 'y':
        print("Thanks for confirming you don't want to withdraw")
        return

    while True:
        amount = int(input("Enter the amount: "))

        if amount > Main_balance:
            print("Amount is greater than balance")
        elif amount < 100:
            print("Withdrawal amount should be min of 100")
        elif amount % 100 != 0:
            print("Amount should be multiple of 100")
        else:
            Main_balance -= amount
            withdraw_amount += amount
            print("This is the amount left in your account:", Main_balance)

        if Main_balance == 0:
            print("There is no money left in your account")
            break

        More_withdrawal = input("Do you want to withdraw more? 'y' or 'n'? ").lower()
        if More_withdrawal != 'y':
            break

    print("\nTotal amount withdrawn:", withdraw_amount)
    print("Remaining balance:", Main_balance)
    print("Thanks for using Anand's ATM")

atm_session()
