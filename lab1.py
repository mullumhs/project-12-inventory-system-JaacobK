"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 1
-----------------------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class named Item that represents a generic item in an inventory system.
               Implement encapsulation using private attributes and public getters and setters.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Define the Item class with initialisation that uses setters for name, price, and quantity.
# Instead of directly setting private attributes in the __init__ method, use the class's own setters
# We will define the setters in later steps to add validation to the setting of these attributes.


class Item():
    def __init__(self, name, price, qty):
        self.set_name(name)
        self.set_price(price)
        self.set_qty(qty)



# Step 2: Implement a getter for the name attribute.
# This method should simply return the value of the private _name attribute.

    def get_name(self):
        return f"{self._name}:"



# Step 3: Implement a setter for the name attribute.
# This method should check if the provided value is a string before setting the _name attribute.
# If the value is not a string, it should raise a ValueError.

    def set_name(self, name):
        if isinstance(name, str) and name != "":
            self._name = name
        else:
            raise ValueError("Not a valid string")

# Step 4: Implement a getter for the price attribute.
# This method should return the price formatted as a string with two decimal places.

    def get_price(self):
        return f"The price is ${self._price:.2f},"

# Step 5: Implement a setter for the price attribute.
# This method should check if the provided value is a non-negative number before setting the _price attribute.
# If the value is negative, it should raise a ValueError.

    def set_price(self, price):
        if isinstance(price, (float, int)) and price >= 0:
            self._price = price
        else:
            raise ValueError("Not a valid float")



# Step 6: Implement a getter for the quantity attribute.
# This method should simply return the value of the private _quantity attribute.

    def get_qty(self):
        return f"{self._qty} in stock."



# Step 7: Implement a setter for the quantity attribute.
# This method should check if the provided value is a non-negative integer before setting the _quantity attribute.
# If the value is negative, it should raise a ValueError.

    def set_qty(self, qty):
            if isinstance(qty, int) and qty >= 0:
                self._qty = qty
            else:
                raise ValueError("Not a valid int")



# Step 8: Create instances of the Item class and demonstrate the use of getters and setters.
# For example, create a new Item and attempt to set its attributes with both valid and invalid values.
# Print the outputs using the getters to show how the data is managed internally.
def main():
    sword = Item("Sword", 3, 5)
    while True:
        try:
            i = input("Sword Name: ")
            sword.set_name(i)
            break
        except ValueError as error_msg:
            print(error_msg)

    while True:
        try:
            i = float(input("Sword Price: "))
            sword.set_price(i)
            break
        except ValueError as error_msg:
            print(error_msg)

    while True:
        try:
            i = int(input("Sword qty: "))
            sword.set_qty(i)
            break
        except ValueError as error_msg:
            print(error_msg)
if __name__ == "__main__":
    main()