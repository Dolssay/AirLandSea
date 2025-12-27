from enums import Ability, Theater
from unitCard import unitCard

def get_air_cards() -> list[unitCard]:
    return [
            # -------- AIR (1–6) --------
            unitCard(1, "Support", Theater.Air,
                     "You gain +3 strength in each adjacent theater.",
                     Ability.Passive, 1),

            unitCard(2, "Air Drop", Theater.Air,
                     "The next time you play a card, you may play it to a non-matching theater.",
                     Ability.Activate, 2),

            unitCard(3, "Maneuver", Theater.Air,
                     "Flip an uncovered card in an adjacent theater.",
                     Ability.Activate, 3),

            unitCard(4, "Aerodrome", Theater.Air,
                     "You may play cards of strength 3 or less to non-matching theaters.",
                     Ability.Activate, 4),

            unitCard(5, "Containment", Theater.Air,
                     "If any player plays a facedown card, destroy that card.",
                     Ability.Passive, 5),

            unitCard(6, "Heavy Bombers", Theater.Air,
                     "",
                     Ability.No, 6),
    ]

def get_land_cards() -> list[unitCard]:
    return [
            # -------- LAND (7–12) --------
            unitCard(7, "Reinforce", Theater.Land,
                     "Draw a card and play it facedown to an adjacent theater.",
                     Ability.Activate, 1),

            unitCard(8, "Ambush", Theater.Land,
                     "Flip any uncovered card.",
                     Ability.Activate, 2),

            unitCard(9, "Maneuver", Theater.Land,
                     "Flip an uncovered card in an adjacent theater.",
                     Ability.Activate, 3),

            unitCard(10, "Cover Fire", Theater.Land,
                     "All cards covered by this card are now strength 4.",
                     Ability.Passive, 4),

            unitCard(11, "Disrupt", Theater.Land,
                     "Starting with you, both players choose and flip 1 of their uncovered cards.",
                     Ability.Activate, 5),

            unitCard(12, "Heavy Tanks", Theater.Land,
                     "",
                     Ability.No, 6),
    ]

def get_sea_cards() -> list[unitCard]:
    return [
            # -------- SEA (13–18) --------
            unitCard(13, "Transport", Theater.Sea,
                     "You may move 1 of your cards to a different theater.",
                     Ability.Activate, 1),

            unitCard(14, "Escalation", Theater.Sea,
                     "All of your facedown cards are now strength 4.",
                     Ability.Passive, 2),

            unitCard(15, "Maneuver", Theater.Sea,
                     "Flip an uncovered card in an adjacent theater.",
                     Ability.Activate, 3),

            unitCard(16, "Redeploy", Theater.Sea,
                     "You may return 1 of your facedown cards to your hand. If you do, play a card.",
                     Ability.Activate, 4),

            unitCard(17, "Blockade", Theater.Sea,
                     "If any player plays a card in an adjacent theater occupied by 3 or more cards, destroy that card.",
                     Ability.Passive, 5),

            unitCard(18, "Super Battleship", Theater.Sea,
                     "",
                     Ability.No, 6),
    ]

class baseDeck:
    _deck: list[unitCard]

    def __init__(self):
        self._deck = []
        self._deck.extend(get_air_cards())
        self._deck.extend(get_land_cards())
        self._deck.extend(get_sea_cards())

    def get_deck(self) -> list[unitCard]:
        return self._deck