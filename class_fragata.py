
import pygame
import colores

class FragataAliada:
    def __init__(self, x, y, ancho, alto):
        self.tamanio = [120, 90]
        self.imagen = pygame.image.load("fragata_aliada.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vida = 100
        self.distancia_de_ataque = pygame.Rect((x - 400), (y + 25), (400), (alto/2))
    
    def actualizar(self, pantalla,modo_debug):
        if modo_debug:
            pygame.draw.rect(pantalla,colores.RED1,self.rect,2) 
            pygame.draw.rect(pantalla, colores.YELLOW2, self.distancia_de_ataque,2)
        self.barra_vida = pygame.Rect(self.rect.x,self.rect.y+25,self.vida,5)#barra de salud
        pantalla.blit(self.imagen, self.rect)
                
        
    def mover(self,velocidad):
        if self.rect.x > 1000:
            self.rect.x -= velocidad
            self.distancia_de_ataque.x -= velocidad
            
def crear_lista_fragatas(cantidad):
    lista_fragatas = []
    for i in range(cantidad):
        fragata = FragataAliada(1800, 35 + (i * 82), 130, 100)
        lista_fragatas.append(fragata)
    return lista_fragatas

def actualizar_pantalla(lista_fragatas, pantalla,modo_debug):
    for fragata in lista_fragatas:
        fragata.actualizar(pantalla,modo_debug)
        
        if fragata.vida > 30:
            barra_fragata=colores.GREEN
        elif fragata.vida <= 30 and fragata.vida > 15:
            barra_fragata=colores.YELLOW1
        elif fragata.vida <= 15:
            barra_fragata=colores.RED1        
        pygame.draw.rect(pantalla,barra_fragata,fragata.barra_vida)
