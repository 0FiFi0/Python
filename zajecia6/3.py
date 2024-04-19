class BankAccount:
    def __init__(self, number, currency, balance, owner):
        self.number = number
        self.currency = currency
        self.__balance = balance
        self.__owner = owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @staticmethod
    def convert_currency(amount, exchange_rate):
        return amount * exchange_rate

account1 = BankAccount(123456, "PLN", 1000, "John Smith")
print(account1.convert_currency(100, 4.5))
euro_amount = BankAccount.convert_currency(1000, 4.5)
print("Amount in euro:", euro_amount)
