class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display_account(self):
        print("\nAccount Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance: ₹", self.balance)


atm = ATM("ACC101", "Rahul", 10000)

while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.display_account()

    elif choice == 5:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice.")
