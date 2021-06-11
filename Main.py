import pygame, time, os

from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP
from Arrow import Arrow
from Circle import Circle
from random import randint


class GameScreen:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.size = (800,800)
        
        self.arrows = pygame.sprite.Group()
        self.circles = pygame.sprite.Group()
        
        self.countColumn = 4
        self.posSpawnArrowY = 100
        self.posSpawnCircleY = self.size[1] - 200
        self.widthArrow = 100
        self.distanceBetween = 50
        self.spawnArrowTime = 500

        self.gameFolder = os.path.dirname(__file__)
        self.gameFolder = os.path.join(self.gameFolder,"Image")
        self.namesArrow = ["DArrow.png","UArrow.png","LArrow.png","RArrow.png"]
        self.circlName = "Circle.png"

        self.listPoint = [[self.widthArrow * i + (i + 1) * self.distanceBetween,0] for i in range(0,self.countColumn)]

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.SpawnCircle()

    def SpawnArrow(self):
        randSpawnIndex = randint(0,self.countColumn-1)

        pos = self.listPoint[randSpawnIndex]
        pos[1] = self.posSpawnArrowY

        filename = os.path.join(self.gameFolder,self.namesArrow[randSpawnIndex])
        
        arrow = Arrow(pos, filename, self.widthArrow)

        self.arrows.add(arrow)
        self.circles.sprites()[randSpawnIndex].groupArrow.add(arrow)

    def SpawnCircle(self):
        for pos in self.listPoint:
            p = pos
            p[1] = self.posSpawnCircleY

            filename = os.path.join(self.gameFolder,self.circlName)

            self.circles.add(Circle(p,filename,self.widthArrow))

    def CheckOutArrow(self):
        for arrow in self.arrows:
            if arrow.CheckBorder(self.size[1]):
                arrow.kill()
                
    def CheckArrowInsideCircle(self, index):
        circle = self.circles.sprites()[index]
        circle.CheckArowInsideCircle()

    def LoadGame(self):
        print("start game")

        lastSpawn = pygame.time.get_ticks()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.CheckArrowInsideCircle(0)
                    elif event.key == K_UP:
                        self.CheckArrowInsideCircle(1)
                    elif event.key == K_LEFT:
                        self.CheckArrowInsideCircle(2)
                    elif event.key == K_RIGHT:
                        self.CheckArrowInsideCircle(3)


            self.CheckOutArrow()

            if pygame.time.get_ticks() - lastSpawn > self.spawnArrowTime:
                lastSpawn = pygame.time.get_ticks()
                self.SpawnArrow()

            self.arrows.update()
            self.circles.update()

            self.screen.fill((50,50,50))
            self.arrows.draw(self.screen)
            self.circles.draw(self.screen)

            pygame.display.update()

            self.clock.tick(60)


gs = GameScreen()
gs.LoadGame()
pygame.quit()