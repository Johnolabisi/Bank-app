# This is a sample Python script
class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds.")

    def transfer(self, amount, recipient):
        if amount <= self.balance:
            self.withdraw(amount)
            recipient.deposit(amount)
            self.history.append(f"Transferred ${amount} to {recipient.name}")
            recipient.history.append(f"Received ${amount} from {self.name}")
        else:
            print("Insufficient funds for transfer.")

    def show_history(self):
        print(f"Transaction history for {self.name}:")
        for transaction in self.history:
            print("-", transaction)



john = Account("John")
victor = Account("Victor")

john.deposit(500)
john.transfer(200, victor)

# View transaction history
john.show_history()
victor.show_history()


