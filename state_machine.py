# Wizard Team
# January 2015
#
# Wizard Quest State Machine
#
# Creates the state machine of the game
#

####################### Setup #########################
# pygameSetup contains useful imports
# import pygame, sys, random, os
from pygameSetup import *
import time

# import map class
import map

from SMS import *
from treeInterp import *
import levelGenerator

from startScreen import *
from menu import *

import spellfunctions as sf

# import character class
import character

# set the display window's title
pygame.display.set_caption('Wizard Quest')

# initialize the fonts
try:
	pygame.font.init()
except:
	print "Fonts unavailable"
	sys.exit()

# Create a game clock
gameClock = pygame.time.Clock()

# set the initial state
state = "Start_Setup"

####################### Make Content for Start Screen ####################################

# content contained in startScreen.py file

####################### Make Content for Rules Page ######################################
rules_font = pygame.font.Font(os.path.join("font", "wiz.ttf"), 80, bold=True)
instr_font = pygame.font.Font(os.path.join("font", "wiz.ttf"), 40, bold=False)

rules = rules_font.render("Rules", True, (0, 0, 0))
story = instr_font.render("Story", True, (0, 0, 0))
controls = instr_font.render("Controls", True, (0, 0, 0))

# align the rules at the top center of the screen
rules_rect = rules.get_rect()
rules_rect.midtop = ( screen.get_rect().centerx, screen.get_rect().top + 10 )

# create a rect for the background of the story box relative to the position of the rules
story_bg = pygame.Rect((screen.get_rect().left + 20, rules_rect.bottom + 10), (screen.get_rect().width - 40, 200))

# create a rect for the background of the controls box relative to the position of the story bos
controls_bg = pygame.Rect((screen.get_rect().left + 20, story_bg.bottom + 20), (screen.get_rect().width - 40, 200))

instructions = pygame.image.load(os.path.join("menu", "RulesPage.png")).convert_alpha()

backButtonUp = pygame.image.load(os.path.join("menu", "BackUp.png")).convert_alpha()
backButtonDown = pygame.image.load(os.path.join("menu", "BackDown.png")).convert_alpha()

# create a rect for the back button
back_button = pygame.Rect((0, 0), (256, 128))

# align the back button at the bottom center of the screen (relative to the controls box)
back_button.midbottom = ( screen.get_rect().centerx, screen.get_rect().bottom - 20 )

######################### Make Content for Credits Page ##################################

wiz_font = pygame.font.Font(os.path.join("font", "wiz.ttf"), 80, bold=True)
wizards = wiz_font.render("Wizard Team", True, (0, 0, 0))
wiz_rect = wizards.get_rect()
wiz_rect.topleft = (screen.get_rect().centerx - wiz_rect.width / 2, 356)

credits1 = pygame.image.load(os.path.join("credits", "CreditsPage.png")).convert_alpha()

# make button to return to the main menu from the credits page
creditsBackRect = pygame.Rect((0, 0), (256, 128))

# make button to quit the game
creditsQuitRect = pygame.Rect((0, 0), (256, 128))

# position the main menu button relative to the bottom center of the screen
creditsBackRect.bottomright = ( (screen.get_rect().centerx - 20), (screen.get_rect().bottom - 20) )

# position the quit button relative to the bottom center of the screen
creditsQuitRect.bottomleft = ( (screen.get_rect().centerx + 20), (screen.get_rect().bottom - 20) )

################################ Map Content #############################################

