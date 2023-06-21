import pygame


class NaveEnemiga:
    def __init__(self, x, y, ancho, alto, imagen):
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = pygame.Rect(x, y, ancho , alto)
        self.rect.x = x
        self.rect.y = y
        self.distancia_de_ataque = pygame.Rect(x, y, ancho +300, alto)
        self.vivo = True
        