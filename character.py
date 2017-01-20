# Zach Schutzman
# January 2015
# Wizard Quest Character Class
# PhatPenguin Games

## This file contains the definitions for the Character superclass
 # and all associated subclasses (player, npc, enemy)

# Import  statements
import sys
import pygame
import os

def testFunc():
	print "CODE STILL WORKS"


''' Defines the Character class, used as a superclass.	
	Takes paramenters for x and y location in the game and images
	for its overworld sprites, and a display object to allow
	Characters to draw themselves
'''


class Character:
	def __init__(self, xloc, yloc, overworldSpriteList, disp):
		self.x = xloc
		self.y = yloc
		self.sprites = []
		self.display = disp
		self.name = None
	
	
		## Initialize sprites
		for x  in range(len(overworldSpriteList)):
			self.sprites.append(pygame.image.load(overworldSpriteList[x]).convert_alpha())
		
		if len(self.sprites) != 0:
			self.currentSprite = self.sprites[0]
			
			self.width = self.sprites[0].get_width()
			self.height = self.sprites[0].get_height()

	
			
			
			## Intialize collision attributes
			self.objectRect = pygame.Rect((self.x, self.y), (self.sprites[0].get_size()))
		
		else:
			self.objectRect = pygame.Rect((self.x, self.y), (32,32))
			self.width = self.height = 32
		self.collisionRect = self.createCollisionRect()

		
	def createCollisionRect(self):	
		# Cases for different sprite sizes
		if self.width <= 36 and self.height <= 36:
			return self.objectRect
		
		if self.width <= 36 and self.height > 36:
			return pygame.Rect((self.x, self.y + self.objectRect.get_height() - 36), (self.objectRect.get_width, 36))
		
		if self.width > 36 and self.height <= 36:
			return pygame.Rect((self.x + ((self.width - 36)/2), self.y), (36, self.height))
			
		if self.width > 36 and self.height > 36:
			return pygame.Rect(((self.x + (self.width - 36)/2), self.y + self.height - 36), (36, 36))
		
		
	def newCollRect(self):
		self.collisionRect = None
		self.collisionRect = self.createCollisionRect()
	
		
	def changeSprite(self, index):
		self.currentSprite = self.sprites[index]
	
	def updateRects(self):
		self.objectRect = pygame.Rect((self.x, self.y), (self.width, self.height))
		self.collisionRect = self.createCollisionRect()
	
	def drawIntoGame(self):
		self.updateRects()
		self.display.blit(self.currentSprite, self.objectRect)
	
	
	def isColliding(self, rect):
		if self.collisionRect.colliderect(rect):
			return True
		else:
			return False
	

''' Obstacle is used to define static objects in the overworld, such as trees. '''				
class Obstacle(Character):
	def __init__(self, xloc, yloc, overworldSpriteList, disp):
		Character.__init__(self, xloc, yloc, overworldSpriteList, disp)

		
		

