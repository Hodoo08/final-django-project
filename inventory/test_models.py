# Python
from django.test import TestCase
from inventory.models import InventoryItem, Category
from django.contrib.auth import get_user_model

class InventoryItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        cls.category = Category.objects.create(name='Test Category')
        cls.inventory_item = InventoryItem.objects.create(
            name='Test Item',
            quantity=10,
            category=cls.category,
            user=cls.user
        )

    def test_inventory_item_creation(self):
        # Test the creation of an InventoryItem instance
        self.assertEqual(self.inventory_item.name, 'Test Item')
        self.assertEqual(self.inventory_item.quantity, 10)
        self.assertEqual(self.inventory_item.category, self.category)
        
        

    def test_inventory_item_str_representation(self):
        # Test the string representation of the InventoryItem model
        self.assertEqual(str(self.inventory_item), 'Test Item')
        self.assertEqual(str(self.category), 'Test Category')
        

    def test_inventory_item_quantity_field(self):
        # Test the quantity field of the InventoryItem model
        self.assertEqual(self.inventory_item.quantity, 10)
        

    def test_inventory_item_category_relationship(self):
        # Test the relationship between InventoryItem and Category
        self.assertEqual(self.inventory_item.category, self.category)

    def test_inventory_item_user_relationship(self):
        # Test the relationship between InventoryItem and User
        self.assertEqual(self.inventory_item.user, self.user)