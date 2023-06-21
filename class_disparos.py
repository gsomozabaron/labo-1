import pygame
import colores
import sonidos

lista_de_tiros = []

def detectar_dist_tiro(lista_de_caza,lista_fragatas,lista_bombardero, crucero):
    for caza in lista_de_caza:
        for fragata in lista_fragatas:
            if caza.distancia_de_ataque .colliderect(fragata.rect):
                    sonidos.disparo_caza.play() ####banaccaa, mucho ruido!!!!!!!!!!!
                    x1 = caza.rect[0] + 50 // 2  # Posición x del primer disparo
                    y1 = caza.rect[1] + 30  # Posición y del primer disparo
                    lista_de_tiros.append(pygame.Rect(x1, y1, 10, 3))                                        
    
    for bombardero in lista_bombardero:
        for fragata in lista_fragatas:
            if bombardero.distancia_de_ataque .colliderect(fragata.rect):
                sonidos.disparo_caza.play() ####banaccaa, mucho ruido!!!!!!!!!!!
                x1 = bombardero.rect[0] + 50 // 2  # Posición x del primer disparo
                y1 = bombardero.rect[1] + 40  # Posición y del primer disparo
                lista_de_tiros.append(pygame.Rect(x1, y1, 10, 5))                
    
    for caza in lista_de_caza:
        if caza.distancia_de_ataque .colliderect(crucero.rect):
            sonidos.disparo_caza.play()
            x1 = caza.rect[0] + 50 // 2  # Posición x del primer disparo
            y1 = caza.rect[1] + 30  # Posición y del primer disparo
            lista_de_tiros.append(pygame.Rect(x1, y1, 10, 3))
    
    for bombardero in lista_bombardero:
        if bombardero.distancia_de_ataque .colliderect(crucero.rect):
            sonidos.disparo_caza.play()
            x1 = bombardero.rect[0] + 50 // 2  # Posición x del primer disparo
            y1 = bombardero.rect[1] + 40  # Posición y del primer disparo
            lista_de_tiros.append(pygame.Rect(x1, y1, 10, 5))
    return lista_de_tiros

lista_de_tiros_fragata = []
def dist_tiro_fragata(lista_de_caza,lista_fragatas,lista_bombardero):
    for caza in lista_de_caza:
        for fragata in lista_fragatas:
            if fragata.distancia_de_ataque. colliderect(caza.rect):
                #x1 = fragata.rect[0] + 20 // 2  # Posición x del primer disparo
                #y1 = fragata.rect[1] + 50  # Posición y del primer disparo
                #lista_de_tiros_fragata.append(pygame.Rect(x1, y1, 10, 2))
                x2 = fragata.rect[0] + 40 // 2  # Posición x del 2do disparo
                y2 = fragata.rect[1] + 60  # Posición y del primer disparo
                lista_de_tiros_fragata.append(pygame.Rect(x2, y2, 10, 2))
                #x3 = fragata.rect[0] + 30 // 2  # Posición x del 3er disparo
                #y3 = fragata.rect[1] + 70  # Posición y del primer disparo
                #lista_de_tiros_fragata.append(pygame.Rect(x3, y3, 10, 2))
    
    for bomber in lista_bombardero:
        for fragata in lista_fragatas:
            if fragata.distancia_de_ataque. colliderect(bomber.rect):
                #x1 = fragata.rect[0] + 20 // 2  # Posición x del primer disparo
                #y1 = fragata.rect[1] + 50  # Posición y del primer disparo
                #lista_de_tiros_fragata.append(pygame.Rect(x1, y1, 10, 2))
                x2 = fragata.rect[0] + 40 // 2  # Posición x del 2do disparo
                y2 = fragata.rect[1] + 60  # Posición y del primer disparo
                lista_de_tiros_fragata.append(pygame.Rect(x2, y2, 10, 2))
                #x3 = fragata.rect[0] + 30 // 2  # Posición x del 3er disparo
                #y3 = fragata.rect[1] + 70  # Posición y del primer disparo
                #lista_de_tiros_fragata.append(pygame.Rect(x3, y3, 10, 2))    
    return lista_de_tiros_fragata

    ####----------------tiros nave heroe------------------------------------------------------####
def mostrar_disparos_heroe(disparos,pantalla,velocidad_de_disparos):
    for disparo in disparos:
        if disparo.x > 0:
            disparo.x -= velocidad_de_disparos  # Mover el disparo hacia la izquierda
        else:
            disparos.remove(disparo) #si salio de la pantalla lo borramos de la lista
    for disparo in disparos:    
        pygame.draw.rect(pantalla, colores.RED1, disparo) 
        
    ####-----------------tiros fragatas--------------------------------------------------------#####
def mostrar_tiros_fragata(lista_de_tiros_fragata,pantalla):
    for tiro in lista_de_tiros_fragata:
        if tiro.x > -10:
            tiro.x -= 3.5 # Mover el disparo hacia la izquierda
        else:
            lista_de_tiros_fragata.remove(tiro)    
        pygame.draw.rect(pantalla,(colores.RED1),tiro)

    ####--------------tiros de cazas y bombers--------------------------------------------------####
def mostrar_lista_de_tiros(lista_de_tiros,pantalla):
    for tiro in lista_de_tiros:
        if tiro.x < 1300:
            tiro.x += 3.5 # Mover el disparo hacia la derecha
        else:
            lista_de_tiros.remove(tiro)
        pygame.draw.rect(pantalla,(colores.GREEN1),tiro)