''' NPC is used to define other characters in the game.	 The class has 
	a method to handle Player interaction with the NPC which triggers 
	that NPC's dialogue.
	
	dialogueImgFiles, playerDialogueImgFiles, voiceFiles, and convo all handle
	dialogue with the player.  The first is the NPC's dialogue, the second is 
	the player's, the third is the set of voice over files, and convo
	is a key used to control the order dialogue occurs
	
	 self.otherActions is a list of functions handled at the very
	 end of the handleInteraction() function
'''
class NPC(Character):
	def __init__(self, level, xloc, yloc, overworldSpriteList, disp, dialogueImgFiles, playerDialogueImgFiles, voiceFiles, convo, otherActions, destroyAfterUse):
		Character.__init__(self, xloc, yloc, overworldSpriteList, disp)
		self.level = level
		
		self.otherActions = otherActions
		self.selfDestruct = destroyAfterUse
		
		self.dialogueRect = pygame.Rect((576,0),(448,256))
		self.playerDialogueRect = pygame.Rect((0,448),(448,256))
		
		if overworldSpriteList == [os.path.join("imgs","RjufusO.png")]:
			self.name = "Rjufus"

		
		
		
		
		self.dialogue = []
		for d in dialogueImgFiles:
			self.dialogue.append(pygame.image.load(d).convert_alpha())
		
		self.playerDialogue = []
		for d in playerDialogueImgFiles:
			self.playerDialogue.append(pygame.image.load(d).convert_alpha())
		
		self.voiceOvers = []
		for v in voiceFiles:
			self.voiceOvers.append(pygame.mixer.Sound(v))
			
		self.conversationKey = convo	
		
		self.tracker = [0,0,0]
		self.done = False
	
	def addToOtherCharacters(self, c):
		self.otherActions.append(c)
					
	'''Handles the case where the Player interacts with an NPC. 
	  Each NPC can be interacted with exactly once.  
	  
	  For quests with multiple parts, some object's 
	  otherActions should include the creation of a new NPC
	  and a call to this instance's destroy().
	   
	'''
	def handleInteraction(self):
		counter = 1
		
	# return
	
		
		if len(self.conversationKey) > 0 and self.done == False:
			curr = self.conversationKey[0]
			if curr[0] == 1:
				self.display.blit(self.dialogue[self.tracker[0]],self.dialogueRect)
			if curr[1] == 1:
				self.display.blit(self.playerDialogue[self.tracker[1]],self.playerDialogueRect)
			if curr[2] == 1:
				self.voiceOvers[self.tracker[2]].play()
		
			pygame.display.update()		
			self.tracker = [self.tracker[0] + curr[0], self.tracker[1] + curr[1], self.tracker[2] + curr[2]]
		
		while self.done == False:
			for e in pygame.event.get():
				if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
					if counter >= len(self.conversationKey):
						self.done = True
					print counter
					
					if self.done == False:
						curr = self.conversationKey[counter]

						if curr[0] == 1:
							self.display.blit(self.dialogue[self.tracker[0]],self.dialogueRect)
						if curr[1] == 1:
							self.display.blit(self.playerDialogue[self.tracker[1]],self.playerDialogueRect)
						pygame.display.update()
						
						if curr[2] == 1:
							try:
								self.voiceOvers[self.tracker[2] - 1].stop()
							except IndexError:
								pass
							self.voiceOvers[self.tracker[2]].play()

						self.tracker = [self.tracker[0] + curr[0], self.tracker[1] + curr[1], self.tracker[2] + curr[2]]
				
						
						counter += 1
					
		self.voiceOvers[self.tracker[2]-1].stop()
		
		for c in self.otherActions:
			self.level.addCharacter(c)
			
		if self.selfDestruct == True:
			self.level.removeCharacter(self)




class Creature(Character):
	def __init__(self, level, xloc, yloc, spriteList, disp, soundEffect = None, destroyAfterUse = False, otherActions = []):
		Character.__init__(self, xloc, yloc, spriteList, disp)
		
		
		self.level = level
		self.selfDestruct = destroyAfterUse
		
		self.otherActions = otherActions
				
		
		if soundEffect != None:
			self.noise = pygame.mixer.Sound(soundEffect)
		else:
			self.noise = None
		
	def handleInteraction(self):
		print self
		print self.selfDestruct
		print self.otherActions
		if self.noise != None:
			self.noise.play()
		if self.selfDestruct == True:
			self.level.removeCharacter(self)
		if self.otherActions != []:
			for c in self.otherActions:
				self.level.addCharacter(c)
			
	

class inactiveCrystal(Creature):
	def __init__(self, level, xloc, yloc, spriteList, disp, otherActions):
		Creature.__init__(self, level, xloc, yloc, spriteList, disp, None, True, otherActions)

		self.used = False
		
	def handleInteraction(self):
		if self.used == True:
			pass
		else:	
			self.level.sam.crystalCount += 1
			if self.selfDestruct == True:
				self.level.removeCharacter(self)
			for c in self.otherActions:
				self.level.addCharacter(c)
			self.used == True
