from player import player
from unitCard import unitCard
from baseDeck import baseDeck
from theaterState import TheaterState
from enums import Theater, Passive
import random


class gameState:
    '''
    A single game for both players.
    '''

    playerA: player
    playerB: player
    theatersA: list[TheaterState]
    theatersB: list[TheaterState]
    theaterAdjecency: dict[Theater, list[Theater]]
    ongoingPassives: list[Passive]
    deck: list[unitCard]


    def __init__(self, playerA: player, playerB: player, 
                playingTheaters: list[Theater], randomState: random.Random):
        self.playerA = playerA
        self.playerB = playerB

        # Shuffle the playing theaters to randomize their order
        randomState.shuffle(playingTheaters)

        self.theatersA = [
            TheaterState(playingTheaters[0]),
            TheaterState(playingTheaters[1]),
            TheaterState(playingTheaters[2])
        ]

        self.theatersB = [
            TheaterState(playingTheaters[0]),
            TheaterState(playingTheaters[1]),
            TheaterState(playingTheaters[2])
        ]

        # The two ends are only adjacent to the middle theater
        self.theaterAdjecency = {
            playingTheaters[0]: [playingTheaters[1]],
            playingTheaters[1]: [playingTheaters[0], playingTheaters[2]],
            playingTheaters[2]: [playingTheaters[1]]
        }

        # Shuffle and set up the deck
        self.deck = baseDeck().get_deck()
        randomState.shuffle(self.deck)

        # Deal each player 6 cards
        for _ in range(6):
            self.playerA.draw_card(self.deck.pop())
            self.playerB.draw_card(self.deck.pop())

        # Initialize ongoing passive abilities
        self.ongoingPassives = []


    def get_theater_adjacency(self) -> dict[Theater, list[Theater]]:
        '''
        Returns the adjacency mapping of theaters.

        :return: Adjacency mapping
        :rtype: dict[Theater, list[Theater]]
        '''
        return self.theaterAdjecency


    def get_player(self, name: str) -> player:
        '''
        Returns the player object for the specified name.

        :param name: The name of the player
        :type name: str

        :return: The player object
        :rtype: player
        '''
        return self.playerA if name == self.playerA.name else self.playerB
    

    def get_theater_state(self, name: str) -> TheaterState:
        '''
        Returns the list of theater states for the specified player.

        :param player: The player whose theater states to get
        :type player: player

        :return: The player's theater states
        :rtype: list[TheaterState]
        '''
        player = self.get_player(name)
        if player.is_player_a():
            return self.theatersA
        else:
            return self.theatersB


    def get_deck_size(self) -> int:
        '''
        Returns the current size of the rest of the deck.

        :return: Size of the deck
        :rtype: int
        '''
        return len(self.deck)
    

    def get_player_hand(self, name: str) -> list[unitCard]:
        '''
        Returns the hand of the specified player.

        :param player: The player whose hand to get
        :type player: player

        :return: The player's hand
        :rtype: list[unitCard]
        '''
        player = self.get_player(name)
        return player.get_hand()
    

    def draw_a_card(self, name: str) -> unitCard:
        '''
        Draws a card from the deck and gives it to the specified player.

        :param player: The player to draw the card for
        :type player: player

        :return: The drawn card
        :rtype: unitCard
        '''
        player = self.get_player(name)
        card = self.deck.pop()
        player.draw_card(card)
        return card