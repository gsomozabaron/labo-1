import pygame
import colores
from animacion_explosion import Explosion

class CruceroAliado:
    def __init__(self, x, y, ancho, alto):
        self.imagen = pygame.image.load("crucero2.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = pygame.Rect(x, 50, 100, 500)
        self.vida = 200

    def actualizar_crucero(self, pantalla,modo_debug):
        if modo_debug:
            pygame.draw.rect(pantalla, colores.RED2, self.rect,2)
        if self.vida > 0:
            pantalla.blit(self.imagen, (self.rect.x, self.rect.y+50))
            self.barra_vida = pygame.Rect(self.rect.x-25, self.rect.y+55, self.vida/2, 5)#barra de salud
            
    def mostrar_barra_de_vida(self,pantalla):
        if self.vida > 30:
            barra_vida=colores.GREEN
        elif self.vida <= 30 and self.vida > 15:
            barra_vida=colores.YELLOW1
        elif self.vida <= 15:
            barra_vida=colores.RED2        
        pygame.draw.rect(pantalla,barra_vida,self.barra_vida)          
        
    def dibujar_crucero(self, pantalla,modo_debug, lista_explo):
        if self.vida > 0:
            CruceroAliado.actualizar_crucero(self,pantalla,modo_debug)
            CruceroAliado.mostrar_barra_de_vida(self,pantalla)
        else:
            explo = Explosion((self.rect.x+25, self.rect.y+100))
            explo2 = Explosion((self.rect.x+25, self.rect.y+200))
            explo3 = Explosion((self.rect.x+25, self.rect.y+300))
            explo4 = Explosion((self.rect.x+25, self.rect.y+400))
            lista_explo.append(explo)
            lista_explo.append(explo2)
            lista_explo.append(explo3)
            lista_explo.append(explo4)