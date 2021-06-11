import pygame

# стрелки, наследуется от sprite
class Arrow(pygame.sprite.Sprite):
    
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

        # задание коллайдера
        self.rect = self.image.get_rect()
        # задание центра
        self.rect.center = coord
        # скорость, пока так
        self.speed = 5

    # переопредение метода update из sprite
    def update(self):
        # движение по y
        self.rect.y += self.speed

    # проверка пересечения границы экрана
    def CheckBorder(self,borderY):
        return self.rect.bottom > borderY