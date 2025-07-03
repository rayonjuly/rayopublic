import numpy as np 
import pandas as pd
# Source: https://www.kaggle.com/code/raskoshik/tutorial-object-oriented-programming-in-python

rank_list = range(1,13+1)
suit_list = ['A', 'B', 'C', 'D']
rank_list_3cay = range(1, 9+1)

# print a number using commas as thousand seperators
def format_number(num):
    return '{:,}'.format(num)

def split_list_into_chunks(l):
    """Split a list into chunks of 3 elements
    """
    try:
        num_of_chunks = int(len(l) / 3)
        np.random.shuffle(l)
        result = []
        for i in range(num_of_chunks):
            low = 3 * i 
            high = 3 * (i+1)
            result.append(l[low : high])

        return result
    
    except ValueError:
        print("The length of the list must be divided by 3.")
    


class Card():
    """Attributes and methods of a Card"""

    def __init__(self, rank:int = None, suit:str = None, game = None): 
        """initiate a new instance"""
        if game == None:
            if rank is None:
                rank = np.random.choice(rank_list, 1)[0]
            if suit is None:
                suit = np.random.choice(suit_list, 1)[0]
        elif game == "3_cay":
            if rank is None:
                rank = np.random.choice(rank_list_3cay, 1)[0]
            if suit is None:
                suit = np.random.choice(suit_list, 1)[0]
        self.__rank = rank
        self.__suit = suit
        self.__name = str(rank) + suit
    # Example of setter methods
    def set_rank(self, rank):
        self.__rank = rank
    def set_suit(self, suit):
        self.__suit = suit
    # Example of getter methods
    def get_rank(self):
        return self.__rank
    def get_suit(self):
        return self.__suit
    def get_name(self):
        return self.__name
    
    # Compare the Cards
    # Check 
    def is_equal(self, other_card):
        if self.get_rank() == other_card.get_rank() and self.get_suit() == other_card.get_suit():
            return True
        else:
            return False
    def is_suit_greater_than(self, other_card):
        if self.get_suit() == other_card.get_suit():
            return False
        else:
            return not (self.get_suit() > other_card.get_suit())
    # Check if a card is greater than another card
    def is_greater_than(self, other_card):
        """Check if a card is greater than another card
        Args:
            other_card (Card): another Card to compare with
        Returns:
           bool
        """
        if self.is_equal(other_card):
            return False 
        elif self.is_suit_greater_than(other_card):
            return True
        elif other_card.is_suit_greater_than(self):
            return False
        elif self.get_suit() == other_card.get_suit() and self.get_suit() != 'A':
            return self.get_rank() > other_card.get_rank()
        elif self.get_suit() == other_card.get_suit() and self.get_suit() == 'A' and self.get_rank() == 1:
            return True
        elif self.get_suit() == other_card.get_suit() and self.get_suit() == 'A' and other_card.get_rank() == 1:
            return False
        else:
            return self.get_rank() > other_card.get_rank()
    # Check if a Card is in a list
    def is_in(self, card_list):
        for c in card_list:
            if self.is_equal(c):
                return True
            else:
                return False
    # print
    def  __str__(self):
        return self.__name
class Player():
    


    def __init__(self, name: str = None, start_budget: int = None):

        # 'hand' attribute
        self.__name = name
        # 'start_budget' attribute
        self.__start_budget = None # declare the attribute __start_budget
        if start_budget == None:
            # while not isinstance(self.__start_budget, int):
            #     try:
            #         self.__start_budget = int(input("What is the player's start_budget? "))
            #     except ValueError:
            #         print("Invalid integer string: start_budget")
            start_budget = 1000 * np.random.randint(low = 10, high = 1000+1)
            self.__start_budget = start_budget
        else:
            self.__start_budget = start_budget

        # 'current_budget' attribute
        self.__current_budget = self.__start_budget

        # 'hand' attribute
        self.__hand = None

    # print
    def __str__(self):
        return (
            self.__name + 
            ': Start budget: ' + format_number(self.get_start_budget()) + 
            '. Type: ' + self.__type + 
            '. Current budget: ' + format_number(self.get_current_budget()) +
            '. PNL: ' + format_number(self.get_pnl())        
            )
    # getter
    def get_start_budget(self):
        return self.__start_budget
    
    def get_current_budget(self):
        return self.__current_budget
    
    def get_type(self):
        return self.__type
    
    def get_pnl(self):
        pnl = self.get_current_budget() - self.get_start_budget()
        return pnl
    
    def get_hand(self):
        return self.__hand
    
    # setter
    def set_name(self, name):
        self.__name = name
        
    def set_hand(self, hand):
        self.__hand = hand
        
