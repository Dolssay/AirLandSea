from player import player
from unitCard import unitCard
from baseDeck import baseDeck
from theaterState import TheaterState
from enums import Ability, Theater, PassiveIDs, TriggerIDs
import random


class gameState:
    '''
    A single game for both players.
    '''
    # Standard attributes
    playerA: player
    playerB: player
    theatersA: list[TheaterState]
    theatersB: list[TheaterState]
    theaterAdjecency: dict[Theater, list[Theater]]
    deck: list[unitCard]

    # In-game attributes
    # Used for Airdrop
    airDrop: dict[str, bool] = {}
    # Used for Containment
    containment: bool = False
    # Used for Escalation
    escalation : bool = False


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

        :param name: The name of the player whose theater states to get
        :type name: str

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

        :param name: The player whose hand to get
        :type name: str

        :return: The player's hand
        :rtype: list[unitCard]
        '''
        player = self.get_player(name)
        return player.get_hand()


    def apply_passive_ability(self, passive_id: PassiveIDs, theater: Theater):
        '''
        Applies all ongoing passive abilities to the game state.
        '''
        if passive_id == PassiveIDs.Support:
            # Support ability effect:
            # +3 strength to adjacent theaters
            adjacent_theaters = self.theaterAdjecency[theater]
        elif passive_id == PassiveIDs.Aerodrome:
            # Implement Aerodrome ability effect
            pass
        elif passive_id == PassiveIDs.Containment:
            # Implement Containment ability effect
            pass
        elif passive_id == PassiveIDs.CoverFire:
            # Implement Cover Fire ability effect
            pass
        elif passive_id == PassiveIDs.Escalation:
            # Implement Escalation ability effect
            pass
        elif passive_id == PassiveIDs.Blockade:
            # Implement Blockade ability effect
            pass

    def remove_passive_ability(self, passive_id: PassiveIDs, theater: Theater):
        '''
        Removes an ongoing passive ability from the game state.
        '''
        if passive_id == PassiveIDs.Support:
            # Remove Support ability effect:
            # -3 strength from adjacent theaters
            adjacent_theaters = self.theaterAdjecency[theater]
        elif passive_id == PassiveIDs.Aerodrome:
            # Implement removal of Aerodrome ability effect
            pass
        elif passive_id == PassiveIDs.Containment:
            # Implement removal of Containment ability effect
            pass
        elif passive_id == PassiveIDs.CoverFire:
            # Implement removal of Cover Fire ability effect
            pass
        elif passive_id == PassiveIDs.Escalation:
            # Implement removal of Escalation ability effect
            pass
        elif passive_id == PassiveIDs.Blockade:
            # Implement removal of Blockade ability effect
            pass


    def apply_triggered_ability(self, triggered_id: TriggerIDs, theater: Theater):
        '''
        Applies all one time triggered abilities to the game state.
        '''
        if triggered_id == TriggerIDs.Airdrop:
            # Implement Airdrop ability effect
            pass
        elif triggered_id in TriggerIDs.Manuever:
            # Implement Manuever ability effect
            pass
        elif triggered_id == TriggerIDs.Reinforce:
            # Implement Reinforce ability effect
            pass
        elif triggered_id == TriggerIDs.Ambush:
            # Implement Ambush ability effect
            pass
        elif triggered_id == TriggerIDs.Disrupt:
            # Implement Disrupt ability effect
            pass
        elif triggered_id == TriggerIDs.Transport:
            # Implement Transport ability effect
            pass
        elif triggered_id == TriggerIDs.Redeploy:
            # Implement Redeploy ability effect
            pass


    def draw_a_card(self, name: str) -> unitCard:
        '''
        Draws a card from the deck and gives it to the specified player.

        :param name: The player to draw the card for
        :type name: str

        :return: The drawn card
        :rtype: unitCard
        '''
        player = self.get_player(name)
        card = self.deck.pop()
        player.draw_card(card)
        return card

    def play_card(self, name: str, index: int, 
                  target_theater: Theater, facedown: bool) -> unitCard:
        '''
        The specified player plays a card from their hand.

        :param name: The player playing the card
        :type name: str
        :param index: The index of the card in the player's hand
        :type index: int

        :return: The played card
        :rtype: unitCard
        '''
        try:
            # Get the player who is playing the card
            player = self.get_player(name)
            card_played =  player.play_card(index, facedown)

            # Then, add the card to the correct theater state
            if player.is_player_a():
                for theater_state in self.theatersA:
                    if theater_state.theater == target_theater:
                        theater_state.add_card(card_played)
                        break
            else:
                for theater_state in self.theatersB:
                    if theater_state.theater == target_theater:
                        theater_state.add_card(card_played)
                        break

            # If the played card has a passive ability, activate it for the game state
            if card_played.ability_type == Ability.Passive:
                self.apply_passive_ability(card_played.id, target_theater)

            # If the card has an active ability, call the ability handler
            if card_played.ability_type == Ability.Activate:
                self.apply_triggered_ability(card_played.id, target_theater)

            return card_played
        except Exception as e:
            raise e