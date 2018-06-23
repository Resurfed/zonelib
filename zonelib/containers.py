class BaseContainer:
    """ Mixin for class self-management. """
    def __init_subclass__(cls):
        cls.containers = {}

    @classmethod
    def get_containers(cls):
        return cls.containers.values()

    @classmethod
    def get_container(cls, index):
        try:
            return cls.containers[index.as_key()]
        except KeyError:
            container = cls(index)
            cls.containers[index] = container
            return container

    @classmethod
    def make_container(cls, index):
        container = cls(index)
        cls.containers[index] = container
        return container


class RouteContainer(BaseContainer):
    """ Manages instances of routes. """
    def __init__(self, route):
        self.route = route
