class Category:
    amount = 0
    category = ""

    def __init__(self, amount):
        self.amount = amount

    #methods
    def deposit(self, total):
        if(type(total) == int):
            self.amount += total
            
        else:
            return "Invalid Input"
        return "Updated balance is $" + str(self.amount)

    def checkBalance(self):
        return self.amount

    def withdraw(self, total):
        if(type(total) == int):
            if(total > self.amount):
                return "Amount is higher than budget alloted"
            self.amount -= total
        else:
            return "Invalid Input"

        return "Updated balance is $" + str(self.amount)

    def transfer(self, toHere, total):
        if(type(total) == int):
            if(total > self.amount):
                return "Amount is higher than budget alloted"
            else:
                self.amount -= total
                toHere.deposit(total)
        else:
            return "Invalid Input"
        
        return "Updated balance: " + self.category + ": $" + str(self.amount) + " " + toHere.getCategory() + ": $" + str(toHere.checkBalance())

    def getCategory(self):
        return self.category

# Child Classes that are currently created, more can be added in the future
class Clothing(Category):
    def __init__(self, amount):
        super().__init__(amount)
        self.category = "Clothing"

class Food(Category):
    def __init__(self, amount):
        super().__init__(amount)
        self.category = "Food"

class Car(Category):
    def __init__(self, amount):
        super().__init__(amount)
        self.category = "Car"
