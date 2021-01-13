# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

hda1 = [
    {'nome': 'Corda de 15 metros', 'tipo': 'geral', 'peso': 15},
    {'nome': 'Frasco de óleo', 'tipo': 'geral', 'peso': 1},
    {'nome': 'Mochila de couro', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Tocha', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Traje de exploração', 'tipo': 'geral', 'peso': 2.5},
    {'nome': 'Vara de 3 metros', 'tipo': 'geral', 'peso': 0.5}
]

hda2 = [
    {'nome': 'Bandagem', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Corda de 15 metros', 'tipo': 'geral', 'peso': 15},
    {'nome': 'Luvas grossas', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Mochila de couro', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Perdeneira e isqueiro', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Pote para cozinhar', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Tocha', 'tipo': 'geral', 'peso': 0.5}
]

kits_hda = [hda1, hda2]

hda_armas = [
    {'nome': 'Arco curto, fecha de caça', 'peso': 0.5, 'tipo':
     'arma', 'categoria': 'distancia', 'iniciativa': 3, 'dano': '1d6',
     'alcance': '15/30/45' },
    {'nome': 'Espada curta', 'peso': 1.5, 'tipo': 'arma', 'categoria':
     'corpo-a-corpo', 'iniciativa': 7, 'dano': '1d6'},
    {'nome': 'Espada longa', 'peso': 2, 'tipo': 'arma', 'categoria':
     'corpo-a-corpo', 'iniciativa': 5, 'dano': '1d8'},
    {'nome': 'Machado', 'peso': 3.5, 'tipo': 'arma', 'categoria':
     'corpo-a-corpo', 'iniciativa': 3, 'dano': '1d8'},
    {'nome': 'Porrete', 'peso': 0.5, 'tipo': 'arma', 'categoria':
     'corpo-a-corpo', 'iniciativa': 6, 'dano': '1d6'}
]

hda_protecao = [
    {'nome': 'Armadura de couro', 'tipo': 'protecao', 'bonus': 2, 'peso': 10},
    {'nome': 'Escudo de madeira', 'tipo': 'protecao', 'bonus': 1, 'peso': 5}
]

clerigo1 = [
    {'nome': 'Bandagem', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Pote para cozinhar', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Mochila de couro', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Perdeneira e isqueiro', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Tocha', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Tinta (vidro 30ml)', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Água benta', 'tipo': 'geral', 'peso': 0.3},
    {'nome': 'Vestimentas de clérigo', 'tipo': 'geral', 'peso': 3},
    {'nome': 'Velas', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1}
]

clerigo2 = [
    {'nome': 'Mochila de couro', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1},
    {'nome': 'Pergaminhos', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Pena de aço', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Água benta', 'tipo': 'geral', 'peso': 0.3},
    {'nome': 'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Tinta (vidro 30ml)', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Simbolo divino', 'tipo': 'geral', 'peso': 0.5}
]

kits_clerigo = [clerigo1, clerigo2]

clerigo_armas = [
    {'nome': 'Maça', 'peso': 5, 'iniciativa': 3, 'tipo': 'arma', 'dano': '1d8',
     'categoria': 'corpo-a-corpo'},
    {'nome': 'Martelo', 'peso': 3, 'iniciativa': 6, 'tipo': 'arma', 'dano':
     '1d6',
     'categoria': 'corpo-a-corpo', 'alcance': '3/6/9'},
    {'nome': 'Porrete', 'peso': 0.5, 'iniciativa': 6, 'tipo': 'arma', 'dano':
     '1d6',
     'categoria': 'corpo-a-corpo'},
    {'nome': 'Funda', 'peso': 0, 'iniciativa': 4, 'tipo': 'arma', 'dano':
     '1d3',
     'categoria': 'distancia', 'alcance': '10/20/30'}
]

clerigo_protecao = [
    {'nome': 'Armadura de couro', 'tipo': 'protecao', 'bonus': 2, 'peso': 10},
    {'nome': 'Escudo de madeira', 'tipo': 'protecao', 'bonus': 1, 'peso': 5}
]

ladrao1 = [
    {'nome': 'Mochila de lona', 'tipo': 'geral', 'peso': 1.5},
    {'nome': 'Corda de 15 metros', 'tipo': 'geral', 'peso': 15},
    {'nome': 'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Velas', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Perdeneira e isqueiro', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Luvas', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Ferramentas de ladrão', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Gancho para escalada', 'tipo': 'geral', 'peso': 1.5},
    {'nome': 'Lente de aumento', 'tipo': 'geral', 'peso': 0.3}
]

ladrao2 = [
    {'nome': 'Mochila de lona', 'tipo': 'geral', 'peso': 1.5},
    {'nome': 'Corda de seda', 'tipo': 'geral', 'peso': 6},
    {'nome': 'Bolsa para cinto', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Ferramentas de ladrão', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1},
    {'nome': 'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Traje de exploração', 'tipo': 'geral', 'peso': 2.5}
]

kits_ladrao = [ladrao1, ladrao2]

ladrao_armas = [
    {'nome': 'Besta', 'peso': 3.5, 'iniciativa': 3, 'tipo': 'arma', 'dano':
     '1d6',
     'categoria': 'distancia', 'alcance': '20/40/60'},
    {'nome': 'Espada curta', 'peso': 1.5, 'iniciativa': 7, 'tipo': 'arma',
     'categoria': 'corpo-a-corpo', 'dano': '1d6'},
    {'nome': 'Adaga', 'peso': 0.5, 'iniciativa': 8, 'tipo': 'arma',
     'categoria': 'corpo-a-corpo', 'dano': '1d4', 'alcance': '3/6/9'}
]

ladrao_protecao = [
    {'nome': 'Armadura de couro', 'tipo': 'protecao', 'bonus': 2, 'peso': 10}
]

mago1 = [
    {'nome': 'Velas', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Mochila de lona', 'tipo': 'geral', 'peso': 1.5},
    {'nome': 'Saco de couro grande', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Tinta (vidro 30ml)', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Traje de mago', 'tipo': 'geral', 'peso': 1.5},
    {'nome': 'Pena de aço', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1},
    {'nome': 'Pergaminhos', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Grimório', 'tipo': 'geral', 'peso': 3}
]

mago2 = [
    {'nome': 'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1},
    {'nome': 'Pergaminhos', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Grimório', 'tipo': 'geral', 'peso': 3},
    {'nome': 'Mochila de lona', 'tipo': 'geral', 'peso': 1.5},
    {'nome': 'Perdeneira e isqueiro', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': 'Tocha', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Frasco 150ml vazio', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Frasco 250ml vazio', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Frasco 500ml vazio', 'tipo': 'geral', 'peso': 0.5},
    {'nome': 'Tinta (vidro 30ml)', 'tipo': 'geral', 'peso': 0},
    {'nome': 'Incenso exótico', 'tipo': 'geral', 'peso': 0}
]

kits_mago = [mago1, mago2]

mago_armas = [
    {'nome': 'Espada curta', 'peso': 1.5, 'iniciativa': 7, 'tipo': 'arma',
     'dano': '1d6', 'categoria': 'corpo-a-corpo'},
    {'nome': 'Adaga', 'peso': 0.5, 'iniciativa': 8, 'tipo': 'arma', 'dano':
     '1d4',
     'categoria': 'corpo-a-corpo', 'alcance': '3/6/9'},
    {'nome': 'Funda', 'peso': 0, 'iniciativa': 4, 'tipo': 'arma', 'dano':
     '1d3',
     'categoria': 'distancia', 'alcance': '10/20/30'},
    {'nome': 'Cajado', 'peso': 1.5, 'iniciativa': 7, 'tipo': 'arma', 'dano':
     '1d4', 'categoria': 'corpo-a-corpo'}
]
