 import random

        class Card
            def __init__(self, suit, rank):
                self.suit = suit
                self.rank = rank
        
        class Deck
            def __init__(self):
                self.cards = []
                self.create_deck()
        
            def create_deck(self):
                suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
                ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
                for suit in suits:
                    for rank in ranks:
                        self.cards.append(Card(suit, rank))
        
            def shuffle(self):
                random.shuffle(self.cards)
        
            def draw_card(self):
                return self.cards.pop()
        
        class Hand:
            def __init__(self):
                self.cards = []
        
            def add_card(self, card):
                self.cards.append(card)
        
            def get_value(self):
                value = 0
                ace_count = 0
                for card in self.cards:
                    if card.rank in ['Jack', 'Queen', 'King']:
                        value += 10
                    elif card.rank == 'Ace':
                        value += 11
                        ace_count += 1
                    else:
                        value += int(card.rank)
        
                while value > 21 and ace_count > 0:
                    value -= 10
                    ace_count -= 1
        
                return value
        
        class Player:
            def __init__(self, name):
                self.name = name
                self.hand = Hand()
        
            def hit(self, deck):
                card = deck.draw_card()
                self.hand.add_card(card)
        
            def show_hand(self):
                print(f"{self.name}'s hand:")
                for card in self.hand.cards:
                    print(f"{card.rank} of {card.suit}")
        
        class BlackjackGame:
            def __init__(self):
                self.deck = Deck()
                self.deck.shuffle()
                self.player = Player("Player")
                self.dealer = Player("Dealer")
                self.player.hit(self.deck)
                self.player.hit(self.deck)
                self.dealer.hit(self.deck)
                self.dealer.hit(self.deck)
        
            def play(self):
                print("Welcome to Blackjack!")
                self.player.show_hand()
                print("Dealer's hand:")
                print(f"{self.dealer.hand.cards[0].rank} of {self.dealer.hand.cards[0].suit}")
                self.player_turn()
                self.dealer_turn()
                self.determine_winner()
        
            def player_turn(self):
                while True:
                    choice = input("Do you want to hit or stand? (h/s): ")
                    if choice.lower() == 'h':
                        self.player.hit(self.deck)
                        self.player.show_hand()
                        if self.player.hand.get_value() > 21:
                            print("Player busts! You lose.")
                            break
                    elif choice.lower() == 's':
                        break
        
            def dealer_turn(self):
                print("Dealer's turn:")
                print("Dealer's hand:")
                self.dealer.show_hand()
                while self.dealer.hand.get_value() < 17:
                    self.dealer.hit(self.deck)
                    print("Dealer hits.")
                    print("Dealer's hand:")
                    self.dealer.show_hand()
                    if self.dealer.hand.get_value() > 21:
                        print("Dealer busts! You win.")
                        break
                else:
                    print("Dealer stands.")
        
            def determine_winner(self):
                player_value = self.player.hand.get_value()
                dealer_value = self.dealer.hand.get_value()
                if player_value > dealer_value:
                    print("You win!")