# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

classes = [
    {
        "nome": u"Clérigo",
        "dado_vida": 8,
        "atributos_minimos": {
            "sabedoria": 14
        },
        "tabela":
        {
            1:
            {
                "nivel": 1,
                "xp": 0,
                "bonus_ataque": 0,
                "jogada_protecao": 15,
                "magias": [
                    1,
                    0,
                    0
                ],
                "esqueleto": 13,
                "zumbi": 17,
                "carnical": 19,
                "inumano": "N",
                "aparicao": "N",
                "espectro": "N",
                "mumia": "N",
                "vampiro": "N",
            },
            2:
            {
                "nivel": 2,
                "xp": 1500,
                "bonus_ataque": 1,
                "jogada_protecao": 15,
                "magias": [
                    2,
                    0,
                    0
                ],
                "esqueleto": 11,
                "zumbi": 15,
                "carnical": 18,
                "inumano": 20,
                "aparicao": "N"
            },
            3:
            {
                "nivel": 3,
                "xp": 3000,
                "bonus_ataque": 2,
                "jogada_protecao": 15,
                "magias": [
                    2,
                    1,
                    0
                ],
                "esqueleto": 9,
                "zumbi": 13,
                "carnical": 17,
                "inumano": 19,
                "aparicao": "N"
            },
            4:
            {
                "nivel": 4,
                "xp": 6000,
                "bonus_ataque": 2,
                "jogada_protecao": 14,
                "magias": [
                    3,
                    2,
                    0
                ],
                "esqueleto": 7,
                "zumbi": 11,
                "carnical": 15,
                "inumano": 18,
                "aparicao": 20
            },
            5:
            {
                "nivel": 5,
                "xp": 12000,
                "bonus_ataque": 3,
                "jogada_protecao": 14,
                "magias": [
                    3,
                    2,
                    1
                ],
                "esqueleto": 5,
                "zumbi": 9,
                "carnical": 13,
                "inumano": 17,
                "aparicao": 19
            }
        }
    },
    {
        "nome": u"Homem de armas",
        "dado_vida": 10,
        "atributos_minimos": {
            "forca": 12,
            "constituicao": 12,
        },
        "tabela": {
            1:
            {
                "nivel": 1,
                "xp": 0,
                "bonus_ataque": 1,
                "jogada_protecao": 16
            },
            2:
            {
                "nivel": 2,
                "xp": 2000,
                "bonus_ataque": 2,
                "jogada_protecao": 16
            },
            3:
            {
                "nivel": 3,
                "xp": 4000,
                "bonus_ataque": 3,
                "jogada_protecao": 16
            },
            4:
            {
                "nivel": 4,
                "xp": 8000,
                "bonus_ataque": 4,
                "jogada_protecao": 15
            },
            5:
            {
                "nivel": 5,
                "xp": 16000,
                "bonus_ataque": 5,
                "jogada_protecao": 15
            }
        }
    },
    {
        "nome": u"Mago",
        "dado_vida": 4,
        "atributos_minimos": {
            "inteligencia": 14
        },
        "tabela": {
            1:
            {
                "nivel": 1,
                "xp": 0,
                "bonus_ataque": 0,
                "jogada_protecao": 14,
                "magias": [
                    1,
                    0,
                    0
                ]
            },
            2:
            {
                "nivel": 2,
                "xp": 2500,
                "bonus_ataque": 0,
                "jogada_protecao": 14,
                "magias": [
                    2,
                    0,
                    0
                ]
            },
            3:
            {
                "nivel": 3,
                "xp": 5000,
                "bonus_ataque": 1,
                "jogada_protecao": 14,
                "magias": [
                    2,
                    1,
                    0
                ]
            },
            4:
            {
                "nivel": 4,
                "xp": 6000,
                "bonus_ataque": 1,
                "jogada_protecao": 13,
                "magias": [
                    2,
                    2,
                    0
                ]
            },
            5:
            {
                "nivel": 5,
                "xp": 12000,
                "bonus_ataque": 2,
                "jogada_protecao": 13,
                "magias": [
                    2,
                    2,
                    1
                ]
            }
        }
    },
    {
        "nome": u"Ladrão",
        "dado_vida": 6,
        "atributos_minimos": {
            "destreza": 12
        },
        "tabela": {
            1:
            {
                "nivel": 1,
                "xp": 0,
                "bonus_ataque": 1,
                "jogada_protecao": 15,
                "ataque_costas": 2,
                "abrir_fechaduras": 15,
                "desarmar_armadilhas": 20,
                "escalar_muros": 80,
                "mover_silencio": 20,
                "esconder_sombras": 10,
                "pungar": 20,
                "ouvir_barulhos": "1-2"
            },
            2:
            {
                "nivel": 2,
                "xp": 1250,
                "bonus_ataque": 1,
                "jogada_protecao": 15,
                "ataque_costas": 2,
                "abrir_fechaduras": 20,
                "desarmar_armadilhas": 25,
                "escalar_muros": 81,
                "mover_silencio": 25,
                "esconder_sombras": 15,
                "pungar": 25,
                "ouvir_barulhos": "1-2"
            },
            3:
            {
                "nivel": 3,
                "xp": 2500,
                "bonus_ataque": 2,
                "jogada_protecao": 15,
                "ataque_costas": 2,
                "abrir_fechaduras": 25,
                "desarmar_armadilhas": 20,
                "escalar_muros": 82,
                "mover_silencio": 30,
                "esconder_sombras": 20,
                "pungar": 30,
                "ouvir_barulhos": "1-2"
            },
            4:
            {
                "nivel": 4,
                "xp": 5000,
                "bonus_ataque": 2,
                "jogada_protecao": 14,
                "ataque_costas": 2,
                "abrir_fechaduras": 30,
                "desarmar_armadilhas": 25,
                "escalar_muros": 83,
                "mover_silencio": 35,
                "esconder_sombras": 25,
                "pungar": 35,
                "ouvir_barulhos": "1-2"
            },
            5:
            {
                "nivel": 5,
                "xp": 10000,
                "bonus_ataque": 2,
                "jogada_protecao": 14,
                "ataque_costas": 2,
                "abrir_fechaduras": 35,
                "desarmar_armadilhas": 30,
                "escalar_muros": 84,
                "mover_silencio": 40,
                "esconder_sombras": 30,
                "pungar": 40,
                "ouvir_barulhos": "1-3"
            }
        }
    }
]
