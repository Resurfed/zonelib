from . import zones

from zones.models import Zone
from zones.serializers import ZoneSerializer
from mathlib import Vector


def course_zone_enter(user, **flags):
    pass


def course_zone_exit(user, **flags):
    pass


zone_list = [
    Zone(name='start', Vector(1, 3, 5), Vector(2, 5, 9)).create(),
    Zone(name='end', Vector(2, 3, 4), Vector(5, 1, 9))
]

zones.create(zone_list)

zones.set_event_handlers(
    [
        zones.route(id='course', course_zone_enter, event=zones.events.ENTER),
        zones.route(id='course', course_zone_exit, event=zones.events.EXIT)
    ]
)



'''
OO Words

Dispatcher



'''