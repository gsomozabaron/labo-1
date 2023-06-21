import pygame
import random
import sonidos
import colores
from class_naves_enemigas import NaveEnemiga


class CazaEnemigo(NaveEnemiga):
    def __init__(self, x, y):
        imagen_caza = "tie.png"
        super().__init__(x, y, 50, 50, imagen_caza)
        self.salud = 5
    
    def update(lista_de_cazas, velocidad):
        eliminar_caza = []
        for caza in lista_de_cazas:
            if caza.salud > 0:
                caza.rect.x += float(velocidad)
                caza.distancia_de_ataque.x += float(velocidad)
                if caza.rect.x > 1300:
                    caza.rect.x = -100
                    caza.distancia_de_ataque.x = -100
            else:
                sonidos.explota.play()
                eliminar_caza.append(caza) 
                
        for caza in eliminar_caza:
            if caza in lista_de_cazas:
                lista_de_cazas.remove(caza)

    def mostrar(pantalla,lista_de_cazas,modo_debug):
        for caza in lista_de_cazas:     
            pantalla.blit(caza.imagen, caza.rect)
            if modo_debug:
                pygame.draw.rect(pantalla,(colores.YELLOW1),caza.distancia_de_ataque,2)
                pygame.draw.rect(pantalla,(colores.RED1),caza.rect,2)

    def crear_lista_de_cazas(cantidad):
        lista_de_cazas = []
        for i in range(cantidad):
            x_random = random.randrange(-1000, 0, 160)
            y_random = random.randrange(60, 492, 82) #60 en y copado!!
            lista_de_cazas.append(CazaEnemigo(x_random, y_random))
        return lista_de_cazas

    def dibujar_cazas(lista_de_cazas,velocidad_cazas,modo_debug,pantalla):
        CazaEnemigo.update(lista_de_cazas,velocidad_cazas)#lista + velocidad de movim
        CazaEnemigo.mostrar(pantalla,lista_de_cazas,modo_debug)