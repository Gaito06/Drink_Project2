# Class to represent a Drink, which has a base and flavors
class Drink:
    # List of possible valid bases and flavors (these don't change)
    _valid_bases = ["water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"]
    _valid_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]

    # Size cost table
    SIZE_COSTS = {
        'small': 1.50,
        'medium': 1.75,
        'large': 2.05,
        'mega': 2.15
    }
    
    FLAVOR_COST = 0.15  # Cost for each flavor added

    def __init__(self, base, size='small'):
        """Constructor to initialize the base, size, and flavors."""
        self._base = None
        self._flavors = []
        self._size = size.lower()  # Ensure size is case-insensitive

        # Set the base if it's valid
        if base in Drink._valid_bases:
            self._base = base
        else:
            raise ValueError("Invalid base")
        
        # Validate size
        if self._size not in Drink.SIZE_COSTS:
            raise ValueError("Invalid size")

    # Getter for the base of the drink
    def get_base(self):
        return self._base

    # Getter for the list of flavors
    def get_flavors(self):
        return self._flavors

    # Getter for the number of flavors
    def get_num_flavors(self):
        return len(self._flavors)

    # Getter for the size of the drink
    def get_size(self):
        return self._size

    # Setter for size
    def set_size(self, size):
        size = size.lower()
        if size not in Drink.SIZE_COSTS:
            raise ValueError("Invalid size")
        self._size = size

    # Getter for the total cost of the drink
    def get_cost(self):
        """Calculate the total cost of the drink based on size and flavors."""
        cost = Drink.SIZE_COSTS[self._size]
        cost += len(self._flavors) * Drink.FLAVOR_COST
        return cost

    # Add a flavor to the drink
    def add_flavor(self, flavor):
        """Ensure that the flavor is valid and isn't already in the list."""
        if flavor not in Drink._valid_flavors:
            raise ValueError("Invalid flavor")
        if flavor not in self._flavors:
            self._flavors.append(flavor)
        else:
            print(f"Flavor '{flavor}' is already added.")

    # Set the list of flavors (replaces existing flavors)
    def set_flavors(self, flavors):
        """Set the list of flavors, ensuring they're valid and without duplicates."""
        for flavor in flavors:
            if flavor not in Drink._valid_flavors:
                raise ValueError(f"Invalid flavor: {flavor}")
        self._flavors = list(set(flavors))  # Remove duplicates by converting to a set

    # String representation of the drink (for easy printing)
    def __str__(self):
        flavor_str = f" with {', '.join(self._flavors)}" if self._flavors else ""
        return f"{self._base.capitalize()} ({self._size.capitalize()}){flavor_str} - ${self.get_cost():.2f}"


class Order:
    TAX_RATE = 0.0725  # 7.25% tax

    def __init__(self):
        # Private list to store drinks
        self._items = []

    # Getter for the list of items in the order
    def get_items(self):
        return self._items

    # Getter for the total price of the order
    def get_total(self):
        """Calculate the total order cost, including tax."""
        total = sum(drink.get_cost() for drink in self._items)  # Sum costs of all drinks
        total_with_tax = total * (1 + Order.TAX_RATE)
        return total_with_tax

    # Getter for the number of items in the order
    def get_num_items(self):
        return len(self._items)

    # Getter for the receipt (returns a string summary of the order)
    def get_receipt(self):
        """Generate the receipt for the order."""
        receipt = "Receipt:\n"
        for i, drink in enumerate(self._items):
            receipt += f"Drink {i + 1}: Base = {drink.get_base()}, Size = {drink.get_size()}, Flavors = {', '.join(drink.get_flavors())}, Cost: ${drink.get_cost():.2f}\n"
        
        total_order_cost = self.get_total()
        receipt += f"\nTotal Order Cost (including tax): ${total_order_cost:.2f}"
        return receipt

    # Add a drink to the order
    def add_item(self, drink):
        """Add a drink to the order."""
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise ValueError("Item must be a Drink object")

    # Remove a drink from the order by index
    def remove_item(self, index):
        """Remove a drink from the order by index."""
        if 0 <= index < len(self._items):
            del self._items[index]
        else:
            raise IndexError("Item index out of range")
