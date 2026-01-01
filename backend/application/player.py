from unitCard import unitCard

class player:
    '''
    A single player in the game.
    '''

    name: str
    isA: bool
    hand: list[unitCard]
    winningPoints: int


    def __init__(self, name: str, isA: bool):
        self.name = name
        self.isA = isA
        self.hand = []
        self.winningPoints = 0


    def is_player_a(self) -> bool:
        '''
        Returns whether the player is the first player.

        :return: True if player A (first), False otherwise
        :rtype: bool
        '''
        return self.isA
    

    def draw_card(self, card: unitCard):
        '''
        Adds a card to the player's hand.

        :param card: the card to add
        :type card: unitCard
        '''
        self.hand.append(card)
    

    def get_hand(self) -> list[unitCard]:
        '''
        Return all cards in the player's hand.
        
        :return: List of cards in hand
        :rtype: list[unitCard]
        '''
        return self.hand


    def play_card(self, index: int, facedown: bool) -> unitCard:
        '''
        Removes a card from the player's hand and returns it.

        :param index: the index of the card to play
        :type index: int
        :param facedown: whether the card is going to be played facedown
        :type facedown: bool

        :return: the played card, unitCard
        :rtype: unitCard
        '''
        card = self.hand[index]
        self.hand.remove(card)
        card.facedown = facedown
        card.strength = 2 if facedown else card.strength
        return card
    

    def add_winning_points(self, points: int):
        '''
        Adds winning points to the player.

        :param points: the points to add
        :type points: int
        '''
        self.winningPoints += points