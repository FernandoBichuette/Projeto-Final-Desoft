import pygame
import random
import time
from os import path

from configuracoes import img_dir, BLACK, GAME, QUIT


        
def tela_inic(screen):

    
    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(img_dir, 'Capa_desoft.png')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
                
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_n:
                    state = QUIT
                    running = False
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_b:
                    state = GAME
                    running = False
            
            
            
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
