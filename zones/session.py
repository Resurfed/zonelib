"""
"""

from models import Map
from helpers import create_trigger


class MapSession(Map):
    """ Manages the map state. """
    def add_zone(self, zone):
        if zone not in self.__zones.values():
            entity = create_trigger(zone)
            self.__zones[entity] = zone

    def add_zones(self, zones):
        for zone in zones:
            self.__zones(zone)

    def delete_zone(self, zone):
        self.__zones.pop(zone)

map_session = MapSession('name')
