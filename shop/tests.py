from django.test import TestCase
from django.shortcuts import get_object_or_404

# Create your tests here.
  
class TestViews(TestCase):

    def test_get_shop_page(self):
        page = self.client.get("/shop/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "shop.html")