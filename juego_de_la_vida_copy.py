import pygame  # <- Nos ayuda a crear gráficos con python
import numpy as np  # <- Nos ayuda a hacer "cálculos complejos" con python
import sys  # <- Nos ayuda a controlar partes del sistema operativo
import time

# Inicializamos pygame
pygame.init()

# Estas variables definirán el tamaño de la pantalla
color_celda = (0, 0, 0)
alto = 1000
ancho = 1000
numero_celdas_x = 50
numero_celdas_y = 50

ancho_celda = ancho / numero_celdas_x
alto_celda = alto / numero_celdas_y

#control de fps
clock = pygame.time.Clock()
fps = 10

# estado inicial
game_state = np.zeros((numero_celdas_x, numero_celdas_y), dtype=int)

# Creamos una variable que controla la pantalla
screen = pygame.display.set_mode((ancho, alto))
color_fondo = (162, 189, 243)

def glider(game_state,x,y):
    pattern = [
        (x, y),
        (x + 1, y + 1),
        (x + 1, y + 2),
        (x, y + 2),
        (x - 1, y + 2),
    ]
    for px, py in pattern:
        game_state[px % numero_celdas_x,py % numero_celdas_y] = 1

glider(game_state,5,1)
glider(game_state,5,5)
glider(game_state,10,10)
glider(game_state,20,20)



# game_state[30, 30] = 1
# game_state[30, 31] = 1
# game_state[30, 32] = 1
# game_state[30, 33] = 1
# game_state[31, 30] = 1
# game_state[31, 33] = 1
# game_state[32, 33] = 1
# game_state[33, 32] = 1



# # game_state[5, 1] = 1
# # game_state[6, 2] = 1
# # game_state[6, 3] = 1
# # game_state[5, 3] = 1
# # game_state[4, 3] = 1


# # #sapo
# # game_state[20, 20] = 1
# # game_state[20, 21] = 1
# # game_state[20, 22] = 1
# # game_state[21, 21] = 1
# # game_state[21, 22] = 1
# # game_state[21, 23] = 1


# # # Configuración inicial del tablero
# # game_state[10, 10] = 1
# # game_state[10, 11] = 1
# # game_state[10, 12] = 1

# game_state[21, 21] = 1
# game_state[22, 22] = 1
# game_state[22, 23] = 1
# game_state[21, 23] = 1
# game_state[20, 23] = 1

running = True
paused = False

# Bucle principal de nuestro juego
while running:
    new_game_state = np.copy(game_state)

    screen.fill(color_fondo)

    # pygame.QUIT event means the user clicked X to close your windo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    # Cuadrícula del lienzo
    # Hacemos dos ciclos for (anidados) para dibujar el "tablero" del juego.
    for y in range(0, numero_celdas_y):
        for x in range(0, numero_celdas_x):

            # Contamos los vecinos vivos
            n_neigh = (
                game_state[(x - 1) % numero_celdas_x, (y - 1) % numero_celdas_y]
                + game_state[x % numero_celdas_x, (y - 1) % numero_celdas_y]
                + game_state[(x + 1) % numero_celdas_x, (y - 1) % numero_celdas_y]
                + game_state[(x - 1) % numero_celdas_x, y % numero_celdas_y]
                + game_state[(x + 1) % numero_celdas_x, y % numero_celdas_y]
                + game_state[(x - 1) % numero_celdas_x, (y + 1) % numero_celdas_y]
                + game_state[x % numero_celdas_x, (y + 1) % numero_celdas_y]
                + game_state[(x + 1) % numero_celdas_x, (y + 1) % numero_celdas_y]
            )

            # Aplicamos las reglas del juego
            if game_state[x, y] == 0 and n_neigh == 3:
                new_game_state[x, y] = 1
            elif game_state[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                new_game_state[x, y] = 0

            # Dibujamos la celda
            poly = [
                (x * ancho_celda, y * alto_celda),
                ((x + 1) * ancho_celda, y * alto_celda),
                ((x + 1) * ancho_celda, (y + 1) * alto_celda),
                (x * ancho_celda, (y + 1) * alto_celda),
            ]
            if new_game_state[x, y] == 0:
                pygame.draw.polygon(screen, color_celda, poly, 2)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualizamos el estado del juego
    if not paused:
        game_state = np.copy(new_game_state)

    # Actualizamos la pantalla
    pygame.display.flip()

    clock.tick(fps)
    

pygame.quit()
 