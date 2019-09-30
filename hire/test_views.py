from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Commition

# Create your tests here.
  
class TestViews(TestCase):

    def test_get_estimate_page(self):
        this_estimate = Commition(name='create a Test')
        this_estimate.save()

        page = self.client.get("/estimate/{0}".format(this_estimate.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "estimate.html")
        
    def test_get_hire_page(self):
        page = self.client.get("/hire")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "hire.html")