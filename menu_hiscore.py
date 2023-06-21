import pygame
import colores
import hi_scores

def mostrar_menu(ANCHO_VENTANA, ALTO_VENTANA, pantalla):
    lista_hiscores = hi_scores.leerDatos() #nos traemos la data de la base de datos
    fondo_menu = pygame.image.load("fondo5.jpg")  # lee la imagen
    fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO_VENTANA, ALTO_VENTANA))  # escala la imagen a la medida "tamaño"

    #botones del menu
    rect_boton1 = pygame.Rect(700, 200, 25, 25)
    rect_selec = pygame.Rect(0, 0, 5, 5)

    fuente = pygame.font.SysFont("starjedi", 50)
    fuente2 = pygame.font.SysFont("starjedi", 25)
    
    # Definir las posiciones base de los nombres y puntajes
    posiciones = [(200, 150), (200, 200), (200, 250), (200, 300), (200, 350), (200, 400), (200, 450), (200, 500), (200, 550)]
    


    flag_correr = True
    while flag_correr:
        pantalla.fill(colores.WHITE)
        pantalla.blit(fondo_menu, (0, 0)) 
        
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: 
                JUGANDO = "salir"
                flag_correr = False
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                rect_selec.topleft = evento.pos
                if rect_selec.colliderect(rect_boton1):
                    JUGANDO = "menu"
                    flag_correr = False
        
        texto_bienvenida = fuente.render("Los mejores pilotos!!", True, colores.WHITE)
        texto_rect = texto_bienvenida.get_rect(center=(ANCHO_VENTANA // 2, 100))
        
        #funca!!!        
        for i, hiscore in enumerate(lista_hiscores[:9]):  #limite 9 scores, enumerate trae los indices y valores de la lista
            pos_name = pygame.Rect(200, posiciones[i][1], 200, 50) #genera rectangulo para el nombre para el valor i de la iteracion 
            pos_score = pygame.Rect(400, posiciones[i][1], 200, 50) #genera rectangulo para el score
            text_name = fuente2.render("{}".format(hiscore[0]), True, colores.RED1)
            text_score = fuente2.render("{}".format(hiscore[1]), True, colores.WHITE)
            pantalla.blit(text_name, pos_name)
            pantalla.blit(text_score, pos_score)
            
        sel_juego = fuente2.render("volver al menu", True, colores.RED1)
        sel_juego_rect = pygame.Rect(750, 190, 200, 50)
         
        pantalla.blit(sel_juego, sel_juego_rect)
        pantalla.blit(texto_bienvenida, texto_rect)     
        pygame.draw.rect(pantalla, colores.SILVER, rect_boton1)
        pygame.display.flip()

    return JUGANDO

