
from SMS import *
from treeInterp import *
import map
import random

''' This class defines a level generator tool which allows the game loop to request a level.
	Each level is predesigned and code is kept here to keep the game file clean.
	
	Each method returns the generated list of NPCs (obstacles, NPCs, Player).
	
	Construtor takes the display object and Player object from the game to maintain continuity
'''

class LevelGen:
	def __init__(self, Player, map, disp):
		self.map = map
		self.sam = Player
		self.display = disp
		self.NPCList = []
		
		## Make some boundaries
		for i in range(32):
			t = character.Obstacle(32*i, -48, [os.path.join("imgs", "TransparencySmall.png")], self.display)
			self.NPCList.append(t)
	

		for i in range(32):
			t = character.Obstacle(32*i, 704, [os.path.join("imgs", "TransparencySmall.png")], self.display)
			self.NPCList.append(t)

		for i in range(22):
			t = character.Obstacle(-48, 32*i, [os.path.join("imgs", "TransparencySmall.png")], self.display)
			self.NPCList.append(t)

		for i in range(22):
			t = character.Obstacle(1072, 32*i, [os.path.join("imgs", "TransparencySmall.png")], self.display)
			self.NPCList.append(t)

		self.flattenedMapList = []
		
		for i in self.map.mapList:
			for j in i:
				self.flattenedMapList.append(j)
		
	def renderLevel(self):
		for c in self.NPCList:
			c.drawIntoGame()
		self.sam.drawIntoGame()
			
	def updateNearby(self):
		
		nearbyMap = renderOrderNearby(self.flattenedMapList, self.sam, 96)
		nearbyNPC = renderOrderNearby(self.NPCList, self.sam, 96)
		
		toUpdate = []
		
		for mt in nearbyMap[0]:
			toUpdate.append(mt.tileRect)
			mt.drawIntoGame(self.display)
		for mt in nearbyMap[1]:
			toUpdate.append(mt.tileRect)
			mt.drawIntoGame(self.display)
				
		
		
		for c in nearbyNPC[0]:
			toUpdate.append(c.objectRect)
			c.drawIntoGame()
		
		self.sam.drawIntoGame()
		
		toUpdate.append(self.sam.objectRect)
		
		for c in nearbyNPC[1]:
			toUpdate.append(c.objectRect)
			c.drawIntoGame()
			
		return toUpdate
		
		
	def addCharacter(self, c):
		if c not in self.NPCList:
			self.NPCList = [c] + self.NPCList
	def removeCharacter(self, c):
		if c in self.NPCList:
			self.NPCList.remove(c)

		
		
