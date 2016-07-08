
import random

class Card(object):
	"""docstring for cards"""
	suits = ["hearts", "diamonds", "clubs", "spades"]
	values = ["Zero","Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
	
	def __init__(self, suit=0, value=0):
		self.suit = suit
		self.value = value
	
	def __str__(self):
		return (self.values[self.value] + " of " + self.suits[self.suit])

class Deck(object):
	"""docstring for deck"""

	def __init__(self):
		self.cards = []
		for suit in range(4):
			for value in range(1, 14):
				self.cards.append(Card(suit,value))

	def __str__(self):
		str2 = " "
		for card in self.cards:
			str2 = str2 + str(card) + "\n"
		return str2

	def shuffle(self):
		a = len(self.cards)
		b = a-1
		for d in range(b,0,-1):
			e = random.randint(0,d)
			if e == d:
				continue
			self.cards[d], self.cards[e] = self.cards[e], self.cards[d]
		return self


	def deal(self):
		# hand = ""
		# for x in xrange(0,2,1):
		return self.cards.pop()
		
	
	def print_deck(self):
		for card in self.cards:
			print card

class Player(object):
	"""docstring for ClassName"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
		if self.age < 21:
			print "You are not of age"
		else:
			print "Let's play!"
		self.balance = 1000
		self.hand = []


	def draw(self, deck):
		self.hand.append(deck.deal())
		return self



	# def betting(self):
	# 	self.place_bet = place_bet

	# def hit(self):
	# 	self.hit = hit
		
deck1 = Deck()		
deck1.shuffle()

player1 = Player('Bob',23)

player1.draw(deck1).draw(deck1)

print player1.hand[0]