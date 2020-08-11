import pygame, sys, random
from pygame.locals import *

def veriSuperposicionRects(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]: #Verifica si las esquinas de a se encuentran dentro de b
        if ((puntoDentroDeRect(a.left, a.top, b)) or
            (puntoDentroDeRect(a.left, a.bottom, b)) or
            (puntoDentroDeRect(a.right, a.top, b)) or
            (puntoDentroDeRect(a.right, a.bottom, b))):
            return True

    return False

def PuntoDentroDeRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False

pygame.init()
relojPrincipal = pygame.time.Clock()

ANCHOVENTANA = 400
ALTOVENTANA = 400
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)
pygame.displat.set_caption('Deteccion de Colisiones')

# variables de direccion
ABAJOIZQUIERDA = 1
ABAJODERECHA = 3
ARRIBAIZQUIERDA = 7
ARRIBADERECHA = 9

VELOCIDADMOVIMIENTO = 4

NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
BLANCO = (225, 225, 225)

#Estructura de datos rebotin y comida
contadorComida = 0
NUEVACOMIDA = 40
TAMAÑOCOMIDA = 20
rebotin = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':ARRIBAIZQUIERDA}
comidas =[]
for i in range(20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), RANDOM.RANDINT(0, ANCHOVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    contadorComida += 1
    if contadorComida >= NUEVACOMIDA:
        contadorComida = 0
        comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), RANDOM.RANDINT(0, ANCHOVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

    superficieVentana.fill(NEGRO)

    #mueve estructura de datos del rebotin
    if rebotin['dir'] == ABAJOIZQUIERDA:
        rebotin['rect'].left -= VELOCIDADMOVIMIENTO
        rebotin['rect'].top += VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ABAJODERECHA:
        rebotin['rect'].left += VELOCIDADMOVIMIENTO
        rebotin['rect'].top += VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ARRIBAIZQUIERDA:
        rebotin['rect'].left -= VELOCIDADMOVIMIENTO
        rebotin['rect'].top -= VELOCIDADMOVIMIENTO
    if rebotin['dir'] == ARRIBADERECHA:
        rebotin['rect'].left += VELOCIDADMOVIMIENTO
        rebotin['rect'].top -= VELOCIDADMOVIMIENTO

    if rebotin['rect'].top < 0:
            # el bloque se movio por arriba de la ventana
        if rebotin['dir'] == ARRIBAIZQUIERDA:
            rebotin['dir'] = ABAJOIZQUIERDA
        if rebotin['dir'] == ARRIBADERECHA:
            rebotin['dir'] = ABAJODERECHA
    if rebotin['rect'].bottom > ALTOVENTANA:
            # el bloque se movio por debajo de la ventana
        if rebotin['dir'] == ABAJOIZQUIERDA:
            rebotin['dir'] = ARRIBAIZQUIERDA
        if rebotin['dir'] == ABAJODERECHA:
            rebotin['dir'] = ARRIBADERECHA
    if rebotin['rect'].left < 0:
            # el bloque se movio por la izquierda de la ventana
        if rebotin['dir'] == ABAJOIZQUIERDA:
            rebotin['dir'] = ABAJODERECHA
        if rebotin['dir'] == ARRIBAIZQUIERDA:
            rebotin['dir'] = ARRIBADERECHA
    if rebotin['rect'].right > ANCHOVENTANA:
            # el bloque se movio por la derecha de la ventana
        if rebotin['dir'] == ABAJODERECHA:
            rebotin['dir'] = ABAJOIZQUIERDA
        if rebotin['dir'] == ARRIBADERECHA:
            rebotin['dir'] = ARRIBAIZQUIERDA

    pygame.draw.rect(superficieVentana, BLANCO, rebotin['rect'])

    #verifica si rebotin intersectó algun cuadrado de comida
    for comida in comida[:]:
        if veriSuperposicionRects(rebotin['rec'], comida):
            comidas.remove(comida)

    #dibujar comida
    for i in range(len(comidas)):
        pygame.draw.rects(superficieVentana, VERDE, comidas[i])

    #Dibuja la ventana en la pantalla
    pygame.display.update()
    relojPrincipal.tick(60)
    
