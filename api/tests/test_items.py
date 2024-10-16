import json
import os
import pytest
from models.items import Items


class TestItems:

    def setup(self):
        self.item_file = 'data/items.json'

        # Backup het originele bestand als het bestaat
        if os.path.exists(self.item_file):
            with open(self.item_file, 'r') as f:
                self.original_data = json.load(f)
        else:
            self.original_data = []

        # Dummy data
        self.initial_data = [
            {
                "uid": "P011720",
                "code": "mYt79640E",
                "description": "Down-sized system-worthy productivity",
                "short_description": "pass",
                "upc_code": "2541112620796",
                "model_number": "ZK-417773-PXy",
                "commodity_code": "z-761-L5A",
                "item_line": 81,
                "item_group": 83,
                "item_type": 74,
                "unit_purchase_quantity": 3,
                "unit_order_quantity": 18,
                "pack_order_quantity": 13,
                "supplier_id": 10,
                "supplier_code": "SUP468",
                "supplier_part_number": "ZH-103509-MLv",
                "created_at": "1997-05-13 02:30:31",
                "updated_at": "2003-10-18 00:21:57"
            }
        ]

        # Schrijf dummy data naar testbestand
        with open(self.item_file, 'w') as f:
            json.dump(self.initial_data, f)

        # Instantieer Items class
        self.items = Items(root_path='data/', is_debug=False)

    def teardown_method(self):
        # Zet originele data terug
        with open(self.item_file, 'w') as f:
            json.dump(self.original_data, f)

    def test_get_items(self):
        items_data = self.items.get_items()
        assert isinstance(items_data, list)
        assert len(items_data) == 1

    def test_get_item(self):
        item = self.items.get_item("P011720")
        assert item is not None
        assert item["uid"] == "P011720"

    def test_add_item(self):
        # Dummy item met uniek ID
        new_item = {
            "uid": "P011721_dummy",  # Nieuw, uniek ID
            "code": "mYt79640F_dummy",
            "description": "Dummy productivity system",
            "short_description": "dummy_pass",
            "upc_code": "2541112620797",
            "model_number": "ZK-417773-PXz-dummy",
            "commodity_code": "z-762-L5B-dummy",
            "item_line": 82,
            "item_group": 84,
            "item_type": 75,
            "unit_purchase_quantity": 5,
            "unit_order_quantity": 20,
            "pack_order_quantity": 15,
            "supplier_id": 11,
            "supplier_code": "SUP469-dummy",
            "supplier_part_number": "ZH-103510-MLy-dummy"
        }

        self.items.add_item(new_item)
        self.items.save()

        items_data = self.items.get_items()
        assert len(items_data) == 2

    def test_update_item(self):
        updated_item = {
            "uid": "P011720",
            "code": "UpdatedCode",
            "description": "Updated description",
            "short_description": "updated_pass",
            "upc_code": "2541112620798",
            "model_number": "ZK-417773-PXy-updated",
            "commodity_code": "z-761-L5A",
            "item_line": 81,
            "item_group": 83,
            "item_type": 74,
            "unit_purchase_quantity": 4,
            "unit_order_quantity": 19,
            "pack_order_quantity": 14,
            "supplier_id": 10,
            "supplier_code": "SUP468",
            "supplier_part_number": "ZH-103509-MLv-updated"
        }

        self.items.update_item("P011720", updated_item)
        item = self.items.get_item("P011720")
        assert item["code"] == "UpdatedCode"
        assert item["description"] == "Updated description"

    def test_remove_item(self):
        self.items.remove_item("P011720")
        self.items.save()
        item = self.items.get_item("P011720")
        assert item is None
