import pygame, time, os

from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP

from Arrow import Arrow
from Circle import Circle
from SoundReader import SoundReader

from random import randint

# основной класс игры
class GameScreen:

    def __init__(self):
        # отслеживание времени
        self.clock = pygame.time.Clock()
        # размер экрана
        self.size = (800,800)
        
        # список всех стрелок
        self.arrows = pygame.sprite.Group()
        # список всех кругов
        self.circles = pygame.sprite.Group()
        
        # кол-во столбцов
        self.countColumn = 4
        # у координата спавна стрелок
        self.posSpawnArrowY = 100
        # у координата спавна кругов
        self.posSpawnCircleY = self.size[1] - 200
        # размер спрайта стрелки
        self.widthArrow = 80
        # размер спрайта круга
        self.widthCircle = 100

        # расстояние между спрайтами по x
        self.distanceBetween = 50
        # время респавна стрелок
        self.spawnArrowTime = 1000

        # получение имя папки с спрайтами
        self.gameFolder = os.path.dirname(__file__)
        self.gameFolder = os.path.join(self.gameFolder,"Image")
        # список имен стрелок
        self.namesArrow = ["DArrow.png","UArrow.png","LArrow.png","RArrow.png"]
        # имя картинки круга
        self.circlName = "Circle.png"

        # список координат колонок по x
        self.listPoint = [[self.widthArrow * i + (i + 1) * self.distanceBetween,0] for i in range(0,self.countColumn)]

        # инициализация pygame
        pygame.init()
        # создание экрана
        self.screen = pygame.display.set_mode(self.size)

        # спавн кругов
        self.SpawnCircle()

        self.reader = SoundReader("Sound\\test.wav",self.spawnArrowTime/1000,4)
        self.sound = pygame.mixer.Sound('Sound\\test.wav')

    # спавн стрелок
    def SpawnArrow(self, listData):
        # случайный индекс колонки
        # randSpawnIndex = randint(0,self.countColumn-1)

        middle = sum(listData)/4

        listValue = [i > middle for i in listData]

        for i in range(0,4):
            if not listValue[i]:
                continue


            randSpawnIndex = i

            # получение позиции спавна
            pos = self.listPoint[randSpawnIndex]
            pos[1] = self.posSpawnArrowY

            # получение имени файла
            filename = os.path.join(self.gameFolder,self.namesArrow[randSpawnIndex])
            
            # создание стрелки
            arrow = Arrow(pos, filename, self.widthArrow)

            # добавление стрелки в общий список
            self.arrows.add(arrow)
            # добавление стрелки в список круга
            self.circles.sprites()[randSpawnIndex].groupArrow.add(arrow)

    # спавн кругов
    def SpawnCircle(self):
        for pos in self.listPoint:

            # получение позиции спавна
            p = pos
            p[1] = self.posSpawnCircleY

            # получение имени файла
            filename = os.path.join(self.gameFolder,self.circlName)

            # добавление круга в общий список
            self.circles.add(Circle(p,filename,self.widthCircle))

    # проверка выхода стрелки из экрана
    def CheckOutArrow(self):
        for arrow in self.arrows:
            if arrow.CheckBorder(self.size[1]):
                # уничтожение стрелки и удаление из всех списков
                arrow.kill()
    
    # Провека попадания стрелки в круг, index - номер круга
    def CheckArrowInsideCircle(self, index):
        circle = self.circles.sprites()[index]
        circle.CheckArowInsideCircle()

    # игра
    def LoadGame(self):
        print("start game")

        lastSpawn = pygame.time.get_ticks()
        index = 0
        gameOver = False

        self.sound.play()

        while (not gameOver or len(self.arrows) != 0):
            # события
            for event in pygame.event.get():
                # закрытие игры
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                # проверка кнопок для стрелок
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.CheckArrowInsideCircle(0)
                    elif event.key == K_UP:
                        self.CheckArrowInsideCircle(1)
                    elif event.key == K_LEFT:
                        self.CheckArrowInsideCircle(2)
                    elif event.key == K_RIGHT:
                        self.CheckArrowInsideCircle(3)

            # проверка выхода стрелок 
            self.CheckOutArrow()

            # спавн раз в self.spawnArrowTime
            if pygame.time.get_ticks() - lastSpawn > self.spawnArrowTime:
                lastSpawn = pygame.time.get_ticks()

                if len(self.reader.Calculation()) > index:
                    self.SpawnArrow(self.reader.Calculation()[index])
                    index+=1
                else:
                    gameOver = True

            # вызовы update у всех спрайтов
            self.arrows.update()
            self.circles.update()

            # заливка экрана
            self.screen.fill((50,50,50))
            
            # рисование спрайтов
            self.arrows.draw(self.screen)
            self.circles.draw(self.screen)

            # обновление экрана
            pygame.display.update()

            # фпс
            self.clock.tick(30)


# создание игры, загрузка
gs = GameScreen()
gs.LoadGame()

# выход
pygame.quit()