"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py

from lab1 import Item

# Step 2: Define tadw ahe InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.

class InventroryManager:
    def __init__(self):
        self._items = []

    def add(self, name, price, qty):
        for item in self._items:
            if item.get_name() == name:
                print(f"{name} already exixsts")
                return
        new_item = Item(name, price, qty)
        self._items.append(new_item)
    
    def remove(self, name):
        for item in self._items:
            if item.get_name() == name:
                self._items.remove(item)
                return
        print("item not found")

    def update_price(self, name, price):
        for item in self._items:
            if item.get_name() == name:
                item.set_price(price)
                return
        print(f"{name} not found")
        
    def update_qty(self, name, qty):
        for item in self._items:
            if item.get_name() == name:
                item.set_price(qty)
                return
        print(f"{qty} not found")

    def display(self):
        for item in self._items:
            print(f"{item.get_name()} {item.get_price()} {item.get_qty()}")

# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

milk_isle = InventroryManager()
milk_isle.add("chocy milk", 2, 20)
milk_isle.add("strawsberry milk", 1.50231321, 10)
milk_isle.add("banana milk", 2.5, 3)
milk_isle.add("banana milk", 2.5, 3)
milk_isle.display()
milk_isle.remove("chocy milk")
milk_isle.display()
