import json
import importlib
from messages import SayText2
from engines.server import global_vars
from mathlib import Vector
import sys
from paths import DATA_PATH
import zonelib
import importlib
importlib.reload(zonelib)

@zonelib.ZoneRoute('course', zonelib.ZoneEvents.ENTER)
def dec_course_enter(zone, player):
    SayText2(f"entered decorated zone {zone.endpoint}").send()


def course_zone_enter(zone, player):
    SayText2(f"entered custom zone {zone.endpoint}").send()


def course_zone_exit(zone, player):
    SayText2(f"left custom zone {zone.endpoint}").send()

zone_list = []

with open(DATA_PATH + '/zones.json') as json_data:
    data = json.load(json_data)

    for zone in data[global_vars.map_name]['zones']:

        tz = zonelib.Zone(
            zone['endpoint'],
            Vector(*zone['start']),
            Vector(*zone['end'])
        )

        zone_list.append(tz)

zonelib.create(zone_list)

zonelib.set_event_handlers(
    [
        zonelib.Route(
            endpoint='course',
            event=zonelib.ZoneEvents.ENTER,
            handler=course_zone_enter
        ),
        zonelib.Route(
            endpoint='course',
            event=zonelib.ZoneEvents.EXIT,
            handler=course_zone_exit
        )
    ]
)
