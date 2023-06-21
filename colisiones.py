import pygame
import sonidos

def verificar_colisiones(disparos, cazas, bombarderos, dict_nave_heroe, lista_de_tiros, lista_fragatas, crucero, lista_de_tiros_fragata):
    disparos_eliminar = []  # Lista para almacenar los disparos que colisionaron
    
    for disparo in disparos:
        ##------cazas alcanzados por heroe-----##
        for caza in cazas:
            if disparo.colliderect(caza.rect):
                dict_nave_heroe["score"] += 10 ##-test-##vajar a 10
                caza.salud -= 3
                disparos_eliminar.append(disparo)
                break
        ##------bombers alcanzados por heroe-----##    
        for bombardero in bombarderos:
            if disparo.colliderect(bombardero.rect):
                dict_nave_heroe["score"] += 20 ##-test-##vajar a 20
                bombardero.salud -= 3  
                disparos_eliminar.append(disparo)
                break
        ##------cazas alcanzados por fragatas-----##    
    for disparo in lista_de_tiros_fragata:
        for caza in cazas:
            if disparo.colliderect(caza.rect):
                caza.salud -= 2 
                disparos_eliminar.append(disparo)
                break
        ##------bombarderos alcanzados por fragatas-----##    
        for bombardero in bombarderos:
            if disparo.colliderect(bombardero.rect):
                bombardero.salud -= 1  
                disparos_eliminar.append(disparo)
                break
            #borarr de las listas los tiros que colisionaron
    eliminar_tiros = []
    
    for tiro in lista_de_tiros:
        for fragata in lista_fragatas:
            if tiro.colliderect(fragata.rect):
                fragata.vida -= 1
                eliminar_tiros.append(tiro)
                break
            #si la fragata se queda sin vida vuelve a la posic de salida    
            if fragata.vida < 0:
                dict_nave_heroe["score"] -= 1000
                fragata.rect.x = -1000
                fragata.distancia_de_ataque.x = -1000
                fragata.vida += 1000
                sonidos.explota.play()
                
        if tiro. colliderect(crucero.rect):
            crucero.vida -= 1
            eliminar_tiros.append(tiro)
            break
    
        # borrar los disparos que colisionaron
    for disparo in disparos_eliminar:
        if disparo in disparos:
            disparos.remove(disparo)

    for disparo in disparos_eliminar:        
        if disparo in lista_de_tiros_fragata:
            lista_de_tiros_fragata.remove(disparo)

    for disparo in eliminar_tiros:
        if disparo in lista_de_tiros:
            lista_de_tiros.remove(disparo) 