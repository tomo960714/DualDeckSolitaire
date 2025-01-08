from typing import List

from enum import Enum

##{"Hearts", "Diamonds", "Clubs", "Spades"}
class CardSuit(Enum):
    HEARTS = "H"
    DIAMONDS = "D"
    CLUBS = "C"
    SPADES = "S"

CardRank = Enum("CardRank", {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13})



class CardClass:
    """ 
    Class to uniquely identify cards

    Args:
    suit: Suits : "Hearts" | "Diamonds" | "Clubs" | "Spades"
    number: numeric representaion of the cards (1-13)
    AB_deck: distinction between A and B decks
    name: representaion of the cards color,symbol and AB_deck (eg. Hearts Ace A -> HAA)
     """

    def __init__(self,suit:str,rank:int,AB_deck:str):
        
        if not self._is_valid_card_suit(suit):
            raise ValueError(f"Invalid card rank: {rank}. Must be between 1 (Ace) and 13 (King).")
        if not self._is_valid_card_number(rank):
            raise ValueError(f"Invalid card rank: {rank}. Must be between 1 (Ace) and 13 (King).")
        if not self._is_deck_valid(AB_deck):
            raise ValueError(f"Invalid value: {AB_deck}. Must be 'A' or 'B'.")

        
        
        self.suit = CardSuit(suit)
        self.rank = CardRank(rank)
        self.AB_deck = AB_deck.upper()
        self.name = self._set_name()

    
    @staticmethod
    def _is_valid_card_number(value:int) -> bool :
        """Internal method to check if a rank is valid."""
        try:
            CardRank(value)
            return True
        except ValueError:
            return False
        
    @staticmethod
    def _is_valid_card_suit(value:str) -> bool:
        """Internal method to check if a suit is valid."""
        try:
            CardSuit(value)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def _is_deck_valid(value:str) -> bool:
        """Internal method to check if the deck is valid."""
        try:
            if value in ("A","B"):
                return True
        except ValueError:
            return False

    def _set_name(self) -> str:
        return self.suit.value + str(self.rank.name) + self.AB_deck
    
class StackClass:
    def __init__(self,position: int):
        if position < 1 or position > 13:
            raise ValueError( f"Invalid Stack position at position {position}, number has to be between 1 and 13")
        if position >10:
            position = position 
        self.position = position
        self.cards: List[CardClass] = []

    def add_card(self,new_card:CardClass):
        self.cards.append(new_card)
    
    def take_card_out(self,position_in_list: int):
        if position_in_list > self.cards.length:
            raise ValueError(f"Stack has less than {position_in_list} cards! Pick a smaller number!")
        
        return self.cards.pop(position_in_list) # return the taken out card
    
    def show_all_cards(self):
        print(f"Cards at position {self.position}:")
        print(*[card.name for card in self.cards], sep=", ")

    def reset_stack(self):
        self.cards.clear()

class DeckClass:
    def __init__(self):
        self.cards: List[CardClass] = []

    def get_top_card(self):
        return self.cards[-1]
    
    def add_card(self,new_card:CardClass):
        self.cards.append(new_card)
    
    def show_all_cards(self):
        print("Cards in Deck:")
        print(*[card.name for card in self.cards], sep=", ")