from django.test import TestCase
from .forms import CommitionForm
from .models import Commition

# Create your tests here.

class TestCommitionForm(TestCase):
    def Can_create_a_commition_form(self):
        self.assertEqual(1, 1)