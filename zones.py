from messages import SayText2
from mathlib import Vector

from . import zonelib


def course_zone_enter(zone, player):
    SayText2(f"entered custom zone {zone.endpoint}").send()


def course_zone_exit(zone, player):
    SayText2(f"left custom zone {zone.endpoint}").send()

zone_list = [
    zonelib.Zone(
        'course',
        Vector(-1096, -752, 11488),
        Vector(-843, -292, 11759),
        properties=["this worked"]
    )
]

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
