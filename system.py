from models import MenuItem, Order, Customer

class RestaurantSystem:
    """Main system to manage menu, customers, and orders."""

    def __init__(self):
        """Create a new empty restaurant system."""
        self.menu = []
        self.customers = []
        self.orders = []
        self.next_order_id = 1  

    def add_menu_item(self, name, price, category):
        """Create and add a new menu item to the menu."""
        item = MenuItem(name, price, category)
        self.menu.append(item)

    def list_menu_items(self):
        """Print all menu items."""
        if not self.menu:
            print("No menu items yet.")
            return

        for index, item in enumerate(self.menu, start=1):
            print(f"{index}. {item}")

    def find_customer_by_name(self, name):
        """Return the customer with this name, or None if not found."""
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def create_customer_if_not_exists(self, name, phone):
        """Find a customer by name, or create a new one if not found."""
        customer = self.find_customer_by_name(name)
        if customer is None:
            customer = Customer(name, phone)
            self.customers.append(customer)
        return customer

    def create_order_for_customer(self, customer_name, phone):
        """Create a new order for a customer and return it."""
        customer = self.create_customer_if_not_exists(customer_name, phone)
        order = Order(self.next_order_id)
        self.next_order_id += 1

        self.orders.append(order)
        customer.add_order(order)

        return order

    def show_main_menu(self):
        """Show the main menu and handle user choices."""
        while True:
            print("\n--- RESTAURANT SYSTEM MENU ---")
            print("1. Show menu items")
            print("2. Add a new menu item")
            print("3. Create a new order")
            print("4. Add item to an order")
            print("5. Show all orders")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.list_menu_items()

            elif choice == "2":
                self.add_menu_item_interactive()

            elif choice == "3":
                self.create_order_interactive()

            elif choice == "4":
                self.add_item_to_order_interactive()

            elif choice == "5":
                self.show_all_orders()

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    def add_menu_item_interactive(self):
        """Ask user for menu item details and add it."""
        name = input("Enter item name: ")
        category = input("Enter category: ")

        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("Invalid price. Item not added.")
            return

        self.add_menu_item(name, price, category)
        print("Menu item added.")

    def create_order_interactive(self):
        """Ask user for customer info and create an order."""
        name = input("Customer name: ")
        phone = input("Customer phone: ")

        order = self.create_order_for_customer(name, phone)
        print(f"Order {order.order_id} created for {name}.")

    def add_item_to_order_interactive(self):
        """Add a menu item to an existing order."""
        try:
            order_id = int(input("Enter order ID: "))
        except ValueError:
            print("Invalid order ID.")
            return

        order = None
        for o in self.orders:
            if o.order_id == order_id:
                order = o
                break

        if order is None:
            print("Order not found.")
            return

        self.list_menu_items()
        try:
            item_number = int(input("Enter menu item number: "))
        except ValueError:
            print("Invalid number.")
            return

        if 1 <= item_number <= len(self.menu):
            order.add_item(self.menu[item_number - 1])
            print("Item added to order.")
        else:
            print("Invalid item number.")

    def show_all_orders(self):
        """Print all orders."""
        if not self.orders:
            print("No orders yet.")
            return

        for order in self.orders:
            print(order)

    def save_menu_to_file(self, filename="menu.csv"):
        """Save menu items to a CSV file."""
        with open(filename, "w") as file:
            for item in self.menu:
                file.write(f"{item.name},{item.price},{item.category}\n")
        print("Menu saved to file.")

    def load_menu_from_file(self, filename="menu.csv"):
        """Load menu items from a CSV file."""
        try:
            with open(filename, "r") as file:
                for line in file:
                    name, price, category = line.strip().split(",")
                    self.add_menu_item(name, float(price), category)
            print("Menu loaded from file.")
        except FileNotFoundError:
            print("Menu file not found. Starting with empty menu.")