class Level_Tutorial(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()
	
	''' Initializes the level by constructing all of the NPCs and obstacles in it.
	
		When defining NPCs, they should be generated based on order of appearance
		in reverse chronological order.  This way, an NPC which spawns another
		will be able to reference that other object.
	'''
	def generate(self):
		
		# Send me to level 1!
		l1Transport = character.Transport(1024, 320, self.display, (0, 448, 1))
		l1Transport2 = character.Transport(1024, 384, self.display, (0, 448, 1))

		extraPoacher1 = character.Enemy(
		
			# Reference to self, starting x, y
			self, 192, 192, 
			
			#List of sprite
			[os.path.join("imgs", "Poacher.png")], 
			
			# Display
			self.display, 
		
			# List of other character objects spawned after interaction
			[], 
			
			# Sound effect
			[os.path.join("sounds", "SPOOKYMOAN1.wav")]
			
			)
		extraPoacher2 = character.Enemy(
		
			# Reference to self, starting x, y
			self, 192, 384, 
			
			#List of sprite
			[os.path.join("imgs", "Poacher.png")], 
			
			# Display
			self.display, 
		
			# List of other character objects spawned after interaction
			[], 
			
			# Sound effect
			[os.path.join("sounds", "SPOOKYMOAN1.wav")]
			
			)
		extraPoacher3 = character.Enemy(
		
			# Reference to self, starting x, y
			self, 704, 192, 
			
			#List of sprite
			[os.path.join("imgs", "Poacher.png")], 
			
			# Display
			self.display, 
		
			# List of other character objects spawned after interaction
			[], 
			
			# Sound effect
			[os.path.join("sounds", "SPOOKYMOAN1.wav")]
			
			)
		extraPoacher4 = character.Enemy(
		
			# Reference to self, starting x, y
			self, 704, 384, 
			
			#List of sprite
			[os.path.join("imgs", "Poacher.png")], 
			
			# Display
			self.display, 
		
			# List of other character objects spawned after interaction
			[], 
			
			# Sound effect
			[os.path.join("sounds", "SPOOKYMOAN1.wav")]
			
			)
		
		# Initialize!
		chelbi2 = character.NPC(
			
			# Reference to itself, starting x, y
			self, 832, 320, 
			
			# List of sprite
			[os.path.join("imgs", "Chelbi.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "tutorial", "Chelbi12.png"), os.path.join("dialogue", "tutorial", "Chelbi13.png"), os.path.join("dialogue", "tutorial", "Chelbi14.png")], 
			
			# Player's dialogue boxes list
			[os.path.join("dialogue", "tutorial", "Player8.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "tutorial", "CHELBI13.wav"), os.path.join("sounds", "voiceovers", "tutorial", "CHELBI14.wav"), os.path.join("sounds", "voiceovers", "tutorial", "CHELBI15.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1), (1, 0, 1)], 
			
			# List of other character objects spawned after interaction
			[extraPoacher1, extraPoacher2, extraPoacher3, extraPoacher4, l1Transport], 
			
			# Remove this character after interacting?
			False)


		# Initialize
		squirrel1 = character.Creature(
			
			# Reference to self, starting x, y
			self, 448, 320, 
			
			# List of sprite
			[os.path.join("imgs", "Squirrel.png")], 
			
			# Display
			self.display, 
			
			#Sound effect
			os.path.join("sounds", "SQUIRREL.wav"), 
			
			)

		# Initialize
		squirrel2 = character.Creature(
			
			# Reference to self, starting x, y
			self, 192, 256, 
			
			# List of sprite
			[os.path.join("imgs", "Squirrel.png")], 
			
			# Display
			self.display, 
			
			#Sound effect
			os.path.join("sounds", "SQUIRREL.wav"), 
			
			)

		# Initialize
		squirrel3 = character.Creature(
			
			# Reference to self, starting x, y
			self, 192, 448, 
			
			# List of sprite
			[os.path.join("imgs", "Squirrel.png")], 
			
			# Display
			self.display, 
			
			#Sound effect
			os.path.join("sounds", "SQUIRREL.wav"), 
			
			)

		# Initialize
		squirrel4 = character.Creature(
			
			# Reference to self, starting x, y
			self, 704, 256, 
			
			# List of sprite
			[os.path.join("imgs", "Squirrel.png")], 
			
			# Display
			self.display, 
			
			#Sound effect
			os.path.join("sounds", "SQUIRREL.wav"), 
			
			)

		# Initialize
		squirrel5 = character.Creature(
			
			# Reference to self, starting x, y
			self, 704, 448, 
			
			# List of sprite
			[os.path.join("imgs", "Squirrel.png")], 
			
			# Display
			self.display, 
			
			#Sound effect
			os.path.join("sounds", "SQUIRREL.wav"), 
			
			)
			
		# Initialize
		poacher = character.Enemy(
		
			# Reference to self, starting x, y
			self, 512, 320, 
			
			#List of sprite
			[os.path.join("imgs", "PoacherCaptain.png")], 
			
			# Display
			self.display, 
		
			# List of other character objects spawned after interaction
			[chelbi2], 
			
			# Sound effect
			[os.path.join("sounds", "SPOOKYMOAN1.wav")]
			
			)
		
			

		# Initialize!
		chelbi1 = character.NPC(
			
			# Reference to itself, starting x, y
			self, 832, 320, 
			
			# List of sprite
			[os.path.join("imgs", "Chelbi.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "tutorial", "Chelbi1.png"), os.path.join("dialogue", "tutorial", "Chelbi2.png"), os.path.join("dialogue", "tutorial", "Chelbi3.png"), 
			os.path.join("dialogue", "tutorial", "Chelbi4.png"), os.path.join("dialogue", "tutorial", "Chelbi5.png"), os.path.join("dialogue", "tutorial", "Chelbi6.png"), 
			os.path.join("dialogue", "tutorial", "Chelbi6_2.png"), os.path.join("dialogue", "tutorial", "Chelbi7.png"), os.path.join("dialogue", "tutorial", "Chelbi8.png"), 
			os.path.join("dialogue", "tutorial", "Chelbi9.png")], 
			
			# Player's dialogue boxes list
			[os.path.join("dialogue", "tutorial", "Player1.png"), os.path.join("dialogue", "tutorial", "Player2.png"), os.path.join("dialogue", "tutorial", "Player3.png"), 
			os.path.join("dialogue", "tutorial", "Player4.png"), os.path.join("dialogue", "tutorial", "Player5.png"), os.path.join("dialogue", "tutorial", "Player6.png"), 
			os.path.join("dialogue", "tutorial", "Player7.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "tutorial", "CHELBI1.wav"), os.path.join("sounds", "voiceovers", "tutorial", "CHELBI2.wav"), os.path.join("sounds", "voiceovers", "tutorial", "CHELBI3.wav"), 
			os.path.join("sounds", "voiceovers", "tutorial", "CHELBI4.wav"), os.path.join("sounds", "voiceovers", "tutorial", "CHELBI5.wav"), os.path.join("sounds", "voiceovers", "tutorial", "CHELBI6.wav"), 
			os.path.join("sounds", "voiceovers", "tutorial", "CHELBI7.wav"), os.path.join("sounds", "voiceovers", "tutorial", "CHELBI8.wav"), os.path.join("sounds", "voiceovers", "tutorial", "CHELBI9.wav"), 
			os.path.join("sounds", "voiceovers", "tutorial", "CHELBI10.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1), (0, 1, 0), 
			 (1, 0, 1), (0, 1, 0), (1, 0, 1), (0, 1, 0), 
			 (1, 0, 1), (1, 0, 1), (1, 0, 1), (0, 1, 0), 
			 (1, 0, 1), (0, 1, 0), (1, 0, 1), (0, 1, 0), 
			 (1, 0, 1)], 
			
			# List of other character objects spawned after interaction
			[poacher], 
			
			# Remove this character after interacting?
			True)
		
		
		trees = sortObjects(treePlacer([
			# Tree cells listed by column
			(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), 
			
			(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 7), (1, 8), (1, 9), (1, 10), 
			
			(2, 0), (2, 1), (2, 2), (2, 9), (2, 10), 
			
			(3, 0), (3, 1), (3, 2), (3, 9), (3, 10), 
			
			(4, 0), (4, 1), (4, 2), (4, 9), (4, 10), 
			
			(5, 0), (5, 1), (5, 2), (5, 3), (5, 7), (5, 8), (5, 9), (5, 10), 
			
			(6, 0), (6, 1), (6, 2), (6, 3), (6, 7), (6, 8), (6, 9), (6, 10), 
			
			(7, 0), (7, 1), (7, 2), (7, 3), (7, 7), (7, 8), (7, 9), (7, 10), 
			
			(8, 0), (8, 1), (8, 2), (8, 3), (8, 7), (8, 8), (8, 9), (8, 10), 
			
			(9, 0), (9, 1), (9, 2), (9, 3), (9, 7), (9, 8), (9, 9), (9, 10), 
			
			(10, 0), (10, 1), (10, 2), (10, 9), (10, 10), 
			
			(11, 0), (11, 1), (11, 2), (11, 9), (11, 10), 
			
			(12, 0), (12, 1), (12, 2), (12, 9), (12, 10), 
			
			(13, 0), (13, 1), (13, 2), (13, 3), (13, 7), (13, 8), (13, 9), (13, 10), 
			
			(14, 0), (14, 1), (14, 2), (14, 3), (14, 7), (14, 8), (14, 9), (14, 10), 
			
			(15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 7), (15, 8), (15, 9), (15, 10), 
			
			], 
		self.display))
		
		
		# Append the trees and NPCs to the NPCList
		self.NPCList = self.NPCList + [chelbi1, squirrel1, squirrel2, squirrel3, squirrel4, squirrel5] + trees
		
		# Sort everything to prepare for rendering
		self.NPCList = sortObjects(self.NPCList)

		
		
class Level_Field(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()
		
		
	def generate(self):
		
		# Back to level 0!
		l0Transport = character.Transport(-64, 384, self.display, (940, 320, 0))
		l0Transport2 = character.Transport(-64, 448, self.display, (940, 320, 0))
		
		# Up to 2!
		l2Transport = character.Transport(128, -64, self.display, (128, 640, 2))
		l2Transport2 = character.Transport(192, -64, self.display, (196, 640, 2))
		
		# Right to 3!
		l3Transport = character.Transport(1048, 256, self.display, (0, 256, 3))
		l3Transport2 = character.Transport(1048, 320, self.display, (0, 320, 3))
		
		
		#Initialize!
		farmer = character.NPC(
			
			# Reference to itself, starting x, y
			self, 320, 448, 
			
			# List of sprite
			[os.path.join("imgs", "Female1.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "field", "Hand1.png"), os.path.join("dialogue", "field", "Hand2.png")], 
		
			# Player's dialogue boxes list
			[os.path.join("dialogue", "field", "HHand1.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "field", "FARMER1.wav"), os.path.join("sounds", "voiceovers", "field", "FARMER2.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(1, 0, 1), (1, 1, 1)], 
			
			# List of other character objects spawned after interaction
			[l2Transport, l2Transport2], 
			# Remove this character after interacting?
			False)
			
		#Initialize!
		dullard = character.NPC(
			
			# Reference to itself, starting x, y
			self, 576, 54, 
			
			# List of sprite
			[os.path.join("imgs", "Male5.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "field", "Dull1.png"), os.path.join("dialogue", "field", "Dull2.png"), os.path.join("dialogue", "tutorial", "Chelbi14.png")], 
			
			# Player's dialogue boxes list
			[os.path.join("dialogue", "field", "HDull1.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "field", "DULLARD.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 0)], 
			
			# List of other character objects spawned after interaction
			[], 
			# Remove this character after interacting?
			False)
			
			
		h1 = character.Obstacle(
		832,512,[os.path.join("imgs","BuildingLeftEnd.png")],self.display)

		h2 = character.Obstacle(
		896,512,[os.path.join("imgs","BuildingRightEnd.png")],self.display)

		house = [h1,h2]
			
		# Trees!
		trees = sortObjects(treePlacer([
			(0, 0), (1, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), 
			(0, 1), (5, 1), (6, 1), (7, 1), (8, 1), (12, 1), (13, 1), (14, 1), (15, 1), 
			(0, 2), (14, 2), (15, 2), (0, 3), (15, 3), 
			(0, 4), 
			(0, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), 
			(6, 6), (7, 6), (8, 6), (13, 6), (14, 6), (15, 6), (14, 7), (15, 7), 
			(0, 8), (1, 8), (2, 8), (15, 8), 
			(0, 9), (1, 9), (2, 9), (15, 9), (0, 10), 
			(1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10)
		
		], self.display))

		self.NPCList = self.NPCList + [farmer, dullard] + trees + house
		self.NPCList = [l0Transport, l0Transport2, l3Transport, l3Transport2] + sortObjects(self.NPCList)

			
#Wheat:(9, 6), (10, 6), (11, 6), (12, 6), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9)



			
class Level_Jungle(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()
		
		
	def generate(self):
		
		# Back to 1!
		l1Transport = character.Transport(128, 672, self.display, (128, 0, 1))
		l1Transport2 = character.Transport(192, 672, self.display, (192, 0, 1))
			
		#Initialize!
		baboon = character.Enemy(
			
			# Reference to itself, starting x, y
			self, 832, 448, 
			
			# List of sprite
			[os.path.join("imgs", "Baboon.png")], 
			
			# Display 
			self.display, 
			
			# Spawn on defeat
			[l1Transport, l1Transport2], 
			
			# Sound effect
			[os.path.join("sounds", "WOLOLO1.wav")]
			
		)
			
			
			
		# Trees!
		trees = sortObjects(treePlacer([
			(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), 
			(0, 1), (1, 1), (2, 1), (3, 1), (6, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), 
			(0, 2), (1, 2), (2, 2), (4, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), 
			(0, 3), (1, 3), (2, 3), (6, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), 
			(0, 4), (1, 4), (2, 4), (5, 4), (6, 4), (7, 4), (9, 4), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), 
			(0, 5), (1, 5), (4, 5), (5, 5), (6, 5), (11, 5), (12, 5), (13, 5), (14, 5), (15, 5), 
			(0, 6), (1, 6), (3, 6), (4, 6), (5, 6), (9, 6), (10, 6), (11, 6), (14, 6), (15, 6), 
			(0, 7), (1, 7), (4, 7), (5, 7), (7, 7), (8, 7), (9, 7), (10, 7), (14, 7), (15, 7), 
			(0, 8), (1, 8), (2, 8), (4, 8), (5, 8), (7, 8), (14, 8), (15, 8), 
			(0, 9), (1, 9), (4, 9), (5, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9), (15, 9), 
			(0, 10), (1, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10)
		], self.display))
		
		self.NPCList = self.NPCList + [baboon] + trees
		self.NPCList = sortObjects(self.NPCList)
		

class Level_Bridge(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()
		
		
	def generate(self):
		
		# Back to 1!
		l1Transport = character.Transport(-64, 256, self.display, (960, 256, 1))
		l1Transport2 = character.Transport(-64, 320, self.display, (960, 320, 1))
		
		# Ahead to 4!
		l4Transport = character.Transport(1048, 448, self.display, (0, 448, 4))
		l4Transport2 = character.Transport(1048, 512, self.display, (0, 512, 4))
		
		
		skelly = character.Enemy(
			self, 192,192,[os.path.join("imgs","SkeletonSpear.png")], self.display, [], [os.path.join("sounds","SPOOKYMOAN1.wav")], 15, 2)
		
		
		#Initialize!
		man = character.NPC(
			
			# Reference to itself, starting x, y
			self, 896, 192, 
			
			# List of sprite
			[os.path.join("imgs", "Male3.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "bridge", "SM1.png"), os.path.join("dialogue", "bridge", "SM2.png")], 
			
			# Player's dialogue boxes list
			[os.path.join("dialogue", "bridge", "HSM1.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "bridge", "SM1.wav"), os.path.join("sounds", "voiceovers", "bridge", "SM2.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1)], 
			
			# List of other character objects spawned after interaction
			[], 
			# Remove this character after interacting?
			False)

		
		#Initialize!
		woman = character.NPC(
			
			#Reference to itself, starting x, y
			self, 832, 192, 
			
			#Listofsprite
			[os.path.join("imgs", "Female2.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "habitat", "SW1.png"), os.path.join("dialogue", "habitat", "SW2.png"), os.path.join("dialogue", "habitat", "SW3.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "habitat", "HSW1.png"),os.path.join("dialogue", "habitat", "HSW2.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers","habitat", "HELPSK1.wav"), os.path.join("sounds", "voiceovers","habitat", "HELPSK2.wav"), os.path.join("sounds", "voiceovers","habitat", "THANKS1.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1), (0,1,0), (1, 0, 1)], 
			
			#List of other character objects spawned after interaction
			[skelly], 
			
			#Remove this character after interacting?
			False)
		
		
		
		
		
		
		
		
		
		
			
			
			
		
		# Borders for the water
		
		waterTextures = [os.path.join("imgs", "WaterLE1.png"), os.path.join("imgs", "WaterLE2.png"), 
						 os.path.join("imgs", "WaterRE1.png"), os.path.join("imgs", "WaterRE2.png")]
		
		waterBorder = []
		
		for i in range(11):
			if i <=  3 or i >=  8:
				tex = waterTextures[random.randint(0, 1)]
				waterBorder.append(character.Obstacle(256, i*64, [tex], self.display))
		
		for j in range(11):
			if j <=  3 or j  >=  8:
				tex = waterTextures[random.randint(2, 3)]
				waterBorder.append(character.Obstacle(702, j*64, [tex], self.display))

		barriers = []
		
		for i in range(15):
			barriers.append(character.Obstacle(256 + ((i+1) * 32) , 224, [os.path.join("imgs", "TransparencySmall.png")], self.display))
			barriers.append(character.Obstacle(256 + ((i+1) * 32) , 512, [os.path.join("imgs", "TransparencySmall.png")], self.display))
		
		
		# Trees!
		trees = sortObjects(treePlacer([
			(0, 0), (1, 0), (2, 0), (3, 0), (12, 0), (13, 0), (14, 0), (15, 0), 
			(0, 1), (12, 1), (13, 1), (15, 1), 
			(0, 2), (12, 2), (15, 2), (0, 3), (15, 3), 
			(15, 4), 
			(15, 5), 
			(0, 6), (15, 6), 
			(0, 7), 
			(0, 8), 
			(0, 9), (1, 9), (2, 9), (3, 9), (12, 9), (13, 9), (15, 9), 
			(0, 10), (14, 10), (15, 10)
		
		], self.display))
		
		h1 = character.Obstacle(
			64,64,[os.path.join("imgs","BuildingLeftEnd.png")],self.display
		)
		h2 = character.Obstacle(
			128,64,[os.path.join("imgs","BuildingCenter1.png")],self.display
		)
		h3 = character.Obstacle(
			192,64,[os.path.join("imgs","BuildingRightEnd.png")],self.display
		)
		
		house = [h1,h2,h3]
		
		
		self.NPCList = self.NPCList + barriers + [man, woman] + trees + house
		self.NPCList = waterBorder  + [l1Transport, l1Transport2, l4Transport, l4Transport2] + sortObjects(self.NPCList)
		



class Level_Town(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()

		
	def generate(self):
		
		
		# Back to 3!
		l3Transport = character.Transport(-64, 448, self.display, (960, 448, 3))
		l3Transport2 = character.Transport(-64, 512, self.display, (960, 512, 3))
		
		# Down to 5!
		l5Transport = character.Transport(640, 672, self.display, (640, 0, 5))
		l5Transport2 = character.Transport(704, 672, self.display, (704, 0, 5))
		
		# Ahead to 6!
		l6Transport = character.Transport(1048, 64, self.display, (0, 64, 6))
		l6Transport2 = character.Transport(1048, 128, self.display, (0, 128, 6))

		# Up to 7!
		l7Transport = character.Transport(192, -64, self.display, (192, 640, 7))
		l7Transport2 = character.Transport(256, -64, self.display, (256, 640, 7))
		
			
		
		#Initialize!
		defenseGuy = character.NPC(
			
			# Reference to itself, starting x, y
			self, 768, 448, 
			
			# List of sprite
			[os.path.join("imgs", "Female3.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "town", "Town1.png"), os.path.join("dialogue", "town", "Town2.png"), os.path.join("dialogue", "town", "Town2_2.png")], 
			
			# Player's dialogue boxes list
			[os.path.join("dialogue", "town", "HTown1.png"), os.path.join("dialogue", "town", "HTown2.png"), os.path.join("dialogue", "town", "HTown3.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "town", "DEFENSESYSTEM1.wav"), os.path.join("sounds", "voiceovers", "town", "DEFENSESYSTEM3.wav"), os.path.join("sounds", "voiceovers", "town", "DEFENSESYSTEM4.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(0, 1, 0), (1, 0, 1), (0, 1, 0), (1, 0, 1), (1,0,1), (0,1,0)], 
			
			# List of other character objects spawned after interaction
			[l5Transport, l5Transport2], 
			# Remove this character after interacting?
			False)
		



		#Initialize!
		littleGirl = character.NPC(
			
			# Reference to itself, starting x, y
			self, 576, 128, 
			
			# List of sprite
			[os.path.join("imgs", "Female1.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "town", "LittleGirl.png")], 
			
			# Player's dialogue boxes list
			[], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "town", "LITTLEGIRL1.wav")], 
			# Conversation key (list of 3-tuples)
			[(1, 0, 1)], 
			
			# List of other character objects spawned after interaction
			[], 
			# Remove this character after interacting?
			False)




		#Initialize!
		man3 = character.NPC(
			
			# Reference to itself, starting x, y
			self, 704, 128, 
			
			# List of sprite
			[os.path.join("imgs", "OldMan.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "town", "TM1.png"), os.path.join("dialogue", "town", "TM1_2.png"), os.path.join("dialogue", "town", "TM2.png")], 
			
			# Player's dialogue boxes list
			[os.path.join("dialogue", "town", "HTM1.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "town", "SKELLYQUEST1.wav"), os.path.join("sounds", "voiceovers", "town", "SKELLYQUEST2.wav"), os.path.join("sounds", "voiceovers", "town", "SKELLYQUEST3.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(1, 0, 1), (1, 0, 1), (0, 1, 0), (1, 0, 1)], 
			
			# List of other character objects spawned after interaction
			[], 
			# Remove this character after interacting?
			False)
			

		#Initialize!
		jazzyJill = character.NPC(
			
			# Reference to itself, starting x, y
			self, 448, 448, 
			
			# List of sprite
			[os.path.join("imgs", "JazzyJill.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "town", "JazzyJill.png")], 
			
			# Player's dialogue boxes list
			[], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "town", "JAZZYJILL.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(1, 0, 1)], 
			
			# List of other character objects spawned after interaction
			[], 
			# Remove this character after interacting?
			False)


		#Initialize!
		man1 = character.NPC(
			
			# Reference to itself, starting x, y
			self, 64, 256, 
			
			# List of sprite
			[os.path.join("imgs", "Male3.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "town", "FM1.png"), os.path.join("dialogue", "town", "FM2.png"), os.path.join("dialogue", "town", "FM3.png")], 
			
			# Player's dialogue boxes list
			[os.path.join("dialogue", "town", "HFM1.png"), os.path.join("dialogue", "town", "HFM2.png"), os.path.join("dialogue", "town", "HFM3.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "town", "GUY1.wav"), os.path.join("sounds", "voiceovers", "town", "GUY2.wav"), os.path.join("sounds", "voiceovers", "town", "GUY3.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(0, 1, 0), (1, 0, 1), (0, 1, 0), (1, 0, 1), (0, 1, 0), (1, 0, 1)], 
			
			# List of other character objects spawned after interaction
			[], 
			
			# Remove this character after interacting?
			False)
			
		
		h1 = character.Obstacle(
			64,64,[os.path.join("imgs","BuildingLeftEnd.png")],self.display)

		h2 = character.Obstacle(
			128,64,[os.path.join("imgs","BuildingRightEnd.png")],self.display)

		
		h3 = character.Obstacle(
			256,128,[os.path.join("imgs","BuildingLeftEnd.png")],self.display)

		h4 = character.Obstacle(
			320,128,[os.path.join("imgs","BuildingCenter1.png")],self.display)
		
		h5 = character.Obstacle(
			384,128,[os.path.join("imgs","BuildingCenter2.png")],self.display)
		
		h6 = character.Obstacle(
			448,128,[os.path.join("imgs","BuildingRightEnd.png")],self.display)
		

		house = [h1,h2,h3,h4,h5,h6]
			
		trees = sortObjects(treePlacer([
			(0, 0), (1, 0), (2, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), 
			(0, 1), (9, 1), (10, 1), (11, 1), (0, 2), (10, 2), 
			(0, 3), (10, 3), (14, 3), (15, 3), 
			(0, 4), (3, 4), (10, 4), (14, 4), (15, 4), 
			(0, 5), (3, 5), (15, 5), 
			(0, 6), (3, 6), (7, 6), (15, 6), 
			(6, 7), (13, 7), (15, 7), 
			(15, 8), 
			(0, 9), (3, 9), (9, 9), (14, 9), (15, 9), 
			(0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (12, 10), (13, 10), (14, 10), (15, 10)		
		], self.display))


		self.NPCList = self.NPCList + trees + house + [man1, man3, defenseGuy, littleGirl, jazzyJill] + [l3Transport, l3Transport2, l6Transport, l6Transport2, l7Transport, l7Transport2]
		
		self.NPCList = sortObjects(self.NPCList)
											


class Level_Maze(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()
		
	def generate(self):
	
		# Back to 4!
		l4Transport = character.Transport(640, -64, self.display, (640, 640, 4))
		l4Transport2 = character.Transport(704, -64, self.display, (704, 640, 4))
	
		
		# Initialize
		activeCrystal1 = character.Creature(
			
			# Reference to self, starting x, y
			self, 64, 64, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalActive.png")], 
			
			# Display
			self.display, 
			
			None, False, [], 
			
			)
		
		# Initialize
		activeCrystal2 = character.Creature(
			
			# Reference to self, starting x, y
			self, 896, 192, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalActive.png")], 
			
			# Display
			self.display, 
			
			None, False, [], 
			)
	
		# Initialize
		activeCrystal3 = character.Creature(
			
			# Reference to self, starting x, y
			self, 192, 64, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalActive.png")], 
			
			# Display
			self.display, 
			
			None, False, [], 
			)

		# Initialize
		activeCrystal4 = character.Creature(
			
			# Reference to self, starting x, y
			self, 64, 512, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalActive.png")], 
			
			# Display
			self.display, 
			
			None, False, [], 
			)
		
		# Initialize
		activeCrystal5 = character.Creature(
			
			# Reference to self, starting x, y
			self, 320, 448, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalActive.png")], 
			
			# Display
			self.display, 
			
			None, False, [], 
			)
		
		# Initialize
		activeCrystal6 = character.Creature(
			
			# Reference to self, starting x, y
			self, 768, 384, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalActive.png")], 
			
			# Display
			self.display, 
			
			None, False, [], 
			)
		
		

		# Initialize
		inactiveCrystal1 = character.Creature(
			
			# Reference to self, starting x, y
			self, 64, 64, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalInactive.png")], 
			
			# Display
			self.display, 
			
			# No sounds
			None, 
			
			# Destroy after use?
			True, 
			
			#Spawn corresponding activeCrystal
			otherActions = [activeCrystal1]
			)
		
		# Initialize
		inactiveCrystal2 = character.Creature(
			
			# Reference to self, starting x, y
			self, 896, 192, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalInactive.png")], 
			
			# Display
			self.display, 
			
			# No sounds
			None, 
			
			# Destroy after use?
			True, 
			
			#Spawn corresponding activeCrystal
			otherActions = [activeCrystal2]
			)
	
		# Initialize
		inactiveCrystal3 = character.Creature(
			
			# Reference to self, starting x, y
			self, 192, 64, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalInactive.png")], 
			
			# Display
			self.display, 
			
			# No sounds
			None, 
			
			# Destroy after use?
			True, 
			
			#Spawn corresponding activeCrystal
			otherActions = [activeCrystal3]
			)

		# Initialize
		inactiveCrystal4 = character.Creature(
			
			# Reference to self, starting x, y
			self, 64, 512, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalInactive.png")], 
			
			# Display
			self.display, 
			
			# No sounds
			None, 
			
			# Destroy after use?
			True, 
			
			#Spawn corresponding activeCrystal
			otherActions = [activeCrystal4]
			)
		
		# Initialize
		inactiveCrystal5 = character.Creature(
			
			# Reference to self, starting x, y
			self, 320, 448, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalInactive.png")], 
			
			# Display
			self.display, 
			
			# No sounds
			None, 
			
			# Destroy after use?
			True, 
			
			#Spawn corresponding activeCrystal
			otherActions = [activeCrystal5]
			)
		
		# Initialize
		inactiveCrystal6 = character.Creature(
			
			# Reference to self, starting x, y
			self, 768, 384, 
			
			# List of sprite
			[os.path.join("imgs", "CrystalInactive.png")], 
			
			# Display
			self.display, 
			
			# No sounds
			None, 
			
			# Destroy after use?
			True, 
			
			#Spawn corresponding activeCrystal
			otherActions = [activeCrystal6]
			)








		
		trees = sortObjects(treePlacer([
			(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), 
			(1, 0), (1, 10), 
			(2, 0), (2, 1), (2, 4), (2, 5), (2, 9), (2, 10), 
			(3, 0), (3, 7), (3, 9), (3, 10), 
			(4, 0), (4, 2), (4, 4), (4, 5), (4, 6), (4, 7), (4, 10), 
			(5, 0), (5, 6), (5, 10), 
			(6, 0), (6, 1), (6, 2), (6, 3), (6, 6), (6, 7), (6, 10), 
			(7, 0), (7, 4), (7, 5), (7, 9), (7, 10), 
			(8, 0), (8, 2), (8, 4), (8, 5), (8, 7), (8, 10), 
			(9, 0), (9, 2), (9, 8), (9, 10), 
			(10, 2), (10, 4), (10, 6), (10, 8), (10, 10), 
			(11, 2), (11, 5), (11, 8), (11, 10), 
			(12, 0), (12, 3), (12, 5), (12, 10), 
			(13, 0), (13, 2), (13, 3), (13, 6), (13, 8), (13, 9), (13, 10), 
			(14, 0), (14, 2), (14, 10), 
			(15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10)
		], self.display))
		
		
		self.NPCList = self.NPCList+[l4Transport, l4Transport2]+ trees + [inactiveCrystal1, inactiveCrystal2, inactiveCrystal3, inactiveCrystal4, inactiveCrystal5, inactiveCrystal6]
		self.NPCList = sortObjects(self.NPCList)
		



class Level_Hairy(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()

		
	def generate(self):
		
		
		
		#Backto4!
		l4Transport = character.Transport(-64, 64, self.display, (960, 64, 4))
		l4Transport2 = character.Transport(-64, 128, self.display, (960, 128, 4))

		
		

			
		#Initialize!
		beardedMan = character.NPC(
			
			#Reference to itself, starting x, y
			self, 448, 320, 
			
			#Listofsprite
			[os.path.join("imgs", "BeardedMan.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "hairy", "BM3.png")], 
			
			#Player's dialogueboxes list
			[], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "hairy", "RUNAWAYBEARDTHANKS.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1)], 
			
			#List of other character objects spawned after interaction
			[], 
			#Remove this character after interacting?
			False)


		#Initialize!
		baldlessWoman = character.NPC(
			
			#Reference to itself, starting x, y
			self, 320, 320, 
			
			#Listofsprite
			[os.path.join("imgs", "BaldlessWoman.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "hairy", "BW3.png")], 
			
			#Player's dialogueboxes list
			[], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "hairy", "LOWBALDWOMANTHANKS.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1)], 
			
			#List of other character objects spawned after interaction
			[], 
			#Remove this character after interacting?
			False)
		


			
		#Initialize!
		loiteringMan = character.NPC(
			
			#Reference to itself, starting x, y
			self, 704, 512, 
			
			#Listofsprite
			[os.path.join("imgs", "Male5.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "tutorial", "Chelbi12.png"), os.path.join("dialogue", "tutorial", "Chelbi13.png"), os.path.join("dialogue", "tutorial", "Chelbi14.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "tutorial", "Player8.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "CHELBI13.wav"), os.path.join("sounds", "voiceovers", "CHELBI14.wav"), os.path.join("sounds", "voiceovers", "CHELBI15.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1), (1, 0, 1)], 
			
			#List of other character objects spawned after interaction
			[], 
			#Remove this character after interacting?
			False)

		#Initialize!
		beardSkel = character.Enemy(
			
			#Reference to itself, starting x, y
			self, 768, 128, 
			
			#Listofsprite
			[os.path.join("imgs", "BeardedSkeleton.png")], 
			
			#Display
			self.display, 
			
			#Spawnondefeat
			[beardedMan], 
			
			#Soundeffect
			[os.path.join("sounds", "WOLOLO1.wav")]
	
		)
			
		#Initialize!
		wigBarb = character.Enemy(
			
			#Reference to itself, starting x, y
			self, 64, 256, 
			
			#Listofsprite
			[os.path.join("imgs", "BarbarianWithWig.png")], 
			
			#Display
			self.display, 
			
			#Spawnondefeat
			[baldlessWoman], 
			
			#Soundeffect
			[os.path.join("sounds", "WOLOLO1.wav")]
	
		)
			

		#Initialize!
		baldWoman = character.NPC(
			
			#Reference to itself, starting x, y
			self, 320, 320, 
			
			#Listofsprite
			[os.path.join("imgs", "BaldWoman.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "hairy", "BW1.png"), os.path.join("dialogue", "hairy", "BW2.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "hairy", "HBW1.png"), os.path.join("dialogue", "hairy", "HBW2.png"), os.path.join("dialogue", "hairy", "HBW3.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "hairy", "LOWBALDWOMAN1.wav"), os.path.join("sounds", "voiceovers", "hairy", "LOWBALDWOMAN2.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(0, 1, 0), (1, 0, 1), (0, 1, 0), (1, 0, 1), (0, 1, 0)], 
			
			#List of other character objects spawned after interaction
			[wigBarb], 
			
			#Remove this character after interacting?
			True)
		
		
		#Initialize!
		beardlessMan = character.NPC(
			
			#Reference to itself, starting x, y
			self, 448, 320, 
			
			#Listofsprite
			[os.path.join("imgs", "BeardlessMan.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "hairy", "BM1.png"), os.path.join("dialogue", "hairy", "BM1_2.png"), os.path.join("dialogue", "hairy", "BM2.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "hairy", "HBM1.png"), os.path.join("dialogue", "hairy", "HBM2.png"), os.path.join("dialogue", "hairy", "HBM3.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "hairy", "RUNAWAYBEARD1.wav"), os.path.join("sounds", "voiceovers", "hairy", "RUNAWAYBEARD1_2.wav"), os.path.join("sounds", "voiceovers", "hairy", "RUNAWAYBEARD2.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(0, 1, 0), (1, 0, 1), (1, 0, 1), (0, 1, 0), (1, 0, 1), (0, 1, 0)], 
			
			#List of other character objects spawned after interaction
			[beardSkel], 
			#Remove this character after interacting?
			True)





			
			
		trees = sortObjects(treePlacer([
			(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), 
			(7, 1), (8, 1), (9, 1), (15, 1), (9, 2), (10, 2), (13, 2), (15, 2), 
			(0, 3), (1, 3), (2, 3), (3, 3), (9, 3), (10, 3), (15, 3), 
			(0, 4), (3, 4), (8, 4), (10, 4), (11, 4), (12, 4), (15, 4), 
			(0, 5), (3, 5), (6, 5), (10, 5), (15, 5), 
			(0, 6), (3, 6), (6, 6), (9, 6), (12, 6), (15, 6), 
			(0, 7), (2, 7), (8, 7), (13, 7), (15, 7), 
			(0, 8), (2, 8), (3, 8), (7, 8), (8, 8), (9, 8), (10, 8), (13, 8), (15, 8), 
			(0, 9), (15, 9), 
			(0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10)
		], self.display))


		self.NPCList = self.NPCList+trees+[baldWoman, beardlessMan]+[l4Transport, l4Transport2]
		
		self.NPCList = sortObjects(self.NPCList)
											
											
											
											
class Level_CityLimits(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()

		
	def generate(self):
		
		
		
		#Backto4!
		l4Transport = character.Transport(192, 672, self.display, (192, 0, 4))
		l4Transport2 = character.Transport(256, 672, self.display, (256, 0, 4))
		
		#Upto8!
		l8Transport = character.Transport(448, -64, self.display, (448, 640, 8))
		l8Transport2 = character.Transport(512, -64, self.display, (512, 640, 8))
		
		#Aheadto9!
		l9Transport = character.Transport(1024, 256, self.display, (0, 448, 9))
		l9Transport2 = character.Transport(1024, 320, self.display, (0, 512, 9))

		
		
		#Initialize!
		nonBeliever = character.NPC(
			
			#Reference to itself, starting x, y
			self, 192, 64, 
			
			#Listofsprite
			[os.path.join("imgs", "Female4.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "citylimits", "NB1.png"), os.path.join("dialogue", "citylimits", "NB2.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "citylimits", "HNB1.png"), os.path.join("dialogue", "citylimits", "HNB2.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "citylimits", "NONBELIEVER1.wav"), os.path.join("sounds", "voiceovers", "citylimits", "NONBELIEVER2.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1), (0, 1, 0)], 
			
			#List of other character objects spawned after interaction
			[], 
			#Remove this character after interacting?
			False)
	
	

		#Initialize!
		guardPost = character.NPC(
			
			#Reference to itself, starting x, y
			self, 576, 256, 
			
			#Listofsprite
			[os.path.join("imgs", "Guard.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "citylimits", "Guard7.png")], 
			
			#Player's dialogueboxes list
			[], 
			#Sound files list
			[os.path.join("sounds", "voiceovers", "citylimits", "RUDEKNIGHTTHANKS.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1)], 
			
			#List of other character objects spawned after interaction
			[], 
			
			#Remove this character after interacting?
			False)
		
		
		
		
		
		#Initialize!
		guardEnemy = character.Enemy(
			
			#Reference to itself, starting x, y
			self, 576, 256, 
			
			#Listofsprite
			[os.path.join("imgs", "Guard.png")], 
			
			#Display
			self.display, 
			
			#Spawnondefeat
			[guardPost], 
			
			#Soundeffect
			[os.path.join("sounds", "voiceovers", "citylimits", "RUDEKNIGHT5.wav")]
		)

		#Initialize!
		guardPre = character.NPC(
			
			#Reference to itself, starting x, y
			self, 576, 256, 
			
			#Listofsprite
			[os.path.join("imgs", "Guard.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "citylimits", "Guard1.png"), os.path.join("dialogue", "citylimits", "Guard2.png"), os.path.join("dialogue", "citylimits", "Guard3.png"), os.path.join("dialogue", "citylimits", "Guard3_2.png"), 
			os.path.join("dialogue", "citylimits", "Guard4.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "citylimits", "HGuard1.png"), os.path.join("dialogue", "citylimits", "HGuard2.png"), os.path.join("dialogue", "citylimits", "HGuard3.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "citylimits", "RUDEKNIGHT1.wav"), os.path.join("sounds", "voiceovers", "citylimits", "RUDEKNIGHT2.wav"), os.path.join("sounds", "voiceovers", "citylimits", "RUDEKNIGHT3_1.wav"), 
			os.path.join("sounds", "voiceovers", "citylimits", "RUDEKNIGHT3_2.wav"), os.path.join("sounds", "voiceovers", "citylimits", "RUDEKNIGHT4.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1), (0, 1, 0), (1, 0, 1), (1, 0, 1), (0, 1, 0), (1, 0, 1)], 
			
			#List of other character objects spawned after interaction
			[guardEnemy], 
			
			#Remove this character after interacting?
			True)
			
			
			
		#Initialize!
		sweaterGuy = character.NPC(
			
			#Reference to itself, starting x, y
			self, 704, 512, 
			
			#Listofsprite
			[os.path.join("imgs", "SweaterGuy.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "citylimits", "SG1.png")],
			
			#Player's dialogueboxes list
			[], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "citylimits", "FYBRO1.wav")],
			
			#Conversationkey(listof3-tuples)
			[(1,0,1)], 
			
			#List of other character objects spawned after interaction
			[], 
			
			#Remove this character after interacting?
			False)
		
		
		
		h1 = character.Obstacle(
			192,320,[os.path.join("imgs","BuildingLeftEnd.png")],self.display)

		h2 = character.Obstacle(
			256,320,[os.path.join("imgs","BuildingCenter2.png")],self.display)

		h3 = character.Obstacle(
			320,320,[os.path.join("imgs","BuildingRightEnd.png")],self.display)

		house = [h1,h2,h3]

		trees = sortObjects(treePlacer([
			(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), 
			(0, 1), (1, 1), (2, 1), (5, 1), (6, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), 
			(0, 2), (1, 2), (5, 2), (12, 2), (13, 2), (14, 2), (15,2), 
			(0, 3), (4, 3), (8, 3), (9, 3), (13, 3), (15, 3), 
			(0, 4), (3, 4), (4, 4), (5, 4), (10, 4), 
			(0, 5), (3, 5), (5, 5), (10, 5), (11, 5), 
			(0, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (14, 6), (15, 6), 
			(0, 7), (1, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), 
			(0, 8), (1, 8), (2, 8), (7, 8), (13, 8), (14, 8), (15, 8), 
			(0, 9), (1, 9), (2, 9), (14, 9), (15, 9), 
			(0, 10), (1, 10), (2, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10)
			
			], self.display))


		self.NPCList = self.NPCList+trees+house+[guardPre, sweaterGuy, nonBeliever]+[l4Transport, l4Transport2, l8Transport, 
												l8Transport2, l9Transport, l9Transport2]
		
		self.NPCList = sortObjects(self.NPCList)
											
	

class Level_Habitat(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()

		
	def generate(self):
		
		
		
		
		#Backto7!
		l7Transport = character.Transport(-64, 448, self.display, (960, 256, 7))
		l7Transport2 = character.Transport(-64, 512, self.display, (960, 320, 7))

		#Aheadto10!
		l11Transport = character.Transport(1024, 64, self.display, (0, 256, 10))
		l11Transport2 = character.Transport(1024, 128, self.display, (0, 320, 10))

		
		#Initialize!
		veteranPost = character.NPC(
			
			#Reference to itself, starting x, y
			self, 128, 192, 
			
			#Listofsprite
			[os.path.join("imgs", "VeteranDruid.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "habitat", "Vet6.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "habitat", "HVet3.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers","habitat", "OLDDRUID5.wav")],
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1), (0, 1, 0)], 
			
			#List of other character objects spawned after interaction
			[l11Transport, l11Transport2], 
			
			#Remove this character after interacting?
			False)
		
		
		
		#Initialize!
		veteranEnemy = character.Enemy(
			
			#Reference to itself, starting x, y
			self, 128, 192, 
			
			#Listofsprite
			[os.path.join("imgs", "VeteranDruid.png")], 
			
			#Display
			self.display, 
			
			#Spawnondefeat
			[veteranPost], 
			
			#Soundeffect
			[os.path.join("sounds", "voiceovers","habitat", "OLDDRUID4.wav")]
		)
		
		
		#Initialize!
		veteranPre = character.NPC(
			
			#Reference to itself, starting x, y
			self, 128, 192, 
			
			#Listofsprite
			[os.path.join("imgs", "VeteranDruid.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "habitat", "Vet1.png"), os.path.join("dialogue", "habitat", "Vet2.png"), os.path.join("dialogue", "habitat", "Vet3.png"),
			os.path.join("dialogue", "habitat", "Vet4.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "habitat", "HVet1.png"),os.path.join("dialogue", "habitat", "HVet2.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers","habitat", "OLDDRUID1_1.wav"), os.path.join("sounds", "voiceovers","habitat", "OLDDRUID1_2.wav"), os.path.join("sounds", "voiceovers","habitat", "OLDDRUID2.wav"), 
			os.path.join("sounds", "voiceovers","habitat", "OLDDRUID3.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1), (0, 1, 0), (1,0,1),  (0,1,0), (1, 0, 1), (1,0,1)], 
			
			#List of other character objects spawned after interaction
			[veteranEnemy], 
			
			#Remove this character after interacting?
			True)


		#Initialize!
		woman = character.NPC(
			
			# Reference to itself, starting x, y
			self, 832, 320, 
			
			# List of sprite
			[os.path.join("imgs", "Female2.png")], 
			
			# Display 
			self.display, 
			
			# NPC's dialogue boxes list
			[os.path.join("dialogue", "bridge", "FW1.png"), os.path.join("dialogue", "bridge", "FW2.png")], 
			
			# Player's dialogue boxes list
			[os.path.join("dialogue", "bridge", "HFW1.png")], 
			
			# Sound files list
			[os.path.join("sounds", "voiceovers", "bridge", "FW1.wav"), os.path.join("sounds", "voiceovers", "bridge", "FW2.wav")], 
			
			# Conversation key (list of 3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1)], 
			
			# List of other character objects spawned after interaction
			[], 
			
			# Remove this character after interacting?
			False)




			
		trees = sortObjects(treePlacer([
			(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),
			(0,1),(5,1),(6,1),(7,1),
			(0,2),(2,2),(3,2),(8,2),
			(0,3),(9,3),(12,3),(13,3),(14,3),(15,3),
			(0,4),(10,4),(13,4),(14,4),(15,4),
			(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(10,5),(15,5),
			(0,6),(1,6),(2,6),(9,6),(15,6),
			(12,7),(15,7),
			(12,8),(15,8),
			(0,9),(1,9),(8,9),(9,9),(11,9),(15,9),
			(0,10),(1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(10,10),(11,10),(12,10),(13,10),(14,10),(15,10)],
			self.display))


		self.NPCList = self.NPCList+trees+[woman, veteranPre]+[l7Transport, l7Transport2]
		
		self.NPCList = sortObjects(self.NPCList)





	
class Level_Lair(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()

		
	def generate(self):
		
		
		
		
		#Backto7!
		l7Transport = character.Transport(448, 672, self.display, (448, 0, 7))
		l7Transport2 = character.Transport(512, 672, self.display, (512, 0, 7))

	
		#Initialize!
		warlockPost = character.NPC(
			
			#Reference to itself, starting x, y
			self, 128, 448, 
			
			#Listofsprite
			[os.path.join("imgs", "Warlock.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "lair", "W4.png")],
			
			#Player's dialogueboxes list
			[],
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "lair", "WARLOCK5.wav")],
			
			#Conversationkey(listof3-tuples)
			[(1,0,1)],
			
			#List of other character objects spawned after interaction
			[], 
			#Remove this character after interacting?
			
			True)
	
		
		#Initialize!
		warlockEnemy = character.Enemy(
			
			#Reference to itself, starting x, y
			self, 128, 448, 
			
			#Listofsprite
			[os.path.join("imgs", "Warlock.png")], 
			
			#Display
			self.display, 
			
			#Spawnondefeat
			[warlockPost], 
			
			#Soundeffect
			[os.path.join("sounds", "voiceovers", "lair", "WARLOCK4.wav")]
	
		)
		
		#Initialize!
		warlockPre = character.NPC(
			
			#Reference to itself, starting x, y
			self, 128, 448, 
			
			#Listofsprite
			[os.path.join("imgs", "Warlock.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "lair", "W1.png"),os.path.join("dialogue", "lair", "W1_2.png"),os.path.join("dialogue", "lair", "W2.png")],
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "lair", "HW6.png")],
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "lair", "WARLOCK1.wav"),os.path.join("sounds", "voiceovers", "lair", "WARLOCK2.wav"),os.path.join("sounds", "voiceovers", "lair", "WARLOCK3.wav")],
			
			#Conversationkey(listof3-tuples)
			[(0,1,0),(1,0,1),(1,0,1)],
			
			#List of other character objects spawned after interaction
			[warlockEnemy], 
			
			#Remove this character after interacting?
			
			True)
	
	

		#Initialize!
		warlockQuest = character.NPC(
			
			#Reference to itself, starting x, y
			self, 448, 512, 
			
			#Listofsprite
			[os.path.join("imgs", "Female1.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "lair", "WP1.png"),os.path.join("dialogue", "lair", "WP2.png"),os.path.join("dialogue", "lair", "WP3.png"),
			os.path.join("dialogue", "lair", "WP3_2.png"),os.path.join("dialogue", "lair", "WP4.png"),os.path.join("dialogue", "lair", "WP4_2.png"),
			os.path.join("dialogue", "lair", "WP5.png")],
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "lair", "HW1.png"),os.path.join("dialogue", "lair", "HW2.png"),os.path.join("dialogue", "lair", "HW3.png"),
			os.path.join("dialogue", "lair", "HW4.png"),os.path.join("dialogue", "lair", "HW5.png")],
			
			#Sound files list
			[os.path.join("sounds", "voiceovers", "lair", "WARLOCKQUEST1.wav"),os.path.join("sounds", "voiceovers", "lair", "WARLOCKQUEST2.wav"),os.path.join("sounds", "voiceovers", "lair", "WARLOCKQUEST3.wav"),
			os.path.join("sounds", "voiceovers", "lair", "WARLOCKQUEST4.wav"),os.path.join("sounds", "voiceovers", "lair", "WARLOCKQUEST5.wav"),os.path.join("sounds", "voiceovers", "lair", "WARLOCKQUEST6.wav"),
			os.path.join("sounds", "voiceovers", "lair", "WARLOCKQUEST8.wav")],
			
			#Conversationkey(listof3-tuples)
			[(1,0,1),(0,1,0),(1,0,1),(0,1,0),(1,0,1),(1,0,1),(0,1,0),(1,0,1),(1,0,1),(0,1,0),(1,0,1),(0,1,0)],			
			
			#List of other character objects spawned after interaction
			[warlockPre], 
			#Remove this character after interacting?
			False)


			
			
			
			
		trees = sortObjects(treePlacer([
			(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0),
			(0, 1), (10, 1), (15, 1), 
			(0, 2), (8, 2), (10, 2), (12, 2), (13, 2), (15, 2),
			(0, 3), (2, 3), (5, 3), (6, 3), (10, 3), (12, 3), (15, 3), 
			(0, 4), (2, 4), (7, 4), (9, 4), (10, 4), (13, 4), (15, 4), 
			(0, 5), (2, 5), (3, 5), (8, 5), (9, 5), (13, 5), (15, 5), 
			(0, 6), (2, 6), (3, 6), (4, 6), (12, 6), (15, 6), 
			(0, 7), (3, 7), (4, 7), (5, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (13, 7), (15, 7), 
			(0, 8), (3, 8), (4, 8), (5, 8), (6, 8), (12, 8), (15, 8), 
			(0, 9), (1, 9), (2, 9), (9, 9), (10, 9), (15, 9),
			(0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10)			
			
			], self.display))


		self.NPCList = self.NPCList+trees+[warlockQuest]+[l7Transport, l7Transport2]
		
		self.NPCList = sortObjects(self.NPCList)
											
											
class Level_Turtle(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()

		
	def generate(self):
		
		
		
		
		#Back to 9!
		l9Transport = character.Transport(-64, 256, self.display, (960, 64, 9))
		l9Transport2 = character.Transport(-64, 320, self.display, (960, 128, 9))

		#Ahead to 11!
		l11Transport = character.Transport(1024, 448, self.display, (0, 64, 11))
		l11Transport2 = character.Transport(1024, 512, self.display, (0, 128, 11))


		
		#Initialize!
		wiseTurtle = character.NPC(
			
			#Reference to itself, starting x, y
			self, 832, 512, 
			
			#Listofsprite
			[os.path.join("imgs", "TurtleMan.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "turtle", "WTM1.png"), os.path.join("dialogue", "turtle", "WTM2.png"), os.path.join("dialogue", "turtle", "WTM3.png"),
			os.path.join("dialogue", "turtle", "WTM4.png"), os.path.join("dialogue", "turtle", "WTM5.png"), os.path.join("dialogue", "turtle", "WTM6.png"),
			os.path.join("dialogue", "turtle", "WTM7.png"), os.path.join("dialogue", "turtle", "WTM8.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "turtle", "HWTM1.png"), os.path.join("dialogue", "turtle", "HWTM2.png"), os.path.join("dialogue", "turtle", "HWTM3.png"),
			os.path.join("dialogue", "turtle", "HWTM4.png"), os.path.join("dialogue", "turtle", "HWTM5.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers","turtle", "WTM1.wav"), os.path.join("sounds", "voiceovers","turtle", "WTM2.wav"), os.path.join("sounds", "voiceovers","turtle", "WTM3.wav"),
			os.path.join("sounds", "voiceovers","turtle", "WTM4.wav"), os.path.join("sounds", "voiceovers","turtle", "WTM5.wav"), os.path.join("sounds", "voiceovers","turtle", "WTM6.wav"),
			os.path.join("sounds", "voiceovers","turtle", "WTM7_1.wav"), os.path.join("sounds", "voiceovers","turtle", "WTM7_2.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1), (0, 1, 0), (1, 0, 1), (0,1,0),(1, 0, 1), (0, 1, 0), (1, 0, 1), (0,1,0),(1,0,1),(1, 0, 1), (0,1,0),(1,0,1),(1,0,1)], 
			
			#List of other character objects spawned after interaction
			[l11Transport, l11Transport2], 
			#Remove this character after interacting?
			False)
	

		trees = sortObjects(treePlacer([
			(0,0), (0, 1), (0, 2), (0, 3), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), 
			(1, 0), (1, 1), (1, 6), (1, 7), (1, 8), (1, 10), 
			(2, 0), (2, 7), (2, 8), (2, 10), 
			(3, 0), (3, 1), (3, 7), (3, 9), (3, 10), 
			(4, 0), (4, 1), (4, 7), (4, 10), 
			(5,0), (5, 2), (5, 7), (5, 10), 
			(6, 0), (6, 1), (6, 2), (6, 3), (6, 6),(6, 8), (6, 10), 
			(7, 0), (7, 2), (7, 7), (7, 8), (7, 10), 
			(8, 0), (8, 1), (8, 3), (8, 4), (8, 8), (8, 10), 
			(9, 0), (9, 3), (9, 8), (9, 10), 
			(10, 0), (10, 2), (10, 4), (10, 9), (10, 10), 
			(11, 0), (11, 1), (11, 2), (11, 9), (11, 10), 
			(12, 0), (12, 1), (12, 2), (12, 3), (12, 10), 
			(13, 0), (13, 1), (13, 2), (13, 3), (13, 4),(13, 10), 
			(14, 0), (14, 1), (14, 2), (14, 3), (14, 5), (14, 10), 
			(15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 9), (15, 10)			], self.display))
											
		
		self.NPCList = self.NPCList + [wiseTurtle] + trees
		self.NPCList = [l9Transport, l9Transport2] + sortObjects(self.NPCList)

		
											
											



class Level_Last(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()

		
	def generate(self):
		
		# Back to 10!
		l10Transport = character.Transport(-64, 64, self.display, (960, 448, 10))
		l10Transport2 = character.Transport(-64, 128, self.display, (960, 512, 10))
		
		# Ahead to 12!
		l12Transport = character.Transport(1024, 256, self.display, (192, 320, 12))
		l12Transport2 = character.Transport(1024, 320, self.display, (192, 320, 12))




		trees = sortObjects(treePlacer([
		(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),
		(6,1),(7,1),(8,1),(9,1),(15,1),
		(5,2),(7,2),(8,2),(9,2),(11,2),(12,2),(13,2),(15,2),
		(0,3),(1,3),(7,3),(8,3),(9,3),(13,3),(15,3),
		(0,4),(3,4),(6,4),(7,4),(10,4),(13,4),
		(0,5),(1,5),(5,5),(6,5),(10,5),(11,5),(14,5),
		(0,6),(4,6),(5,6),(11,6),(14,6),(15,6),
		(0,7),(3,7),(4,7),(8,7),(11,7),(15,7),
		(0,8),(3,8),(7,8),(8,8),(11,8),(12,8),(15,8),
		(0,9),(6,9),(7,9),(15,9),
		(0,10),(1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(10,10),(11,10),(12,10),(13,10),(14,10),(15,10)],
		self.display))

		self.NPCList = self.NPCList + trees+ [l10Transport, l10Transport2, l12Transport, l12Transport2]
		
		self.NPCList = sortObjects(self.NPCList)


		
		
class Level_Rjufus(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
		self.generate()

		
	def generate(self):

		
		
		#Initialize!
		rjufusPost = character.NPC(
			
			#Reference to itself, starting x, y
			self, 768, 256, 
			
			#Listofsprite
			[os.path.join("imgs", "RjufusO.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "rjufus", "Rjufus6.png"), os.path.join("dialogue", "rjufus", "Rjufus7.png"), os.path.join("dialogue", "rjufus", "Rjufus8.png"),
			os.path.join("dialogue", "rjufus", "Rjufus8_2.png"), os.path.join("dialogue", "rjufus", "Rjufus9.png"), os.path.join("dialogue", "rjufus", "Rjufus9_2.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "rjufus", "Hero6.png")],
			
			#Sound files list
			[os.path.join("sounds", "voiceovers","rjufus", "RJUFUS6.wav"), os.path.join("sounds", "voiceovers","rjufus", "RJUFUS7.wav"), os.path.join("sounds", "voiceovers","rjufus", "RJUFUS8.wav"),
			os.path.join("sounds", "voiceovers","rjufus", "RJUFUS9.wav"), os.path.join("sounds", "voiceovers","rjufus", "RJUFUS10.wav"), os.path.join("sounds", "voiceovers","rjufus", "RJUFUS11.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1),(1, 0, 1),(1, 0, 1),(1, 0, 1),(0,1,0),(1, 0, 1),(1, 0, 1)], 
			
			#List of other character objects spawned after interaction
			[], 
			
			#Remove this character after interacting?
			False)
		
		
		
		#Initialize!
		rjufusEnemy = character.Enemy(
			
			#Reference to itself, starting x, y
			self, 768, 256, 
			
			#Listofsprite
			[os.path.join("imgs", "Rjufus.png")], 
			
			#Display
			self.display, 
			
			#Spawnondefeat
			[rjufusPost], 
			
			#Soundeffect
			[os.path.join("sounds", "voiceovers","rjufus", "RJUFUS5.wav")]
		)
		
		
		#Initialize!
		rjufusPre = character.NPC(
			
			#Reference to itself, starting x, y
			self, 768, 256, 
			
			#Listofsprite
			[os.path.join("imgs", "Rjufus.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "rjufus", "Rjufus1.png"), os.path.join("dialogue", "rjufus", "Rjufus2.png"), os.path.join("dialogue", "rjufus", "Rjufus3.png")], 
			
			#Player's dialogueboxes list
			[],
			
			#Sound files list
			[os.path.join("sounds", "voiceovers","rjufus", "RJUFUS1.wav"), os.path.join("sounds", "voiceovers","rjufus", "RJUFUS2.wav"), os.path.join("sounds", "voiceovers","rjufus", "RJUFUS3.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(1, 0, 1), (1,0,1), (1,0,1)], 
			
			#List of other character objects spawned after interaction
			[rjufusEnemy], 
			
			#Remove this character after interacting?
			True)

		#Initialize!
		evilChelbi = character.NPC(
			
			#Reference to itself, starting x, y
			self, 768, 256, 
			
			#Listofsprite
			[os.path.join("imgs", "Chelbi.png")], 
			
			#Display
			self.display, 
			
			#NPC's dialogue boxes list
			[os.path.join("dialogue", "rjufus", "Chelbi1.png"), os.path.join("dialogue", "rjufus", "Chelbi2.png"), os.path.join("dialogue", "rjufus", "Chelbi3.png"),
			os.path.join("dialogue", "rjufus", "Chelbi4.png")], 
			
			#Player's dialogueboxes list
			[os.path.join("dialogue", "rjufus", "Hero1.png"),os.path.join("dialogue", "rjufus", "Hero2.png"),os.path.join("dialogue", "rjufus", "Hero3.png"),
			os.path.join("dialogue", "rjufus", "Hero4.png"), os.path.join("dialogue", "rjufus", "Hero5.png")], 
			
			#Sound files list
			[os.path.join("sounds", "voiceovers","rjufus", "ENDCHELBI1.wav"), os.path.join("sounds", "voiceovers","rjufus", "ENDCHELBI2.wav"), os.path.join("sounds", "voiceovers","rjufus", "ENDCHELBI3.wav"), 
			os.path.join("sounds", "voiceovers","rjufus", "ENDCHELBI4.wav")], 
			
			#Conversationkey(listof3-tuples)
			[(0,1,0),(1, 0, 1), (0,1,0), (1,0,1), (0, 1, 0), (1, 0, 1), (0,1,0), (1, 0, 1), (0,1,0)], 
			
			#List of other character objects spawned after interaction
			[rjufusPre], 
			
			#Remove this character after interacting?
			True)


		# Initialize
		squirrel1 = character.Creature(
			
			# Reference to self, starting x, y
			self, 640, 192, 
			
			# List of sprite
			[os.path.join("imgs", "Squirrel.png")], 
			
			# Display
			self.display, 
			
			#Sound effect
			os.path.join("sounds", "SQUIRREL.wav"), 
			
			)

		# Initialize
		squirrel2 = character.Creature(
			
			# Reference to self, starting x, y
			self, 768, 192, 
			
			# List of sprite
			[os.path.join("imgs", "Squirrel.png")], 
			
			# Display
			self.display, 
			
			#Sound effect
			os.path.join("sounds", "SQUIRREL.wav"), 
			
			)

		# Initialize
		squirrel3 = character.Creature(
			
			# Reference to self, starting x, y
			self, 640, 384, 
			
			# List of sprite
			[os.path.join("imgs", "Squirrel.png")], 
			
			# Display
			self.display, 
			
			#Sound effect
			os.path.join("sounds", "SQUIRREL.wav"), 
			
			)





			
		
		trees = sortObjects(treePlacer([
			(0,0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), 
			(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), 
			(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), 
			(3, 0), (3, 1), (3, 2), (3, 3), (3, 7), (3, 8), (3, 9), (3, 10), 
			(4, 0), (4, 1), (4, 2), (4, 3), (4, 6), (4, 8), (4, 9), (4, 10), 
			(5,0), (5, 1), (5, 2), (5, 7), (5, 8), (5, 9), (5, 10), 
			(6, 0), (6, 1), (6, 2), (6, 8), (6, 9), (6, 10), 
			(7, 0), (7, 1), (7, 2), (7, 8), (7, 9), (7, 10), 
			(8, 0), (8, 1), (8, 2), (8, 3), (8, 7), (8, 8), (8, 9), (8, 10), 
			(9, 0), (9, 1), (9, 2), (9, 6), (9, 8), (9, 9), (9, 10), 
			(10, 0), (10, 1), (10, 2), (10, 8), (10, 9), (10, 10), 
			(11, 0), (11, 1), (11, 2), (11, 3), (11, 7), (11, 8), (11, 9), (11, 10), 
			(12, 0), (12, 1), (12, 2), (12, 6), (12, 8), (12, 9), (12, 10), 
			(13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), 
			(14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), 
			(15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10)],
		self.display))
		
		
		self.NPCList = self.NPCList + trees + [squirrel1, squirrel2, squirrel3, evilChelbi]
		
		self.NPCList = sortObjects(self.NPCList)
		
		
		
class Level_Null(LevelGen):
	def __init__(self, Player, map, disp):
		LevelGen.__init__(self, Player, map, disp)
	
		self.NPCList = []
		
