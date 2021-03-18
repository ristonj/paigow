from enum import Enum

class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self) -> str:
        switcher = {
            1: "♣",
            2: "♦",
            3: "♥",
            4: "♠"
        }
        return switcher[self.value]


class Card:
    def __init__(self, rank: int, suit: Suit) -> None:
        if((rank < 1) or (rank > 13)):
            raise ValueError("Rank must be between 1 and 13")
        self._rank = rank
        self._suit = suit
    
    def __eq__(self, card: object) -> bool:
        if not isinstance(card, Card):
            raise NotImplementedError

        return self._rank == card._rank
    
    def __ge__(self, card: object) -> bool:
        return not self < card
    
    def __gt__(self, card: object) -> bool:
        return (not self < card) and self != card
    
    def __le__(self, card: object) -> bool:
        return self < card or self == card
    
    def __lt__(self, card: object) -> bool:
        if not isinstance(card, Card):
            raise NotImplementedError
        
        if(self._rank == 1):
            return False

        if(card._rank == 1):
            return True
        
        return self._rank < card._rank
    
    def __ne__(self, card: object) -> bool:
        return not self == card
    
    def __str__(self) -> str:
        rank_lookup = {
            1: "A",
            10: "T",
            11: "J",
            12: "Q",
            13: "K"
        }
        rank_str = rank_lookup.get(self._rank)
        if not rank_str:
            rank_str = str(self._rank)
        return rank_str + str(self._suit)