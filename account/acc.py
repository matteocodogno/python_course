class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read())


    def withdraw(self, amount):
        self.balance -= amount


    def deposit(self, amount):
        self.balance += amount


    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects"""
    type = "Checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee


    def transfer(self, amount):
        self.balance -= amount - self.fee


account = Checking('./balance.txt', 0.2)
account.withdraw(12.5)
account.deposit(9.3)
account.commit()
account.transfer(7)
account.commit()
print(account.balance)
