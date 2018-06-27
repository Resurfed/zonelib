from enum import Enum
from entities.hooks import EntityPostHook, EntityCondition
from listeners import OnEntityDeleted, OnEntityOutput
from .session import map_session
from .containers import RouteContainer
from .decorators import PostHookFilter


class ZoneEvents(Enum):
    """ All possible zone events. """
    ENTER = "start_touch"
    EXIT = "end_touch"


@EntityPostHook(EntityCondition.equals_entity_classname("trigger_multiple"), 'start_touch')
@PostHookFilter("trigger_multiple")
def on_start_touch(entity, player):
    print(f"whoa this happens id {entity.index}")
    try:
        zone = map_session.get_zone(entity.index)
    except KeyError:
        return

    RouteContainer.get_container(
        (zone.endpoint, ZoneEvents.ENTER)
    ).route.call(zone, player)


@EntityPostHook(EntityCondition.equals_entity_classname("trigger_multiple"), 'end_touch')
@PostHookFilter("trigger_multiple")
def on_end_touch(entity, player):
    try:
        zone = map_session.get_zone(entity.index)
    except KeyError:
        return

    RouteContainer.get_container(
        (zone.endpoint, ZoneEvents.EXIT)
    ).route.call(zone, player)


@OnEntityDeleted
def on_entity_deleted(entity):
    if entity.classname == 'trigger_multiple':
        map_session.delete_zone(entity.index)
