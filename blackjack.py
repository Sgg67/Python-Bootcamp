# import random module
import random
# intialize the playing variable
playing = True
# set up card details
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}
# Card class
class Card:
    # set the suit and rank of cards
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    # return the string equivalent of the cards
    def __str__(self):
        return f" {self.rank} of {self.suit}"

# Deck class
class Deck:
    def __init__(self):
        # intialize an arr corresponding to an empty deck
        self.deck = []
        # add all 52 cards to the deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    # shuffle cards
    def shuffle(self):
        random.shuffle(self.deck)

    # deal one card at a time
    def deal(self):
        single_card = self.deck.pop()
        return single_card

    # return string version of the cards in  the deck
    def __str__(self):
        whole_deck = ""
        for card in self.deck:
            whole_deck += '\n' + card.__str__()
        return "The Deck contains: " + whole_deck
        
    # a class for the value of the cards in a players hand
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# a class to keep track of a players chips
class Chips:
    def __init__(self):
        isValid = True
        while(isValid):
            try:
                num_chips = input("Enter the number of chips you want to buy: ")
                self.total = int(num_chips)
                isValid = False
                break
            except:
                print("That was not a valid number enter a valid number for the amount of chips you want to buy")
                continue
    # when player wins bet they get more chips 
    def win_bet(self):
        self.total += self.bet
    # when player loses bet they get lose chips
    def lose_bet(self):
        self.total -= self.bet

# logic for a player taking a bet
def take_bet(chips):
    while(True):
        try:
            chips.bet = int(input("Select the number of chips that you want to bet: "))
            break
        except ValueError:
            print("Value entered is not an integer, enter a valid integer")
        except:
            if chips.total - chips.bet < 0:
                print("Invalid bet, you do not have enough chips")
            else:
                break

# method signifying a player hitting
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# method that determines if a player hits or stands controlled by user input
def hit_or_stand(deck, hand):
    while(True):
            decision = input("Do you want to hit or stand, type h for hit or s for stand: ")
            if decision[0].lower() == "h":
                hit(deck, hand)
                break
            elif decision[0].lower() == "s":
                playing = False
                break
            else:
                print("Invalid choice enter h for hit and s for stand")
                continue

# dealer shows second card, player shows all cards
def show_some(player, dealer):
    print("\nDealers Cards")
    print(" Card Hidden")
    print(f"\n Dealers second card {dealer.cards[1]}")
    print("\n Player's Hand: ", *player.cards, sep="\n")

# both players show all decks
def show_all(player, dealer):
    print("\n Dealers deck: ", *dealer.cards)
    print("\n Players deck: ", *player.cards)
    print(f"\nValue of dealers deck: {dealer.value}")
    print(f"\nValue of players deck: {player.value}")

# method signifying player busts and they lose chips
def player_busts(chips):
    print("player busts! \n")
    chips.lose_bet()

# method signifying player wins and they gain chips
def player_wins(chips):
    print("Player wins \n")
    chips.win_bet()

# dealer wins and gains chips
def dealer_wins(chips):
    print("Dealer wins \n")
    chips.lose_bet()

# delaer loses and gives player chips
def dealer_busts(chips):
    print("Dealer busts! \n")
    chips.lose_bet()

# This is when it is a tie and neither parties lose or gain chips
def push():
    print("Dealer and Player tie! It's a push \n")

# logic for the black jack game
def main():
    global playing
    # while the game is still being played
    while True:
        # Introduce the game
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()
        take_bet(player_chips)
        show_some(player_hand, dealer_hand)

        while playing:
            # ask the player to hit or stand
            hit_or_stand(deck, player_hand)

            # show both player cards and one dealer card
            show_some(player_hand, dealer_hand)

            # If players hand is greater than 21 bust
            if player_hand.value > 21:
                player_busts(player_chips)
                break
            
        if player_hand.value <= 21:
                 
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

                show_all(player_hand, dealer_hand)

                if(dealer_hand.value > 21):
                     dealer_busts(player_chips)
                elif dealer_hand.value > player_hand.value:
                     dealer_wins(player_chips)
                elif dealer_hand.value < player_hand.value:
                     player_wins(player_chips)
                else:
                    push()
                 
        print("\nPlayer's winnings stand at",player_chips.total)

        new_game = input("Would you like to play another hand, enter y for yes and n for no? ")

        if new_game[0].lower()=='y':
            playing = True
            continue
        else:
            print("Thanks for playing")
            break


if  __name__ == "__main__":
    main()



