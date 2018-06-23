
from .session import map_session
from .models import Route
from .containers import RouteContainer


def create(zones):
    map_session.add_zones(zones)


def set_event_handlers(routes):
    for r in routes:
        RouteContainer.make_container(r)
