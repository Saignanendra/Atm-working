# demo values
n = 123456
amountC = 20000
amountS = 10000
print("welcome to ATM")
username = input("enter your name: ")  # taking username
pin = int(input("enter pin number: "))  # pin num taking

# Checking pin is Correct or Not

if n == pin:
    # to display options
    print('''
             1.Deposit
             2.Withdraw
             3.Balance Check
             4.Exit''')

# To take user option

    option = int(input(" select any option you want: "))
    if option == 1:  # display data according to user option
        print('''
               1.Saving Account
               2.Current Account
               ''')
        DepO = int(input("enter any option : "))  # asking for user account type

        if DepO == 1:
            DepS = int(input("enter the amount : "))   # for Deposit saving amount to account
            amountS += DepS
            print("Saving Account Total Balance : ", amountS)  # display total saving amount after deposit
        elif DepO == 2:
            DepC = int(input("enter the amount : "))  # for Deposit current amount to account
            amountC += DepC
            print("Total Balance: ", amountC)  # display total current amount after deposit

    elif option == 2:     # to withdraw amount
        print('''
        1.Saving Account
        2.Current Account
        ''')
        Select = int(input("enter any option : "))   # asking for user account type
        if Select == 1:
            WithDS = int(input("Enter the amount : "))         # to withdraw amount from saving account
            if WithDS > amountS:       # if withdraw amount is greater than account balance
                print("insufficient amount!")
                exit()    # exit loop
            amountS -= WithDS
            print("Remaining Balance: ", amountS)  # display total saving amount after withdraw
        elif Select == 2:
            WithDC = int(input("enter the amount:"))   # to withdraw amount from current account
            if amountC < WithDC:
                print("insufficient amount!")
                exit()
            amountC -= WithDC

            print("Remaining amount :", amountC)  # display total current amount after withdraw

    elif option == 3:      # to display account details
        print("************")
        print("Username:", username)
        print("Current Account Balance:", amountC)
        print("Saving Account Balance :", amountS)
        print("Thanks for Visiting")
        print("************")
    elif option == 4:       # to exit
        print("Successfully exit")
    else:
        print("enter a valid option")
else:  # if pin is wrong.
    print("incorrect pin")
