class GroceryListApp:
    def __init__(self):
        self.items = {} #Initialize a dictionary to store items and quantity
        
    def add_item(self, item, quantity):
        #add an item to the grocery list. If it exists, update the quantity
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
            
    def remove_item(self, item, quantity):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]
                
    def display_list(self):
        #display the current contents of the grocery store apply
        print("Grocery List App:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
            
def main():
    # Create an instance of the GroceryList class
    grocery_list = GroceryListApp()

    while True:
        # Display menu options to the user
        print("\n1. Add item to the list")
        print("2. Remove item from the list")
        print("3. Display the list")
        print("4. Quit")

        # Get user input for their choice
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Option to add an item to the list
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            grocery_list.add_item(item, quantity)
        elif choice == '2':
            # Option to remove an item from the list
            item = input("Enter the item name to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            grocery_list.remove_item(item, quantity)
        elif choice == '3':
            # Option to display the current grocery list
            grocery_list.display_list()
        elif choice == '4':
            # Option to quit the program
            print("Exiting the program. Your final grocery list:")
            grocery_list.display_list()
            break  # Exit the while loop when the user chooses to quit
        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 4.")

# Rest of the code remains unchanged
 
if __name__ == "__main__":
    main()
        
        
    
