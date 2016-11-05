from geometry import *
import elemento_fisico
G_CTE = 2

def forca_gravidade(el1, el2):
    coords_dist = delta_coord(el1.posicao, el2.posicao)
    modulo = modulo_quad_vetor(coords_dist)**(3/2)
    modulo_reverso = 1/modulo if abs(modulo) > 0.001 else 0
    fator = G_CTE * el1.massa * el2.massa * modulo_reverso
    return [coords_dist[0] * fator, coords_dist[1] * fator, coords_dist[2] * fator]
