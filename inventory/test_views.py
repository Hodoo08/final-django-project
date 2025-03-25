# Python
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from inventory.models import InventoryItem, Category

class IndexViewTest(TestCase):
    def test_index_view_status_code(self):
        # Test the status code of the index view
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template_used(self):
        # Test the template used by the index view
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'inventory/index.html')  # Replace with the correct template name

    def test_index_view_content(self):
        # Test the content rendered by the index view
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Track and Manage Your Inventory")  # Replace with expected content


class DashboardViewTest(TestCase):
    def setUp(self):
        # Set up test data and client for authenticated user
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.item = InventoryItem.objects.create(
            name='Test Item',
            quantity=10,
            category=self.category,
            user=self.user
        )
        
    def test_dashboard_view_status_code(self):
        # Test the status code of the dashboard view
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        
    def test_dashboard_view_template_used(self):
        # Test the template used by the dashboard view
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'inventory/dashboard.html')  # Replace with the correct template name
        
    def test_dashboard_view_context_data(self):
        # Test the context data passed to the dashboard view
        response = self.client.get(reverse('dashboard'))
        self.assertIn('items', response.context)
        self.assertIn('low_inventory_ids', response.context)
        self.assertEqual(len(response.context['items']), 1)  # Ensure one item is passed   


class SignUpViewTest(TestCase):
    def test_signup_view_status_code(self):
        # Test the status code of the signup view
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
                    
    def test_signup_view_template_used(self):
        # Test the template used by the signup view
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'account/signup.html')  # Replace with the correct template name
                    
    def test_signup_view_form_submission(self):
        # Test the form submission in the signup view
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect after successful signup
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())  # Ensure the user is created

class AddItemViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')

    def test_add_item_view_status_code(self):
        # Test the status code of the add-item view
        response = self.client.get(reverse('add-item'))
        self.assertEqual(response.status_code, 200)

    def test_add_item_view_template_used(self):
        response = self.client.get(reverse('add-item'))
        self.assertTemplateUsed(response, 'inventory/item_form.html')  # Update to match the actual template

    def test_add_item_view_form_submission(self):
        # Test the form submission in the add-item view
        response = self.client.post(reverse('add-item'), {
            'name': 'New Item',
            'quantity': 5,
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission
        self.assertTrue(InventoryItem.objects.filter(name='New Item').exists())

class EditItemViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.item = InventoryItem.objects.create(
            name='Test Item',
            quantity=10,
            category=self.category,
            user=self.user
        )

    def test_edit_item_view_status_code(self):
        # Test the status code of the edit-item view
        response = self.client.get(reverse('edit-item', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_item_view_template_used(self):
        response = self.client.get(reverse('edit-item', args=[self.item.id]))
        self.assertTemplateUsed(response, 'inventory/item_form.html')  # Update to match the actual template

    def test_edit_item_view_form_submission(self):
        # Test the form submission in the edit-item view
        response = self.client.post(reverse('edit-item', args=[self.item.id]), {
            'name': 'Updated Item',
            'quantity': 15,
            'category': self.category.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')
        self.assertEqual(self.item.quantity, 15)

        

class DeleteItemViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.item = InventoryItem.objects.create(
            name='Test Item',
            quantity=10,
            category=self.category,
            user=self.user
        )

    def test_delete_item_view_status_code(self):
        # Test the status code of the delete-item view
        response = self.client.get(reverse('delete-item', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_item_view_template_used(self):
        # Test the template used by the delete-item view
        response = self.client.get(reverse('delete-item', args=[self.item.id]))
        self.assertTemplateUsed(response, 'inventory/delete_item.html')  # Replace with the correct template name

    def test_delete_item_view_deletion(self):
        # Test the deletion of an item in the delete-item view
        response = self.client.post(reverse('delete-item', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful deletion
        self.assertFalse(InventoryItem.objects.filter(id=self.item.id).exists())