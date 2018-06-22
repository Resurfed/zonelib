
import secrets
from engines.precache import Model
from entities.entity import Entity
from entities.constants import SolidType
from mathlib import Vector

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
    return entity