textures = [
			# 0,1
			os.path.join("imgs", "grass1.png"), os.path.join("imgs", "grass2.png"), 
			# 2,3
			os.path.join("imgs", "grass3.png"),	os.path.join("imgs", "grass4.png"),
			#4,5
			os.path.join("imgs", "WaterC1.png"), os.path.join("imgs", "WaterC1.png"),
			#6,7
			os.path.join("imgs", "WaterC2.png"), os.path.join("imgs", "WaterC2.png"),
			#8,9
			os.path.join("imgs", "HorBridgeCenter1.png"), os.path.join("imgs", "HorBridgeCenter2.png"),
			#10,11
			os.path.join("imgs", "HorBridgeBotEdge.png"), os.path.join("imgs", "HorBridgeTopEdge.png"),
			#12,13
			os.path.join("imgs", "HorBridgeTopEndLeft.png"), os.path.join("imgs", "HorBridgeTopEndRight.png"),
			#14,15
			os.path.join("imgs", "HorBridgeBotEndLeft.png"), os.path.join("imgs", "HorBridgeBotEndRight.png"),
			#16,17
			os.path.join("imgs", "CropCornerTL.png"), os.path.join("imgs", "CropsCornerTR.png"),
			#18,19
			os.path.join("imgs", "CropsCornerLL.png"), os.path.join("imgs", "CropCornerLR.png"),
			#20,21
			os.path.join("imgs", "CropsBottom1.png"), os.path.join("imgs", "CropsBottom2.png"),
			#22,23
			os.path.join("imgs", "CropsTop1.png"), os.path.join("imgs", "CropsTop2.png"),
			#24,25
			os.path.join("imgs", "CropsLeft.png"), os.path.join("imgs", "CropsRight.png"),
			#26,27
			os.path.join("imgs", "CropsCenter1.png"), os.path.join("imgs", "CropsCenter2.png"),
			
			
]

layout = [[random.randint(0, 3) for i in xrange(11)] for i in xrange(16)]

bridgeLayout = [[random.randint(0, 3) for i in xrange(11)] for i in xrange(16)]

k = 4
for i in range(8):
	for j in range(11):
		if j == 4:
			if k == 4:
				bridgeLayout[k][j] = 12
			elif k == 11:
				bridgeLayout[k][j] = 13
			else:
				bridgeLayout[k][j] = 11
		elif j == 7:
			if k == 4:
				bridgeLayout[k][j] = 14
			if k == 11:
				bridgeLayout[k][j] = 15
			else:
				if k != 4 and k != 11:
					bridgeLayout[k][j] = 10
		elif 4 < j < 7:
			bridgeLayout[k][j] = random.randint(8, 9)

		elif k != 4 and k != 11:
			bridgeLayout[k][j] += 4
	k = k + 1
	
	
fieldLayout = [[random.randint(0, 3) for i in xrange(11)] for i in xrange(16)]

fieldLayout[9][6] = 16
fieldLayout[9][7] = 24
fieldLayout[9][8] = 24
fieldLayout[9][9] = 18
fieldLayout[10][6] = 22
fieldLayout[10][7] = 26
fieldLayout[10][8] = 27
fieldLayout[10][9] = 20
fieldLayout[11][6] = 23
fieldLayout[11][7] = 27
fieldLayout[11][8] = 26
fieldLayout[11][9] = 21
fieldLayout[12][6] = 17
fieldLayout[12][7] = 25
fieldLayout[12][8] = 25
fieldLayout[12][9] = 19



map1 = map.Map(textures, layout)
map2 = map.Map(textures, bridgeLayout)
map3 = map.Map(textures, fieldLayout)

########################### In-game buttons ############################

pauseRect = pygame.Rect((768, 704), (256, 64))
pauseUp = pygame.image.load(os.path.join("menu", "PauseUp.png")).convert_alpha()
pauseDown = pygame.image.load(os.path.join("menu", "PauseDown.png")).convert_alpha()

characterRect = pygame.Rect((512, 704), (256, 64))
characterUp = pygame.image.load(os.path.join("menu", "CharacterUp.png")).convert_alpha()
characterDown = pygame.image.load(os.path.join("menu", "CharacterDown.png")).convert_alpha()

######################### In Game Pause Menu Buttons ###########################

pause_resume = pygame.Rect((384, 128), (256, 128))
pause_main_menu = pygame.Rect((384, 288), (256, 128))
pause_quit = pygame.Rect((384, 448), (256, 128))

menuButtonUp = pygame.image.load(os.path.join("menu", "MenuUp.png")).convert_alpha()
menuButtonDown = pygame.image.load(os.path.join("menu", "MenuDown.png")).convert_alpha()

resumeButtonUp = pygame.image.load(os.path.join("menu", "ResumeUp.png")).convert_alpha()
resumeButtonDown = pygame.image.load(os.path.join("menu", "ResumeDown.png")).convert_alpha()

########################## Character Menu Buttons / Text #################################

spellRect1 = pygame.Rect((832, 384), (64, 64))
spellRect2 = pygame.Rect((832, 448), (64, 64))
spellRect3 = pygame.Rect((832, 512), (64, 64))

