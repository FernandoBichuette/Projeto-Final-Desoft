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

contador_de_vida=100

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
        self.rect.x = 500
        self.rect.y = HEIGHT-100
                       
        # Centraliza embaixo da tela.
        self.img_referencia = self.image

        # Velocidade 
        self.velocidade = 0

    def update(self):
        pass
        self.rect.x += self.velocidade
    
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
        self.rect.x = 65
        self.rect.y = HEIGHT-100
                       
        # Centraliza embaixo da tela.
        self.img_referencia = self.image

        # Velocidade 
        self.velocidade = 0



    def update(self):
        self.rect.x += self.velocidade

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
        

class Galho(pygame.sprite.Sprite):
    
    def __init__(self,x):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        
        if random.randint(0,1) == 0:
            player_img = pygame.image.load(path.join(img_dir, "Esquerda.png")).convert()
            self.image = player_img
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(player_img, (100,100))
        
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            

            self.rect.x = x - 100
        
        else:
            player_img = pygame.image.load(path.join(img_dir, "Direito.png")).convert()
            self.image = player_img
             # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(player_img, (100,100))
        
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            
            self.rect.x = x + 40
        
               
        self.speedy = 0     

        self.rect.y = HEIGHT - 350
        # Centraliza embaixo da tela.
        self.img_referencia = self.image    

    def update(self):
        self.rect.y += self.speedy
        # Se o galho passar do chão da tela, morre.
        if self.rect.bottom > HEIGHT:
            self.kill()
            


        
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

# Cria um grupo para os galhos e player
galhos = pygame.sprite.Group()
players = pygame.sprite.Group()

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player,player2,tronco1,tronco2)


# for i in range(8):
#     ga = Galho()
#     all_sprites.add(ga)
#     galhos.add(ga)


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

                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    """
                    player.image = pygame.image.load(path.join(img_dir,'posicao3.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image,(50, 100))
                    player.image.set_colorkey(BLACK)
"""
                    galho = Galho(tronco2.rect.x)
                    all_sprites.add(galho)
                    galhos.add(galho)
                    
                    player.rect.x = 350
                    galho.speedy = 1  
                   

                if event.key == pygame.K_RIGHT:

                    player.image = pygame.image.load(path.join(img_dir,'posicao3.png')).convert_alpha()
                    player.image = pygame.transform.scale(player.image,(50, 100))
                    player.image.set_colorkey(BLACK)

                    galho = Galho(tronco2.rect.x)
                    all_sprites.add(galho)
                    galhos.add(galho)

                    player.rect.x = 510
                    galho.speedy = 1  

                if event.key == pygame.K_a:
                    
                    player2.rect.x = 30
                    galho1.speedy = 1

                if event.key == pygame.K_d:
                    player2.rect.x= 190
                    galho1.speedy = 1
            
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_a:
                    player.speedx = 0
                if event.key == pygame.K_d:
                    player.speedx = 0


        # Atualiza a acao de cada sprite.
        all_sprites.update()

        # Verifica se houve colisão entre tiro e meteoro
        hits = pygame.sprite.groupcollide(players, galhos, True, True)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            ga = Galho()
            all_sprites.add(ga)
            galhos.add(ga)

         # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

finally:
    pygame.quit()
  
    