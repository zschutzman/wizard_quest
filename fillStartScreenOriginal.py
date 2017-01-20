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

# fillStartScreen background
def fillStartScreen():
	# Do corners
	screen.blit( topLeft, (0, 0) )
	screen.blit( topRight, (960, 0) )	
	screen.blit( bottomLeft, (0, 704) )	
	screen.blit( bottomRight, (960, 704) )
	
	pygame.draw.rect(screen, (170, 170, 170), credits_button)
	
	# Fill Middle and edges
	for i in range(16):
		for j in range(12):
			
			# Middle
			if i != 0 and j != 0:
				if i != 15 and j != 11:
					screen.blit(centerTiles[random.randint(0,3)], (64* i, 64 * j))
			
			# Left Edge
			if i == 0 and j != 0 and j != 11:
				screen.blit(left, (0, j*64))
			# Right Edge
			if i == 15 and j != 0 and j != 11:
				screen.blit(right, (960, j*64))
			# Top Edge
			if j == 0 and i != 0 and i != 15:
				screen.blit(top, (64 * i, 0))
			# Bottom Edge
			if j == 11  and i != 0 and i != 15:
				screen.blit(bottom, (64 * i, 704))