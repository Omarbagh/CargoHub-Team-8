import unittest
# from models import shipments
import json
from api.models.shipments import Shipments


class TestShipments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.shipments_instance = Shipments(
            "path/to/your/root/", is_debug=True)

    def test_get_suppliers_by_id(self):
        with open('data/suppliers.json') as file:
            expected_data = json.load(file)

        # assuming `get_supplier_by_id` is the actual method
        result = self.shipments_instance.get_supplier_by_id(1)

        self.assertEqual(result, expected_data.get('id') == 1)

    def test_get_transfers_invalid_id(self):
        result = self.shipments_instance.get_shipments(999)
        self.assertIsNone(result)

    def test_add_transfers(self):
        new_shipment = {
            "id": 600,
            "order_id": 1,
            "source_id": 331,
            "order_date": "2000-03-09",
            "request_date": "2000-03-11",
            "shipment_date": "2000-03-13",
            "shipment_type": "I",
            "shipment_status": "Pending",
            "notes": "Zee vertrouwen.",
            "carrier_code": "DPD",
            "carrier_description": "Dynamic Parcel Distribution",
            "service_code": "Fastest",
            "payment_type": "Manual",
            "transfer_mode": "Ground",
            "total_package_count": 31,
            "total_package_weight": 594.42,
            "created_at": "2000-03-10T11:11:14Z",
            "updated_at": "2000-03-11T13:11:14Z",
            "items": [
                {
                    "item_id": "P007435",
                    "amount": 23
                },
                {
                    "item_id": "P009557",
                    "amount": 1
                },
                {
                    "item_id": "P009553",
                    "amount": 50
                },
                {
                    "item_id": "P010015",
                    "amount": 16
                },
                {
                    "item_id": "P002084",
                    "amount": 33
                },
                {
                    "item_id": "P009663",
                    "amount": 18
                },
                {
                    "item_id": "P010125",
                    "amount": 18
                },
                {
                    "item_id": "P005768",
                    "amount": 26
                },
                {
                    "item_id": "P004051",
                    "amount": 1
                },
                {
                    "item_id": "P005026",
                    "amount": 29
                },
                {
                    "item_id": "P000726",
                    "amount": 22
                },
                {
                    "item_id": "P008107",
                    "amount": 47
                },
                {
                    "item_id": "P001598",
                    "amount": 32
                },
                {
                    "item_id": "P002855",
                    "amount": 20
                },
                {
                    "item_id": "P010404",
                    "amount": 30
                },
                {
                    "item_id": "P010446",
                    "amount": 6
                },
                {
                    "item_id": "P001517",
                    "amount": 9
                },
                {
                    "item_id": "P009265",
                    "amount": 2
                },
                {
                    "item_id": "P001108",
                    "amount": 20
                },
                {
                    "item_id": "P009110",
                    "amount": 18
                },
                {
                    "item_id": "P009686",
                    "amount": 13
                }
            ]
        }

        self.shipments_instance.add_shipment(new_shipment)

        result = self.shipments_instance.get_shipments(60)

        self.assertIsNotNone(
            result, "Shipment with ID 60 should be added but returned None")
        self.assertEqual(result["id"], new_shipment["id"])


if __name__ == '__main__':
    unittest.main()
