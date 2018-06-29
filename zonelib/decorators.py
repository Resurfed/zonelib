import memory
from entities.entity import Entity
from players.entity import Player
from .models import Route
from .containers import route_container


class ZoneRoute:

    def __init__(self, endpoint, event):
        self.endpoint = endpoint
        self.event = event

    def __call__(self, callback):
        self.callback = callback
        route = Route(
            endpoint=self.endpoint,
            event=self.event,
            handler=callback
        )

        route_container.store(route)
        return callback


def PostHookFilter(classname):
    def real_decorator(f):
        def wrapper(*args, **kwargs):
            entity = memory.make_object(Entity, args[0][0])
            player = memory.make_object(Player, args[0][1])
            return f(entity, player) if entity.classname == classname else None
        return wrapper
    return real_decorator
