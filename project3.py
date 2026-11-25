account={
    "name":"chandru",
    "balance":"500000",
    "pin":"1234",
    "type":"savings"
    
}
print("==MINI ATM")
pin = input("Enter your pin: ")
if pin == account["pin"]:
    while True:
        print("\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Your balance is:", account["balance"])
        
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= float(account["balance"]):
                account["balance"] = str(float(account["balance"]) - amount)
                print("Withdrawal successful. New balance is:", account["balance"])
            else:
                print("Insufficient balance.")
        
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            account["balance"] = str(float(account["balance"]) + amount)
            print("Deposit successful. New balance is:", account["balance"])
        
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        
        else:
            print("Invalid choice. Please try again.")
            