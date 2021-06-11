import pygame

class Circle(pygame.sprite.Sprite):
    
    def __init__(self, coord, spriteFullName, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(spriteFullName)
        self.image = pygame.transform.scale(self.image, (size,size))
        self.image.set_colorkey((0,0,0))
        self.groupArrow = pygame.sprite.Group()

        self.rect = self.image.get_rect()
        self.rect.center = coord

    def CheckArowInsideCircle(self):
        for arrow in self.groupArrow.sprites():
            if self.rect.collidepoint(arrow.rect.center):
                arrow.kill();