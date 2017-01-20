# Zach Schutzman
# January 2015
# Wizard Quest Button Class
# PhatPenguin Games

# This file defines the Button class

import pygame
import sys
import twrap

class Button:
	def __init__(self, xloc, yloc, width, height, image, target)
		self.image = image
		self.next = target
		self.clickableArea = pygame.Rect(xloc, yloc, width, height)
		
		def drawIntoGame(self):
			game.display.blit(self)
		
		def handleInteraction(self):
			pass
			## Go to self.next