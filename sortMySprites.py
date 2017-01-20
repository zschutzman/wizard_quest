# Zach Schutzman
# January 2015
# Wizard Quest sortMySprites auxiliary function
# PhatPenguin Games


'''sortMySprites() is a method which takes in a list of Character objects and sorts them into two lists:
   the first for the state_machine to draw before (behind) the pivot Character and the second to be drawn
   in front.  Returns as a list of two lists [[BEFORE],[AFTER]]
   
   The sort is based on the Character's y-location, with Characters below the playerCharacter in the BEFORE
   list and Characters above the playerCharacter being drawn after
'''

def sortMySprites(listOfCharacters, playerCharacter):
	BEFORE = []
	AFTER = []
	for c in listOfCharacters:
		if isinstance(c, character.Transport):
			BEFORE = [c] + BEFORE
		elif c.y > playerCharacter.y:
			BEFORE.append(c)
		else:
			AFTER.append(c)
	
	return [BEFORE, AFTER]