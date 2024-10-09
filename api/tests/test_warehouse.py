import unittest
from api.models import warehouses

class TestWarehouses(unittest.TestCase):

    def test_get_warehouse_by_id(self):
        expected_warehouse = {
        "id": 1,
        "code": "YQZZNL56",
        "name": "Heemskerk cargo hub",
        "address": "Karlijndreef 281",
        "zip": "4002 AS",
        "city": "Heemskerk",
        "province": "Friesland",
        "country": "NL",
        "contact": {
            "name": "Fem Keijzer",
            "phone": "(078) 0013363",
            "email": "blamore@example.net"
        },
        "created_at": "1983-04-13 04:59:55",
        "updated_at": "2007-02-08 20:11:00"
    }
        
        result = warehouses.Warehouses.get_warehouse(1)
        self.assertEqual(result, expected_warehouse)

    def test_get_warehouse_invalid_id(self):
        result = warehouses.Warehouses.get_warehouse(999)
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
        },
        "created_at": "1983-04-13 04:59:55",
        "updated_at": "2007-02-08 20:11:00"
    }   
        warehouses.Warehouses.add_warehouse(new_warehouse)
        
        result = warehouses.Warehouses.get_warehouse(60)
        self.assertEqual(result["name"], "Schiedam cargo hub")

if __name__ == '__main__':
    unittest.main()