plusButtonUp = pygame.image.load(os.path.join("menu", "SmallButtonUp.png")).convert_alpha()
plusButtonDown = pygame.image.load(os.path.join("menu", "SmallButtonDown.png")).convert_alpha()

stats = pygame.image.load(os.path.join("menu", "statsSmall2.png")).convert_alpha()
spellText = pygame.image.load(os.path.join("menu", "Spell.png")).convert_alpha()

hp = pygame.image.load(os.path.join("menu", "HP.png")).convert_alpha()
xp = pygame.image.load(os.path.join("menu", "XP.png")).convert_alpha()

health_bar = pygame.image.load(os.path.join("bars", "emptyHB.png")).convert_alpha()
single_bar = pygame.image.load(os.path.join("bars", "hpBar.png")).convert_alpha()
total_health = 64

################################## Battle Menu ###########################################
spellButtonUp = pygame.image.load(os.path.join("buttons", "SmallButtonUp.png")).convert_alpha()
spellButtonDown = pygame.image.load(os.path.join("buttons", "SmallButtonDown.png")).convert_alpha()
staffButtonUp = pygame.image.load(os.path.join("buttons", "staffButtonUp.png")).convert_alpha()
staffButtonDown = pygame.image.load(os.path.join("buttons", "staffButtonDown.png")).convert_alpha()
flame_button_up = pygame.image.load(os.path.join("buttons", "FlameButtonUp.png")).convert_alpha()
flame_button_down = pygame.image.load(os.path.join("buttons", "FlameButtonDown.png")).convert_alpha()
ice_button_up = pygame.image.load(os.path.join("buttons", "IceButtonUp.png")).convert_alpha()
ice_button_down = pygame.image.load(os.path.join("buttons", "IceButtonDown.png")).convert_alpha()
venom_button_up = pygame.image.load(os.path.join("buttons", "VenomButtonUp.png")).convert_alpha()
venom_button_down = pygame.image.load(os.path.join("buttons", "VenomButtonDown.png")).convert_alpha()

battleSpell1 = pygame.Rect((80, 608), (64, 64))
battleSpell2 = pygame.Rect((176, 608), (64, 64))
battleSpell3 = pygame.Rect((272, 608), (64, 64))
battleSpell4 = pygame.Rect((368, 608), (64, 64))

################################# Character Content ######################################

sprite_list = [os.path.join("imgs", "SamFront.png")]
sprite_north = [os.path.join("imgs", "SamBackDefault.png"), os.path.join("imgs", "SamBackWalk1.png"),
				os.path.join("imgs", "SamBackDefault.png"), os.path.join("imgs", "SamBackWalk2.png")]
sprite_south = [os.path.join("imgs", "SamFrontDefault.png"), os.path.join("imgs", "SamFrontWalk1.png"),
				os.path.join("imgs", "SamFrontDefault.png"), os.path.join("imgs", "SamFrontWalk2.png")]
sprite_east = [os.path.join("imgs", "SamRightDefault.png"), os.path.join("imgs", "SamRightWalk1.png"),
			   os.path.join("imgs", "SamRightDefault.png"), os.path.join("imgs", "SamRightWalk2.png")]
sprite_west = [os.path.join("imgs", "SamLeftDefault.png"), os.path.join("imgs", "SamLeftWalk1.png"),
			   os.path.join("imgs", "SamLeftDefault.png"), os.path.join("imgs", "SamLeftWalk2.png")]

treeSprite = [os.path.join("imgs", "Tree1.png")]

listOfNPCs = []


################################ Battle Background #######################################

battleBackground = pygame.image.load(os.path.join("menu", "battleBackground2.png")).convert_alpha()

################################## Cursor #################################################

cursor = pygame.image.load(os.path.join("cursor", "cursor.png")).convert_alpha()

# if pygame.mouse.get_focused():
# pygame.mouse.set_visible(False)


#### LEVEL CHANGE DEFINITIONS ###
sam = None	

def newSam():
	return character.Player(64, 320, screen, sprite_north, sprite_south, sprite_east, sprite_west)

sam = newSam()
currLvl = None
levels = []

