from enum import Enum


class Theater(Enum):
    Air = 1
    Land = 2
    Sea = 3


class Ability(Enum):
    Activate = 1
    Passive = 2
    No = 3


class PassiveIDs(Enum):
    Support = 1
    Aerodrome = 4
    Containment = 5
    CoverFire = 10
    Escalation = 14
    Blockade = 17

class TriggerIDs(Enum):
    Airdrop = 2
    Manuever = (3, 9, 15)
    Reinforce = 7
    Ambush = 8
    Disrupt = 11
    Transport = 13
    Redeploy = 16