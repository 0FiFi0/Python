class BankAccount:
    def __init__(self, number, currency, balance , owner):
        self.number = number
        self.currency = currency
        self.__balance = balance
        self.__owner = owner

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def set_owner(self, new_owner):
        self.__owner = new_owner

    def get_balance(self):
        print(f"Balance: {self.__balance}")

    def get_owner(self):
        print(f"Balance: {self.__owner}")

    def __str__(self):
        return f"Account number: {self.number}\nCurrency: {self.currency}\nBalance: {self.__balance}\nOwner: {self.__owner}"

    def __len__(self):
        return self.__balance

    def __add__(self, other):
        if (self.number == other.number) and (self.currency == other.currency) and (self.__owner == other.__owner):
            new_balance = self.__balance + other.get_balance()
            return new_balance
        else:
            raise ValueError("Cannot add accounts - different numbers, currencies, or owners")

account1 = BankAccount(111111, "EUR", 1000, "John Snow")
account2 = BankAccount(111111, "EUR", 2690, "John Smith")
print(account1)
account1.set_owner("Jacek Śniegowy")
print(account1)

try:
    account3 = account1 + account2
    print(account3)
except ValueError as e:
    print(e)

