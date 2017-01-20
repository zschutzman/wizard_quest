from pygameSetup import *


def spell_func1():
    pass


def spell_func2():
    pass


def spell_func3():
    pass


def spell_func4():
    pass


spell_level_unfilled = pygame.image.load(os.path.join("menu", "SpellUnfilled.png")).convert_alpha()
spell_level_filled = pygame.image.load(os.path.join("menu", "SpellFilled.png")).convert_alpha()

spell1_level_array = [0, 0, 0, 0, 0, 0]

def upgrade_spell1():
    global spell1_level_array
    print spell1_level_array

    if spell1_level_array[len(spell1_level_array) - 1] == 1:
        spell1_level_array = [0, 0, 0, 0, 0, 0]

    for i in range(len(spell1_level_array)):
        if spell1_level_array[i] == 0:
            spell1_level_array[i] = 1
            break

    for x in range(len(spell1_level_array)):
        if spell1_level_array[x] == 0:
            screen.blit(spell_level_unfilled, (640 + x * 30, 405))
        else:
            screen.blit(spell_level_filled, (640 + x * 30, 405))

    pygame.display.update()


def upgrade_spell2():
    pass


def upgrade_spell3():
    pass


def upgrade_spell4():
    pass