from enums import Theater, Ability

class unitCard:
    # Static attributes
    id: int
    name: str
    theater: Theater
    ability: str
    ability_type: Ability
    strength: int

    # Changing attribute in the game
    facedown: bool
    covered: bool

    def __init__(self, id: int, name: str, 
                 theater: Theater, ability: str, 
                 ability_type: Ability, strength: int):
        self.id = id
        self.name = name
        self.theater = theater
        self.ability = ability
        self.ability_type = ability_type
        self.strength = strength
        self.facedown = False
        self.covered = False

