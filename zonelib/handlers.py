from enum import Enum
from entities.hooks import EntityPostHook, EntityCondition
from listeners import OnEntityDeleted, OnEntityOutput, OnLevelInit
from events import Event
from .containers import route_container, map_container
from .decorators import PostHookFilter


class ZoneEvents(Enum):
    """ All possible zone events. """
    ENTER = "start_touch"
    EXIT = "end_touch"


@EntityPostHook(
    EntityCondition.equals_entity_classname("trigger_multiple"),
    ZoneEvents.ENTER.value
)
@PostHookFilter("trigger_multiple")
def on_start_touch(entity, player):
    try:
        zone = map_container.get_session().get_zone(entity.index)
    except KeyError:
        return

    for route in route_container.get(zone.endpoint, ZoneEvents.ENTER):
        route.call(zone, player)


@EntityPostHook(
    EntityCondition.equals_entity_classname("trigger_multiple"),
    ZoneEvents.EXIT.value
)
@PostHookFilter("trigger_multiple")
def on_end_touch(entity, player):

    try:
        zone = map_container.get_session().get_zone(entity.index)
    except KeyError:
        return

    for route in route_container.get(zone.endpoint, ZoneEvents.EXIT):
        route.call(zone, player)


@OnEntityDeleted
def on_entity_deleted(entity):
    if entity.classname == 'trigger_multiple':
        try:
            map_container.get_session().deactivate_zone(entity.index)
        except KeyError:
            pass


@OnLevelInit
def on_level_init(map_name):
    map_container.reset_session()


@Event('round_start')
def round_start(game_event):
    map_container.get_session().respawn_zones()
