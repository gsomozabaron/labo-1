import pygame

ANCHO_VENTANA = 1300
ALTO_VENTANA = 600

###---fondo---###
imagen_fondo = pygame.image.load("fondo2.jpg")#del 2 al 6 estan copados
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA, ALTO_VENTANA))

#DS Death Star 
tamanio_ds_base = 380
tamanio_ds = [tamanio_ds_base+130, tamanio_ds_base]
imagen_ds = pygame.image.load("ds2.png")
imagen_ds = pygame.transform.scale(imagen_ds, tamanio_ds)


###---imagen menu---###
imagen_menu = pygame.image.load("fondo3.jpg")#del 2 al 6 estan copados
imagen_menu = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA, ALTO_VENTANA))
