from enums import Theater
from unitCard import unitCard

class TheaterState:
    theater: Theater
    cards: list[unitCard]
    strength: int

    def __init__(self, theater: Theater):
        self.theater = theater
        self.cards: list[unitCard] = []
        self.strength = 0

    def add_card(self, card: unitCard):
        '''
        Adds a card to the theater, updates total strength and card list.
        
        :param card: The card to add
        :type card: unitCard
        '''
        # Update strength based on whether the card is facedown
        if not card.facedown:
            self.strength += card.strength
        else:
            self.strength += 2

        self.cards.append(card)

    def remove_card(self, index: int):
        '''
        Removes a card from the theater by index, updates total strength and card list.

        :param index: The index of the card to remove
        :type index: int
        '''
        card = self.cards[index]
        if not card.facedown:
            self.strength -= card.strength
        else:
            self.strength -= 2
        self.cards.remove(self.cards[index])

    def get_strength(self) -> int:
        '''
        Returns the total strength of the theater.

        :return: Total strength
        :rtype: int
        '''
        return self.strength
    
    def get_cards(self) -> list[unitCard]:
        '''
        Returns the list of cards in the theater.

        :return: List of cards
        :rtype: list[unitCard]
        '''
        return self.cards
    
    def update_strength(self, added_strength: int):
        '''
        Updates the total strength of the theater.

        :param added_strength: The amount to add to the strength
        :type added_strength: int
        '''
        self.strength += added_strength