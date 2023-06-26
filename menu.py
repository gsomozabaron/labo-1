import pygame
import colores

def mostrar_menu(ANCHO_VENTANA, ALTO_VENTANA, pantalla,JUGANDO):

    nombre_jugador = ""

    fondo_menu = pygame.image.load("fondo5.jpg")  # lee la imagen
    fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))  # escala la imagen a la medida "tamaño"

    rect_boton1 = pygame.Rect(700, 200, 25, 25)#boton 1 ir al juego
    rect_boton2 = pygame.Rect(700, 300, 25, 25)#boton 2 menu hiscore
    rect_boton3 = pygame.Rect(700, 400, 25, 25)#boton 3 salir del juego
    rect_selec = pygame.Rect(0, 0, 5, 5)
    fuente = pygame.font.SysFont("starjedi", 50)
    fuente2 = pygame.font.SysFont("starjedi", 25)

    flag_correr = True
    while flag_correr:
        pantalla.blit(fondo_menu, (0, 0))
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: 
                JUGANDO = "salir"
                flag_correr = False
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    # Borrar un carácter cuando se presiona la tecla Retroceso
                    nombre_jugador = nombre_jugador[:-1]
                else:
                    # Agregar el carácter ingresado al nombre del usuario
                    if len(nombre_jugador) < 10:
                        nombre_jugador += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                rect_selec.topleft = evento.pos
                if rect_selec.colliderect(rect_boton1):
                    #print("Boton 1")
                    if nombre_jugador != "": #si el jugador ingresa al menos un caracter puede jugar
                        pygame.mixer.music.load("8bit.mp3")
                        pygame.mixer.music.set_volume(0.2)   
                        pygame.mixer.music.play(-1)  # -1 música en bucle
                        JUGANDO = "intro"
                        flag_correr = False        
                    #flag_correr = False
                
                elif rect_selec.colliderect(rect_boton2):
                    #print("Boton 2")
                    pygame.mixer.music.load("sw_electro.mp3")
                    pygame.mixer.music.set_volume(0.3)   
                    pygame.mixer.music.play(-1)  # -1 música en bucle
                    JUGANDO = "menu_hiscore"
                    flag_correr = False
                
                elif rect_selec.colliderect(rect_boton3):
                    #print("Boton 3")
                    JUGANDO = "salir"
                    flag_correr = False

        texto_bienvenida = fuente.render("Bienvenido a rebel pilot 2", True, colores.WHITE)
        texto_rect = texto_bienvenida.get_rect(center=(ANCHO_VENTANA // 2, 100))
        pantalla.blit(texto_bienvenida, texto_rect)

        sel_juego = fuente2.render("A jugar", True, colores.RED2)
        sel_juego_rect = pygame.Rect(750, 190, 200, 50)
        pantalla.blit(sel_juego, sel_juego_rect)
        
        sel_juego2 = fuente2.render("Hi Scores", True, colores.RED2)
        sel_juego_rect2 = pygame.Rect(750, 290, 200, 50)
        pantalla.blit(sel_juego2, sel_juego_rect2)
        
        sel_juego3 = fuente2.render("Salir", True, colores.RED3)
        sel_juego_rect3 = pygame.Rect(750, 390, 200, 50)
        pantalla.blit(sel_juego3, sel_juego_rect3)

        texto_nombre = fuente2.render("ingresa tu nombre:", True, colores.BLACK)
        texto_nombre_rect = texto_nombre.get_rect(center=(400, ALTO_VENTANA // 2))
        pantalla.blit(texto_nombre, texto_nombre_rect)

        nombre_rect = pygame.Rect(300, ALTO_VENTANA // 2 + 50, 200, 40)
        pygame.draw.rect(pantalla, colores.WHITE, nombre_rect, 2)

        nombre_jugador_texto = fuente2.render(nombre_jugador, True, colores.BLACK)
        nombre_jugador_rect = nombre_jugador_texto.get_rect(center=nombre_rect.center)
        pantalla.blit(nombre_jugador_texto, nombre_jugador_rect)

        if nombre_jugador != "":
            pygame.draw.rect(pantalla, colores.GREEN, rect_boton1)#si el jugador ingresa al menos un caracter puede jugar
        else:
            pygame.draw.rect(pantalla, colores.RED2, rect_boton1)#si no ingresa nombre no se habilita el boton jugar
        
        pygame.draw.rect(pantalla, colores.SILVER, rect_boton2)
        pygame.draw.rect(pantalla, colores.SILVER, rect_boton3)

        pygame.display.flip()

    return JUGANDO, nombre_jugador
