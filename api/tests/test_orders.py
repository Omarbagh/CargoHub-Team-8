import unittest
# from models import orders
import json
from api.models.orders import Orders


class TestOrders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.orders_instance = Orders(
            "path/to/your/root/", is_debug=True)

    def test_get_order_by_id(self):
        with open('data/orders.json') as file:
            expected_data = json.load(file)

        result = self.orders_instance.get_order_by_id(
            1)  # assuming `get_order_by_id` is the method

        self.assertEqual(result, expected_data.get('id') == 1)

    def test_get_order_invalid_id(self):
        result = self.orders_instance.get_order_by_id(999)
        self.assertIsNone(result)

    def test_add_order(self):
        new_order = {
            "id": 1,
            "source_id": 33,
            "order_date": "2019-04-03T11:33:15Z",
            "request_date": "2019-04-07T11:33:15Z",
            "reference": "ORD00001",
            "reference_extra": "Bedreven arm straffen bureau.",
            "order_status": "Delivered",
            "notes": "Voedsel vijf vork heel.",
            "shipping_notes": "Buurman betalen plaats bewolkt.",
            "picking_notes": "Ademen fijn volgorde scherp aardappel op leren.",
            "warehouse_id": 18,
            "ship_to": None,
            "bill_to": None,
            "shipment_id": 1,
            "total_amount": 9905.13,
            "total_discount": 150.77,
            "total_tax": 372.72,
            "total_surcharge": 77.6,
            "created_at": "2019-04-03T11:33:15Z",
            "updated_at": "2019-04-05T07:33:15Z",
            "items": [
                {"item_id": "P007435", "amount": 23},
                {"item_id": "P009557", "amount": 1},
                {"item_id": "P009553", "amount": 50},
            ]
        }

        self.orders_instance.add_order(new_order)

        result = self.orders_instance.get_order_by_id(1)

        self.assertIsNotNone(
            result, "Order with ID 1 should be added but returned None")
        self.assertEqual(result["id"], new_order["id"])


if __name__ == '__main__':
    unittest.main()
