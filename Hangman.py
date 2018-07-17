#hangman
import random
import time
random.seed(a=None)

def word_introduction(x):
	for i in range(len(x)):
		covered.append("_")
	print covered



def guessing():
	
	hangman = int(10)
	discovered = int(0)
	print "USE UPPER LETTERS"

	while hangman != int(0):
		letter = raw_input ( "Write Your letter: " ) 	
		how_many_letters = int(0)
		for i in range ( len(word) ):
			if letter == word[i]:
				covered[i] = letter
				print (" ")
				how_many_letters +=1
				discovered +=1
		
		
		if how_many_letters == int(0):
			hangman -= 1
			print "Letter %s is not in this word" %letter
			print "You have %s more chances" % hangman
			print " "
		print covered
		
		
		if discovered == len(word):
			print "Congrats you've found the word :D"
			break

		if hangman == int(0):
			print "dead"
			print "Actually the word was: ",
			time.sleep(10)
			print " %s." %word
		



if __name__ == "__main__":
	part = ''
	pool = []
	
	file = open("dictionary.txt", "r") 
	part += file.read()
	pool = part.split()
	
	how_many = len(pool)
	word = pool [ random.randint(1,how_many) ] 
	covered = []
	
	word_introduction (word)
	guessing()
	
