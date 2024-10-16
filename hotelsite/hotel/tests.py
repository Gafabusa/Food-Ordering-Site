from django.test import TestCase
from django.urls import reverse

class URLTests(TestCase):
    def test_index_url(self):
        """Test if the index page is accessible"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_about_url(self):
        """Test if the about page is accessible"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_book_url(self):
        """Test if the book page is accessible"""
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, 200)
    
    def test_menu_url(self):
        """Test if the menu page is accessible"""
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
    
    def test_order_success_url(self):
        """Test if the order success page is accessible"""
        response = self.client.get(reverse('order_success'))
        self.assertEqual(response.status_code, 200)
