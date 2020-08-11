import pygame, sys, random
from pygame.locals import *

pygame.init()
relojPrincipal = pygame.time.Clock()

ANCHOVENTANA = 400
ALTURAVENTANA = 400
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTURAVENTANA), 0, 32)
pygame.display.set_caption('Entrada')

NEGRO = (0, 0, 0)
VERDE = (0, 225, 0)
BLANCO = (225, 225, 225)

contadorDeComida = 0
NUEVACOMIDA = 40
TAMAÑOCOMIDA = 20
jugador = pygame.Rect(300, 100, 50, 50)
comidas = []
for i in range (20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))
    
moverseIzquierda = False
moverseDerecha = False
moverseArriba = False
moverseAbajo = False

VELOCIDADMOVIMIENTO = 6

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWM: #Cambiar variables del teclado
            if evento.key == K_LEFT or evento.key == ord('a'):
                moverseDerecha = False
                moverseIzquierda = True
            if evento.key == K_RIGHT or evento.key == ord('d'):
                moverseIzquierda = False
                moverseDerecha = True
            if evento.key == K_UP or evento.key == ord('w'):
                moverseAbajo = False
                moverseArriba = True
            if evento.key == k_DOWN or evento.key == ord('s'):
                moverseArriba = False
                moverseAbajo = True
        if evento.type == KEYUP:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if evento.key == K_LEFT or evento.key == ord('a'):
                moverseIzquierda = False
            if evento.key == K_RIGHT or evento.key == ord('d'):
                moverseDerecha = False
            if evento.key == k_UP or evento.key == ord('w'):
                moverseArriba = False
            if evento.key == K_DOWN or evento.key == ord('s'):
                moverseAbajo = False
            if evento.key == ord('x'):
                jugador.top = random.randint(0, ALTURAVENTANA - jugador.height)
                jugador.left = random.randin(0, ANCHOVENTANA - jugador.width)

        if evento.type == MOUSEBUTTONUP:
                comidas.append(pygame.Rect(evento.pos[0], evento.pos[1], TAMAÑOCOMIDA, TAMAÑOCOMIDA))

    contadorDeComida += 1
    if contadorDeComida >= NUEVACOMIDA:
        contadorDeComida = 0
        comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), random.randint(0, ALTURAVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

    superficieVentana.fill(NEGRO)

    if moverseAbajo and jugador.bottom < ALTURAVENTANA:
        jugador.top += VELOCIDADMOVIMIENTO
    if moverseArriba and jugador.top > 0:
        jugador.top -= VELOCIDADMOVIMIENTO
    if moverseIzquierda and jugador.left > 0:
        jugador.left -= VELOCIDADMOVIMIENTO
    if moverseDerecha and jugador.right < ANCHOVENTANA:
        jugador.right += VELOCIDADMOVIMIENTO

    pygame.draw.rect(superficieVentana, BLANCO, jugador)

    for comida in comidas[:]:
        if jugador.colliderect(comida):
            comidas.remove(comida)

    for i in range(len(comidas)):
        pygame.draw.rect(superficieVentana, VERDE, comidas[i])

    pygame.display.update()
    relojPrincipal.tick(40)