''' The Enemy class is used for enemies in the overworld.  On collision, 
	the game state changes and the Player enters combat with the enemy.
''' 
class Enemy(Character):
	def __init__(self, level, xloc, yloc, overworldSpriteList, disp, spawnOnDefeat, soundEffect, startHP = 30, atkDmg = 1):
		Character.__init__(self, xloc, yloc, overworldSpriteList, disp)
		
		self.name = None
		
		
		self.level = level

		self.sound = pygame.mixer.Sound(soundEffect[0])
		self.spawnOnDefeat = spawnOnDefeat
		
		self.maxHP = startHP
		self.hp = startHP
		
		self.damageDone = atkDmg
		
		self.damagePerTurn = 0
		self.frozen = False
		
		self.battSp = pygame.image.load(overworldSpriteList[0][:5] + 'B' + overworldSpriteList[0][5:]).convert_alpha()
		
	'''Handles the case where the Player interacts with the enemy in the overworld.
	   Triggers the combat state.
	'''
	def handleInteraction(self):

		pass
		
		
	'''Removes the enemy from the overworld map when it is defeated. '''
	def isDefeated(self):
		self.level.removeCharacter(self)

		for c in self.spawnOnDefeat:
			self.level.addCharacter(c)
		
	

	def takeTurn(self, player):
		if self.damagePerTurn > 0:
			self.hp = self.hp - self.damagePerTurn
		if self.hp == 0:
			self.isDefeated()
			return True
		if self.frozen:
			self.frozen = False
			return False
		player.takeDamage(self.damageDone)
			
		
	def takeDamage(self, dmg):
		self.hp = self.hp - dmg
	
	def healDamage(self, heal):
		self.hp = min(self.hp + heal, self.maxHP)
		
	def takeDmgOverTime(self, dot):
		self.damagePerTurn = dot
		
	def freeze(self):
		self.frozen = True
	
		
	
