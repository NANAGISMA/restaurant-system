class MenuItem:
    """Represents one item on the restaurant menu."""

    def __init__(self, name, price, category):
        """Create a new menu item with name, price, and category."""
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, new_price):
        """Update the price of this menu item."""
        self.price = new_price

    def to_dict(self):
        """Return the data as a dictionary (useful for saving to file)."""
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category
        }

    def __str__(self):
        """Return a nice text description of the menu item."""
        return f"{self.name} ({self.category}) - {self.price:.2f} EUR"
    
class Order:
    """Represents a customer's order."""

    def __init__(self, order_id):
        """Create a new order with a given ID."""
        self.order_id = order_id
        self.items = []
        self.status = "open"

    def add_item(self, menu_item):
        """Add a MenuItem to this order."""
        self.items.append(menu_item)

    def remove_item(self, item_name):
        """Remove the first item with the given name from the order."""
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return True
        return False

    def calculate_total(self):
        """Calculate the total price of all items in the order."""
        total = 0.0
        for item in self.items:
            total += item.price
        return total

    def mark_paid(self):
        """Mark this order as paid."""
        self.status = "paid"

    def __str__(self):
        """Return a text description of the order."""
        item_names = [item.name for item in self.items]
        items_text = ", ".join(item_names) if item_names else "no items"
        total = self.calculate_total()
        return f"Order {self.order_id} ({self.status}): {items_text} | Total: {total:.2f} EUR"
class Customer:
    """Represents a restaurant customer."""

    def __init__(self, name, phone):
        """Create a new customer with name and phone."""
        self.name = name
        self.phone = phone
        self.orders = []

    def add_order(self, order):
        """Add an order to this customer."""
        self.orders.append(order)

    def get_total_spent(self):
        """Return the total amount of money spent by this customer."""
        total = 0.0
        for order in self.orders:
            total += order.calculate_total()
        return total

    def list_orders(self):
        """Return a list of text descriptions of all orders."""
        return [str(order) for order in self.orders]

    def __str__(self):
        """Return a text description of the customer."""
        return f"{self.name} ({self.phone})"