def genLevels():	
	global sam
	global currLvl
	
	lvl0 = levelGenerator.Level_Tutorial(sam, map1, screen)
	lvl1 = levelGenerator.Level_Field(sam, map3, screen)
	lvl2 = levelGenerator.Level_Jungle(sam, map1, screen)
	lvl3 = levelGenerator.Level_Bridge(sam, map2, screen)
	lvl4 = levelGenerator.Level_Town(sam, map1, screen)
	lvl5 = levelGenerator.Level_Maze(sam, map1, screen)
	lvl6 = levelGenerator.Level_Hairy(sam, map1, screen)
	lvl7 = levelGenerator.Level_CityLimits(sam, map1, screen)
	lvl8 = levelGenerator.Level_Lair(sam, map1, screen)
	lvl9 = levelGenerator.Level_Habitat(sam, map1, screen)
	lvl10 = levelGenerator.Level_Turtle(sam, map1, screen)
	lvl11 = levelGenerator.Level_Last(sam, map1, screen)
	lvl12 = levelGenerator.Level_Rjufus(sam, map1, screen)

	return [lvl0, lvl1, lvl2, lvl3, lvl4, lvl5, lvl6, lvl7, lvl8, lvl9, lvl10, lvl11, lvl12]

nullLevel = levelGenerator.Level_Null(sam, map1, screen)

levels = genLevels()
currLvl = levels[0]

keypressed = False
key = None

################################ Auxiliary Functions #######################################

def updateEverything():
	pygame.display.update()

#################### Draw Health ####################
def draw_health_bar(current_health, x, y):
	bar_list = []
	empty_bar_rect = pygame.Rect((x, y), (320, 64))
	screen.blit(health_bar, empty_bar_rect)
	bar_list.append(empty_bar_rect)
	for i in range(current_health):
		single_bar_rect = pygame.Rect(((x + 8) + i * 8, y), (8, 64))
		screen.blit(single_bar, single_bar_rect)
		bar_list.append(single_bar_rect)
	pygame.display.update(bar_list)


################################# State Functions ########################################

# handle_start function
def handle_start(state):

	# setup
	if state == "Start_Setup":
		##################### Fill the Screen ####################
		fillBackground(0, 0, 16, 12)
		fillStartScreen()

	state = "Start"

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if play_button.collidepoint(pygame.mouse.get_pos()):
				pressedPlay()
			if rules_button.collidepoint(pygame.mouse.get_pos()):
				pressedHelp()
			if quit_button.collidepoint(pygame.mouse.get_pos()):
				pressedQuit()
			if credits_button.collidepoint(pygame.mouse.get_pos()):
				pressedCredits()

		if event.type == pygame.MOUSEBUTTONUP:

			unpressedPlay()
			unpressedHelp()
			unpressedQuit()
			unpressedCredits()

			if play_button.collidepoint(pygame.mouse.get_pos()):
				state = "Game_Setup"
			if rules_button.collidepoint(pygame.mouse.get_pos()):
				state = "Rules_Setup"
			if quit_button.collidepoint(pygame.mouse.get_pos()):
				sys.exit()
			if credits_button.collidepoint(pygame.mouse.get_pos()):
				state = "Credits_Setup"

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()

	return state

character_menu = pygame.image.load(os.path.join("menu", "CharacterPage.png")).convert_alpha()

