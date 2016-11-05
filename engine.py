import os, sys
import pygame
import random
from pygame.locals import *
from physics import forca_gravidade
from elemento_fisico import ElementoFisico
from geometry import soma_coord, valor_negado, modulo_quad_vetor, delta_coord

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

class UniverseEngine:
    width = 800
    height = 600


    def __init__(self):
        self.width = UniverseEngine.width
        self.height = UniverseEngine.height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.elementos = []


    def sistema(self):
        self.elementos.clear()
        for x in range(0, 50):
            factor_rand = random.uniform(0.01, 7)
            factor_x = random.uniform(x / 20 - factor_rand - 13, 13 + x / 20 * factor_rand)
            factor_y = random.uniform(x / 20 - factor_rand - 13, 13 + x / 20 * factor_rand)
            posicao = (160 + 5 * x + random.uniform(-1, 1) * factor_x, 240 + random.uniform(-3, 3) * factor_y, 0)
            massa = random.uniform(500, 1000)
            #velocidade = (factor_x, factor_y, 0)
            velocidade = (random.uniform(-10, 10), random.uniform(-20, 20), 0)
            asteroide = ElementoFisico(posicao=posicao, size=2, color=(133, 90, 133), velocidade=velocidade, massa=massa)
            self.elementos.append(asteroide)

    def sistema_teste_terra(self):
        self.elementos.clear()
        terra = ElementoFisico(posicao=(600, 300, 0), size=3, color=(0, 255, 0), velocidade=(0, -40, 0), massa=1)
        lua = ElementoFisico(posicao=(590, 290, 0), size=2, color=(120, 255, 120), velocidade=(2, -40, 0), massa=0.012)
        jupiter = ElementoFisico(posicao=(100, 300, 0), size=6, color=(255, 0, 200), velocidade=(0, 35, 0), massa=317)
        lua_jupiter = ElementoFisico(posicao=(80, 290, 0), size=2, color=(120, 255, 120), velocidade=(2, 42, 0), massa=0.012)
        saturno = ElementoFisico(posicao=(700, 300, 0), size=6, color=(200, 200, 120), velocidade=(0, -35, 0), massa=95)
        netuno = ElementoFisico(posicao=(750, 300, 0), size=5, color=(0, 35, 255), velocidade=(0, -35, 0), massa=17)
        sol = ElementoFisico(posicao=(400, 300, 0), size=10, color=(255, 255, 0), velocidade=(0, 0, 0), massa=317*1047)
        self.elementos.append(terra)
        self.elementos.append(lua)
        self.elementos.append(lua_jupiter)
        self.elementos.append(jupiter)
        self.elementos.append(saturno)
        self.elementos.append(netuno)
        self.elementos.append(sol)
        for x in range(0, 20):
            factor_rand = random.uniform(0.01, 7)
            factor_x = random.uniform(x / 20 - factor_rand - 13, 13 + x / 20 * factor_rand)
            factor_y = random.uniform(x / 20 - factor_rand - 13, 13 + x / 20 * factor_rand)
            posicao = (20 + 5 * x + random.uniform(-1, 1) * factor_x, 240 + random.uniform(-3, 3) * factor_y, 0)
            massa = random.uniform(0.1, 0.3)
            velocidade = (0, 42, 0)
            asteroide = ElementoFisico(posicao=posicao, size=2, color=(133, 90, 133), velocidade=velocidade, massa=massa)
            self.elementos.append(asteroide)


    def sistema_test(self):
        self.elementos.clear()

        estrela1 = ElementoFisico(posicao=(460, 400, 0), size=6, color=(255, 255, 0), velocidade=(9, -9, 0), massa=1000)
        estrela2 = ElementoFisico(posicao=(340, 200, 0), size=6, color=(255, 0, 0), velocidade=(-9, 9, 0), massa=1000)
        self.elementos.append(estrela1)
        self.elementos.append(estrela2)

        planeta1 = ElementoFisico(posicao=(250, 150, 0), size=3, color=(0, 255, 0), velocidade=(-70, 80, 0), massa=100)
        planeta2 = ElementoFisico(posicao=(550, 450, 0), size=3, color=(0, 255, 0), velocidade=(70, -80, 0), massa=100)
        self.elementos.append(planeta1)
        self.elementos.append(planeta2)

        planeta1 = ElementoFisico(posicao=(100, 100, 0), size=3, color=(120, 255, 120), velocidade=(-17, 50, 0), massa=80)
        planeta2 = ElementoFisico(posicao=(700, 500, 0), size=3, color=(120, 255, 120), velocidade=(17, -50, 0), massa=80)
        self.elementos.append(planeta1)
        self.elementos.append(planeta2)

        planeta1 = ElementoFisico(posicao=(120, 70, 0), size=2, color=(120, 120, 120), velocidade=(10, -5, 0),
                                  massa=3)
        planeta2 = ElementoFisico(posicao=(680, 530, 0), size=2, color=(120, 120, 120), velocidade=(-10, 5, 0),
                                  massa=3)
        self.elementos.append(planeta1)
        self.elementos.append(planeta2)
        """
        for x in range(20, 50):
            factor_rand = random.uniform(0.01,7)
            factor_x = random.uniform(x/20 -factor_rand - 13, 13 + x/20 * factor_rand)
            factor_y = random.uniform(x/20 -factor_rand - 13, 13 + x/20 * factor_rand)
            posicao = (200 + 5 * x + random.uniform(-1, 1) * factor_x, 240 + random.uniform(-3, 3) * factor_y, 0)
            massa = 1 + random.uniform(-0.5, 3)
            velocidade = (random.uniform(-10, 10) * factor_x + 10, random.uniform(-6, 6) * factor_y + random.uniform(-6, 6), 0)
            asteroide = ElementoFisico(posicao=posicao, size=2, color=(133, 90, 133), velocidade=velocidade, massa=massa)
            self.elementos.append(asteroide)
        """


    def main_loop(self):
        tique_taque = pygame.time.Clock()
        acc = 0
        destruir = []
        acrescer = []
        while True:
            destruir.clear()
            acrescer.clear()
            self.screen.fill((0,0,0))
            delta_seconds = (tique_taque.get_time()) / 1000
            acc += delta_seconds
            tique_taque.tick(600)

            forca_resultante = [(0,0,0) for i in self.elementos]

            # cálculo de forças/colisões
            for i in range(0, len(self.elementos) - 1):
                for j in range(i + 1, len(self.elementos)):
                    el_i = self.elementos[i]
                    el_j = self.elementos[j]
                    f = forca_gravidade(el_i, el_j)
                    forca_resultante[i] = soma_coord(forca_resultante[i], f)
                    forca_resultante[j] = soma_coord(forca_resultante[j], valor_negado(f))
                    if modulo_quad_vetor(delta_coord(el_i.posicao, el_j.posicao)) <= (el_i.size + el_j.size)**2:
                        mergeado = el_i.merged(el_j)
                        el_i.destino = mergeado
                        el_j.destino = mergeado

            # acelerar/mover/renderizar
            for i in range(0, len(self.elementos)):
                el = self.elementos[i]
                f = forca_resultante[i]
                el.aplica_forca(f, delta_seconds)
                el.move(delta_seconds)
                el.render(self.screen, self.width, self.height)
                if el.destino:
                    destruir.append(el)
                    if not el.destino_final() in acrescer:
                        acrescer.append(el.destino_final())
                quad_dist2center = modulo_quad_vetor(delta_coord(el.posicao, [UniverseEngine.width/2, UniverseEngine.height/2, 0]))

                if quad_dist2center >= ((UniverseEngine.width + UniverseEngine.height) * 4)**2:
                    destruir.append(el)

            # elementos novos e os mergeados colocados no mapa
            for destruto in destruir:
                try:
                    self.elementos.remove(destruto)
                except:
                    pass
            for somado in acrescer:
                self.elementos.append(somado)

            if len(self.elementos) == 1:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.update()


if __name__ == '__main__':
    import profile
    universo = UniverseEngine()
    profile.run('universo.sistema()')
    profile.run('universo.main_loop()')
    sys.exit()