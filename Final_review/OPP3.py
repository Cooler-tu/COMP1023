import math
import numpy as np
import copy
import random
    
class Account:
    def __init__(self, id = 0, balance = 100., mir = 0.):
        self.__id = id
        self.__balance = balance
        self.__mir = mir
    def accessor_id(self):
        return self.__id
    def accessor_balance(self):
        return round(self.__balance, 1)
    def accessor_mir(self):
        return self.__mir

    def getAnnualInterestRate(self):
        return self.__mir*12
    def getAnnualInterest(self):
        return round(self.getAnnualInterestRate() * self.__balance, 1)
    
    def withdraw(self, n):
        if(n <= self.__balance):
            self.__balance -= n
            return self.__balance
        else:
            print("NO SUFFICIENT MONEY!!")
            return self.__balance
    
    def deposit(self, n):
        self.__balance+=n
        return self.__balance
    
    def print_all(self):
        print(f"Account ID: {self.accessor_id()}")
        print(f"Balance: ${self.accessor_balance()}")
        x = self.getAnnualInterestRate()
        print(f"Annual Interest Rate: {x}({x*100}%)")
        print(f"Annual Interest: ${self.getAnnualInterest()}")

def main():
    A = Account(id = 1122, balance = 20000, mir = 0.375* 0.01)
    A.print_all()

    A.withdraw(2500)
    A.print_all()
    A.deposit(3000)
    A.print_all()

if __name__ == "__main__":
    main()