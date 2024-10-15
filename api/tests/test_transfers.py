import unittest
from models import transfers
import json

class TestTransfers(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.transfers_instance = transfers.Transfers("path/to/your/root/", is_debug=True)

    def test_get_warehouse_by_id(self):
        
        with open('data/transfers.json') as file:
            expected_data = json.load(file)
            return expected_data
        
        
        result = self.transfers_instance.get_transfers(1)

        self.assertEqual(result, excepted_data[id] == 1)


    def test_get_transfers_invalid_id(self):
        result = self.transfers_instance.get_transfers(999)
        self.assertIsNone(result) 

    def test_add_transfers(self):
        new_transfers = {
            "id": 1,
        "reference": "TR00001",
        "transfer_from": null,
        "transfer_to": 9229,
        "transfer_status": "Completed",
        "created_at": "2000-03-11T13:11:14Z",
        "updated_at": "2000-03-12T16:11:14Z",
        "items": [
            {
                "item_id": "P007435",
                "amount": 23
            }
        ]
        }
        
        self.transfers_instance.add_warehouse(new_transfers)

        result = self.transfers_instance.get_transfers(60)

        self.assertIsNotNone(result, "Transfers with ID 60 should be added but returned None")

        self.assertEqual(result["id"], new_transfers["id"])


        

if __name__ == '__main__':
    unittest.main()