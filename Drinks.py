from typing import List

class Drink:
    """
    A class to represent a drink with a base and a list of flavors.
    
    Attributes:
        base (str): The base of the drink (e.g., 'water', 'sbrite').
        flavors (List[str]): A list of added flavors to the drink.
    
    Methods:
        get_base: Returns the base of the drink.
        get_flavors: Returns the list of flavors in the drink.
        add_flavor: Adds a flavor to the drink if it is valid.
        set_flavors: Sets a list of flavors for the drink.
        get_total: Returns the total cost of the drink based on size and flavors.
    """
    
    # List of possible valid bases and flavors (these don't change)
    _valid_bases = ["water", "sbrite", "pokeacola", "Mr. Salt", "hill fog", "leaf wine"]
    _valid_flavors = ["lemon", "cherry", "strawberry", "mint", "blueberry", "lime"]
    
    # List of possible sizes and their associated prices
    _size_prices = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.15
    }
    
    def __init__(self, base: str, size: str):
        """
        Initializes the drink with a base and size.
        
        Args:
            base (str): The base of the drink (e.g., 'water', 'sbrite').
            size (str): The size of the drink (e.g., 'small', 'medium', 'large', 'mega').
        
        Raises:
            ValueError: If the base or size is invalid.
        """
        # Set base if it's valid, else raise an exception
        if base.lower() in Drink._valid_bases:
            self._base = base.lower()  # Store base in lowercase
        else:
            raise ValueError("Invalid base")
        
        # Set size if it's valid, else raise an exception
        if size.lower() in Drink._size_prices:
            self._size = size.lower()  # Store size in lowercase
        else:
            raise ValueError("Invalid size")
        
        # Initialize flavors as an empty list
        self._flavors = []

    def get_base(self) -> str:
        """
        Returns the base of the drink.
        
        Returns:
            str: The base of the drink.
        """
        return self._base

    def get_flavors(self) -> List[str]:
        """
        Returns the list of flavors in the drink.
        
        Returns:
            List[str]: List of flavors added to the drink.
        """
        return self._flavors

    def add_flavor(self, flavor: str):
        """
        Adds a valid flavor to the drink.
        
        Args:
            flavor (str): The flavor to be added to the drink.
        
        Raises:
            ValueError: If the flavor is invalid or already added.
        """
        if flavor.lower() not in Drink._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        if flavor.lower() not in self._flavors:
            self._flavors.append(flavor.lower())
        else:
            print(f"Flavor '{flavor}' is already added.")

    def set_flavors(self, flavors: List[str]):
        """
        Sets the list of flavors for the drink, replacing any existing ones.
        
        Args:
            flavors (List[str]): A list of flavors to set for the drink.
        
        Raises:
            ValueError: If any flavor is invalid.
        """
        for flavor in flavors:
            if flavor.lower() not in Drink._valid_flavors:
                raise ValueError(f"Invalid flavor: {flavor}")
        self._flavors = list(set(flavors))  # Remove duplicates by converting to a set

    def get_total(self) -> float:
        """
        Calculates the total cost of the drink based on its size and added flavors.
        
        Returns:
            float: The total cost of the drink.
        """
        # Start with the base price for the drink size
        total_cost = Drink._size_prices[self._size]
        
        # Add $0.15 for each added flavor
        total_cost += 0.15 * len(self._flavors)
        
        return total_cost


class Order:
    """
    A class to represent an order containing multiple drinks.
    
    Attributes:
        items (List[Drink]): A list of drinks in the order.
    
    Methods:
        add_item: Adds a drink to the order.
        get_items: Returns the list of drinks in the order.
        get_total: Returns the total cost of the order, including tax.
        get_receipt: Returns a string summary of the order.
    """
    
    def __init__(self):
        """
        Initializes the order with an empty list of items (drinks).
        """
        self._items = []

    def add_item(self, drink: Drink):
        """
        Adds a drink to the order.
        
        Args:
            drink (Drink): The drink object to add to the order.
        
        Raises:
            ValueError: If the item added is not a valid Drink object.
        """
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise ValueError("Item must be a Drink object")

    def get_items(self) -> List[Drink]:
        """
        Returns the list of drinks in the order.
        
        Returns:
            List[Drink]: A list of Drink objects in the order.
        """
        return self._items

    def get_total(self) -> float:
        """
        Calculates the total cost of the order, including tax (7.25%).
        
        Returns:
            float: The total cost of the order, including tax.
        """
        subtotal = sum(drink.get_total() for drink in self._items)
        tax = subtotal * 0.0725  # Tax rate of 7.25%
        return subtotal + tax

    def get_receipt(self) -> str:
        """
        Generates a receipt summarizing the order, including each drink and the total cost.
        
        Returns:
            str: A string receipt summarizing the order.
        """
        receipt = "Receipt:\n"
        for i, drink in enumerate(self._items):
            receipt += f"Drink {i + 1}: Base = {drink.get_base()}, Flavors = {', '.join(drink.get_flavors())}, Total = ${drink.get_total():.2f}\n"
        receipt += f"Order Total: ${self.get_total():.2f}\n"
        return receipt
