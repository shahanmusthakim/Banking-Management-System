
import random


class Bank:
    def __init__(self, name):
        self.name = name
        self.account_list = []
        self.total_balance = 10000
        self.total_loan = 0
        self.loan_facility = True
        self.bankrupt = False

    def create_account(self, name, email, phone, password):
        account = Account(name, email, phone, password, "user")
        self.account_list.append(account)
        print(f"\nAccount created successfully!")
        print(f"Your account number is {account.account_no}")

    def delete_account(self, account_no):
        for account in self.account_list:
            if account.account_no == account_no:
                self.total_balance -= account.total_balance
                self.account_list.remove(account)
                print(f"Account {account_no} deleted successfully.")
                return
        print("Account not found.")

    def show_users(self):
        print("\n***** ALL USERS *****\n")
        for user in self.account_list:
            print(f"Name: {user.name}\t Account No: {user.account_no}")

    def show_total_balance(self):
        print(f"Total bank balance: {self.total_balance}tk")

    def show_total_loan(self):
        print(f"Total loan: {self.total_loan}tk")

    def loan_on(self):
        self.loan_facility = True
        print("Loan facility activated.")

    def loan_off(self):
        self.loan_facility = False
        print("Loan facility deactivated.")

    def declare_bankrupt(self):
        self.bankrupt = True
        print("Bank has been declared bankrupt.")


class Account:
    def __init__(self, name, email, phone, password, user_type):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.user_type = user_type
        self.account_no = self.generate_account_no()
        self.total_balance = 0
        self.loan_count = 0
        self.transaction_history = []

    def generate_account_no(self):
        return random.randint(100000, 199999)

    def deposit(self, bank, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        if bank.bankrupt:
            print("Bank is bankrupt. Transactions are disabled.")
            return

        self.total_balance += amount
        bank.total_balance += amount

        print(f"\nSuccessfully deposited {amount}tk.")
        print(f"Your current balance is {self.total_balance}tk")

        self.transaction_history.append(f"Deposited {amount}tk")

    def withdraw(self, bank, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if bank.bankrupt:
            print("Bank is bankrupt. Transactions are disabled.")
            return

        if self.total_balance >= amount:
            self.total_balance -= amount
            bank.total_balance -= amount

            print(f"\nHere is your {amount}tk.")
            print(f"Your current balance is {self.total_balance}tk")

            self.transaction_history.append(f"Withdraw {amount}tk")
        else:
            print("Not sufficient balance.")

    def show_balance(self):
        print(f"\nYour current balance is {self.total_balance}tk")

    def show_transaction_history(self):
        print("\n----- Transaction History -----\n")
        if not self.transaction_history:
            print("No transactions found.")
            return

        for history in self.transaction_history:
            print(history)

    def take_loan(self, bank, amount):
        if amount <= 0:
            print("Invalid loan amount.")
            return

        if bank.bankrupt:
            print("Bank is bankrupt.")
            return

        if not bank.loan_facility:
            print("Taking loan is currently disabled by admin.")
            return

        if self.loan_count >= 2:
            print("Sorry, you cannot take a loan more than twice.")
            return

        if bank.total_balance >= amount:
            self.total_balance += amount
            bank.total_balance -= amount
            bank.total_loan += amount
            self.loan_count += 1

            print(f"\nCongrats! You have taken a loan of {amount}tk.")
            print(f"Your current balance is {self.total_balance}tk")

            self.transaction_history.append(f"Loan taken: {amount}tk")
        else:
            print("Sorry, bank doesn't have enough money to provide a loan.")


print("\n----- Welcome to Central Bank -----\n")

bank = Bank("Central Bank")


def logged_in_as_user(user):
    print(f"\nWelcome {user.name} to Central Bank.")
    print(f"Your account No. is {user.account_no}")

    while True:
        print("\n_________________________________________")
        print("| Press 1 for Check Balance.             |")
        print("| Press 2 for Deposit Money.             |")
        print("| Press 3 for Withdraw Money.            |")
        print("| Press 4 for Take Loan.                 |")
        print("| Press 5 for Transaction History.       |")
        print("| Press 6 for Logout.                    |")
        print("|______________________________________ _|")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            user.show_balance()

        elif choice == 2:
            try:
                amount = int(input("Enter deposit amount: "))
                user.deposit(bank, amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == 3:
            try:
                amount = int(input("Enter withdrawal amount: "))
                user.withdraw(bank, amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == 4:
            try:
                amount = int(input("Enter loan amount: "))
                user.take_loan(bank, amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == 5:
            user.show_transaction_history()

        elif choice == 6:
            print("Logging out...")
            break

        else:
            print("Invalid choice.")


def logged_in_as_admin(user):
    print(f"\nWelcome {user.name} to Central Bank.")
    print(f"Your Administrative account No. is {user.account_no}")

    while True:
        print("\n_________________________________________")
        print("| Press 1 for Create an user account.    |")
        print("| Press 2 for Delete an user account.    |")
        print("| Press 3 for Show all users.            |")
        print("| Press 4 for Show total bank balance.   |")
        print("| Press 5 for Show total loan amount.    |")
        print("| Press 6 for Turn on loan.              |")
        print("| Press 7 for Turn off loan.             |")
        print("| Press 8 for Declare Bankrupt.          |")
        print("| Press 9 for Logout.                    |")
        print("|________________________________________|")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone No: ")
            password = input("Password: ")
            bank.create_account(name, email, phone, password)

        elif choice == 2:
            try:
                acnt = int(input("Enter account number to delete: "))
                bank.delete_account(acnt)
            except ValueError:
                print("Invalid account number.")

        elif choice == 3:
            bank.show_users()

        elif choice == 4:
            bank.show_total_balance()

        elif choice == 5:
            bank.show_total_loan()

        elif choice == 6:
            bank.loan_on()

        elif choice == 7:
            bank.loan_off()

        elif choice == 8:
            bank.declare_bankrupt()

        elif choice == 9:
            print("Logging out...")
            break

        else:
            print("Invalid choice.")


while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    op = input("Enter your choice: ")

    if op == '1':
        user_type = input("User/Admin (u/a): ").lower()

        if user_type not in ['u', 'a']:
            print("Invalid user type.")
            continue

        if user_type == 'a' and any(
            account.user_type == "admin" for account in bank.account_list
        ):
            print("An admin account already exists.")
            continue

        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone No: ")
        password = input("Password: ")

        role = "admin" if user_type == 'a' else "user"

        user = Account(name, email, phone, password, role)

        bank.account_list.append(user)

        print(f"\nWelcome {name} to Central Bank.")
        print(f"Your account No. is {user.account_no}")

    elif op == '2':
        user_type = input("User/Admin (u/a): ").lower()
        name = input("Enter your name: ")
        password = input("Password: ")

        logged_in = False

        for user in bank.account_list:
            if user.name == name and user.password == password:
                if user_type == 'a' and user.user_type == 'admin':
                    logged_in_as_admin(user)
                    logged_in = True
                    break

                elif user_type == 'u' and user.user_type == 'user':
                    logged_in_as_user(user)
                    logged_in = True
                    break

        if not logged_in:
            print("Invalid name, password, or user type.")

    elif op == '3':
        print("Thank you for using Central Bank.")
        break

    else:
        print("Invalid choice.")
