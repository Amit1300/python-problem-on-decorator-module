
import random

class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value

    def show(self):
        # print "{0} of {1}".format(self.value,self.suit)
        print(self.value,"of",self.suit)

class Deck:
    def __init__(self):
        self.cards=[]
        self.build()



    def build(self):
        for s in ["Club","Spade","Diamonds","Hearts"]:
            for v in range(1,13):
                self.cards.append(Card(s,v))
    
    def show(self):
        for c in self.cards:
            c.show()


    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r=random.randint(0,i)
            self.cards[i],self.cards[r]=self.cards[r],self.cards[i]


    def drawcard(self):
        return self.cards.pop()
# card=Card("clubs",6)
# card.show()


class Player(object):
    def __init__(self,name):
        self.hand=[]
        self.name=name



    def draw(self,deck):
        self.hand.append(deck.drawcard())
        return self

    def drawhand(self):
        for i in self.hand:
            i.show()
        

deck=Deck()
deck.shuffle()
# card=deck.draw()
# card.show()

amit=Player("amit")
amit.draw(deck).draw(deck)
amit.drawhand()