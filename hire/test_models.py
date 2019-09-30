from django.test import TestCase
from .models import Commition


class TestCommitionModel(TestCase):

    def test_done_defaults_to_False(self):
        commition = Commition(yourname="Create a Test")
        commition.save()
        self.assertEqual(commition.yourname, "Create a Test")
        self.assertFalse(commition.done)