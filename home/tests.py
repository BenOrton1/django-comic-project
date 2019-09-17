from django.test import TestCase
from django.shortcuts import get_object_or_404

# Create your tests here.
  
class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_about_page(self):
        page = self.client.get("/about")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_get_hire_page(self):
        page = self.client.get("/hire")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "hire.html")
