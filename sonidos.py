import pygame
 
pygame.mixer.init()

####-----------disparos heroe-----------------------------------------------####
disparo_heroe = pygame.mixer.Sound("blast .mp3")
disparo_heroe.set_volume(0.8)  # Establece el volumen al 50%

####------------explosiones-------------------------------------------------####
explota = pygame.mixer.Sound("explode.mp3")
explota.set_volume(0.8)  # Establece el volumen al 50%

####-----------disparos caza enemigo----------------------------------------####
disparo_caza = pygame.mixer.Sound("disparo_caza.mp3")
disparo_caza.set_volume(0.1)  # Establece el volumen al 50%

####-----------sonido caza enemigo----------------------------------------####
sonido_vuelo_caza = pygame.mixer.Sound("vuelosonido.mp3")
sonido_vuelo_caza.set_volume(0.8)  # Establece el volumen al 50%
