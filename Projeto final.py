# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:33:40 2019

@author: Fernando
"""

import pygame as pygame
import random
import time
from os import path
import math

img_dir = path.join(path.dirname(__file__), 'img')
fnt_dir = path.join(path.dirname(__file__), 'font')

WIDTH = 640
HEIGHT = 400
FPS = 100

BLACK = (0, 0, 0)
WHITE = (255,255,255)
GRAY = (169, 169, 169)
YELLOW = (255, 255, 0)

TAXA_VIDA = 200
SAUDE = 100

class Lenhador(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,distancia):
        
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
        self.rect.x = distancia
        self.rect.y = HEIGHT-100
                       
        # Centraliza embaixo da tela.
        self.img_referencia = self.image

        # Colisor 
        self.mask = pygame.mask.from_surface(self.image)

        # Velocidade 
        self.velocidade = 0

    def update(self):
        pass
        self.rect.x += self.velocidade


class Barra_de_vida(pygame.sprite.Sprite):
    def __init__(self,distancia):
        pygame.sprite.Sprite.__init__(self)

        self.SAUDE = SAUDE
        self.image = pygame.image.load(path.join(img_dir,'Barra de vida.png')).convert()
        self.image = pygame.transform.scale(self.image,(self.SAUDE,20))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = distancia
        self.rect.y = HEIGHT - 350

        self.regen = 1

    def update(self):
        if self.SAUDE >= 100:
            self.regen = -5
        self.SAUDE += self.regen
        if self.SAUDE < 0:
            self.SAUDE = 0
        self.image = pygame.transform.scale(self.image,(self.SAUDE,20))
        self.regen = 0


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
            galho_img = pygame.image.load(path.join(img_dir, "Esquerda.png")).convert()
            self.image = galho_img
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(galho_img, (100,100))
        
            # Deixando transparente.
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            

            self.rect.x = x - 100
        
        else:
            galho_img = pygame.image.load(path.join(img_dir, "Direito.png")).convert()
            self.image = galho_img
             # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(galho_img, (100,100))
        
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

def load_assets(img_dir, fnt_dir):
    assets = {}
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    return assets       


        
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

# Carrega todos os assets uma vez só e guarda em um dicionário
assets = load_assets(img_dir, fnt_dir)

# Carrega a fonte para desenhar o score.
score_font = assets["score_font"]

# Cria as sprites. O construtor será chamado automaticamente.

player_arvore_1 = Lenhador(65)
player_arvore_2 = Lenhador(500)
tronco1 = Tronco(160)
tronco2 = Tronco(480)
vida_player_1 = Barra_de_vida(110)
vida_player_2 = Barra_de_vida(430)

# Cria um grupo para os galhos e player
galhos = pygame.sprite.Group()
players = pygame.sprite.Group()


# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player_arvore_1,player_arvore_2,tronco1,tronco2,vida_player_1,vida_player_2)


try:
    score_player1=0
    score_player2=0
    
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        TEMPO = pygame.time.get_ticks()

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get(): 
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
    
            # Verifica se a tecla foi apertado 
            if event.type == pygame.KEYDOWN:

                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    
                    player_arvore_2.image = pygame.image.load(path.join(img_dir,'posicao3.png')).convert()
                    player_arvore_2.image = pygame.transform.scale(player_arvore_2.image,(100, 120))
                    player_arvore_2.image.set_colorkey(BLACK)

                    galho = Galho(tronco2.rect.x)
                    all_sprites.add(galho)
                    galhos.add(galho)

                    player_arvore_2.rect.x = 350
                    galho.speedy = 1
                   

                if event.key == pygame.K_RIGHT:

                    player_arvore_2.image = pygame.image.load(path.join(img_dir,'posicao3-Invertido.png')).convert()
                    player_arvore_2.image = pygame.transform.scale(player_arvore_2.image,(100, 120))
                    player_arvore_2.image.set_colorkey(BLACK)

                    galho = Galho(tronco2.rect.x)
                    all_sprites.add(galho)
                    galhos.add(galho)

                    player_arvore_2.rect.x = 510
                    galho.speedy = 1  

                if event.key == pygame.K_a:
                    
                    player_arvore_1.image = pygame.image.load(path.join(img_dir,'posicao3.png')).convert()
                    player_arvore_1.image = pygame.transform.scale(player_arvore_1.image,(100, 120))
                    player_arvore_1.image.set_colorkey(BLACK)

                    galho = Galho(tronco1.rect.x)
                    all_sprites.add(galho)
                    galhos.add(galho)

                    player_arvore_1.rect.x = 30
                    galho.speedy = 1

                if event.key == pygame.K_d:

                    player_arvore_1.image = pygame.image.load(path.join(img_dir,'posicao3-Invertido.png')).convert()
                    player_arvore_1.image = pygame.transform.scale(player_arvore_1.image,(100, 120))
                    player_arvore_1.image.set_colorkey(BLACK)

                    galho = Galho(tronco1.rect.x)
                    all_sprites.add(galho)
                    galhos.add(galho)

                    player_arvore_1.rect.x= 190
                    galho.speedy = 1
            
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:

                    player_arvore_2.image = pygame.image.load(path.join(img_dir,'posicao1-Invertida.png')).convert()
                    player_arvore_2.image = pygame.transform.scale(player_arvore_2.image,(50, 100))
                    player_arvore_2.image.set_colorkey(BLACK)

                    player_arvore_2.speedx = 0
                    score_player2+=1

                if event.key == pygame.K_RIGHT:

                    player_arvore_2.image = pygame.image.load(path.join(img_dir,'posicao1.png')).convert()
                    player_arvore_2.image = pygame.transform.scale(player_arvore_2.image,(50, 100))
                    player_arvore_2.image.set_colorkey(BLACK)
                    
                    player_arvore_2.speedx = 0
                    score_player2+=1

                if event.key == pygame.K_a:

                    player_arvore_1.image = pygame.image.load(path.join(img_dir,'posicao1.png')).convert()
                    player_arvore_1.image = pygame.transform.scale(player_arvore_1.image,(50, 100))
                    player_arvore_1.image.set_colorkey(BLACK)

                    player_arvore_1.speedx = 0
                    score_player1+=1

                if event.key == pygame.K_d:

                    player_arvore_1.image = pygame.image.load(path.join(img_dir,'posicao1-Invertida.png')).convert()
                    player_arvore_1.image = pygame.transform.scale(player_arvore_1.image,(50, 100))
                    player_arvore_1.image.set_colorkey(BLACK)

                    player_arvore_1.speedx = 0
                    score_player1+=1
        
        

        # Atualiza a acao de cada sprite.
        all_sprites.update()

        # Verifica se houve colisão entre tiro e meteoro
        hits = pygame.sprite.spritecollide(player_arvore_1, galhos, False, pygame.sprite.collide_mask)
        if hits:
           player_arvore_1.kill()

        hits = pygame.sprite.spritecollide(player_arvore_2, galhos, False, pygame.sprite.collide_mask)
        if hits:
            player_arvore_2.kill()
        

         # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
       
        # Desenha o score
        text_surface_arvore1 = score_font.render("{:02d}".format(score_player1), True, YELLOW)
        text_surface_arvore2 = score_font.render("{:02d}".format(score_player2), True, YELLOW)
        text_rect1 = text_surface_arvore1.get_rect()
        text_rect2 = text_surface_arvore2.get_rect()
        text_rect1.midtop = (160,  10)
        text_rect2.midtop = (480,  10)
        screen.blit(text_surface_arvore1, text_rect1)
        screen.blit(text_surface_arvore2, text_rect2)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

finally:
    pygame.quit()
  
    