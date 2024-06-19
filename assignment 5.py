import datetime

class Products:                  # Define a class to represent products in the inventory
    def __init__(self, name, category, price, quantity, expdate):
        self.name = name              #initialize the name of the product
        self.category = category      #initialize the category to which the product belongs to
        self.price = price            #initialize the price of the product
        self.quantity = quantity      #initialize the quantity of the product
        self.expdate = expdate        #initialize thenexpiration date of the product

inventory = []             # Initialize an empty list to store inventory products

def add_product(product):           # Function to add a product to the inventory
    inventory.append(product)

def remove_product(product_name):       # Function to remove a product from the inventory by its name
    global inventory
    inventory = [product for product in inventory if product.name != product_name]

def search_products(search_term):        # Function to search for products in the inventory by name or category
    return [product for product in inventory if search_term.lower() in product.name.lower() or search_term.lower() in product.category.lower()]  # Returns a list of products where the search term matches (case insensitive) either the product's name or category

def list_all_products():      # Function to list all products in the inventory
    for product in inventory:
        print(f"{product.name} ({product.category}): {product.quantity} available, {product.price:.2f} each")

def categorize_products():           # Function to categorize products by their category
    categories = {}
    for product in inventory:
        if product.category not in categories:
            categories[product.category] = []
        categories[product.category].append(product)
    return categories

def remove_expired_products():    # Function to remove expired products from the inventory
    today = datetime.date.today()
    global inventory
    inventory = [product for product in inventory if product.expdate >= today]

def save_inventory(file_name):        # Function to save the inventory to a file
    try:
        with open(file_name, 'w') as file:
            for product in inventory:
                file.write(f"{product.name},{product.category},{product.price},{product.quantity},{product.expdate}\n")
    except IOError:
        print(f"Error: Could not write to file {file_name}")

def load_inventory(file_name):        # Function to load the inventory from a file
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, category, price, quantity, expdate = line.strip().split(',')
                product = Products(name, category, float(price), int(quantity), datetime.datetime.strptime(expdate, '%Y-%m-%d').date())
                inventory.append(product)
    except IOError:
        print(f"Error: Could not read file {file_name}")

def main():        # Main function to interact with the user and manage the inventory
    while True:
        print("\nInventory Management System")      # Display menu options
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Products")
        print("4. List All Products")
        print("5. Categorize Products")
        print("6. Remove Expired Products")
        print("7. Save Inventory to File")
        print("8. Load Inventory from File")
        print("9. Exit")
        
        choice = input("Enter your choice: ")         # Get user choice

        if choice == '1':   # Add a new product
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            expdate = datetime.datetime.strptime(input("Enter product expiration date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            product = Products(name, category, price, quantity, expdate)
            add_product(product)
            print("Product added successfully.")

        elif choice == '2':            # Remove a product
            product_name = input("Enter product name to remove: ")
            remove_product(product_name)
            print("Product removed successfully.")

        elif choice == '3':            # Search for products
            search_term = input("Enter product name or category to search: ")
            results = search_products(search_term)
            if results:
                for product in results:
                    print(f"{product.name} ({product.category}): {product.quantity} available, {product.price:.2f} each")
            else:
                print("No products found.")

        elif choice == '4':            # List all products
            list_all_products()

        elif choice == '5':            # Categorize products
            categorized = categorize_products()
            for category, products in categorized.items():
                print(f"Category: {category}")
                for product in products:
                    print(f"  - {product.name}")

        elif choice == '6':             # Remove expired products
            remove_expired_products()
            print("Expired products removed successfully.")

        elif choice == '7':            # Save inventory to a file
            file_name = input("Enter file name to save inventory: ")
            save_inventory(file_name)
            print("Inventory saved successfully.")

        elif choice == '8':            # Load inventory from a file
            file_name = input("Enter file name to load inventory: ")
            load_inventory(file_name)
            print("Inventory loaded successfully.")

        elif choice == '9':            # Exit the program
            print("Thank you for visiting the Inventory Management System.")
            break

        else:            # Invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":          # Run the main function if this script is executed
    main()
