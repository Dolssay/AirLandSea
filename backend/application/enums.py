from enum import Enum


class Theater(Enum):
    Air = "Air"
    Land = "Land"
    Sea = "Sea"


class Ability(Enum):
    Activate = 1
    Passive = 2
    No = 3


class Passive(Enum):
    Support = 1
    Aerodrome = 2
    Containment = 3
    CoverFire = 4
    Escalation = 5
    Blockade = 6