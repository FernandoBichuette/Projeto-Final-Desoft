# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:33:40 2019

@author: Fernando
"""

import pygame 
import random
import time
from os import path
import math

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 460
HEIGHT = 600
FPS = 100

BLACK = (0, 0, 0)



class Lenhador(pygame.sprite.Sprite):
    
    # Construtor da classe.
  def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "Lenhador.jpg")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
                       
        # Centraliza embaixo da tela.
        self.img_referencia = self.image
        
         # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Lenhador")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'fundo.jpg')).convert()
background_rect = background.get_rect()


# Cria uma nave. O construtor será chamado automaticamente.
player = Lenhador()

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

try:
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
                
         # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

finally:
    pygame.quit()
  
    