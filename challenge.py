loop = 1

balance = 10000

print("Menu"
      "\n1 - Deposit"
      "\n2 - Withdraw"
      "\n3 - Check Balance"
      "\n4 - Exit")

option = int(input("Enter your choice: "))

while loop:
    if option == 1:
        deposit = int(input("Enter your deposit: "))
        balance += deposit
    elif option == 2:
        withdraw = int(input("Enter your withdraw: "))
        balance -= withdraw
    elif option == 3:
        print(f"Your balance is: {balance}")
    elif option == 4:
        break
    print("Menu"
          "\n1 - Deposit"
          "\n2 - Withdraw"
          "\n3 - Check Balance"
          "\n4 - Exit")

    option = int(input("Enter your choice: "))
else:
    print("Thank You!")