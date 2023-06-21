import pygame
import colores

# Disparos
tamanio_disparo = [10, 3]
imagen_disparo = pygame.Surface(tamanio_disparo)
imagen_disparo.fill(colores.RED1)
disparos = []  # Lista para almacenar los disparos disparados

def crear_heroe(x,y,ancho,alto):
    imagen_heroe = "xwing.png"
    dict_nave_heroe = {}
    dict_nave_heroe ["imagen"] = pygame.image.load(imagen_heroe)
    dict_nave_heroe ["imagen"] =pygame.transform.scale(dict_nave_heroe ["imagen"],(ancho,alto))
    dict_nave_heroe ["imagen"] = pygame.transform.rotate(dict_nave_heroe ["imagen"], 90)
    dict_nave_heroe ["rect"] = pygame.Rect(x, y, 50, 50)
    dict_nave_heroe ["score"] = 0
    return dict_nave_heroe
 
def comandos(dict_nave_heroe,velocidad_de_movimiento,ANCHO_VENTANA,ALTO_VENTANA,tamanio_nave_heroe):
    lista_teclas = pygame.key.get_pressed()  # hace una lista de las teclas que están presionadas
    if (lista_teclas[pygame.K_d] or lista_teclas[pygame.K_RIGHT]) and dict_nave_heroe["rect"][0] < (ANCHO_VENTANA-tamanio_nave_heroe[0]):
        dict_nave_heroe["rect"][0] += velocidad_de_movimiento
    if (lista_teclas[pygame.K_a] or lista_teclas[pygame.K_LEFT]) and dict_nave_heroe["rect"][0] > 500:
        dict_nave_heroe["rect"][0] -= velocidad_de_movimiento
    if (lista_teclas[pygame.K_w] or lista_teclas[pygame.K_UP]) and dict_nave_heroe["rect"][1] > 25:
        dict_nave_heroe["rect"][1] -= velocidad_de_movimiento
    if (lista_teclas[pygame.K_s] or lista_teclas[pygame.K_DOWN]) and dict_nave_heroe["rect"][1] < ((ALTO_VENTANA-tamanio_nave_heroe[1])-25):
        dict_nave_heroe["rect"][1] += velocidad_de_movimiento


def disparar_heroe(dict_nave_heroe,tamanio_nave_heroe):
    # Disparar disparo
    x1 = dict_nave_heroe["rect"][0] + tamanio_nave_heroe[0] // 2  # Posición x del primer disparo
    y1 = dict_nave_heroe["rect"][1] + 1  # Posición y del primer disparo
    disparos.append(pygame.Rect(x1, y1, tamanio_disparo[0], tamanio_disparo[1]))

    x2 = dict_nave_heroe["rect"][0] + tamanio_nave_heroe[0] // 2  # Posición x del segundo disparo
    y2 = dict_nave_heroe["rect"][1] + tamanio_nave_heroe[1] - 3  # Posición y del segundo disparo
    disparos.append(pygame.Rect(x2, y2, tamanio_disparo[0], tamanio_disparo[1]))
    return disparos



def actualizar_pantalla(dict_nave_heroe,pantalla,modo_debug):
    if modo_debug:
        pygame.draw.rect(pantalla,(colores.RED1),dict_nave_heroe["rect"],2)
    pantalla.blit(dict_nave_heroe["imagen"], (dict_nave_heroe["rect"][0], dict_nave_heroe["rect"][1]))
    
    fuente = pygame.font.SysFont("Arial",30)
    score_text = fuente.render("SCORE {0}".format(dict_nave_heroe ["score"]),True,colores.WHITE)
    pantalla.blit (score_text,(1000, 0)) 
