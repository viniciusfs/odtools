# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

hda1 = [
    {'nome': u'Corda de 15 metros', 'tipo': 'geral', 'peso': 15},
    {'nome': u'Frasco de óleo', 'tipo': 'geral', 'peso': 1},
    {'nome': u'Mochila de couro', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Tocha', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Traje de exploração', 'tipo': 'geral', 'peso': 2.5},
    {'nome': u'Vara de 3 metros', 'tipo': 'geral', 'peso': 0.5}
]

hda2 = [
    {'nome': u'Bandagem', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Corda de 15 metros', 'tipo': 'geral', 'peso': 15},
    {'nome': u'Luvas grossas', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Mochila de couro', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Perdeneira e isqueiro', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Pote para cozinhar', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Tocha', 'tipo': 'geral', 'peso': 0.5}
]

kits_hda = [hda1, hda2]

hda_armas = [
    {'nome': u'Arco curto, fecha de caça', 'peso': 0.5, 'tipo':
     'arma', 'categoria': 'distancia', 'iniciativa': 3, 'dano': '1d6',
     'alcance': '15/30/45' },
    {'nome': u'Espada curta', 'peso': 1.5, 'tipo': 'arma', 'categoria':
     'corpo-a-corpo', 'iniciativa': 7, 'dano': '1d6'},
    {'nome': u'Espada longa', 'peso': 2, 'tipo': 'arma', 'categoria':
     'corpo-a-corpo', 'iniciativa': 5, 'dano': '1d8'},
    {'nome': u'Machado', 'peso': 3.5, 'tipo': 'arma', 'categoria':
     'corpo-a-corpo', 'iniciativa': 3, 'dano': '1d8'},
    {'nome': u'Porrete', 'peso': 0.5, 'tipo': 'arma', 'categoria':
     'corpo-a-corpo', 'iniciativa': 6, 'dano': '1d6'}
]

hda_protecao = [
    {'nome': u'Armadura de couro', 'tipo': 'protecao', 'bonus': 2, 'peso': 10},
    {'nome': u'Escudo de madeira', 'tipo': 'protecao', 'bonus': 1, 'peso': 5}
]

clerigo1 = [
    {'nome': u'Bandagem', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Pote para cozinhar', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Mochila de couro', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Perdeneira e isqueiro', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Tocha', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Tinta (vidro 30ml)', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Água benta', 'tipo': 'geral', 'peso': 0.3},
    {'nome': u'Vestimentas de clérigo', 'tipo': 'geral', 'peso': 3},
    {'nome': u'Velas', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1}
]

clerigo2 = [
    {'nome': u'Mochila de couro', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1},
    {'nome': u'Pergaminhos', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Pena de aço', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Água benta', 'tipo': 'geral', 'peso': 0.3},
    {'nome': u'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Tinta (vidro 30ml)', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Simbolo divino', 'tipo': 'geral', 'peso': 0.5}
]

kits_clerigo = [clerigo1, clerigo2]

clerigo_armas = [
    {'nome': u'Maça', 'peso': 5, 'iniciativa': 3, 'tipo': 'arma', 'dano': '1d8',
     'categoria': 'corpo-a-corpo'},
    {'nome': u'Martelo', 'peso': 3, 'iniciativa': 6, 'tipo': 'arma', 'dano':
     '1d6',
     'categoria': 'corpo-a-corpo', 'alcance': '3/6/9'},
    {'nome': u'Porrete', 'peso': 0.5, 'iniciativa': 6, 'tipo': 'arma', 'dano':
     '1d6',
     'categoria': 'corpo-a-corpo'},
    {'nome': u'Funda', 'peso': 0, 'iniciativa': 4, 'tipo': 'arma', 'dano':
     '1d3',
     'categoria': 'distancia', 'alcance': '10/20/30'}
]

clerigo_protecao = [
    {'nome': u'Armadura de couro', 'tipo': 'protecao', 'bonus': 2, 'peso': 10},
    {'nome': u'Escudo de madeira', 'tipo': 'protecao', 'bonus': 1, 'peso': 5}
]

ladrao1 = [
    {'nome': u'Mochila de lona', 'tipo': 'geral', 'peso': 1.5},
    {'nome': u'Corda de 15 metros', 'tipo': 'geral', 'peso': 15},
    {'nome': u'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Velas', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Perdeneira e isqueiro', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Luvas', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Ferramentas de ladrão', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Gancho para escalada', 'tipo': 'geral', 'peso': 1.5},
    {'nome': u'Lente de aumento', 'tipo': 'geral', 'peso': 0.3}
]

ladrao2 = [
    {'nome': u'Mochila de lona', 'tipo': 'geral', 'peso': 1.5},
    {'nome': u'Corda de seda', 'tipo': 'geral', 'peso': 6},
    {'nome': u'Bolsa para cinto', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Ferramentas de ladrão', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1},
    {'nome': u'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Traje de exploração', 'tipo': 'geral', 'peso': 2.5}
]

kits_ladrao = [ladrao1, ladrao2]

ladrao_armas = [
    {'nome': u'Besta', 'peso': 3.5, 'iniciativa': 3, 'tipo': 'arma', 'dano':
     '1d6',
     'categoria': 'distancia', 'alcance': '20/40/60'},
    {'nome': u'Espada curta', 'peso': 1.5, 'iniciativa': 7, 'tipo': 'arma',
     'categoria': 'corpo-a-corpo', 'dano': '1d6'},
    {'nome': u'Adaga', 'peso': 0.5, 'iniciativa': 8, 'tipo': 'arma',
     'categoria': 'corpo-a-corpo', 'dano': '1d4', 'alcance': '3/6/9'}
]

ladrao_protecao = [
    {'nome': u'Armadura de couro', 'tipo': 'protecao', 'bonus': 2, 'peso': 10}
]

mago1 = [
    {'nome': u'Velas', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Mochila de lona', 'tipo': 'geral', 'peso': 1.5},
    {'nome': u'Saco de couro grande', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Tinta (vidro 30ml)', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Traje de mago', 'tipo': 'geral', 'peso': 1.5},
    {'nome': u'Pena de aço', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1},
    {'nome': u'Pergaminhos', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Grimório', 'tipo': 'geral', 'peso': 3}
]

mago2 = [
    {'nome': u'Canudo para pergaminhos', 'tipo': 'geral', 'peso': 0.1},
    {'nome': u'Pergaminhos', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Grimório', 'tipo': 'geral', 'peso': 3},
    {'nome': u'Mochila de lona', 'tipo': 'geral', 'peso': 1.5},
    {'nome': u'Perdeneira e isqueiro', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Ração para viagem', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Saco de dormir', 'tipo': 'geral', 'peso': 2},
    {'nome': u'Tocha', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Frasco 150ml vazio', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Frasco 250ml vazio', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Frasco 500ml vazio', 'tipo': 'geral', 'peso': 0.5},
    {'nome': u'Tinta (vidro 30ml)', 'tipo': 'geral', 'peso': 0},
    {'nome': u'Incenso exótico', 'tipo': 'geral', 'peso': 0}
]

kits_mago = [mago1, mago2]

mago_armas = [
    {'nome': u'Espada curta', 'peso': 1.5, 'iniciativa': 7, 'tipo': 'arma',
     'dano': '1d6', 'categoria': 'corpo-a-corpo'},
    {'nome': u'Adaga', 'peso': 0.5, 'iniciativa': 8, 'tipo': 'arma', 'dano':
     '1d4',
     'categoria': 'corpo-a-corpo', 'alcance': '3/6/9'},
    {'nome': u'Funda', 'peso': 0, 'iniciativa': 4, 'tipo': 'arma', 'dano':
     '1d3',
     'categoria': 'distancia', 'alcance': '10/20/30'},
    {'nome': u'Cajado', 'peso': 1.5, 'iniciativa': 7, 'tipo': 'arma', 'dano':
     '1d4', 'categoria': 'corpo-a-corpo'}
]
