from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
fnt_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo.
WIDTH = 960
HEIGHT = 540
FPS = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2


