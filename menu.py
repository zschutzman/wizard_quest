from pygameSetup import *

# load corners
topLeft = pygame.image.load(os.path.join("menu", "MenuCornerTopLeft.png")).convert_alpha()
topRight = pygame.image.load(os.path.join("menu", "MenuCornerTopRight.png")).convert_alpha()
bottomLeft = pygame.image.load(os.path.join("menu", "MenuCornerBottomLeft.png")).convert_alpha()
bottomRight = pygame.image.load(os.path.join("menu", "MenuCornerBottomRight.png")).convert_alpha()

# load edge tiles
top = pygame.image.load(os.path.join("menu", "MenuSideUp.png")).convert_alpha()
left = pygame.image.load(os.path.join("menu", "MenuSideLeft.png")).convert_alpha()
right = pygame.image.load(os.path.join("menu", "MenuSideRight.png")).convert_alpha()
bottom = pygame.image.load(os.path.join("menu", "MenuSideBottom.png")).convert_alpha()

centerTiles = []
# load center tiles
centerTiles.append(pygame.image.load(os.path.join("menu", "MenuCenter1.png")).convert_alpha())
centerTiles.append(pygame.image.load(os.path.join("menu", "MenuCenter2.png")).convert_alpha())
centerTiles.append(pygame.image.load(os.path.join("menu", "MenuCenter3.png")).convert_alpha())
centerTiles.append(pygame.image.load(os.path.join("menu", "MenuCenter4.png")).convert_alpha())


def fillBackground(x, y, blocksAcross, blocksDown):
    for i in range(blocksAcross):
        for j in range(blocksDown):

            # fill top left block
            if i == 0 and j == 0:
                screen.blit(topLeft, (x, y))

            # fill top blocs
            if j == 0 and i != 0 and i != (blocksAcross - 1):
                screen.blit(top, (x + (i * 64), y))

            # fill top right block
            if i == blocksAcross - 1 and j == 0:
                screen.blit(topRight, (x + (i * 64), y))

            # fill left	blocks
            if i == 0 and j != 0 and j != (blocksDown - 1):
                screen.blit(left, (x, y + (j * 64)))

            # fill bottom left block
            if i == 0 and j == (blocksDown - 1):
                screen.blit(bottomLeft, (x, y + (j * 64)))

            # fill bottom blocks
            if j == (blocksDown - 1) and i != 0 and i != (blocksAcross - 1):
                screen.blit(bottom, (x + (i * 64), y + (j * 64) ))

            # fill bottom right blocks
            if i == (blocksAcross - 1) and j == (blocksDown - 1):
                screen.blit(bottomRight, (x + (i * 64), y + (j * 64)))

            # fill right blocks
            if i == (blocksAcross - 1) and j != 0 and j != (blocksDown - 1):
                screen.blit(right, (x + (i * 64), y + (j * 64)))

            # fill middle blocks (randomly)
            if i != 0 and j != 0:
                if i != (blocksAcross - 1) and j != (blocksDown - 1):
                    screen.blit(centerTiles[(i * j) % 4], (x + (i * 64), y + (j * 64)))