from enums import Theater, Ability


class unitCard:
    '''
    A unit card in the game.
    '''
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


    def change_strength(self, new_strength: int):
        '''
        Changes the current strength of the card.

        :param new_strength: The new strength value
        :type new_strength: int
        '''
        self.strength = new_strength

    def flip_card(self):
        '''
        Flips the card.
        '''
        self.facedown = not self.facedown
