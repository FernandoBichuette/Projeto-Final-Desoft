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

WIDTH = 640
HEIGHT = 400
FPS = 100

BLACK = (0, 0, 0)
WHITE = (255,255,255)
GRAY = (169, 169, 169)

class Lenhador(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "posicao1.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.right = 600
        self.rect.y = HEIGHT - 100
                       
        # Centraliza embaixo da tela.
        self.img_referencia = self.image

        # Velocidade 
        self.velocidade = 1

    def update(self):
        self.rect.x = self.velocidade
    
class Lenhador1(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "posicao1.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH/2 - 30
        self.rect.y = HEIGHT - 100
                       
        # Centraliza embaixo da tela.
        self.img_referencia = self.image

        # Velocidade 
        self.velocidade = 1

    def update(self):
        self.rect.x = self.velocidade
            
   
class Galho(pygame.sprite.Sprite):
    
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "galho.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100,100))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH/2 - 20
        self.rect.y = HEIGHT - 250
                       
        # Centraliza embaixo da tela.
        self.img_referencia = self.image    


class Tronco(pygame.sprite.Sprite):
        # Construtor da classe.
  def __init__(self,x):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        tronco_img = pygame.image.load(path.join(img_dir, "Tronco.jpg")).convert()
        self.image = tronco_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(tronco_img, (50, 300))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
                       
        # Centraliza embaixo da tela.
        self.img_referencia = self.image
        
         # Centraliza embaixo da tela.
        
        self.rect.bottom = HEIGHT - 10
        self.rect.centerx = x 
        
    
    
    
        
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Lenhador")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'Fundo.png')).convert()
background_rect = background.get_rect()


# Cria uma nave. O construtor será chamado automaticamente.
player = Lenhador()
player2 = Lenhador1()
tronco1 = Tronco(160)
tronco2 = Tronco(480)
galho= Galho()
# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player,player2,tronco1,tronco2,galho)

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
    
    # Verifica se a tecla foi apertado 
        if event.type == pygame.KEYDOWN:

            if event.type == pygame.K_RIGHT:
                self.rect.x = -1





         # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

finally:
    pygame.quit()
  
    