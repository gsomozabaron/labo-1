import pygame
import colores
import menu_hiscore

def mostrar_menu(ANCHO_VENTANA, ALTO_VENTANA, pantalla,JUGANDO):    
    #JUGANDO = 3
    
    fondo_menu = pygame.image.load("crucero_destruido.jpg")  # lee la imagen
    fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))  # escala la imagen a la medida "tamaño"

    rect_boton1 = pygame.Rect(700, 200, 25, 25)
    rect_boton2 = pygame.Rect(700, 300, 25, 25)
    rect_boton3 = pygame.Rect(700, 400, 25, 25)
    rect_selec = pygame.Rect(0, 0, 5, 5)
    fuente = pygame.font.SysFont("starjedi", 50)
    fuente2 = pygame.font.SysFont("starjedi", 25)
    
    pygame.mixer.music.load("audio_violin.mp3")
    pygame.mixer.music.set_volume(0.8)   
    pygame.mixer.music.play(-1)  # -1 indica que la música se reproducirá en bucle

    flag_correr = True
    while flag_correr:
        pantalla.fill(colores.WHITE)
        pantalla.blit(fondo_menu, (0, 0))
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                rect_selec.topleft = evento.pos
                if rect_selec.colliderect(rect_boton1):
                    print("Boton 1")
                    JUGANDO = "menu"
                    flag_correr = False
                elif rect_selec.colliderect(rect_boton2):
                    print("Boton 2")
                    menu_hiscore.mostrar_menu(ANCHO_VENTANA, ALTO_VENTANA, pantalla)
                    flag_correr = False
                elif rect_selec.colliderect(rect_boton3):
                    print("Boton 3")
                    JUGANDO = "salir"
                    flag_correr = False

        texto_bienvenida = fuente.render("la flota ha sido destruida", True, colores.WHITE)
        texto_rect = texto_bienvenida.get_rect(center=(ANCHO_VENTANA // 2, 100))
        pantalla.blit(texto_bienvenida, texto_rect)

        sel_juego = fuente2.render("menu principal", True, colores.RED1)
        sel_juego_rect = pygame.Rect(750, 190, 200, 50)
        pantalla.blit(sel_juego, sel_juego_rect)
        
        sel_juego2 = fuente2.render("Hi Scores", True, colores.RED2)
        sel_juego_rect2 = pygame.Rect(750, 290, 200, 50)
        pantalla.blit(sel_juego2, sel_juego_rect2)
        
        sel_juego3 = fuente2.render("Salir", True, colores.RED3)
        sel_juego_rect3 = pygame.Rect(750, 390, 200, 50)
        pantalla.blit(sel_juego3, sel_juego_rect3)

        pygame.draw.rect(pantalla, colores.SILVER, rect_boton1)
        pygame.draw.rect(pantalla, colores.SILVER, rect_boton2)
        pygame.draw.rect(pantalla, colores.SILVER, rect_boton3)
        pygame.display.flip()
    return JUGANDO
