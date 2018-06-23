from enum import Enum
from listeners import OnEntityDeleted, OnEntityOutput
from .session import map_session
from .containers import RouteContainer


class ZoneEvents(Enum):
    """ All possible zone events. """
    ENTER = "OnStartTouch"
    EXIT = "OnEndTouch"


@OnEntityOutput
def on_entity_output(output_name, activator, caller, value, delay):

    if caller.classname != 'trigger_multiple':
        return

    print("end touch event")
    try:
        event = ZoneEvents(output_name)
        zone = map_session.get_zone(caller.index)
    except ValueError:
        return

    print(f"entity output caller {str(caller)}, dir {str(dir(caller))}")
    print(f"entity output zone {str(zone)}, dir {str(dir(zone))}")

    RouteContainer.get_container(
        (zone.endpoint, event)
    ).call(entity, player)


@OnEntityDeleted
def on_entity_deleted(entity):
    if entity.classname == 'trigger_multiple':
        map_session.delete_zone(entity.index)
