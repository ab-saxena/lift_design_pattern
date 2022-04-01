import enum


class Direction(enum):
    up = 'up'
    down = 'down'
    idle = 'idle'


class LiftStatus(enum):
    start = 'start'
    stop = 'stop'
