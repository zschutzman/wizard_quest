

import character
import os
import pygame
import random




''' Takes in a list of coordinate pairs and creates trees selected randomly from the tree textures at
    those locations.  Coordinates are passed in as game cells on the 16x11 grid of 64x64px squares
	and are translated into pixel locations.  For example, (4,3) will put a tree at (256,192).
	display is a screen object passed through to the tree's constructor.
'''
def treePlacer(coordsList, display):
	textureList = [os.path.join("imgs","Tree1.png"), os.path.join("imgs","Tree2.png"), os.path.join("imgs","Tree3.png"), os.path.join("imgs","Tree4.png"), os.path.join("imgs","Tree5.png"), os.path.join("imgs","Tree6.png"), os.path.join("imgs","Tree7.png"), os.path.join("imgs","Tree8.png"), os.path.join("imgs","Tree9.png"), os.path.join("imgs","Tree10.png")]
	
	treesList = []
	
	for i in range(len(coordsList)):
		xloc = 64 * coordsList[i][0] 
		yloc = 64 * (coordsList[i][1] - 1)
		
		chosenSprite = textureList[random.randint(0,9)]
		treesList.append(character.Obstacle(xloc, yloc, [chosenSprite], display))
		
	return treesList