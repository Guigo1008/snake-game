from dqn_agent import DQNAgent
import pygame
import random
import math

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.largura, self.altura = 800, 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("AI_Snake")
        self.tamanho_celula = 20
        self.rodando = True
        self.jogo_comecou = False
        self.energia = 0
        self.reiniciar_jogo()
        
    def reiniciar_jogo(self):
        self.cobra = [[5, 5]]
        self.comida_pos = [random.randint(0, (self.largura // self.tamanho_celula) - 1), 
                           random.randint(0, (self.altura // self.tamanho_celula) - 1)]
        self.direcao = [1, 0]
        self.jogo_comecou = False
        self.energia = 0
        
    def calcular_recompensa(self, comida, movimento):
        recompensa_comer = comida * self.energia
        recompensa_movimento = movimento ** (math.exp(self.energia) / 10)
        recompensa_total = recompensa_comer + recompensa_movimento
        recompensa_normalizada = math.log(1 + recompensa_total)
        return recompensa_normalizada
    
    def calcular_punicao(self, punicao):
        punicao_normalizada = math.log(1 + punicao)
        return punicao_normalizada

    def run(self):
        while self.rodando:
            self.clock.tick(15)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        self.jogo_comecou = True  # Iniciar jogo com a tecla 's'
                        
            if self.jogo_comecou:
                nova_cabeca = [self.cobra[0][0] + self.direcao[0], self.cobra[0][1] + self.direcao[1]]
                self.cobra.insert(0, nova_cabeca)
                
                comida = 0
                movimento = 1
                
                if self.cobra[0] == self.comida_pos:
                    self.comida_pos = [random.randint(0, (self.largura // self.tamanho_celula) - 1), 
                                       random.randint(0, (self.altura // self.tamanho_celula) - 1)]
                    self.energia += 1
                    comida = self.energia
                else:
                    self.cobra.pop()
                
                recompensa = self.calcular_recompensa(comida, movimento)
                
                if self.cobra[0][0] < 0 or self.cobra[0][0] >= self.largura // self.tamanho_celula or                    self.cobra[0][1] < 0 or self.cobra[0][1] >= self.altura // self.tamanho_celula:
                    pygame.time.delay(1000)
                    punicao = self.calcular_punicao(5)  # Exemplo de valor de punição
                    self.reiniciar_jogo()
                    
                self.tela.fill((0, 0, 0))
                for pos in self.cobra:
                    pygame.draw.rect(self.tela, (0, 255, 0), 
                                     (pos[0] * self.tamanho_celula, pos[1] * self.tamanho_celula, 
                                      self.tamanho_celula, self.tamanho_celula))
                pygame.draw.rect(self.tela, (255, 0, 0), 
                                 (self.comida_pos[0] * self.tamanho_celula, self.comida_pos[1] * self.tamanho_celula, 
                                  self.tamanho_celula, self.tamanho_celula))
                pygame.display.flip()


    def reset(self):
        self.reiniciar_jogo()
        initial_state = self.get_state()  # You'll need to implement this method
        return initial_state

    def step(self, action):
        # Implement the logic to take an action based on the 'action' variable
        # Update the game state and calculate the reward
        new_state = self.get_state()  # You'll need to implement this method
        reward = self.calculate_reward()  # You'll need to implement this method
        done = self.game_over()  # You'll need to implement this method
        return new_state, reward, done
if __name__ == "__main__":
    jogo = SnakeGame()
    jogo.run()

