# Team Wizard
# January 2015
#
# Wizard Quest Start Screen Content and Drawing functions
#

from pygameSetup import *

play_button = pygame.Rect((384, 224), (256, 128))
rules_button = pygame.Rect((384, 384), (256, 128))
quit_button = pygame.Rect((384, 544), (256, 128))
credits_button = pygame.Rect((32, 685), (256, 64))

# create a font
title_font = pygame.font.Font("font/wiz.ttf", 100, bold=True)
# comicsansms
copyright_font = pygame.font.Font("font/wiz.ttf", 40, bold=True)

# render a surface with some text
# title = title_font.render("Wizard Quest", True, (0, 0, 0))
title = pygame.image.load(os.path.join("menu", "Title.png")).convert_alpha()

# align the title at the top center of the screen
title_rect = title.get_rect()
title_rect.center = ( screen.get_rect().centerx, 100 )

copyright = copyright_font.render("Copyright 2015", True, (0, 0, 0))

############################### Load Menu Tiles ##########################################

# Load menu buttons
playTileUp = pygame.image.load(os.path.join("menu", "PlayUp.png")).convert_alpha()
playTileDown = pygame.image.load(os.path.join("menu", "PlayDown.png")).convert_alpha()

helpTileUp = pygame.image.load(os.path.join("menu", "HelpUp.png")).convert_alpha()
helpTileDown = pygame.image.load(os.path.join("menu", "HelpDown.png")).convert_alpha()

quitTileUp = pygame.image.load(os.path.join("menu", "QuitUp.png")).convert_alpha()
quitTileDown = pygame.image.load(os.path.join("menu", "QuitDown.png")).convert_alpha()

creditsTileUp = pygame.image.load(os.path.join("menu", "CreditsUp.png")).convert_alpha()
creditsTileDown = pygame.image.load(os.path.join("menu", "CreditsDown.png")).convert_alpha()

# cursor = pygame.image.load(os.path.join("cursor", "cursor.png")).convert_alpha()

############################### Fill Screen ##############################################

def fillStartScreen():
    # blit the title surface onto the screen
    screen.blit(title, title_rect)

    # blit the copyright surface onto the screen
    screen.blit(copyright, (770, 700))

    # draw the buttons on the screen
    screen.blit(playTileUp, play_button)
    screen.blit(helpTileUp, rules_button)
    screen.blit(quitTileUp, quit_button)
    screen.blit(creditsTileUp, credits_button)

    # update the screen
    pygame.display.update()


# mouse down functions
def pressedPlay():
    screen.blit(playTileDown, play_button)
    pygame.display.update()


def pressedHelp():
    screen.blit(helpTileDown, rules_button)
    pygame.display.update()


def pressedQuit():
    screen.blit(quitTileDown, quit_button)
    pygame.display.update()


def pressedCredits():
    screen.blit(creditsTileDown, credits_button)
    pygame.display.update()


# mouse up functions	
def unpressedPlay():
    screen.blit(playTileUp, play_button)
    pygame.display.update()


def unpressedHelp():
    screen.blit(helpTileUp, rules_button)
    pygame.display.update()


def unpressedQuit():
    screen.blit(quitTileUp, quit_button)
    pygame.display.update()


def unpressedCredits():
    screen.blit(creditsTileUp, credits_button)
    pygame.display.update()