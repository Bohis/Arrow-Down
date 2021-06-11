import pygame

class Arrow(pygame.sprite.Sprite):

    def __init__(self, coord, spriteFullName, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(spriteFullName)
        self.image = pygame.transform.scale(self.image, (size,size))
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.center = coord
        self.speed = 5

    def update(self):
        self.rect.y += self.speed

    def CheckBorder(self,borderY):
        return self.rect.bottom > borderY