'''

BlackJack Game

User Stories:

1) User can play the blackjack game in terminal against the dealer
2) Dealer automatically plays his hand with a fixed algorithm (If it's 16 or below they hit, if it's above 16, they stay)
3) User can play the blackjack game repeatedly
4) User can choose to hit or stay
5) User can see what cards they have been dealt
6) User can only see one dealer card, not the bottom card

Extension:
1) Multiple users can play blackjack game in terminal in a turn-based game
2) Consider using the stack data structure
3) User can bet dollar amounts in the blackjack game


'''

import random

suits = ('c','s','h','d')
rank = ('2','3','4','5','6','7','8','9','10','j','q','k','a')

suit_dict = {"c" : "Clubs", "s" : "Spades", "h" : "Hearts", "d" : "Diamonds"}
rank_dict = {"j" : "Jack", "q" : "Queen", "k" : "King", "a" : "Ace"}


class Card:
    def __init__(self,suit,rank):
    # initialize instance of Card with values for suit and rank values
        self.suit = suit
        self.suit = suit_dict[self.suit]
        self.rank = rank
        if self.rank in ["a", "k", "q", "j"]:
            self.rank = rank_dict[self.rank] 

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.rank + " of " + self.suit

    def value(self):
    # assigns value for Aces, face cards, and numeric cards
        if self.rank == "Ace":
            self.val = 11
        elif self.rank in ["Jack", "Queen", "King"]:
            self.val = 10
        else:
            self.val = int(self.rank)
        return self.val


class Deck:
    # initialize an instance of a deck and shuffle it
    def __init__(self):
        self.deck = [Card(s,r) for s in suits for r in rank]

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def one(self):
        return self.deck.pop()


class Player:
    # initialze an instance of a player and related qualities like getting a new card and choosing to hit or stand
    def __init__(self,name):
        self.name = name
        self.thehand = []

    def __str__(self):
        return self.name
    
    def get(self,card):
        #"adds a card to the users hand"
        self.thehand.append(card)

    def choose(self):
        self.decision = raw_input("Do you want to h)it or s)tand? ")

        if self.decision.lower() == "h":
            return True
        elif self.decision.lower() == "s":
            return False
        else:
            print "Please enter 'h' or 's'."
            return self.choose()

    def hand(self):
        self.total = sum([card.value() for card in self.thehand])
        
        if self.total > 21:
            for i in self.thehand:
                if i.rank == "a":
                    self.total -= 10

        return self.total
             
    def bust(self):
        if self.hand() > 21:
            return True
            
    def won(self):
        if self.hand() == 21:
            return True

    def winprompt(self):
        return "You win!"

    def bustprompt(self):
        return "You busted. You're out!"


class Dealer(Player):
    # initialize an instance of Dealer, which inherits from Player, but has a different choose() method
    def __init__(self,name):
       Player.__init__(self,name)

    def __str__(self):
        return self.name

    def choose(self):
        if self.hand() < 17:
            return True
        else:
            return False

    def winprompt(self):
        return "Dealer wins."

    def bustprompt(self):
        return "Dealer busts. You win!"

    
class Game:
    # initialize an instance of the game, including an empty player array, creating a deck, and game-specific methods
    def __init__(self):

        self.players = []
        self.thedeck = Deck()
        self.thedeck.shuffle()
        playercount = raw_input("How many players? ")

        for i in range(0,int(playercount)):
            name = raw_input("Enter the player name: ")
            self.theplayer = Player(name)
            self.players.append(self.theplayer)
        
        self.thedealer = Dealer("The Dealer")
        self.players.append(self.thedealer)
        
        self.play()

    def print_table(self):
        print "\n\n=====CURRENT SCORES====="
        for i in self.players[0:-1]:
            print "%s's Hand:" % (i)
            for x in i.thehand:
                print x
            print "Total: " + str(i.hand()) +"\n"

        print "========================"
        print "The Dealer's Hand:\n" + str(self.thedealer.thehand[0])
        for i in self.thedealer.thehand[1:]:
            print "**"
        print "========================"
        print "\n"

    def deal(self):
        for i in self.players:
            for n in range(0,2):
                i.get(self.thedeck.one())

    def initialresults(self):
        for i in self.players[0:-1]:
            if i.won() == True:
                print z.winprompt()

        if self.players[-1].won():
            print "The dealer hit blackjack."
    

    def results(self):
        for i in self.players[0:-1]:
            print i
            print i.hand()

        # if self.thedealer.hand() > self.theplayer.hand():
        #     print "The dealer has more points and wins."

        # if self.thedealer.hand() < self.theplayer.hand():
        #     print "You have more points and win!"

        # if self.thedealer.hand() == self.theplayer.hand():
        #     print "It's a tie. No blood."

    def play(self):
        self.deal()
        self.print_table()
        self.initialresults()

        #for i in self.players[0:-1]:

        # if more than one player hits blackjack, they both win.
        # if one player hits black jack, they win.
        # if no players hit blackjack, but the dealer hits blackjack, the dealer wins
        # if no one hits blackjack, continue

        if self.theplayer.won() == True:
            print "You hit Blackjack! Winner!"
            return

        if self.thedealer.won() == True:
            print "Bummer. The dealer hit Blackjack."
            return

        for z in self.players:
            print "\n%s's Turn:" % (z)
            while z.choose():
                print "\nIt's still %s's Turn:" % (z)
                z.get(self.thedeck.one())
                self.print_table()

                if z.won() == True:
                    print z.winprompt()
                    break

                if z.bust() == True:
                    print z.bustprompt()
                    break 

        self.results()

g = Game()
