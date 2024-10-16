import json
import unittest
import os
from api.models.inventories import Inventories


class TestClients(unittest.TestCase):
    def setUp(self):
        self.inventories_files = 'data/inventories.json'

        if os.path.exists(self.inventories_files):
            with open(self.inventories_files, 'r') as f:
                self.original_data = json.load(f)
        else:
            self.original_data = []

        self.initial_data = [
            {
                "id": 1,
                "item_id": "P000001",
                "description": "Face-to-face clear-thinking complexity",
                "item_reference": "sjQ23408K",
                "locations": [
                    3211,
                    24700,
                    14123,
                    19538,
                    31071,
                    24701,
                    11606,
                    11817
                ],
                "total_on_hand": 262,
                "total_expected": 0,
                "total_ordered": 80,
                "total_allocated": 41,
                "total_available": 141,
                "created_at": "2015-02-19 16:08:24",
                "updated_at": "2015-09-26 06:37:56"
            },
            {
                "id": 2,
                "item_id": "P000002",
                "description": "Focused transitional alliance",
                "item_reference": "nyg48736S",
                "locations": [
                    19800,
                    23653,
                    3068,
                    3334,
                    20477,
                    20524,
                    17579,
                    2271,
                    2293,
                    22717
                ],
                "total_on_hand": 194,
                "total_expected": 0,
                "total_ordered": 139,
                "total_allocated": 0,
                "total_available": 55,
                "created_at": "2020-05-31 16:00:08",
                "updated_at": "2020-11-08 12:49:21"
            }
        ]

        with open(self.inventories_files, 'w') as f:
            json.dump(self.initial_data, f)

        self.inventories = Inventories(root_path='data/', is_debug=False)

    def tearDown(self):
        with open(self.inventories_files, 'w') as f:
            json.dump(self.original_data, f)

    def test_get_inventories(self):
        inventories_data = self.inventories.get_inventories()
        self.assertIsInstance(inventories_data, list)
        self.assertEqual(len(inventories_data), 2)

    def test_get_inventory(self):
        inventories = self.inventories.get_inventory(1)
        self.assertIsNotNone(inventories)
        self.assertEqual(inventories["id"], 1)

    def test_add_inventory(self):
        new_inventory = {
            "id": 11721,
            "item_id": "P011721",
            "description": "miauw",
            "item_reference": "mYt79641E",
            "locations": [
                30113,
                30437,
                9010,
                11731,
                25614,
                25515,
                4192,
                19302,
                3946,
                26883,
                9308,
                22330,
                14470,
                8871,
                8326,
                18266,
                17880,
                33186,
                33547
            ],
            "total_on_hand": 324,
            "total_expected": 0,
            "total_ordered": 307,
            "total_allocated": 79,
            "total_available": -45,
            "created_at": "1997-05-13 02:30:31",
            "updated_at": "2003-10-18 00:21:57"
        }
        self.inventories.add_inventory(new_inventory)
        print(self.inventories.get_inventories())
        self.assertEqual(len(self.inventories.get_inventories()), 3)

    def test_update_client(self):
        updated_inventory = {
            "id": 1,
            "item_id": "P000001",
            "description": "miauw",
            "item_reference": "sjQ23408K",
            "locations": [
                3211,
                24700,
                14123,
                19538,
                31071,
                24701,
                11606,
                11817
            ],
            "total_on_hand": 262,
            "total_expected": 0,
            "total_ordered": 80,
            "total_allocated": 41,
            "total_available": 141,
            "created_at": "2015-02-19 16:08:24",
            "updated_at": "2015-09-26 06:37:56"
        }
        self.inventories.update_inventory(1, updated_inventory)
        inventory = self.inventories.get_inventory(1)
        self.assertEqual(inventory["description"], "miauw")

    def test_remove_client(self):
        self.inventories.remove_inventory(1)
        inventory = self.inventories.get_inventory(1)
        self.assertIsNone(inventory)


if __name__ == "__main__":
    unittest.main()
