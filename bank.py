account={}
account_number=1001
while True:
    
    create=print("1.Create account")
    Login=print("2.login")
    Deposite=print("3.Deposite")
    withdraw=print("4.Withdraw money")
    Check_balance=print("5.Check Balance")
    Transition_history=print("6.Transition history")
    exit=print("7.Exit")
    choice=input("What we want to access?")

    if choice=="1":
        Name=input("Enter the name")
        Age=int(input("Enter the age"))
        phone=int(input("Enter the Phone"))
        PIN=int(input("ENter the PIN"))
        Intial_deposite=int(input ("ENter the Intial deposite"))
        account[account_number]={
            "Name":Name,
            "Age":Age,
            "phone":phone,
            "PIN":PIN,
            "balance": Intial_deposite,
            "Transition_history":[("Intial_deposit", Intial_deposite)]


        }
        print("Account created successful")
        print("Account number is",account_number)
        account_number += 1
#login
    elif choice == "2":
        acc_no = int(input("Enter the account number"))
        pin = int(input("Enter the PIN"))

        if acc_no in account and account[acc_no]["PIN"] == pin:
          print("\nLogin is successful")
          print("Welcome", account[acc_no]["Name"])
        else:
          print("\nInvalid account No")
#Depostie
    elif choice=="3":
       acc_no=int(input("ENter the account Number"))
       amount=int(input("Enter the amount"))
       if acc_no in account:
          account[acc_no]["balance"]+=amount
          account[acc_no]["Transition_history"].append(("Intial_deposit", amount))
          print(f"Amount{amount}is deposite done")
          print(f"You balanceis {account[acc_no]['balance']}")
       else:
          print("Invalid account number")
#Withdraw
    elif choice=="4":
       acc_no=int(input("Account number"))
       if acc_no in account:
          amount=float(input("Enter the amount"))
          if amount <=account[acc_no]["balance"]:
             account[acc_no]["balance"]-=amount
             account[acc_no]["Transition_history"].append(("Withdraw",amount))
             print(f"Amount{amount} is withdraw done")
             print(f"your balance is {account[acc_no]['balance']}")
       else:
          print("Insufficient balance")
    elif choice=="5":
       acc_no=int(input("Enter the account no" ))
       if acc_no in account:
          print(f"Your balance is{account[acc_no]['balance']}")
       else:
          print("Invalid account number")
    elif choice =='6':
       acc_no=int(input("ENter the account number"))
       if acc_no in account:
            for transaction in account[acc_no]["Transition_history"]:

                print(
                    transaction[0],
                    "₹",
                    transaction[1]
                )

            print(
                "\nCurrent Balance:",
                account[acc_no]["balance"]
            )

       else:

            print("Account not found.")

    elif choice=="7":
       print("Thank you for using our management")
    else:
       print("\nInvalid choice. Please select 1-7.")