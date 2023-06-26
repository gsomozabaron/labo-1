import pygame
import colores

def mostrar_intro(ANCHO_VENTANA, ALTO_VENTANA, pantalla, JUGANDO):
    pygame.font.init()
    fondo_menu = pygame.image.load("fondo5.jpg")
    fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))
    
    plantilla = 0
    
    fuente = pygame.font.SysFont("starjedi", 30)
    fuente2 = pygame.font.SysFont("starjedi", 20)
    
    imagen = pygame.image.load("personajes//pug_pilot.png")
    imagen =pygame.transform.scale(imagen,(400,300))
    imagen_rect = imagen.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 - 100))
    
    
    texto = fuente.render("comandante, recibimos una trasmicion de un crucero aliado:", True, colores.RED2)
    texto_rect = texto.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 100))
    
    texto2 = fuente.render("nuestros motores fallan, estamos atrapados en sector enemigo", True, colores.RED2)
    texto2_rect = texto2.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 150))
    
    texto3 = fuente2.render("barra espaciadora para continuar", True, colores.WHITE)
    texto3_rect = texto3.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 200))
    
    flag_correr = True
    while flag_correr:
        pantalla.blit(fondo_menu, (0, 0))
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: 
                JUGANDO = "salir"
                flag_correr = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                plantilla += 1
                if plantilla == 1:
                    
                    imagen = pygame.image.load("personajes//gato_leia.png")
                    imagen =pygame.transform.scale(imagen,(300,300))
                    imagen_rect = imagen.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 - 100))
                    
                    texto = fuente.render("ayudame obi can perroni", True, colores.RED2)
                    texto_rect = texto.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 100))
                    
                    texto2 = fuente.render("eres nuestra unica esperanza!!", True, colores.RED2)
                    texto2_rect = texto.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 150))
                    
                    texto3 = fuente2.render("barra espaciadora para continuar", True, colores.WHITE)
                    texto3_rect = texto3.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 200))
                
                elif plantilla == 2:
                    
                    imagen = pygame.image.load("personajes//perro_pilot.png")
                    imagen =pygame.transform.scale(imagen,(300,300))
                    imagen_rect = imagen.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 - 100))
                    
                    texto = fuente.render("consigue tiempo para reparar el crucero", True, colores.RED2)
                    texto_rect = texto.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 100))
                    
                    texto2 = fuente.render("naves aliadas estan en camino para asistirte", True, colores.RED2)
                    texto2_rect = texto2.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 150))

                    texto3 = fuente2.render("barra espaciadora para continuar", True, colores.WHITE)
                    texto3_rect = texto3.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 200))
                    
                elif plantilla == 3:
                    
                    imagen = pygame.image.load("personajes//perro_bacca.png")
                    imagen =pygame.transform.scale(imagen,(330,300))
                    imagen_rect = imagen.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 - 100))
    
                    texto = fuente.render("para moverte usa las teclas WASD o las flechas", True, colores.RED2)
                    texto_rect = texto.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2+ 100))
                    
                    texto2 = fuente.render("dispara con el mouse", True, colores.RED2)
                    texto2_rect = texto2.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 150))

                    texto3 = fuente2.render("barra espaciadora para continuar", True, colores.WHITE)
                    texto3_rect = texto3.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA // 2 + 200))
                
                elif plantilla == 4:
                    JUGANDO = "jugando"
                    flag_correr = False
                    
        pantalla.blit(imagen, imagen_rect)            
        pantalla.blit(texto, texto_rect)
        pantalla.blit(texto2, texto2_rect)
        pantalla.blit(texto3, texto3_rect)
        
        pygame.display.flip()

    return JUGANDO
