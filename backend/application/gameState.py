from player import player
from unitCard import unitCard
from baseDeck import baseDeck
from theaterState import TheaterState
from enums import Theater
import random


class gameState:
    playerA: player
    playerB: player
    theatersA: list[TheaterState]
    theatersB: list[TheaterState]
    theaterAdjecency: dict[Theater, list[Theater]]
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