import pygame
import colores
#mensaje que se muestra entre oleadas de enemigos

def mensaje_alerta(pantalla):
    fuente = pygame.font.SysFont("starjedi",25)
    fuente2 = pygame.font.SysFont("starjedi",85)
    alert_text1 = fuente2.render("alerta!!",True,colores.ORANGE1)
    alert_text12 = fuente2.render("alerta!!",True,colores.BLACK)
    alert_text2 = fuente.render("naves enemigas se acercan",True,colores.ORANGE1)
    alert_text21 = fuente.render("naves enemigas se acercan",True,colores.BLACK)
    alert_text3 = fuente.render("protege al crucero",True,colores.ORANGE1)
    alert_text31 = fuente.render("protege al crucero",True,colores.BLACK)
    
    pantalla.blit(alert_text12,(504,124))
    pantalla.blit(alert_text1,(500,120))
    pantalla.blit(alert_text21,(503,253))
    pantalla.blit(alert_text2,(500,250))
    pantalla.blit(alert_text31,(553,303))
    pantalla.blit(alert_text3,(550,300))
