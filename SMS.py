# Zach Schutzman
# January 2015
# Wizard Quest StackingMySprites auxiliary functions
# PhatPenguin Games

import character
import random
import os
import pygame


'''sortMySprites() is a method which takes in a list of Character objects and sorts them into two lists:
   the first for the state_machine to draw before (behind) the pivot Character and the second to be drawn
   in front.  Returns as a list of two lists [[BEFORE],[AFTER]]
   
   The sort is based on the Character's y-location, with Characters below the playerCharacter in the BEFORE
   list and Characters above the playerCharacter being drawn after
'''

def renderOrder(listOfCharacters, playerCharacter):
	BEFORE = []
	AFTER = []
	for c in listOfCharacters:
		if c.y + (c.height - 64) < playerCharacter.y:
			BEFORE.append(c)
		else:
			AFTER.append(c)
	
	return [BEFORE, AFTER]
	
	
'''Provides a pair of renderOrder() lists only containing units less than 
	a given number of units away from the player. 
'''
	
def renderOrderNearby(listOfCharacters, playerCharacter, radius):
	nearbyList = []
	
	for c in listOfCharacters:
		if abs(c.x - playerCharacter.x) < radius:
			nearbyList.append(c)
			
	return renderOrder(nearbyList, playerCharacter)
	
	
''' Performs a sort on the list of NPCs (obstacles, people, enemies) as in order
    to properly display a map, textures should be rendered from bottom to top.  Objects near the
	bottom of the screen (higher y value) go at the back of the list.
'''

def sortObjects(listOfCharacters):
	return sorted(listOfCharacters, key=lambda character: character.y)
	
	
# # ## Test code

# # pygame.init()
# # screen = pygame.display.set_mode( (1024, 768) )


# # L = []

# # for i in range(5):
	# # char = character.Obstacle(random.randint(200,1000), random.randint(300,600), [os.path.join("imgs","Tree1.png")], None)

	# # print char.y

	# # L.append(char)
	
	
# # print "-------------"
# # sortedL = sortObjects(L)

# # for c in sortedL:
	# # print c.y
		