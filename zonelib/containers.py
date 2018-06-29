from .session import MapSession


class RouteContainer:
    """ Manages instances of routes. """
    def __init__(self):
        self.routes = {}

    def get(self, endpoint, event):
        return self.routes.get(hash((endpoint, event)))

    def store(self, route):

        try:
            routes = self.routes[hash(route)]
        except KeyError:
            routes = []
            self.routes[hash(route)] = routes

        routes.append(route)


class MapSessionContainer:
    def get_session(self):
        try:
            return self.sessions
        except AttributeError:
            self.sessions = MapSession()
            return self.sessions

    def reset_session(self, index):
        self.sessions = MapSession()


route_container = RouteContainer()
map_container = MapSessionContainer()
