class Dog:
    def __init__(self, name, cry):
        self.__name = name
        self.__cry = cry # create a private variable
    def bark(self):
        print(f"{self.__name} says: {self.__cry}")

class Cat:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color.lower() # 转小写
    def introduction(self):
        print(f"Hi, I'm {self.__name} and I'm {self.__color}.")


dog_1 = Dog("Bruno", "Woof")
dog_2 = Dog("Rex", "Hrrrr")
cat_1 = Cat("Whiskers", "Black")
cat_2 = Cat("Fluffy", "White")

dog_1.bark()
# It Output:
# > Bruno says: Woof!

dog_2.bark()
# It Output:
# > Rex says: Hrrrr!

cat_1.introduction()
# It Output:
# > Hi, I'm Whiskers and I'm black.

cat_2.introduction()
# It Output:
# > Hi, I'm Fluffy and I'm white.