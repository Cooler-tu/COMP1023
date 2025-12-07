class BankAccount:
    def __init__(self, name, balance, password):
        self.__name = name
        self.__balance = int(balance)
        self.__password = password
    def deposit(self, m, p):
        if(p != self.__password or m < 0):
            raise ValueError("<error message>")
        self.__balance += m
        print(f"Your current balance is {self.__balance}.")
    def withdraw(self, m, p):
        if(p != self.__password or self.__balance < m or m < 0):
            raise ValueError("<error message>")
        self.__balance -= m
        print(f"Your current balance is {self.__balance}.")

def main():
    A = BankAccount('a', 1, 1234)
    B = BankAccount('b', 1, 2222)

if __name__ == "__main__":
    main()