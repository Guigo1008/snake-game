
import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.imagem_titulo = pygame.image.load('titulo.png')
        self.clock = pygame.time.Clock()
        
        self.cor_fundo = (0x1e, 0x16, 0x47)
        self.cor_botao = (0xFF, 0xFF, 0x00)
        self.cor_cobra = (0x61, 0x4a, 0xd3)
        self.cor_comida = (0xFF, 0xFF, 0xFF)
        
        self.largura, self.altura = 800, 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("for_snake")
        
        self.botao_start = pygame.Rect(289, self.altura / 2, 200, 80)
        self.fonte_botao = pygame.font.SysFont("Arial", 48)
        self.texto_botao = self.fonte_botao.render('START', True, (20, 20, 20))
        self.texto_largura, self.texto_altura = self.texto_botao.get_size()
        
        self.fonte_titulo = pygame.font.SysFont("Arial", 50)
        
        self.tamanho_celula = 20
        self.cobra = [[5, 5]]
        self.comida_pos = [random.randint(0, (self.largura // self.tamanho_celula) - 1), random.randint(0, (self.altura // self.tamanho_celula) - 1)]
        self.direcao = [1, 0]
        
        self.rodando = True
        self.jogo_comecou = False
        
        self.reiniciar_jogo()
        self.tela_inicial()

    def reiniciar_jogo(self):
        self.cobra = [[5, 5]]
        self.comida_pos = [random.randint(0, (self.largura // self.tamanho_celula) - 1), random.randint(0, (self.altura // self.tamanho_celula) - 1)]
        self.direcao = [1, 0]
        self.jogo_comecou = False
        self.tela_inicial()

    def tela_inicial(self):
        self.tela.fill(self.cor_fundo)
        pygame.draw.rect(self.tela, self.cor_botao, self.botao_start)
        self.tela.blit(self.texto_botao, (self.botao_start.x + (self.botao_start.width - self.texto_largura) // 2, self.botao_start.y + (self.botao_start.height - self.texto_altura) // 2))
        self.tela.blit(self.imagem_titulo, ((self.largura - self.imagem_titulo.get_width()) // 2, self.altura / 2 - 150))  
        pygame.display.flip()

    def tela_jogo(self):
        self.tela.fill(self.cor_fundo)
        for pos in self.cobra:
            pygame.draw.rect(self.tela, self.cor_cobra, (pos[0] * self.tamanho_celula, pos[1] * self.tamanho_celula, self.tamanho_celula, self.tamanho_celula))
        pygame.draw.rect(self.tela, self.cor_comida, (self.comida_pos[0] * self.tamanho_celula, self.comida_pos[1] * self.tamanho_celula, self.tamanho_celula, self.tamanho_celula))
        pygame.display.flip()


    def run(self):
        while self.rodando:
            self.clock.tick(15)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                if evento.type == pygame.MOUSEBUTTONDOWN and self.botao_start.collidepoint(pygame.mouse.get_pos()) and not self.jogo_comecou:
                    self.jogo_comecou = True
                if evento.type == pygame.KEYDOWN and self.jogo_comecou:
                    if (evento.key == pygame.K_UP) and (self.direcao != [0, 1]):
                        self.direcao = [0, -1]
                    elif (evento.key == pygame.K_DOWN) and (self.direcao != [0, -1]):
                        self.direcao = [0, 1]
                    elif (evento.key == pygame.K_LEFT) and (self.direcao != [1, 0]):
                        self.direcao = [-1, 0]
                    elif (evento.key == pygame.K_RIGHT) and (self.direcao != [-1, 0]):
                        self.direcao = [1, 0]
                        
            if self.jogo_comecou:
                self.tela_jogo()
                nova_cabeca = [self.cobra[0][0] + self.direcao[0], self.cobra[0][1] + self.direcao[1]]
                self.cobra.insert(0, nova_cabeca)
                
                # Adicionando lógica de colisão da cobra com ela mesma
                if self.cobra[0] in self.cobra[1:]:
                    pygame.time.delay(1000)
                    self.reiniciar_jogo()
                    continue
                
                if self.cobra[0] == self.comida_pos:
                    self.comida_pos = [random.randint(0, (self.largura // self.tamanho_celula) - 1), random.randint(0, (self.altura // self.tamanho_celula) - 1)]
                else:
                    self.cobra.pop()
                if self.cobra[0][0] < 0 or self.cobra[0][0] >= self.largura // self.tamanho_celula or self.cobra[0][1] < 0 or self.cobra[0][1] >= self.altura // self.tamanho_celula:
                    pygame.time.delay(1000)
                    self.reiniciar_jogo()

        while self.rodando:
            self.clock.tick(15)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                if evento.type == pygame.MOUSEBUTTONDOWN and self.botao_start.collidepoint(pygame.mouse.get_pos()) and not self.jogo_comecou:
                    self.jogo_comecou = True
                if evento.type == pygame.KEYDOWN and self.jogo_comecou:
                    if (evento.key == pygame.K_UP) and (self.direcao != [0, 1]):
                        self.direcao = [0, -1]
                    elif (evento.key == pygame.K_DOWN) and (self.direcao != [0, -1]):
                        self.direcao = [0, 1]
                    elif (evento.key == pygame.K_LEFT) and (self.direcao != [1, 0]):
                        self.direcao = [-1, 0]
                    elif (evento.key == pygame.K_RIGHT) and (self.direcao != [-1, 0]):
                        self.direcao = [1, 0]
                        
            if self.jogo_comecou:
                self.tela_jogo()
                nova_cabeca = [self.cobra[0][0] + self.direcao[0], self.cobra[0][1] + self.direcao[1]]
                self.cobra.insert(0, nova_cabeca)
                if self.cobra[0] == self.comida_pos:
                    self.comida_pos = [random.randint(0, (self.largura // self.tamanho_celula) - 1), random.randint(0, (self.altura // self.tamanho_celula) - 1)]
                else:
                    self.cobra.pop()
                if self.cobra[0][0] < 0 or self.cobra[0][0] >= self.largura // self.tamanho_celula or self.cobra[0][1] < 0 or self.cobra[0][1] >= self.altura // self.tamanho_celula:
                    pygame.time.delay(1000)
                    self.reiniciar_jogo()

if __name__ == "__main__":
    jogo = SnakeGame()
    jogo.run()
