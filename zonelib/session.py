""" """

from .models import Map
from .helpers import create_trigger


class MapSession(Map):
    """ Manages the map state. """

    def __init__(self):
        super().__init__()
        self._active_zones = {}

    def add_zone(self, zone):
        super().add_zone(zone)

        if zone not in self._active_zones.values():
            zone.entity = create_trigger(zone)
            self._active_zones[zone.entity.index] = zone

    def get_zone(self, index):
        return self._active_zones[index]

    def respawn_zones(self):
        self._active_zones = {}
        for zone in self._zones:
            self.add_zone(zone)

    def deactivate_zone(self, index):
        self._active_zones.pop(index)
