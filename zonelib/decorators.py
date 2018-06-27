import memory
from entities.entity import Entity
from players.entity import Player


def PostHookFilter(classname):
    def real_decorator(f):
        def wrapper(*args, **kwargs):
            entity = memory.make_object(Entity, args[0][0])
            player = memory.make_object(Player, args[0][1])
            return f(entity, player) if entity.classname == classname else None
        return wrapper
    return real_decorator
