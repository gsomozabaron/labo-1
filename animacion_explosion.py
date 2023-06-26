import pygame

lista_explosion = []

for i in range(0, 32):
    explosion = pygame.image.load(f"explosion//expl_09_000{i}.png")
    lista_explosion.append(explosion)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.image = lista_explosion[0]
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = posicion
        self.time = pygame.time.get_ticks()
        self.velocidad_explosion = 40
        self.frames = 0
        

    def update(self):
        tiempo = pygame.time.get_ticks()
        if tiempo - self.time > self.velocidad_explosion:
            self.time = tiempo
            self.frames = (self.frames + 1) % len(lista_explosion)
            if self.frames == 0:
                self.kill()
                
            else:
                posicion = self.rect.center
                self.image = lista_explosion[self.frames]
                self.rect = self.image.get_rect()
                self.rect.center = posicion
    
    def mostrar(self, pantalla):
        pantalla.blit(self.image, self.rect)
        
explosiones_a_eliminar = []
def mostrar_explos(lista_explo, pantalla):
    for explo in lista_explo:
        explo.update()
        explo.mostrar(pantalla)
        if explo.frames == 31:  # Si la explosión ha terminado de mostrarse
            explosiones_a_eliminar.append(explo)
    for explo in explosiones_a_eliminar:
        if explo in lista_explo:
            lista_explo.remove(explo)
