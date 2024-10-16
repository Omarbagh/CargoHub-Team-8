import json
import os
import pytest
from models.locations import Locations


class TestLocations:
    def setup(self):
        self.location_file = 'data/locations.json'

        # Backup het originele bestand als het bestaat
        if os.path.exists(self.location_file):
            with open(self.location_file, 'r') as f:
                self.original_data = json.load(f)
        else:
            self.original_data = []

        # Dummy data
        self.initial_data = [
            {
                "id": 34533,
                "warehouse_id": 58,
                "code": "Q.26.2",
                "name": "Row: Q, Rack: 26, Shelf: 2",
                "created_at": "2018-01-25 21:36:16",
                "updated_at": "2018-01-25 21:36:16"
            }
        ]

        # Schrijf dummy data naar testbestand
        with open(self.location_file, 'w') as f:
            json.dump(self.initial_data, f)

        # Instantieer Locations class
        self.locations = Locations(root_path='data/', is_debug=False)

    def teardown_method(self):
        # Zet originele data terug
        with open(self.location_file, 'w') as f:
            json.dump(self.original_data, f)

    def test_get_locations(self):
        locations_data = self.locations.get_locations()
        assert isinstance(locations_data, list)
        assert len(locations_data) == 1

    def test_get_location(self):
        location = self.locations.get_location(34533)
        assert location is not None
        assert location["id"] == 34533

    def test_add_location(self):
        # Dummy locatie met uniek ID
        new_location = {
            "id": 34534,  # Nieuw, uniek ID
            "warehouse_id": 59,
            "code": "Q.26.3_dummy",
            "name": "Row: Q, Rack: 26, Shelf: 3_dummy"
        }

        self.locations.add_location(new_location)
        self.locations.save()

        locations_data = self.locations.get_locations()
        assert len(locations_data) == 2

    def test_update_location(self):
        updated_location = {
            "id": 34533,
            "warehouse_id": 58,
            "code": "UpdatedCode",
            "name": "Updated location name"
        }

        self.locations.update_location(34533, updated_location)
        location = self.locations.get_location(34533)
        assert location["code"] == "UpdatedCode"
        assert location["name"] == "Updated location name"

    def test_remove_location(self):
        self.locations.remove_location(34533)
        self.locations.save()
        location = self.locations.get_location(34533)
        assert location is None
