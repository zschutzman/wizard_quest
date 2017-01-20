# Zach Schutzman
# January 2015
# Wizard Quest Map Class
# PhatPenguin Games




import pygame
import sys


class Map:
    def __init__(self, listOfTextures, mapLayout):
        self.mapList = [[None for i in xrange(11)] for i in xrange(16)]
        self.imageList = []
        for img in listOfTextures:
            self.imageList.append(pygame.image.load(img).convert_alpha())
        for i in range(16):
            for j in range(11):
                self.mapList[i][j] = MapTile(i, j, self.imageList[mapLayout[i][j]])

    def blitMyMap(self, screen):
        for i in range(16):
            for j in range(11):
                self.mapList[i][j].drawIntoGame(screen)


class MapTile:
    def __init__(self, x, y, img):
        self.x = 64 * x
        self.y = 64 * y
        self.height = self.width = 64
        self.img = img

        self.tileRect = pygame.Rect((self.x, self.y), (self.img.get_size()))

    def drawIntoGame(self, screen):
        screen.blit(self.img, self.tileRect)
