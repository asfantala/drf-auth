from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Item


class ItemTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_item = Item.objects.create(user=testuser1, name='flower', description='test desc ...')
        test_item.save()

    def test_item_model(self):
        item = Item.objects.get(id=1)
        actual_user = str(item.user)
        actual_name = str(item.name)
        actual_desc = str(item.description)
        self.assertEqual(actual_user, "testuser1")
        self.assertEqual(actual_name, "flower")
        self.assertEqual(actual_desc, "test desc ...")
