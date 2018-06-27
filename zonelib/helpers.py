
import secrets
from engines.precache import Model
from entities.entity import Entity
from entities.constants import SolidType
from mathlib import Vector
from messages import SayText2

error = Model('models/error.mdl')


def vector_abs(vec):
    """ Absolute value of vector. """
    return Vector(abs(vec.x), abs(vec.y), abs(vec.z))


def get_relative_coordinates(start, end):
    """ Convert from fixed corner coordinates to origin and offset form."""
    origin = start + ((end - start) / 2.0)
    start -= origin
    end -= origin
    start = vector_abs(start) * -1.0
    end = vector_abs(end)
    start *= -1.0
    return origin, start, end

'''
def create_trigger(zone):
    """ Create an engine trigger. """
    offset = 100
    origin, mins, maxs = get_relative_coordinates(zone.start, zone.end)
    maxs += offset
    entity = Entity.create('trigger_multiple')
    entity.target_name = secrets.token_hex(nbytes=16)
    entity.filter_name = zone.filter_name
    entity.model = error  # error model
    entity.spawn()
    entity.origin = origin
    entity.mins = mins
    entity.maxs = maxs
    entity.wait = 0
    entity.solid_type = SolidType.BBOX
    entity.effects |= 0x020
    entity.spawn_flags = 257
    entity.call_input('Enable')
    print(f"origin: {str(origin)}, min: {str(mins)}, max: {str(maxs)}")
    SayText2(f"origin: {str(origin)}, min: {str(mins)}, max: {str(maxs)}").send()

    return entity

'''


def create_trigger(zone):
    return _create_trigger(zone.start, zone.end, "triggetname")


def _create_trigger(start: Vector, end: Vector, name: str):

    # Get center and points relative to center
    # end.z += 100
    center = ((end - start) * 0.5) + start
    start -= center
    end -= center
    start = Vector(abs(start.x), abs(start.y), abs(start.z))
    end = Vector(abs(end.x), abs(end.y), abs(end.z))
    start *= -1.0

    # Create trigger
    entity = Entity.create('trigger_multiple')
    entity.target_name = name

    entity.model = error  # error model
    entity.spawn()
    entity.origin = center
    entity.mins = start
    entity.maxs = end
    entity.wait = 0
    entity.solid_type = SolidType.BBOX
    entity.effects |= 0x020
    entity.spawn_flags = 257
    entity.call_input('Enable')

    SayText2(f"origin: {str(center)}, min: {str(start)}, max: {str(end)}").send()

    return entity

