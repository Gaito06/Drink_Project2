import unittest
from Drinks import Drink, Order

class TestDrink(unittest.TestCase):
    def test_get_base(self):
        """Test the getter for base."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_base(), "hill fog")
    
    def test_get_flavors_empty(self):
        """Test the getter for flavors when no flavors are added."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_flavors(), [])
    
    def test_get_size(self):
        """Test the getter for size."""
        drink = Drink("hill fog", size="medium")
        self.assertEqual(drink.get_size(), "medium")
    
    def test_get_total(self):
        """Test the total cost calculation, including flavors."""
        drink = Drink("hill fog", size="medium")
        drink.add_flavor("lemon")
        # Base cost of medium + cost of one flavor
        self.assertEqual(drink.get_total(), 1.75 + 0.15)
    
    def test_set_size(self):
        """Test setting the size."""
        drink = Drink("hill fog", size="medium")
        drink.set_size("large")
        self.assertEqual(drink.get_size(), "large")
    
    def test_invalid_base(self):
        """Test invalid base."""
        with self.assertRaises(ValueError):
            drink = Drink("invalid base", size="medium")
    
    def test_invalid_size(self):
        """Test invalid size."""
        with self.assertRaises(ValueError):
            drink = Drink("hill fog", size="extra large")


class TestOrder(unittest.TestCase):
    def test_get_items(self):
        """Test the getter for items in the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        order.add_item(drink1)
        self.assertEqual(order.get_items(), [drink1])
    
    def test_get_total(self):
        """Test the total calculation for the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        drink2 = Drink("Mr. Salt", size="large")
        drink2.add_flavor("cherry")
        order.add_item(drink1)
        order.add_item(drink2)
        
        expected_total = (1.75 + 0.15) + (2.05 + 0.15)  # Base + flavor cost for both drinks
        expected_total_with_tax = expected_total * (1 + 0.0725)
        self.assertAlmostEqual(order.get_total(), expected_total_with_tax, places=2)
    
    def test_get_num_items(self):
        """Test the number of items in the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        order.add_item(drink1)
        self.assertEqual(len(order.get_items()), 1)  # Using len to count items
    
    def test_get_receipt(self):
        """Test the receipt generation."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        drink1.add_flavor("lemon")
        drink2 = Drink("Mr. Salt", size="large")
        drink2.add_flavor("cherry")
        
        order.add_item(drink1)
        order.add_item(drink2)
        
        expected_receipt = (
            "Receipt:\n"
            "Drink 1: Base = hill fog, Size = medium, Flavors = lemon, Cost: $1.90\n"
            "Drink 2: Base = Mr. Salt, Size = large, Flavors = cherry, Cost: $2.20\n"
            "\nTotal Order Cost (including tax): $4.40"
        )
        self.assertEqual(order.get_receipt(), expected_receipt)
    
    def test_remove_item(self):
        """Test removing a drink from the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        drink2 = Drink("Mr. Salt", size="large")
        order.add_item(drink1)
        order.add_item(drink2)
        
        order.remove_item(0)  # Remove the first drink
        self.assertEqual(order.get_items(), [drink2])

    def test_invalid_remove_item(self):
        """Test removing an invalid item from the order."""
        order = Order()
        drink1 = Drink("hill fog", size="medium")
        order.add_item(drink1)
        
        with self.assertRaises(IndexError):
            order.remove_item(1)  # Attempt to remove an item at an invalid index


if __name__ == "__main__":
    unittest.main()
