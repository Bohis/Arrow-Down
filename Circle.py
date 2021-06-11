import pygame

# круги, цель для стрелок, наследуется от sprite
class Circle(pygame.sprite.Sprite):
    # список с координатами, полное имя файла с спрайтом, размер картинки
    def __init__(self, coord, spriteFullName, size):
        # инициализация спрайта
        pygame.sprite.Sprite.__init__(self)

        # загрузка картинки
        self.image = pygame.image.load(spriteFullName)
        # масштабирование
        self.image = pygame.transform.scale(self.image, (size,size))
        # добавили прозрачность
        self.image.set_colorkey((0,0,0))
        # создание списка для контроля стрелочек в столбце
        self.groupArrow = pygame.sprite.Group()

        # задание коллайдера
        self.rect = self.image.get_rect()
        # задание центра
        self.rect.center = coord

    # проверка на попадание в круг стрелочки и ее удаление
    def CheckArowInsideCircle(self):
        for arrow in self.groupArrow.sprites():
            # проверка пересечения коллайдеров
            if self.rect.collidepoint(arrow.rect.center):
                arrow.kill();