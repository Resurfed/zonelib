
from .session import MapSession
from .models import Route
from .containers import route_container, map_container


def create(zones):
    map_container.get_session().add_zones(zones)


def set_event_handlers(routes):
    for r in routes:
        route_container.store(r)
