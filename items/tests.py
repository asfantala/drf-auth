from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Item


class ItemTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_Item = Item.objects.create(
            name="rake",
            owner=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_Item.save()

    # class 32
    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_items_model(self):
        item = Item.objects.get(id=1)
        actual_user = str(item.user)
        actual_name = str(item.name)
        actual_desc = str(item.description)
        self.assertEqual(actual_user, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_desc, "Better for collecting leaves than a shovel."
        )

    def test_get_items_list(self):
        url = reverse("items_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        items = response.data
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["name"], "rake")

    def test_get_item_by_id(self):
        url = reverse("item_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item = response.data
        self.assertEqual(item["name"], "rake")

    def test_create_item(self):
        url = reverse("items_list")
        data = {"user": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        items = Item.objects.all()
        self.assertEqual(len(items), 2)
        self.assertEqual(items.objects.get(id=2).name, "spoon")

    def test_update_thing(self):
        url = reverse("item_detail", args=(1,))
        data = {
            "user": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = Item.objects.get(id=1)
        self.assertEqual(thing.name, data["name"])
        self.assertEqual(thing.user.id, data["user"])
        self.assertEqual(thing.description, data["description"])

    def test_delete_item(self):
        url = reverse("item_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        item = Item.objects.all()
        self.assertEqual(len(item), 0)

    # class 32
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("items_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