''' The class to define the Player.	 Tracks its HP, XP, and level.	Includes methods
	to handle moving and mutators for HP, XP, and level.
''' 
class Player(Character):
	def __init__(self, xloc, yloc, disp, faceNorthSpriteList, faceSouthSpriteList, faceEastSpriteList, faceWestSpriteList):
		Character.__init__(self, xloc, yloc, faceSouthSpriteList, disp)
		
		
		s = pygame.mixer.Sound(os.path.join("sounds","loopable-theme.wav"))
		s.play(loops=-1)
		s.set_volume(.3)

		
		
		self.coll = False
		
		self.otherNPCs = []
		
		## Secondary collision rectangle for movement
		self.movCollRect = self.collisionRect.copy()
		self.movCollRect.inflate(-8,-8)
	
		## Load in all of the sprites
		self.northSprites = []
		self.southSprites = []
		self.eastSprites = []
		self.westSprites = []

		for x  in range(len(faceNorthSpriteList)):
			self.northSprites.append(pygame.image.load(faceNorthSpriteList[x]).convert_alpha())
		for x  in range(len(faceSouthSpriteList)):
			self.southSprites.append(pygame.image.load(faceSouthSpriteList[x]).convert_alpha())
		for x  in range(len(faceEastSpriteList)):
			self.eastSprites.append(pygame.image.load(faceEastSpriteList[x]).convert_alpha())
		for x  in range(len(faceWestSpriteList)):
			self.westSprites.append(pygame.image.load(faceWestSpriteList[x]).convert_alpha())

		
		
		
		## Directional marker used to handle animations
		self.facingDirection = 'east'
		self.currentSpriteList = self.eastSprites
		self.currentSprite = self.eastSprites[0]
		self.currentSpriteIndex = 0

		
		## Initialize Player stats
		self.maxHP = 30
		self.hp = 30
		self.characterLevel = 1
		self.xp = 0
		
		self.speed = 8
		self.stepCount = 0
		self.stepCountThreshold = 11
		
		self.crystalCount = 0
	
	
	def addOtherNPCs(self, listOfNPCs):
		self.otherNPCs = listOfNPCs
	
	
	def addAdditionalNPC(self, NPC):
		self.otherNPCs.append(NPC)
	
	## Cycles through the current sprite list to animate walking
	def nextSprite(self):
		if self.currentSpriteIndex == len(self.currentSpriteList) - 1:
			self.currentSpriteIndex = 0
		else:
			self.currentSpriteIndex += 1
			
		self.currentSprite = self.currentSpriteList[self.currentSpriteIndex]
	
	
	## Changes the set of sprites used when the Player faces a different direction
	def changeSprite(self):
		if self.facingDirection == 'north':
			self.currentSpriteList = self.northSprites
			self.currentSprite = self.northSprites[0]
		
		if self.facingDirection == 'south':
			self.currentSpriteList = self.southSprites
			self.currentSprite = self.southSprites[0]
			
		if self.facingDirection == 'east':
			self.currentSpriteList = self.eastSprites
			self.currentSprite = self.eastSprites[0]
		
		if self.facingDirection == 'west':
			self.currentSpriteList = self.westSprites
			self.currentSprite = self.westSprites[0]
			
			
			
	def levelUp(self):
		self.characterLevel += 1
	
	def takeDamage(self, dmg):
		self.hp -= dmg
		
	def newMaxHP(self, newHP):
		self.maxHP = newHP
	
	def getXp(self, exp):
		self.xp += exp
		
	def handleMoveNorth(self):
		self.movCollRect = self.movCollRect.move(0,-16)
		self.coll = False
		for c in self.otherNPCs:
			if c.collisionRect.colliderect(self.movCollRect):
				self.coll = True
				
				if isinstance(c, NPC) and c.done == False:
					c.handleInteraction()
					return "Game_Setup"
				
				if isinstance(c, Enemy):
					return c
					
				if isinstance(c, Creature):
					c.handleInteraction()

				if isinstance(c,Transport):
					return c.nextLevel

					
		if self.coll == False:
			self.y -= self.speed
		self.stepCount +=3
		self.movCollRect = self.collisionRect.copy()	
		
		
		if self.facingDirection != 'north':
			self.facingDirection = 'north'
			self.changeSprite()
			self.stepCount = 0
		else:
			if self.stepCount > self.stepCountThreshold:
				self.stepCount = 0
				self.nextSprite()
	
		return "Play"
			
	def handleMoveSouth(self):
		
		self.movCollRect = self.movCollRect.move(0,16)
		self.coll = False
		for c in self.otherNPCs:
			if c.collisionRect.colliderect(self.movCollRect):
				self.coll = True
				
				if isinstance(c, NPC) and c.done == False:
					c.handleInteraction()
					return "Game_Setup"
				
				if isinstance(c, Enemy):
					return c
				
				if isinstance(c, Creature):
					c.handleInteraction()
				
				if isinstance(c,Transport):
					return c.nextLevel
					
		
		if self.coll == False:
			self.y += self.speed
		self.stepCount +=3
		self.movCollRect = self.collisionRect.copy()	
		
		if self.facingDirection != 'south':
			self.facingDirection = 'south'
			self.changeSprite()
			self.stepCount = 0
		else:
			if self.stepCount > self.stepCountThreshold:
				self.stepCount = 0
				self.nextSprite()
		
		return "Play"
				
	def handleMoveEast(self):
		self.movCollRect = self.movCollRect.move(16,0)
		self.coll = False
		for c in self.otherNPCs:
			if c.collisionRect.colliderect(self.movCollRect):
				self.coll = True
				
				if isinstance(c, NPC) and c.done == False:
					c.handleInteraction()
					if c.name == "Rjufus":
						return "Win_Setup"
					
					else:
						return "Game_Setup"
				
				if isinstance(c, Enemy):
					return c
					
				if isinstance(c, Creature):
					c.handleInteraction()
				
				if isinstance(c,Transport):
					return c.nextLevel
					
		
		if self.coll == False:
			self.x += self.speed
		self.stepCount +=3
		self.movCollRect = self.collisionRect.copy()	
		
		if self.facingDirection != 'east':
			self.facingDirection = 'east'
			self.changeSprite()
			self.stepCount = 0
			
		else:
			if self.stepCount > self.stepCountThreshold:
				self.stepCount = 0
				self.nextSprite()
		
		return "Play"
		
		
	def handleMoveWest(self):
		
		self.movCollRect = self.movCollRect.move(-16,0)
		self.coll = False
		for c in self.otherNPCs:
			if c.collisionRect.colliderect(self.movCollRect):
				self.coll = True
				
				if isinstance(c, NPC) and c.done == False:
					c.handleInteraction()
					return "Game_Setup"
				
				if isinstance(c, Enemy):
					return c
					
				if isinstance(c, Creature):
					c.handleInteraction()
				
				if isinstance(c,Transport):
					return c.nextLevel
					
						
						
		if self.coll == False:
			self.x -= self.speed
		self.stepCount +=3
		self.movCollRect = self.collisionRect.copy()	
		
		
		
		if self.facingDirection != 'west':
			self.facingDirection = 'west'
			self.changeSprite()
			self.stepCount = 0
		else:
			if self.stepCount > self.stepCountThreshold:
				self.stepCount = 0
				self.nextSprite()
				
		return "Play"		

		
	def stopMoving(self):
		self.stepCount = 0
		self.currentSpriteIndex = 0
		self.currentSprite = self.currentSpriteList[0]
		
		
		
		
		
		
		
class Transport(Character):
	def __init__(self, xloc, yloc, disp, levelInfo):
		Character.__init__(self, xloc, yloc, [os.path.join("imgs","TransparencyMedium.png")], disp)
		
		self.nextLevel = levelInfo
		
