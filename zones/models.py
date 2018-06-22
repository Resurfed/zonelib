from helpers import create_trigger


class Route:
    """ A path from an endpoint to the callback function. """
    def __init__(self, endpoint, event, callback):
        self.endpoint = endpoint
        self.event = event
        self.callback = callback

    def call(self, entity, player):
        self.callback(entity, player)


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
        self.__zones = zones

    def get_zone(self, zone):
        return self.__zones[zone]
