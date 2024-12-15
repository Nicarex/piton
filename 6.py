class Account:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount

    def remove_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

# Пример использования
account = Account("Иван", 10000)
account.add_money(5000)
account.remove_money(2000)

print(account.name)
print(account.balance)
