class Card:
    values=["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    suits=["spades","hearts","diamonds","clubs"]
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def __lt__(self,other):
        if self.value<other.value:
            return True
        elif self.value==other.value:
            if self.suit<other.suit:
                return True
            else:
                return False
        else:
            return False
    def __gt__(self,other):
        if self.value>other.value:
            return True
        elif self.value==other.value:
            if self.suit>other.suit:
                return True
            else:
                return False
        else:
            return False
    def __repr__(self):
        return self.values[self.value]+" of "+self.suits[self.suit]

class Deck:
    def __init__(self):
        import random
        self.cards=[]
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(i,j))
        random.shuffle(self.cards)
    def remove(self):
        if len(self.cards)==0:
            return None
        else:
            return self.cards.pop()

class Player:
    def __init__(self,name):
        self.name=name
        self.wins=0

class Game:
    def __init__(self):
        name1=input("プレイヤー1の名前を入力してください ")
        name2=input("プレイヤー2の名前を入力してください ")
        self.player1=Player(name1)
        self.player2=Player(name2)
        self.deck=Deck()
    def play_game(self):
        cards=self.deck.cards
        print("戦争を始めます")
        while len(cards)>=2:
            player1card=self.deck.remove()
            player2card=self.deck.remove()
            print(self.player1.name+" は {} 、".format(player1card)+self.player2.name+" は {} を引きました".format(player2card))
            if player1card>player2card:
                self.player1.wins+=1
                roundwinner=self.player1.name
            else:
                self.player2.wins+=1
                roundwinner=self.player2.name
            print("このラウンドは "+roundwinner+" の勝ちです")
        if self.player1.wins==self.player2.wins:
            print("ゲーム終了、引き分けです")
        else:
            if self.player1.wins>self.player2.wins:
                gamewinner=self.player1.name
            elif self.player1.wins<self.player2.wins:
                gamewinner=self.player2.name
            print("ゲーム終了、"+gamewinner+" の勝ちです")

game=Game()
game.play_game()