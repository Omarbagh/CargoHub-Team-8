import unittest
from models import warehouses
import json

class TestWarehouses(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.warehouses_instance = warehouses.Warehouses("path/to/your/root/", is_debug=True)

    def test_get_warehouse_by_id(self):
        
        with open('data/warehouses.json') as file:
            expected_data = json.load(file)
            return expected_data
        
        
        result = self.warehouses_instance.get_warehouse(1)

        self.assertEqual(result, excepted_data[id] == 1)


    def test_get_warehouse_invalid_id(self):
        result = self.warehouses_instance.get_warehouse(999)
        self.assertIsNone(result) 

    def test_add_warehouse(self):
        new_warehouse = {
            "id": 60,
            "code": "YQZZNL56",
            "name": "Schiedam cargo hub",
            "address": "Schiedam",
            "zip": "3117 AS",
            "city": "Heemskerk",
            "province": "Zuid-Holland",
            "country": "NL",
            "contact": {
                "name": "O",
                "phone": "(078) 0013363",
                "email": "blamore@example.net"
            }
        }
        
        self.warehouses_instance.add_warehouse(new_warehouse)

        result = self.warehouses_instance.get_warehouse(60)

        self.assertIsNotNone(result, "Warehouse with ID 60 should be added but returned None")

        self.assertEqual(result["id"], new_warehouse["id"])


        

if __name__ == '__main__':
    unittest.main()
