import pygame
import colores

import sonidos
from class_bomber import BombarderoEnemigo
from class_caza import CazaEnemigo
import nave_heroe
from class_crucero import CruceroAliado
import class_fragata
import colisiones
import class_disparos
import disenio_pantalla
import menu
import game_over
import mensajes
import menu_hiscore
import hi_scores

pygame.init()

ANCHO_VENTANA = 1300
ALTO_VENTANA = 600
tiempo_inicial = pygame.time.get_ticks()

##--con F5 cambiamos el modo para ver rectangulos y testear coliciones--##
modo_debug = False

#leer datos del DB para actualizar la lista hi_scores
lista_hiscores = hi_scores.leerDatos()

###################################################################################################
###-----setup nave heroe-----------------------------------------------###
###--------------------- Imagen nave heroe ----------------------------###
velocidad_de_movimiento = 2  # velocidad de translacion del x-wing
tamanio_nave_heroe = [50, 50]
dict_nave_heroe = nave_heroe.crear_heroe(1000,300,tamanio_nave_heroe[0],tamanio_nave_heroe[1])
###------------------Disparos heroe------------------------------------###
tamanio_disparo = [10, 3]
imagen_disparo = pygame.Surface(tamanio_disparo)
imagen_disparo.fill(colores.RED1)
disparos = []  # Lista para almacenar los disparos disparados
velocidad_de_disparos = 5
#####################################################################################################
    
#titulo por ahora vamos con Rebel Pilot 2
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Rebel Pilot 2")
# timer
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,10)

###################-----creacion de naves aliadas--------#############################################
crucero = CruceroAliado(1200, 100, 80, 400)
cantidad_fragatas = 6
lista_fragatas = class_fragata.crear_lista_fragatas(cantidad_fragatas) 
puntajes_objetivo = [500, 1000, 1500, 2000, 2500, 3000]  #puntaje para llamar a fragatas aliadas 

####################---- creacion inicial de naves enemigas   #######################################
cantidad_cazas = 3
cantidad_bombers = 1
velocidad_cazas = 2
velocidad_bombers = 1
lista_de_cazas = CazaEnemigo.crear_lista_de_cazas (cantidad_cazas)
lista_de_bombers = BombarderoEnemigo.crear_lista_de_bombers(cantidad_bombers)

########----creacion lista de tiros enemigos (deteccion de coliciones entre naves aliadas y enemigas)
lista_de_tiros = class_disparos.detectar_dist_tiro(lista_de_cazas,lista_fragatas,lista_de_bombers, crucero)
tiempo_espera = 500  # tiempo entre detecciones para separar los tiros
ultimo_disparo = 0   # con 500 se ve copado
lista_de_tiros_fragata =class_disparos.dist_tiro_fragata(lista_de_cazas,lista_fragatas,lista_de_bombers)


clock = pygame.time.Clock()  # Reloj para controlar la velocidad de actualización    
####--tiempo entre oleadas---######
tiempo_espera_niveles = 2000
tiepo_anterior = 0
igualar_tiempo = True

JUGANDO = "menu" #iniciar en el menu principal

####------------------------INICIO BUCLE DEL JUEGO---------------------------------------------###        
flag_correr = True
while flag_correr:
    # Limita la velocidad de actualización a 120 cuadros por segundo--------------------------###
    clock.tick(120)  
    tiempo_actual = pygame.time.get_ticks()
    ####------------------------------pintar fondo de la pantalla------------------------------###
    pantalla.blit(disenio_pantalla.imagen_fondo, (0, 0))
    pantalla.blit(disenio_pantalla.imagen_ds, (0, 200))
    
    lista_eventos = pygame.event.get()
    
##########--menus y salir--#########################################################################
    if JUGANDO == "menu":
        pygame.mixer.music.load("menu.mp3")
        pygame.mixer.music.set_volume(0.9)   
        pygame.mixer.music.play(-1)  # -1 indica que la música se reproducirá en bucle
        JUGANDO, nombre_jugador = menu.mostrar_menu(ANCHO_VENTANA, ALTO_VENTANA, pantalla,JUGANDO)
        
    elif JUGANDO == "salir":
       flag_correr = False
       
    elif JUGANDO == "gameover":
        JUGANDO = game_over.mostrar_menu(ANCHO_VENTANA,ALTO_VENTANA,pantalla,JUGANDO)
    
    elif JUGANDO == "menu_hiscore":
        JUGANDO = menu_hiscore.mostrar_menu(ANCHO_VENTANA, ALTO_VENTANA, pantalla)
    
