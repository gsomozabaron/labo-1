import pygame
import random
import colores
import sonidos
from class_naves_enemigas import NaveEnemiga

class BombarderoEnemigo(NaveEnemiga):
    def __init__(self, x, y):
        imagen_bombardero = "tie_bomber.png"
        super().__init__(x, y, 80, 80, imagen_bombardero)
        self.salud = 10

    def update(lista_de_bombers,velocidad):
        eliminar_bombardeo = []
        for bomber in lista_de_bombers:
            if bomber.salud > 0:
                bomber.rect.x += velocidad
                bomber.distancia_de_ataque.x += velocidad
                if bomber.rect.x > 1300:
                    bomber.rect.x = -100
                    bomber.distancia_de_ataque.x = -100
            else:
                sonidos.explota.play()
                eliminar_bombardeo.append(bomber)  
                 
        for bomber in eliminar_bombardeo:
            if bomber in lista_de_bombers:
                lista_de_bombers.remove(bomber)
            
             
    def crear_lista_de_bombers(cantidad):
        lista_de_bombers = []
        for i in range(cantidad):
            x_random = random.randrange(-1000, 0, 160)
            y_random = random.randrange(60, 492, 82) #60 en y copado!!
            lista_de_bombers.append(BombarderoEnemigo(x_random, y_random))
        return lista_de_bombers
    
    def mostrar(pantalla,lista_de_bombers, modo_debug):
        for bomber in lista_de_bombers:
            if modo_debug:     
                pygame.draw.rect(pantalla,(colores.YELLOW1),bomber.distancia_de_ataque,2)
                pygame.draw.rect(pantalla,(colores.RED1),bomber.rect,2)
            pantalla.blit(bomber.imagen, bomber.rect)
            
    def dibujar_cazas(lista_de_bombers,velocidad_bombers,modo_debug,pantalla):
        BombarderoEnemigo.update(lista_de_bombers,velocidad_bombers)#lista + velocidad de movim
        BombarderoEnemigo.mostrar(pantalla,lista_de_bombers,modo_debug)