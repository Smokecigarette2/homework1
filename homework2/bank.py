class bank:
    def __init__(self, owner, balance = 0):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("The amount is exceeding ur balance money")
        else:
            self.balance -= amount


user1 = bank("Olzhas", 1000)

user1.deposit(500)
print(user1.balance)
user1.withdraw(2000)
user1.withdraw(200)
print(user1.balance)