class Normal_Player(Player):
    
    min_bet = 10000
    max_bet = 50000
    
    def __init__(self, name: str = None, start_budget: int = None):
        super().__init__(name, start_budget)
        self.__type = 'Normal Player'
        
    def get_max_possible_bet(self):
        return min(
            self.get_current_budget()
            , self.__class__.max_bet
        )
    
    def get_min_possible_bet(self):
        return min(
            self.get_current_budget()
            ,self.__class__.min_bet
        )
        
    # def set_bet(self, manual: bool = False)
    #     if manual == True:
    #         user_input = 0
    #         while True:
    #             try:
    #                 user_input = int(input(f'Your current budget is {self.get_current_budget()}. What is your bet? '))
    #             except ValueError:
    #                 print('Your bet must be an integer.')
    #             else:
    #                 break
        

class Deck():
    def __init__(self, game = None):
        list_of_card = []
        if game == None:
            for i in rank_list:
                for j in suit_list:
                    list_of_card.append(Card(i,j))
        elif game == "3_cay":
            for i in rank_list_3cay:
                for j in suit_list:
                    list_of_card.append(Card(i,j))
        self._content = list_of_card

    def get_content(self):
        return self._content
    def __str__(self):
        for i in self.get_content():
            print(i)

class Hand():
    deck = Deck().get_content()
    # def __init__(self, card1: Card = None, card2: Card = None, card3: Card = None):
    #     kw_cards = [card1, card2, card3] # list all the cards declared in the paramaters
    #     content = [c for c in kw_cards if c != None] # list all the not-none cards declared in the  parameters

    #     for c in kw_cards:
    #         if c == None:
    #             c = Card(game= "3_cay")
    #             while c.is_in(content):
    #                 c = Card()
    #             content.append(c)

    #     self.__card1 = content[0]
    #     self.__card2 = content[1]
    #     self.__card3 = content[2]

    #     self.__content = content

    def __init__(self, card_list: list[Card] = [None, None, None]):
        content = [c for c in card_list if c != None] # list all the not-none cards declared in the  parameters
        for c in card_list:
            if c == None:
                c = Card(game= "3_cay")
                while c.is_in(content):
                    c = Card()
                content.append(c)

        self.__card1 = content[0]
        self.__card2 = content[1]
        self.__card3 = content[2]

        self.__content = content

    def get_content(self):
        return self.__content
    
    def get_sum(self):
        if (self.__card1.get_rank() + self.__card2.get_rank() + self.__card3.get_rank()) % 10 == 0:
            value = 10
        else:
            value = (self.__card1.get_rank() + self.__card2.get_rank() + self.__card3.get_rank()) % 10
        return value
    
    def get_max_card(self):
        c1 = self.__card1
        c2 = self.__card2
        c3 = self.__card3
        if c1.is_greater_than(c2) and c1.is_greater_than(c3):
            return c1
        elif c2.is_greater_than(c1) and c2.is_greater_than(c1):
            return c2
        else:
            return c3
        
    def __str__(self):
        return 'Hand: ' + self.__card1.get_name() + ' ' + self.__card2.get_name() + ' ' + self.__card3.get_name() + '. ' + 'Sum: ' + str(self.get_sum()) + '. Type: ' + self.get_type()
    
    def get_rank_list(self):
        rank_list_of_hand = []
        for card in self.get_content():
            rank_list_of_hand.append(card.get_rank())
        return rank_list_of_hand
    
    def get_suit_list(self):
        suit_list_of_hand = []
        for card in self.get_content():
            suit_list_of_hand.append(card.get_suit())
        return suit_list_of_hand
    
    def rank_is_unique(self):
        return pd.Series(self.get_rank_list()).nunique() == 1
    
    def suit_is_unique(self):
        return pd.Series(self.get_suit_list()).nunique() == 1
    
    def rank_is_incremental(self):
        return (
            pd.Series(self.get_rank_list()).nunique() == 3 
            and
            (pd.Series(self.get_rank_list()).max() - pd.Series(self.get_rank_list()).min() == 2)
        )
    
    def get_type(self):
        if self.rank_is_unique() == True:
            return 'Sáp'
        elif self.rank_is_incremental() == True and self.suit_is_unique() == True:
            return 'Dây'
        elif sum(self.get_rank_list()) == 10:
            return '10'
        else:
            return 'Thường'
        
    def get_type_number_form(self):
        if self.get_type() == 'Dây':
            return 4
        elif self.get_type() == 'Sáp':
            return 3
        elif self.get_type() == '10':
            return 2
        elif self.get_type() == 'Thường':
            return 1
        
    def is_greater_than(self, other_hand):
        """Compare 2 hands. Check if self is greater than other_hand.
        """
        self_type = self.get_type_number_form()
        other_type = other_hand.get_type_number_form()
        self_sum = self.get_sum()
        other_sum = other_hand.get_sum()
        self_max = self.get_max_card()
        other_max = other_hand.get_max_card()
        if self_type > other_type:
            return True
        elif self_type < other_type:
            return False
        elif self_type == other_type and self_type != 1:
            return self_max.is_greater_than(other_max)
        elif self_type == other_type and self_type == 1:
            if self_sum == other_sum:
                return self_max.is_greater_than(other_max)
            else:
                return self_sum > other_sum
