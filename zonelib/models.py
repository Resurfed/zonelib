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

    def __init__(
        self, endpoint, start, end,
        filter_name=None, properties={}, entity=None
    ):

        self.endpoint = endpoint
        self.start = start
        self.end = end
        self.filter_name = filter_name
        self.properties = properties
        self.entity = entity


class Map:
    """  A collection of zones. """
    def __init__(self):
        self._zones = []

    def add_zones(self, zones):
        for zone in zones:
            self.add_zone(zone)

    def add_zone(self, zone):
        if zone not in self._zones:
            self._zones.append(zone)

    def delete_zone(self, zone):
        self._zones.remove(zone, None)