# play state - in game
def handle_play(state):
	global keypressed
	global key
	global currLvl
	global levels
	global total_health
	global spell1_level_array

	if state == "Game_Setup":

		######################## Fill Screen ##########################

		sam.addOtherNPCs(currLvl.NPCList)
		currLvl.map.blitMyMap(screen)

		currLvl.renderLevel()

		# in-game background for buttons
		for x in range(16):
			screen.blit(top, (x * 64, 704))

		screen.blit(pauseUp, pauseRect)
		screen.blit(characterUp, characterRect)

		# update the screen
		pygame.display.update()

	state = "Play"

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:

			# draw the pause menu if the pause button is pressed
			if pauseRect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(pauseDown, pauseRect)
				fillBackground(320, 64, 6, 9)
				screen.blit(resumeButtonUp, pause_resume)
				screen.blit(menuButtonUp, pause_main_menu)
				screen.blit(quitTileUp, pause_quit)
				pygame.display.update()

				x = True
				while x == True:
					for event2 in pygame.event.get():
						if event2.type == pygame.MOUSEBUTTONDOWN:

							if pauseRect.collidepoint(pygame.mouse.get_pos()):
								state = "Game_Setup"
								x = False
							if pause_resume.collidepoint(pygame.mouse.get_pos()):
								screen.blit(resumeButtonDown, pause_resume)
								pygame.display.update()
							if pause_main_menu.collidepoint(pygame.mouse.get_pos()):
								screen.blit(menuButtonDown, pause_main_menu)
								pygame.display.update()
							if pause_quit.collidepoint(pygame.mouse.get_pos()):
								screen.blit(quitTileDown, pause_quit)
								pygame.display.update()

						if event2.type == pygame.MOUSEBUTTONUP:
							screen.blit(resumeButtonUp, pause_resume)
							screen.blit(menuButtonUp, pause_main_menu)
							screen.blit(quitTileUp, pause_quit)
							pygame.display.update()

							if pause_resume.collidepoint(pygame.mouse.get_pos()):
								state = "Game_Setup"
								x = False
							if pause_main_menu.collidepoint(pygame.mouse.get_pos()):
								state = "Start_Setup"
								x = False
							if pause_quit.collidepoint(pygame.mouse.get_pos()):
								sys.exit()

			if characterRect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(characterDown, characterRect)

				screen.blit(character_menu, (64, 64))

				pygame.display.update()

				c = True
				while c:
					for charEvent in pygame.event.get():
						if charEvent.type == pygame.MOUSEBUTTONDOWN:
							if characterRect.collidepoint(pygame.mouse.get_pos()):
								state = "Game_Setup"
								c = False

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_w:
				key = 'w'
				keypressed = True

			if event.key == pygame.K_a:
				key = 'a'
				keypressed = True

			if event.key == pygame.K_s:
				key = 's'
				keypressed = True

			if event.key == pygame.K_d:
				key = 'd'
				keypressed = True

			if event.key == pygame.K_q:
				sys.exit()

			if event.key == pygame.K_p:
				pygame.display.update([None])
				state = "Play"

			if event.key == pygame.K_9:
				state = "Win_Setup"
			if event.key == pygame.K_0:
				state = "Loss_Setup"


		if event.type == pygame.KEYUP:
			sam.stopMoving()

			# map1.blitMyMap(screen)
			pygame.display.update(currLvl.updateNearby())
			keypressed = False

	if keypressed == True:
		if key == 'w':
			state = sam.handleMoveNorth()
		if key == 'a':
			state = sam.handleMoveWest()
		if key == 's':
			state = sam.handleMoveSouth()
		if key == 'd':
			state = sam.handleMoveEast()

		# map1.blitMyMap(screen)
		pygame.display.update(currLvl.updateNearby())

	return state


def handle_rules(state):
	if state == "Rules_Setup":
		####################### Fill Screen #######################
		fillBackground(0, 0, 16, 12)

		screen.blit(rules, rules_rect)

		screen.blit(instructions, (32, 100))

		screen.blit(backButtonUp, back_button)

		pygame.display.update()

	state = "Rules"

	for event in pygame.event.get():

		if event.type == pygame.MOUSEBUTTONDOWN:
			if back_button.collidepoint(pygame.mouse.get_pos()):
				screen.blit(backButtonDown, back_button)
				pygame.display.update()

		if event.type == pygame.MOUSEBUTTONUP:
			screen.blit(backButtonUp, back_button)
			pygame.display.update()

			if back_button.collidepoint(pygame.mouse.get_pos()):
				state = "Start_Setup"

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()

		if event.type == pygame.QUIT:
			sys.exit()

	return state


def handle_credits(state):
	if state == "Credits_Setup":
		################### Fill Screen ######################
		fillBackground(0, 0, 16, 12)

		screen.blit(backButtonUp, creditsBackRect)
		screen.blit(quitTileUp, creditsQuitRect)

		# screen.blit( wizards, wiz_rect )

		screen.blit(credits1, (64, 64))
		# screen.blit(credits2, (64,64))

		pygame.display.update()

	state = "Credits"

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if creditsBackRect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(backButtonDown, creditsBackRect)
				pygame.display.update()
			if creditsQuitRect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(quitTileDown, creditsQuitRect)
				pygame.display.update()

		if event.type == pygame.MOUSEBUTTONUP:
			screen.blit(backButtonUp, creditsBackRect)
			screen.blit(quitTileUp, creditsQuitRect)
			pygame.display.update()

			if creditsBackRect.collidepoint(pygame.mouse.get_pos()):
				state = "Start_Setup"
			if creditsQuitRect.collidepoint(pygame.mouse.get_pos()):
				sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()

		if event.type == pygame.QUIT:
			sys.exit()

	return state


