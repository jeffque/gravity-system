import pygame
from  geometry import soma_coord, vetor_ponderado, norm_to_int

class ElementoFisico:
    def __init__(self, posicao, velocidade, massa=1, size=30, color=(255,255,255)):
        self.posicao = [ordenada for ordenada in posicao]
        self.size = size
        self.color = color
        self.velocidade = [ordenada for ordenada in velocidade]
        self.massa = massa
        self.norm_color = norm_to_int(self.color)
        self.norm_size = int(self.size)
        self.destino = None
        self.size2 = size * 2


    def destino_final(self):
        if self.destino:
            return self.destino.destino_final()
        else:
            return self


    def render(self, screen, width, height):
        if self.posicao[0] + self.size2 < 0:
            return
        if self.posicao[1] + self.size2 < 0:
            return
        if self.posicao[0] - self.size2 > width:
            return
        if self.posicao[1] - self.size2 > height:
            return
        draw_pos = [int(self.posicao[0]), int(self.posicao[1])]
        pygame.draw.circle(screen, self.norm_color, draw_pos, self.norm_size)


    def aplica_forca(self, forca, tempo):
        self.velocidade = soma_coord(self.velocidade, [forca_ord*tempo/self.massa for forca_ord in forca])


    def move(self, tempo):
        self.posicao = soma_coord(self.posicao, [velocidade_ord * tempo for velocidade_ord in self.velocidade])


    def merged(self, another):
        return self.destino_final().merged_basico(another.destino_final())


    def merged_basico(self, another):
        nova_massa = self.massa + another.massa
        nova_cor = vetor_ponderado(self.color, self.massa, another.color, another.massa)
        nova_posicao = vetor_ponderado(self.posicao, self.massa, another.posicao, another.massa)
        nova_velocidade = vetor_ponderado(self.velocidade, self.massa, another.velocidade, another.massa)
        density_self = self.massa / self.size**3
        density_another = another.massa / another.size ** 3
        density_nova = density_self if density_self > density_another else density_another
        novo_tamanho = (nova_massa/density_nova)**0.34
        if novo_tamanho > 50:
            novo_tamanho = 50
        return ElementoFisico(nova_posicao, nova_velocidade, nova_massa, novo_tamanho, nova_cor)
