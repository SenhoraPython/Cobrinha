import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura_tela = 640
altura_tela = 480

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('COBRINHA')

pos_mac_x = randint(0, largura_tela - 20)
pos_mac_y = randint(0, altura_tela - 20)

pos_cobra_y = 0
pos_cobra_x = 0

clock = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 20)
pontos = 0
lista_cobra = []
comprimento_cobra = 10

x_controle = 0
y_controle = 0

estado_jogo = "gamePlay"

def aumentar_cobra(lista_cobra):
    for x_e_y in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (x_e_y[0], x_e_y[1], 20, 20))

def reiniciar_jogo():
    global pos_cobra_x, pos_cobra_y, pontos, lista_cobra, estado_jogo, comprimento_cobra
    pos_cobra_x = 0
    pos_cobra_y = 0
    pontos = 0

    lista_cobra = []
    comprimento_cobra = 10
    estado_jogo = "gamePlay"

def game_over():
    tela.fill((255, 255, 255))
    mensagem = f'Game Over, pressione R para reiniciar'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    tela.blit(texto_formatado, (120, 240))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:

            if event.key == K_r:
                reiniciar_jogo()

            if event.key == K_w:
                x_controle = 0
                y_controle = -5
            if event.key == K_s:
                x_controle = 0
                y_controle = 5
            if event.key == K_d:
                x_controle = 5
                y_controle = 0
            if event.key == K_a:
                x_controle = -5
                y_controle = 0

            

   
    clock.tick(40)

    if estado_jogo == "gamePlay":
        tela.fill((255, 255, 255))

        maca = pygame.draw.rect(tela, (255, 0, 0), (pos_mac_x, pos_mac_y, 20, 20))
        cobra = pygame.draw.rect(tela, (0, 255, 0), (pos_cobra_x, pos_cobra_y, 20, 20))

        mensagem = f'Pontos:{pontos}'
        texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
        tela.blit(texto_formatado, (550, 10))

        if maca.colliderect(cobra):
            pos_mac_x = randint(0, 625)
            pos_mac_y = randint(0, 465)
            pontos += 1
            comprimento_cobra += 5

        pos_cobra_x += x_controle
        pos_cobra_y += y_controle

        lista_cabeca = [pos_cobra_x, pos_cobra_y]
        lista_cobra.append(lista_cabeca)

        aumentar_cobra(lista_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        if pos_cobra_x < 0:
            pos_cobra_x = largura_tela - 20
        elif pos_cobra_x > largura_tela - 20:
            pos_cobra_x = 0

        if pos_cobra_y < 0:
            pos_cobra_y = altura_tela - 20
        elif pos_cobra_y > altura_tela - 20:
            pos_cobra_y = 0

        if lista_cobra.count(lista_cabeca) > 1 and pos_cobra_x > 1:
            estado_jogo = "gameOver"

    if estado_jogo == "gameOver":
        game_over()


    pygame.display.update()
