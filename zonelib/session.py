"""
"""

from .models import Map
from .helpers import create_trigger


class MapSession(Map):
    """ Manages the map state. """
    def add_zone(self, zone):
        if zone not in self._zone.values():
            entity = create_trigger(zone)
            print(f"created entity #{str(entity.index)} - {str(dir(entity))})")
            self._zone[entity.index] = zone

    def add_zones(self, zones):
        for zone in zones:
            self.add_zone(zone)

    def delete_zone(self, zone):
        self._zone.pop(zone, None)

map_session = MapSession('name')
