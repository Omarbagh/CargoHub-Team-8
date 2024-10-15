import json
import unittest
import os
from api.models.item_types import ItemTypes


class TestItemTypes(unittest.TestCase):
    def setUp(self):
        self.item_type_file = 'data/item_types.json'

        if os.path.exists(self.item_type_file):
            with open(self.item_type_file, 'r') as f:
                self.original_data = json.load(f)
        else:
            self.original_data = []

        self.initial_data = [
            {
                "id": 0,
                "name": "Laptop",
                "description": "",
                "created_at": "2001-11-02 23:02:40",
                "updated_at": "2008-07-01 04:09:17"
            },
            {
                "id": 1,
                "name": "Desktop",
                "description": "",
                "created_at": "1993-07-28 13:43:32",
                "updated_at": "2022-05-12 08:54:35"
            }
        ]

        with open(self.item_type_file, 'w') as f:
            json.dump(self.initial_data, f)

        self.item_types = ItemTypes(root_path='data/', is_debug=False)

    def tearDown(self):
        with open(self.item_type_file, 'w') as f:
            json.dump(self.original_data, f)

    def test_get_item_types(self):
        item_types_data = self.item_types.get_item_types()
        self.assertIsInstance(item_types_data, list)
        self.assertEqual(len(item_types_data), 2)

    def test_get_item_type(self):
        item_type = self.item_types.get_item_type(0)
        self.assertIsNotNone(item_type)
        self.assertEqual(item_type["id"], 0)

    def test_add_item_type(self):
        new_item_type = {
            "id": 2,
            "name": "Tablet",
            "description": ""
        }
        self.item_types.add_item_type(new_item_type)
        self.item_types.save()
        self.assertEqual(len(self.item_types.get_item_types()), 3)

    def test_update_item_type(self):
        updated_item_type = {
            "id": 0,
            "name": "Updated Laptop",
            "description": "Updated description"
        }
        self.item_types.update_item_type(0, updated_item_type)
        item_type = self.item_types.get_item_type(0)
        self.assertEqual(item_type["name"], "Updated Laptop")

    def test_remove_item_type(self):
        self.item_types.remove_item_type(0)
        item_type = self.item_types.get_item_type(0)
        self.assertIsNone(item_type)


if __name__ == "__main__":
    unittest.main()
