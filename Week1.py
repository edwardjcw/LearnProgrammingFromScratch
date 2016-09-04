# coding: utf-8
''' 
The assignment this week explores the world between data structures and functions.
 
Data structures in typical object oriented program are mutable. They're like Schrodinger's cat. At any moment, the cat may come out alive or dead. To plan for these dyametrically opposed states is difficult. How can we avoid this in programming? We make the cat immutable. We do this by treating objects as having only one state -- the initialized one. 

Using the cat example, we would never do this (even though it's legal). '''

class Cat (object): 			
	'''create a cat schematic (in Python, it's an object of type class. Everything in Python at some point derives from the general object, in parens) '''
	def __init__(self, alive): # constructor. used if one parameter given 
		self.alive = alive 
		'''Python automatically creates class fields when it first uses it. So here, as above, when Python sees self, it knows Cat will need the field that follows'''

# Let's bring a cat to life
spot = Cat(True) # spot is alive because I specified it so ... uses __init__()
unlucky = Cat(alive = False) # unlucky is dead. notice I can specify the parameter name if I want

# Watch this horrible mutability action. I'm bringing unlucky back from the dead
unlucky.alive = True
# now unlucky is alive

# what's so bad about that?
'''Imagine rigor_mortis() is a function used on dead things. And Nature applies it.'''
def rigor_mortis(thing): # this is a global function. It isn't a class method like __init__
	return ('no movement', thing) # this returns a tuple. Consider it as a pair of things that are now connected.
		
class Nature (object):
	def __init__(self, dead_thing):
		self.dead_thing = dead_thing
	def apply_rigor_mortis(self): # self is always the first argument for object functions (each object instance gets its own copy of the method)
		applied = rigor_mortis(self.dead_thing) # applied is local only to the method (thats why I didn't use self in front of it)
		return applied

#	let's kill unlucky again
unlucky.alive = False	
# let's create an instance of nature with unlucky in it
hell = Nature(unlucky) 
# now let's tell hell to do its thing
processed_unlucky = hell.apply_rigor_mortis()

# okay. Everything is working well. unlucky is can't move and is dead
# well, programmer didn't get the memo about unlucky. And does this:
unlucky.alive = True

# holy crap. Unlucky is alive. But he's being processed by hell. In fact he can't move!
# let's check on unlucky
print('Is unlucky alive? {0}'.format(processed_unlucky[1].alive))
print('What is his condition? {0}'.format(processed_unlucky[0]))

#unlucky is alive AND rogor mortis applies to him. This is the danger of mutability. Others can change basic assumptions without knowing the consequences.

#One way to prevent mutation is by preveting others from changing the state.
from collections import namedtuple
Dog = namedtuple('Dog', 'alive, gender') # shorthand way of creating an immutable class

fido = Dog(alive=True, gender='Male')
try:
	fido.alive = False # causes error
except AttributeError:
	print('Cant do that') # catches error and reports it
	
'''This weeks assignment. 
Part 1 -- easy. Create a global function called transmute that transforms an immutable Cat into an immutable Dog. The fields of the data structures are name, birthday, gender, and alive. The dog should have all the same data as the cat. The alive field should be True/False. The rest should just be strings.
Part 2 -- hard, requires research. Create a global schrodinger_box(thing) function. Using an if-then and try-catch statement, transorm any immutable object into another one of the same kind but with alive being opposite from what goes in. Hint: 1. Each object knows the class from which it was created and 2. Try statements can also catch errors if a method doesn't exist in an object.'
