import json
import unittest
import os
from api.models.item_groups import ItemGroups


class TestClients(unittest.TestCase):
    def setUp(self):
        self.item_group_file = 'data/item_groups.json'

        if os.path.exists(self.item_group_file):
            with open(self.item_group_file, 'r') as f:
                self.original_data = json.load(f)
        else:
            self.original_data = []

        self.initial_data = [
            {
                "id": 0,
                "name": "Electronics",
                "description": "",
                "created_at": "1998-05-15 19:52:53",
                "updated_at": "2000-11-20 08:37:56"
            },
            {
                "id": 1,
                "name": "Furniture",
                "description": "",
                "created_at": "2019-09-22 15:51:07",
                "updated_at": "2022-05-18 13:49:28"
            }
        ]

        with open(self.item_group_file, 'w') as f:
            json.dump(self.initial_data, f)

        self.item_groups = ItemGroups(root_path='data/', is_debug=False)

    def tearDown(self):
        with open(self.item_group_file, 'w') as f:
            json.dump(self.original_data, f)

    def test_get_item_groups(self):
        item_groups_data = self.item_groups.get_item_groups()
        self.assertIsInstance(item_groups_data, list)
        self.assertEqual(len(item_groups_data), 2)

    def test_get_item_group(self):
        item_group = self.item_groups.get_item_group(0)
        self.assertIsNotNone(item_group)
        self.assertEqual(item_group["id"], 0)

    def test_add_item_group(self):
        new_item_group = {
            "id": 2,
            "name": "Appliances",
            "description": ""
        }
        self.item_groups.add_item_group(new_item_group)
        self.item_groups.save()
        print(self.item_groups.get_item_groups())
        self.assertEqual(len(self.item_groups.get_item_groups()), 3)

    def test_update_item_group(self):
        updated_item_group = {
            "id": 0,
            "name": "Updated Electronics",
            "description": "Updated description"
        }
        self.item_groups.update_item_group(0, updated_item_group)
        item_group = self.item_groups.get_item_group(0)
        self.assertEqual(item_group["name"], "Updated Electronics")

    def test_remove_item_group(self):
        self.item_groups.remove_item_group(0)
        item_group = self.item_groups.get_item_group(0)
        self.assertIsNone(item_group)


if __name__ == "__main__":
    unittest.main()