def handle_next(state):
	global currLvl

	global sam

	currLvl = nullLevel
	sam.addOtherNPCs(currLvl.NPCList)
	currLvl.map.blitMyMap(screen)

	currLvl.renderLevel()

	sam.x = state[0]
	sam.y = state[1]
	sam.updateRects()

	currLvl = levels[state[2]]
	pygame.display.update()
	state = "Game_Setup"

	return state


def handle_battle(state):

	badGuy = state

	sam.hp = sam.maxHP
	
	global keypressed
	keypressed = False

	state.sound.play()
	state.handleInteraction()
	screen.blit(battleBackground, (0, 0))
	screen.blit(staffButtonUp, battleSpell1)
	screen.blit(venom_button_up, battleSpell2)
	screen.blit(ice_button_up, battleSpell3)
	screen.blit(flame_button_up, battleSpell4)

	screen.blit(hp, (48, 496))
	screen.blit(hp, (560, 496))

	screen.blit(badGuy.battSp, (608, 128))

	pygame.display.update()

	draw_health_bar(badGuy.hp, 640, 496)
	draw_health_bar(sam.hp, 128, 496)
	while True:
		
		if sam.hp <= 0:
			return "Loss_Setup"
		
		if badGuy.hp <= 0:
			if badGuy.name == "Rjufus":
				return "Win_Setup"
			else:
				badGuy.isDefeated()
				return "Game_Setup"
		for batEvent in pygame.event.get():
			if batEvent.type == pygame.KEYDOWN and batEvent.key == pygame.K_b:
				badGuy.isDefeated()
				return "Game_Setup"
			
			if batEvent.type == pygame.MOUSEBUTTONDOWN:
				if battleSpell1.collidepoint(pygame.mouse.get_pos()):
					rect_list = []
					screen.blit(staffButtonDown, battleSpell1)
					rect_list.append(battleSpell1)
					pygame.display.update(rect_list)
				if battleSpell2.collidepoint(pygame.mouse.get_pos()):
					rect_list = []
					screen.blit(venom_button_down, battleSpell2)
					rect_list.append(battleSpell2)
					pygame.display.update(rect_list)
				if battleSpell3.collidepoint(pygame.mouse.get_pos()):
					rect_list = []
					screen.blit(ice_button_down, battleSpell3)
					rect_list.append(battleSpell3)
					pygame.display.update(rect_list)
				if battleSpell4.collidepoint(pygame.mouse.get_pos()):
					rect_list = []
					screen.blit(flame_button_down, battleSpell4)
					rect_list.append(battleSpell4)
					pygame.display.update(rect_list)
			
			if batEvent.type == pygame.MOUSEBUTTONUP:
				screen.blit(staffButtonUp, battleSpell1)
				screen.blit(venom_button_up, battleSpell2)
				screen.blit(ice_button_up, battleSpell3)
				screen.blit(flame_button_up, battleSpell4)
				rect_list2 = []
				rect_list2.append(battleSpell1)
				rect_list2.append(battleSpell2)
				rect_list2.append(battleSpell3)
				rect_list2.append(battleSpell4)
				pygame.display.update(rect_list2)
				if battleSpell1.collidepoint(pygame.mouse.get_pos()):
					sf.spell_func1(sam, badGuy)
					draw_health_bar(badGuy.hp, 640, 496)
					time.sleep(.5)
					if badGuy.takeTurn(sam) == True:
						return "Game_Setup"
					draw_health_bar(sam.hp, 128, 496)

					print sam.hp, badGuy.hp
				if battleSpell2.collidepoint(pygame.mouse.get_pos()):
					sf.spell_func2(sam, badGuy)
					draw_health_bar(badGuy.hp, 640, 496)
					if badGuy.takeTurn(sam) == True:
						return "Game_Setup"
					draw_health_bar(sam.hp, 128, 496)

				if battleSpell3.collidepoint(pygame.mouse.get_pos()):
					sf.spell_func3(sam, badGuy)
					draw_health_bar(badGuy.hp, 640, 496)
					if badGuy.takeTurn(sam) == True:
						return "Game_Setup"
					draw_health_bar(sam.hp, 128, 496)
					
				if battleSpell4.collidepoint(pygame.mouse.get_pos()):
					sf.spell_func4(sam, badGuy)
					draw_health_bar(badGuy.hp, 640, 496)
					if badGuy.takeTurn(sam) == True:
						return "Game_Setup"
					draw_health_bar(sam.hp, 128, 496)
		time.sleep(.5)
		print sam.hp, badGuy.hp
	return state

