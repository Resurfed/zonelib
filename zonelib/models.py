class Route:
    """ A path from an endpoint to the callback function. """
    def __init__(self, endpoint, event, handler):
        self.endpoint = endpoint
        self.event = event
        self.handler = handler

    def call(self, entity, player):
        self.handler(entity, player)

    def __hash__(self):
        return hash((self.endpoint, self.event))

    def __eq__(self, other):
        return (self.endpoint, self.event) == (other.endpoint, other.event)

    def __ne__(self, other):
        return not self == other


class Zone:
    """ A generic representation of a zone. """

    def __init__(self, endpoint, start, end, filter_name=None, properties={}):
        self.endpoint = endpoint
        self.start = start
        self.end = end
        self.filter_name = filter_name
        self.properties = properties


class Map:
    """ For our needs, just a collection of zones representing
    map triggers. """
    def __init__(self, name, zones={}):
        self.name = name
        self._zone = zones

    def get_zone(self, zone):
        return self._zone[zone]

    def add_zones(self, zones):
        for zone in zones:
            self.add_zone(zone)

    def delete_zone(self, zone):
        self._zone.pop(zone, None)

    def add_zone(self, zone):
        if zone not in self._zone.values():
            self._zone[entity.index] = zone