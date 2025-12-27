from enum import Enum

class Theater(Enum):
    Air = "Air"
    Land = "Land"
    Sea = "Sea"

class Ability(Enum):
    Activate = 1
    Passive = 2
    No = 3