#########################################################################################################    
#######----------------------------bucle del juego-------------------------------------------------######
    elif JUGANDO == "jugando":
        lista_teclas = nave_heroe.comandos(dict_nave_heroe, velocidad_de_movimiento, ANCHO_VENTANA, ALTO_VENTANA, tamanio_nave_heroe)
        
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: 
                flag_correr = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    JUGANDO = "jugando"
                if evento.key == pygame.K_F5: #modo debbugger para mostrar los rectangulos de colision
                    modo_debug = not modo_debug
                          
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Botón izquierdo del mouse
                sonidos.disparo_heroe.play()
                disparos = nave_heroe.disparar_heroe(dict_nave_heroe,tamanio_nave_heroe)          

##########################################################################################################                
########----si todas las naves enemigas son eliminadas, aumentamos la cantidad de enemigos----############    
####--------------------algo asi como pasar de nivel--------------------------------------------------####      
            if igualar_tiempo:
                    tiepo_anterior = tiempo_actual   
            
            if len(lista_de_cazas) == 0 and len(lista_de_bombers) == 0:
                igualar_tiempo=False
                #---mensaje de protege al crucero---##
                mensajes.mensaje_alerta(pantalla)
                
                ###---pausa para descanzar los dedos---###
                if tiempo_actual - tiepo_anterior >= tiempo_espera_niveles:
                    igualar_tiempo = True
                ##--sonido de cazas acercandose--##
                    sonidos.sonido_vuelo_caza.play()
                ##--creacionde listas con las nuevas cantidades de enemigos--##
                    lista_de_cazas = CazaEnemigo.crear_lista_de_cazas(cantidad_cazas)# aca va el reinicio
                    lista_de_bombers = BombarderoEnemigo.crear_lista_de_bombers(cantidad_bombers)
                    cantidad_cazas += 3
                    cantidad_bombers += 1
                ##----igualar tiepo_anterior al tiempo actual para el proximo bucle----##

###########################################################################################################

        # si socre llega a los valores declarados en puntaje objetivo
        # se ejecuta fragata.mover(2) que lleva la fragata a su nueva pocision a la velocidad "(2)"
        for i, fragata in enumerate(lista_fragatas):
                        puntaje_objetivo = puntajes_objetivo[i]
                        if dict_nave_heroe["score"] >= puntaje_objetivo: 
                            fragata.mover(2) #avanzar hasta 1000

############################################################################################################
        # si la vida del crucero se agota se vacian las listas, restaura la vida del crucero
        # se resetea la cantidad de naves iniciales
        # se para el bucle principal y se va al menu "gameover" 
        if crucero.vida < 0:
            lista_de_bombers = []
            lista_de_cazas = []
            lista_fragatas = []
            disparos_nuevos = []
            lista_fragatas = class_fragata.crear_lista_fragatas(cantidad_fragatas) 
            cantidad_cazas = 3
            cantidad_bombers = 1
            crucero.vida = 200
            #se guarda el escore en el archivo hiscores.db y se resetea a cero el score
            hi_scores.insertarColumna(nombre_jugador,dict_nave_heroe["score"])
            dict_nave_heroe["score"] = 0
            JUGANDO = "gameover"

##################################---disparos---###########################################################             
        ######----hace una pausa en los chequeos para que los disparos no sea una linea---##########
        if tiempo_actual - ultimo_disparo >= tiempo_espera:
            class_disparos.detectar_dist_tiro(lista_de_cazas,lista_fragatas,lista_de_bombers,crucero)               
            class_disparos.dist_tiro_fragata(lista_de_cazas,lista_fragatas,lista_de_bombers)
            ultimo_disparo = tiempo_actual   
        ####-----Dibujar los disparos heroe y actualizar su posición--------####    
        class_disparos.mostrar_disparos_heroe(disparos,pantalla,velocidad_de_disparos)
        ####-----disparos-automaticos----------------------------------------###
        class_disparos.mostrar_lista_de_tiros(lista_de_tiros, pantalla)
        class_disparos.mostrar_tiros_fragata(lista_de_tiros_fragata,pantalla)

####################################--naves--################################################################
        ####---verificar coliciones------------------------------------------###
        colisiones.verificar_colisiones(disparos, lista_de_cazas, lista_de_bombers,dict_nave_heroe, lista_de_tiros, lista_fragatas, crucero, lista_de_tiros_fragata)
        ####---dibrujar fragata aliada---------------------------------------###    
        class_fragata.actualizar_pantalla(lista_fragatas,pantalla,modo_debug)
        ####---dibrujar crucero aliado---------------------------------------###
        CruceroAliado.dibujar_crucero(crucero,pantalla,modo_debug)
        ####---mostrar y actualizar naves enemigas---------------------------###
        CazaEnemigo.dibujar_cazas(lista_de_cazas,velocidad_cazas,modo_debug,pantalla)
        BombarderoEnemigo.dibujar_cazas(lista_de_bombers,velocidad_bombers,modo_debug,pantalla)
        ####---dibuja nave heroe---------------------------------------------### 
        nave_heroe.actualizar_pantalla(dict_nave_heroe, pantalla,modo_debug)
        
        #####--------flip---------------------------------------------------####
        pygame.display.flip()     
pygame.quit()