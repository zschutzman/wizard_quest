from pygameSetup import *


def spell_func1(player, enemy):
	enemy.takeDamage(2)


def spell_func2(player, enemy):
	enemy.takeDmgOverTime(1)
	player.takeDamage(0)


def spell_func3(player, enemy):
	enemy.freeze()
	player.takeDamage(0)


def spell_func4(player, enemy):
	enemy.takeDamage(4)
	player.takeDamage(2)


spell_level_unfilled = pygame.image.load(os.path.join("menu", "SpellUnfilled.png")).convert_alpha()
spell_level_filled = pygame.image.load(os.path.join("menu", "SpellFilled.png")).convert_alpha()

spell1_level_array = [0, 0, 0, 0, 0, 0]
spell2_level_array = [0, 0, 0, 0, 0, 0]
spell3_level_array = [0, 0, 0, 0, 0, 0]

def upgrade_spell1():
	global spell1_level_array
	
	if spell1_level_array[len(spell1_level_array) - 1] == 1:
		spell1_level_array = [0, 0, 0, 0, 0, 0]

	for i in range(len(spell1_level_array)):
		if spell1_level_array[i] == 0:
			spell1_level_array[i] = 1
			break

	for x in range(len(spell1_level_array)):
		if spell1_level_array[x] == 0:
			screen.blit(spell_level_unfilled, (640 + x * 30, 405))
		if spell1_level_array[x] == 1:
			screen.blit(spell_level_filled, (640 + x * 30, 405))

	pygame.display.update()


def upgrade_spell2():
	global spell2_level_array
	
	if spell2_level_array[len(spell2_level_array) - 1] == 1:
		spell2_level_array = [0, 0, 0, 0, 0, 0]

	for i in range(len(spell2_level_array)):
		if spell2_level_array[i] == 0:
			spell2_level_array[i] = 1
			break

	for x in range(len(spell2_level_array)):
		if spell2_level_array[x] == 0:
			screen.blit(spell_level_unfilled, (640 + x * 30, 405))
		else:
			screen.blit(spell_level_filled, (640 + x * 30, 405))

	pygame.display.update()


def upgrade_spell3():
	global spell3_level_array
	
	if spell3_level_array[len(spell3_level_array) - 1] == 1:
		spell3_level_array = [0, 0, 0, 0, 0, 0]

	for i in range(len(spell3_level_array)):
		if spell3_level_array[i] == 0:
			spell3_level_array[i] = 1
			break

	for x in range(len(spell3_level_array)):
		if spell3_level_array[x] == 0:
			screen.blit(spell_level_unfilled, (640 + x * 30, 405))
		else:
			screen.blit(spell_level_filled, (640 + x * 30, 405))

	pygame.display.update()


def upgrade_spell4():
	pass