from typing import List


class CardClass:
    """ 
    Class to uniquely identify cards

    Args:
    color: "Hearts" | "Diamonds" | "Clubs" | "Spades"
    number: numeric representaion of the cards (1-13)
    AB_deck: distinction between A and B decks
    symbol: symbolic representaion of the number (A | 1-10 | J | Q | K)
    name: representaion of the cards color,symbol and AB_deck (eg. Hearts Ace A -> HAA)
     """

    def __init__(self,color: str,number: int, AB_deck: str):
        valid_colors = {"Hearts", "Diamonds", "Clubs", "Spades"}
        if number < 1 or number > 13:
            raise ValueError("Number must be between 1 and 13")
        if color not in valid_colors:
            raise ValueError(f"Color must be on of: Hearts, Diamonds, Clubs or Spades and given color is {color}")
        """ if AB_deck != "A" or AB_deck != "B":
            raise ValueError(f"AB_deck has to be A or B ") """
        
        
        self.color = color
        self.number = number
        self.AB_deck = AB_deck.upper()
        self.symbol = self._get_symbol(number)
        self.name = self._set_name()

    # Match the nr to the card symbol
    def _get_symbol(self,number:int) -> str :
        if number == 1:
            return "A"
        elif number == 11:
            return "J"
        elif number == 12:
            return "Q"
        elif number == 13:
            return "K"
        else:
            return str(number)
        
    def _set_name(self):
        return self.color[0] + self.symbol + self.AB_deck
    
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