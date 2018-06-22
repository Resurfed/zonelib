from entities.hooks import EntityPostHook, EntityCondition
from listeners import OnEntityDeleted
from session import map_session
from containers import RouteContainer
from events import ZoneEvents


@EntityPostHook(
    EntityCondition.equals_entity_classname("trigger_multiple"), 
    ZoneEvents.ENTER
)
def on_start_touch(entity, player):
    try:
        zone = map_session.get_zone(entity)
    except KeyError:
        return

    RouteContainer.get_container(
        (zone.endpoint, ZoneEvents.Enter)
    ).call(entity, player)


@EntityPostHook(
    EntityCondition.equals_entity_classname("trigger_multiple"),
    ZoneEvents.EXIT
)
def on_end_touch(entity, player):
    try:
        zone = map_session.get_zone(entity)
    except KeyError:
        return

    RouteContainer.get_container(
        (zone.endpoint, ZoneEvents.EXIT)
    ).call(entity, player)


@OnEntityDeleted
def on_entity_deleted(entity):
    if entity.classname == 'trigger_multiple':
        map_session.delete_zone(entity)
