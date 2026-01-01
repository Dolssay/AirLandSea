from enums import Theater
from unitCard import unitCard

class TheaterState:
    '''
    A state of a single theater for a player.
    '''
    # Static attribute
    theater: Theater
    cards: list[unitCard]

    # In-game attributes
    # used for Support
    added_strength: int = 0
    # used for Blockade
    blocked: bool = False


    def __init__(self, theater: Theater):
        self.theater = theater
        self.cards: list[unitCard] = []


    def add_card(self, card: unitCard, allowed : bool = False):
        '''
        Adds a card to the theater, updates total strength and card list.
        
        :param card: The card to add
        :type card: unitCard
        '''
        if allowed:
            pass
        elif not card.facedown and card.theater != self.theater:
            raise ValueError("Cannot play a faceup card in a different theater.")
        elif self.blocked:
            raise ValueError("Cannot play a card in a blocked theater by Blockade.")
        
        self.cards.append(card)


    def remove_card(self, index: int) -> unitCard:
        '''
        Removes a card from the theater by index, updates total strength and card list.

        :param index: The index of the card to remove
        :type index: int

        :return: The removed card
        :rtype: unitCard
        '''
        return self.cards.pop(index)


    def get_strength(self) -> int:
        '''
        Returns the total strength of the theater.

        :return: Total strength
        :rtype: int
        '''
        return sum(card.strength for card in self.cards)
    

    def get_cards(self) -> list[unitCard]:
        '''
        Returns the list of cards in the theater.

        :return: List of cards
        :rtype: list[unitCard]
        '''
        return self.cards