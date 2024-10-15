import unittest
from models import suppliers
import json

class TestSuppliers(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.supplier_instance = suppliers.Suppliers("path/to/your/root/", is_debug=True)

    def test_get_suppliers_by_id(self):
        
        with open('data/suppliers.json') as file:
            expected_data = json.load(file)
            return expected_data
        
        
        result = self.supplier_instance.get_suppliers(1)

        self.assertEqual(result, excepted_data[id] == 1)


    def test_get_transfers_invalid_id(self):
        result = self.supplier_instance.get_suppliers(999)
        self.assertIsNone(result) 

    def test_add_transfers(self):
        new_supplier = {
        "id": 1,
        "code": "SUP0001",
        "name": "Lee, Parks and Johnson",
        "address": "5989 Sullivan Drives",
        "address_extra": "Apt. 996",
        "city": "Port Anitaburgh",
        "zip_code": "91688",
        "province": "Illinois",
        "country": "Czech Republic",
        "contact_name": "Toni Barnett",
        "phonenumber": "363.541.7282x36825",
        "reference": "LPaJ-SUP0001",
        "created_at": "1971-10-20 18:06:17",
        "updated_at": "1985-06-08 00:13:46"
        }
        
        self.supplier_instance.add_supplier(new_supplier)

        result = self.supplier_instance.get_suppliers(60)

        self.assertIsNotNone(result, "Transfers with ID 60 should be added but returned None")

        self.assertEqual(result["id"], new_supplier["id"])


        

if __name__ == '__main__':
    unittest.main()