win_text = pygame.image.load(os.path.join("end", "WinPage.png")).convert_alpha()
loss_text = pygame.image.load(os.path.join("end", "LostPage.png")).convert_alpha()

end_restart_button_up = pygame.image.load(os.path.join("buttons", "RestartUp.png")).convert_alpha()
end_restart_button_down = pygame.image.load(os.path.join("buttons", "RestartDown.png")).convert_alpha()

end_restart_button_rect = pygame.Rect((64, 608), (256, 128))
end_menu_button_rect = pygame.Rect((384, 608), (256, 128))
end_quit_button_rect = pygame.Rect((704, 608), (256, 128))

def handle_end(state):
	global sam
	global levels
	global currLvl
	
	if state == "Win_Setup":
		fillBackground(0, 0, 16, 12)
		screen.blit(win_text, (0, 0))
		screen.blit(end_restart_button_up, end_restart_button_rect)
		screen.blit(menuButtonUp, end_menu_button_rect)
		screen.blit(quitTileUp, end_quit_button_rect)
		pygame.display.update()

	elif state == "Loss_Setup":
		fillBackground(0, 0, 16, 12)
		screen.blit(loss_text, (0, 0))
		screen.blit(end_restart_button_up, end_restart_button_rect)
		screen.blit(menuButtonUp, end_menu_button_rect)
		screen.blit(quitTileUp, end_quit_button_rect)
		pygame.display.update()
	state = "End"

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
			if event.key == pygame.K_9:
				state = "Game_Setup"
			if event.key == pygame.K_0:
				state = "Game_Setup"

		if event.type == pygame.MOUSEBUTTONDOWN:
			if end_restart_button_rect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(end_restart_button_down, end_restart_button_rect)
				pygame.display.update()
			if end_menu_button_rect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(menuButtonDown, end_menu_button_rect)
				pygame.display.update()
			if end_quit_button_rect.collidepoint(pygame.mouse.get_pos()):
				screen.blit(quitTileDown, end_quit_button_rect)
				pygame.display.update()

		if event.type == pygame.MOUSEBUTTONUP:

			screen.blit(end_restart_button_up, end_restart_button_rect)
			screen.blit(menuButtonUp, end_menu_button_rect)
			screen.blit(quitTileUp, end_quit_button_rect)
			pygame.display.update()

			if end_restart_button_rect.collidepoint(pygame.mouse.get_pos()):
				sam = newSam()
				levels = genLevels()
				currLvl = levels[0]
				state = "Start_Setup"
			if end_menu_button_rect.collidepoint(pygame.mouse.get_pos()):
				state = "Start_Setup"
			if end_quit_button_rect.collidepoint(pygame.mouse.get_pos()):
				sys.exit()


	return state

################################# Main Event Loop ########################################
# enter the main loop
print "Entering main loop"
while 1:

	# print sam.isColliding(tree.collisionRect)

	if state == "Start" or state == "Start_Setup":
		state = handle_start(state)
	elif state == "Play" or state == "Game_Setup":
		state = handle_play(state)
	elif state == "Rules" or state == "Rules_Setup":
		state = handle_rules(state)
	elif state == "Credits" or state == "Credits_Setup":
		state = handle_credits(state)

	elif state == "End" or state == "Win_Setup" or state == "Loss_Setup":
		state = handle_end(state)

	elif type(state) == tuple:
		state = handle_next(state)
	elif isinstance(state, character.Enemy):
		state = handle_battle(state)

	gameClock.tick(60)
# done
print "Terminating"