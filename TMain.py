import pygame
import random
import time

from os import path

from configuracoes import WIDTH, HEIGHT, INIT, GAME, QUIT
from Projeto_final import teste
from t_inicial import tela_inic


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Lenhador")

# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = tela_inic(screen)
        elif state == GAME:
            state = jogo(screen)
        else:
            state = QUIT
finally:
    pygame.quit()