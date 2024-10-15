import json
import unittest
import os
from api.models.item_lines import ItemLines


class TestItemLines(unittest.TestCase):
    def setUp(self):
        self.item_line_file = 'data/item_lines.json'

        if os.path.exists(self.item_line_file):
            with open(self.item_line_file, 'r') as f:
                self.original_data = json.load(f)
        else:
            self.original_data = []

        self.initial_data = [
            {
                "id": 0,
                "name": "Tech Gadgets",
                "description": "",
                "created_at": "2022-08-18 07:05:25",
                "updated_at": "2023-05-15 15:44:28"
            },
            {
                "id": 1,
                "name": "Home Appliances",
                "description": "",
                "created_at": "1979-01-16 07:07:50",
                "updated_at": "2024-01-05 23:53:25"
            }
        ]

        with open(self.item_line_file, 'w') as f:
            json.dump(self.initial_data, f)

        self.item_lines = ItemLines(root_path='data/', is_debug=False)

    def tearDown(self):
        with open(self.item_line_file, 'w') as f:
            json.dump(self.original_data, f)

    def test_get_item_lines(self):
        item_lines_data = self.item_lines.get_item_lines()
        self.assertIsInstance(item_lines_data, list)
        self.assertEqual(len(item_lines_data), 2)

    def test_get_item_line(self):
        item_line = self.item_lines.get_item_line(0)
        self.assertIsNotNone(item_line)
        self.assertEqual(item_line["id"], 0)

    def test_add_item_line(self):
        new_item_line = {
            "id": 2,
            "name": "Office Supplies",
            "description": ""
        }
        self.item_lines.add_item_line(new_item_line)
        self.item_lines.save()
        self.assertEqual(len(self.item_lines.get_item_lines()), 3)

    def test_update_item_line(self):
        updated_item_line = {
            "id": 0,
            "name": "Updated Tech Gadgets",
            "description": "Updated description"
        }
        self.item_lines.update_item_line(0, updated_item_line)
        item_line = self.item_lines.get_item_line(0)
        self.assertEqual(item_line["name"], "Updated Tech Gadgets")

    def test_remove_item_line(self):
        self.item_lines.remove_item_line(0)
        item_line = self.item_lines.get_item_line(0)
        self.assertIsNone(item_line)


if __name__ == "__main__":
    unittest.main()
