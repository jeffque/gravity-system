def delta_coord(base, outro):
    'Distância vetorial entre dois pontos'
    return [outro[0] - base[0], outro[1] - base[1], outro[2] - base[2]]


def modulo_quad_vetor(vetor):
    return vetor[0]**2 + vetor[1]**2 + vetor[2]**2


def valor_negado(vetor):
    return [-vetor[0],-vetor[1],-vetor[2]]


def soma_coord(base, outro):
    'Soma de dois vetores'
    return [base[0] + outro[0], base[1] + outro[1], base[2] + outro[2]]


def vetor_ponderado(vet1, peso1, vet2, peso2):
    peso_pond_1 = [peso1 * ord for ord in vet1]
    peso_pond_2 = [peso2 * ord for ord in vet2]
    novo_peso = peso1 + peso2
    return [ord / novo_peso for ord in soma_coord(peso_pond_1, peso_pond_2)]


def norm_to_int(vetor):
    return [int(ordenada) for ordenada in vetor]
