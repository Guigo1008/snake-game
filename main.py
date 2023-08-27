import pygame
import random

def tela_inicial():
    if botao_start.collidepoint(pygame.mouse.get_pos()):
        cor_atual_botao = cor_botao_hover
    else:
        cor_atual_botao = cor_botao

    tela.fill(cor_fundo)
    pygame.draw.rect(tela, cor_botao, botao_start)
    tela.blit(texto_botao, (botao_start.x + (botao_start.width - texto_largura) // 2, botao_start.y + (botao_start.height - texto_altura) // 2))
    tela.blit(imagem_titulo, ((largura - imagem_titulo.get_width()) // 2, altura / 2 - 150))  
    pygame.display.flip()

def tela_jogo():
    tela.fill(cor_fundo)
    for pos in cobra:
        pygame.draw.rect(tela, cor_cobra, (pos[0] * tamanho_celula, pos[1] * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.draw.rect(tela, cor_comida, (comida_pos[0] * tamanho_celula, comida_pos[1] * tamanho_celula, tamanho_celula, tamanho_celula))
    pygame.display.flip()

def reiniciar_jogo():
    global cobra, comida_pos, direcao, jogo_comecou
    cobra = [[5, 5]]
    comida_pos = [random.randint(0, (largura // tamanho_celula) - 1), random.randint(0, (altura // tamanho_celula) - 1)]
    direcao = [1, 0]
    jogo_comecou = False
    tela_inicial()

pygame.init()

imagem_titulo = pygame.image.load('titulo.png')
clock = pygame.time.Clock()

cor_fundo = (0x1e, 0x16, 0x47)
cor_botao = (0xFF, 0xFF, 0x00)
cor_botao_hover = (0xFF, 0xAA, 0x00)
cor_cobra = (0x61, 0x4a, 0xd3)
cor_comida = (0xFF, 0xFF, 0xFF)
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("for_snake")

botao_start = pygame.Rect(289, altura / 2, 200, 80)
fonte_botao = pygame.font.SysFont("Arial", 48)
texto_botao = fonte_botao.render('START', True, (20, 20, 20))
texto_largura, texto_altura = texto_botao.get_size()

fonte_titulo = pygame.font.SysFont("Arial", 50)
texto_titulo = fonte_titulo.render("for_snake", True, (255, 255, 255))
titulo_largura, _ = texto_titulo.get_size()

tamanho_celula = 20
cobra = [[5, 5]]
comida_pos = [random.randint(0, (largura // tamanho_celula) - 1), random.randint(0, (altura // tamanho_celula) - 1)]
direcao = [1, 0]

rodando = True
jogo_comecou = False
tela_inicial()

while rodando:
    clock.tick(300)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN and botao_start.collidepoint(pygame.mouse.get_pos()) and not jogo_comecou:
            jogo_comecou = True
        if evento.type == pygame.KEYDOWN and jogo_comecou:
            if evento.key == pygame.K_UP:
                direcao = [0, -1]
            elif evento.key == pygame.K_DOWN:
                direcao = [0, 1]
            elif evento.key == pygame.K_LEFT:
                direcao = [-1, 0]
            elif evento.key == pygame.K_RIGHT:
                direcao = [1, 0]
    pygame.time.delay(85)
    if jogo_comecou:
        tela_jogo()
        nova_cabeca = [cobra[0][0] + direcao[0], cobra[0][1] + direcao[1]]
        cobra.insert(0, nova_cabeca)
        if cobra[0] == comida_pos:
            comida_pos = [random.randint(0, (largura // tamanho_celula) - 1), random.randint(0, (altura // tamanho_celula) - 1)]
        else:
            cobra.pop()
        if cobra[0][0] < 0 or cobra[0][0] >= largura // tamanho_celula or cobra[0][1] < 0 or cobra[0][1] >= altura // tamanho_celula:
            pygame.time.delay(1000)
            reiniciar_jogo()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.MOUSEBUTTONDOWN and botao_start.collidepoint(pygame.mouse.get_pos()) and not jogo_comecou:
            jogo_comecou = True
        if evento.type == pygame.KEYDOWN and jogo_comecou:
            if evento.key == pygame.K_UP:
                direcao = [0, -1]
            elif evento.key == pygame.K_DOWN:
                direcao = [0, 1]
            elif evento.key == pygame.K_LEFT:
                direcao = [-1, 0]
            elif evento.key == pygame.K_RIGHT:
                direcao = [1, 0]

pygame.quit()