class Match():

    __num_of_round = None

    # start
    def set_start_player_num(self, num: int):
        self.__start_player_num = num

    def get_start_player_num(self):
        return self.__start_player_num
    
    def get_start_player_list(self):
        return self.__start_player_list
    
    def set_round_num(self, num: int):
        self.__num_of_round = num
        
    def get_round_num(self):
        return self.__num_of_round
    
    # current
    def set_current_player_num(self, num: int):
        self.__class__.__current_player_num = num

    def get_current_player_num(self):
        return self.__class__.__current_player_num
    


    def __init__(self, start_player_num: int):

        self.__start_player_num = start_player_num
        print(f'Number of players in this Match: {self.get_start_player_num()}')
        self.__start_player_list = [] # declare the attribute __player_list
        for i in range(self.__start_player_num): # initiate the players
            if i == 0:
                name = 'Host'
                p = Player(name = name, type = 'host')
            else:
                name = 'Player ' + str(i)
                p = Player(name = name, type = 'normal')

            print(p)
            self.__start_player_list.append(p)

class Round():

    deck = Deck(game = '3_cay').get_content()
    __current_player_num = None

    def __init__(self, current_player_num: int):
        self.__current_player_num = current_player_num
        self.__card_num = 3 * self.__current_player_num 
        self.__card_dealt = split_list_into_chunks(list(np.random.choice(a = self.__class__.deck, size = self.__card_num , replace = False)))

    def __str__(self):
        return str([c.get_name() for c in self.get_card_dealt()])

    # setter
    def set_current_player_num(self, num):
        self.__current_player_num = num

    # getter
    def get_current_player_num(self, num):
        return self.__current_player_num
    
    def get_card_dealt(self):
        return self.__card_dealt
    
    def get_hand_list(self):
        hand_list = []
        for i in self.get_card_dealt():
            hand_list.append(Hand(i))

        return hand_list
    
    # other
    def deal_hand_to_player(self, player: Player, hand: Hand):
        player.set_hand(hand)

    
    
    

