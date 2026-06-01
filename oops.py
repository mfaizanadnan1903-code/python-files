"""
Polymorphism with classes
"""
class Bird:
    def sound(self):
        print("Birds make sounds")
class Crow(Bird):
    def sound(self):
        print("Crow makes sound of 'Caca caca'")
class Parrot(Bird):
    def sound(self):
        print("Parrot copies the sound of human")

bird1 = Crow()
bird2 = Parrot()
bird1.sound()
bird2.sound()


"""
Encapsulation 
"""
class BankAccount:
    def __init__(self,accountno,balance):
        self.accountno = accountno
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposited : {amount}\nNew Balnace : {self.__balance}")
    def get_balance(self):
        return self.__balance
        
        
account1 = BankAccount("123456789",50000)
account1.deposit(45000)
print(account1.get_balance())

"""
Inheritence
"""
