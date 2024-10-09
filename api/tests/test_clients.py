import json
import unittest
import os
from api.models.clients import Clients


class TestClients(unittest.TestCase):
    def setUp(self):
        self.client_file = 'data/clients.json'

        if os.path.exists(self.client_file):
            with open(self.client_file, 'r') as f:
                self.original_data = json.load(f)
        else:
            self.original_data = []

        self.initial_data = [
            {
                "id": 1,
                "name": "Raymond Inc",
                "address": "1296 Daniel Road Apt. 349",
                "city": "Pierceview",
                "zip_code": "28301",
                "province": "Colorado",
                "country": "United States",
                "contact_name": "Bryan Clark",
                "contact_phone": "242.732.3483x2573",
                "contact_email": "robertcharles@example.net",
                "created_at": "2010-04-28 02:22:53",
                "updated_at": "2022-02-09 20:22:35"
            },
            {
                "id": 2,
                "name": "Example Corp",
                "address": "123 Example St",
                "city": "Example City",
                "zip_code": "12345",
                "province": "Example State",
                "country": "Example Country",
                "contact_name": "John Doe",
                "contact_phone": "123-456-7890",
                "contact_email": "john@example.com",
                "created_at": "2011-01-01 12:00:00",
                "updated_at": "2021-01-01 12:00:00"
            }
        ]

        with open(self.client_file, 'w') as f:
            json.dump(self.initial_data, f)

        self.clients = Clients(root_path='data/', is_debug=False)

    def tearDown(self):
        with open(self.client_file, 'w') as f:
            json.dump(self.original_data, f)

    def test_get_clients(self):
        clients_data = self.clients.get_clients()
        self.assertIsInstance(clients_data, list)
        self.assertEqual(len(clients_data), 2)

    def test_get_client(self):
        client = self.clients.get_client(1)
        self.assertIsNotNone(client)
        self.assertEqual(client["id"], 1)

    def test_add_client(self):
        new_client = {
            "id": 3,
            "name": "New Client",
            "address": "456 New St",
            "city": "New City",
            "zip_code": "67890",
            "province": "New State",
            "country": "New Country",
            "contact_name": "Jane Smith",
            "contact_phone": "987-654-3210",
            "contact_email": "jane@example.com"
        }
        self.clients.add_client(new_client)
        print(self.clients.get_clients())
        self.assertEqual(len(self.clients.get_clients()), 3)

    def test_update_client(self):
        updated_client = {
            "id": 1,
            "name": "Updated Raymond Inc",
            "address": "Updated Address",
            "city": "Updated City",
            "zip_code": "99999",
            "province": "Updated Province",
            "country": "Updated Country",
            "contact_name": "Updated Bryan Clark",
            "contact_phone": "111-222-3333",
            "contact_email": "updated@example.com"
        }
        self.clients.update_client(1, updated_client)
        client = self.clients.get_client(1)
        self.assertEqual(client["name"], "Updated Raymond Inc")

    def test_remove_client(self):
        self.clients.remove_client(1)
        client = self.clients.get_client(1)
        self.assertIsNone(client)


if __name__ == "__main__":
    unittest.main()
