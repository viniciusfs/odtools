# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

import copy
import dice
import random

from flask import current_app as app
from ..regras import racas as tbl_racas
from ..regras import classes as tbl_classes
from ..regras import atributos as tbl_atributos
from ..regras import alinhamentos
from ..regras import kits_hda, hda_armas, hda_protecao



def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


class Modificador(object):
    def modificar(self, personagem):
        raise NotImplementedError


class Atributo(Modificador):
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def valor(self, valor):
        return self.tabela[str(valor)]


@singleton
class Forca(Atributo):
    pass


@singleton
class Destreza(Atributo):
    pass


@singleton
class Constituicao(Atributo):
    pass


@singleton
class Sabedoria(Atributo):
    pass


@singleton
class Inteligencia(Atributo):
    pass


@singleton
class Carisma(Atributo):
    pass


FOR = Forca(tbl_atributos['forca'])
DES = Destreza(tbl_atributos['destreza'])
CON = Constituicao(tbl_atributos['constituicao'])
INT = Inteligencia(tbl_atributos['inteligencia'])
SAB = Sabedoria(tbl_atributos['sabedoria'])
CAR = Carisma(tbl_atributos['carisma'])


class Personagem(object):
    def __init__(self):
        self.nivel = 1
        self.atributos = {}
        self.raca = ""
        self.classe = {}
        self.idiomas = []
        self.alinhamento = ""
        self.equipamentos = []
        self.dinheiro = {}
        self.movimento = 0

    @property
    def FOR(self):
        return self.atributos['forca']['valor']

    @FOR.setter
    def FOR(self, value):
        self.atributos['forca'] = FOR.valor(value)

    @property
    def DES(self):
        return self.atributos['destreza']['valor']

    @DES.setter
    def DES(self, value):
        self.atributos['destreza'] = DES.valor(value)

    @property
    def CON(self):
        return self.atributos['constituicao']['valor']

    @CON.setter
    def CON(self, value):
        self.atributos['constituicao'] = CON.valor(value)

    @property
    def INT(self):
        return self.atributos['inteligencia']['valor']

    @INT.setter
    def INT(self, value):
        self.atributos['inteligencia'] = INT.valor(value)

    @property
    def SAB(self):
        return self.atributos['sabedoria']['valor']

    @SAB.setter
    def SAB(self, value):
        self.atributos['sabedoria'] = SAB.valor(value)

    @property
    def CAR(self):
        return self.atributos['carisma']['valor']

    @CAR.setter
    def CAR(self, value):
        self.atributos['carisma'] = CAR.valor(value)

    @property
    def BA(self):
        return self.classe['tabela']['bonus_ataque']

    @property
    def PV(self):
        return self.nivel * (self.classe['dv'] + self.atributos['constituicao']['ajuste'])

    @property
    def peso(self):
        total = 0

        for item in self.equipamentos:
            total += item['peso']

        return total

    @property
    def CA(self):
        protecao_equipamentos = 0

        for item in self.equipamentos:
            if item['tipo'] == 'protecao':
                protecao_equipamentos += item['bonus']

        return 10 + self.atributos['destreza']['ajuste'] + protecao_equipamentos

    def __str__(self):
        return "%s %s nivel %d (%d %d %d %d %d %d)" % (self.raca,
                                                        self.classe['nome'],
                                                        self.nivel,
                                                        self.FOR,
                                                        self.DES,
                                                        self.CON,
                                                        self.INT,
                                                        self.SAB,
                                                        self.CAR)


    def to_json(self):
        """
{
  "nivel": 1,
  "raca": "Humano",
  "classe": "Ladrão",
  "alinhamento": "Neutro",
  "atributos": {
    "FOR": 10,
    "DES": 14,
    "CON": 9,
    "INT": 11,
    "SAB": 10,
    "CAR": 13
  },
  "movimento": 9,
  "idiomas": [
    "Comum"
  ],
  "dinheiro": {
    "PPL": 0,
    "PE": 0,
    "PO": 0,
    "PP": 0,
    "PC": 0
  },
  "equipamentos": []
}
        """
        pass


class Atributos3d6(Modificador):
    def modificar(self, personagem):
        personagem.atributos['forca'] = FOR.valor(dice.roll('3d6t'))
        personagem.atributos['destreza'] = DES.valor(dice.roll('3d6t'))
        personagem.atributos['constituicao'] = CON.valor(dice.roll('3d6t'))
        personagem.atributos['inteligencia'] = INT.valor(dice.roll('3d6t'))
        personagem.atributos['sabedoria'] = SAB.valor(dice.roll('3d6t'))
        personagem.atributos['carisma'] = CAR.valor(dice.roll('3d6t'))


class Raca(Modificador):
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

        if self.nome == "Humano":
            lst_atributos = [ 'forca', 'destreza', 'constituicao',
                               'inteligencia', 'sabedoria', 'carisma' ]

            atributo1 = random.choice(lst_atributos)
            lst_atributos.remove(atributo1)
            atributo2 = random.choice(lst_atributos)
            lst_atributos.remove(atributo2)

            self.atributos = { atributo1: 2, atributo2: -2 }

    def modificar(self, personagem):
        personagem.raca = self.nome
        personagem.movimento = self.movimento
        personagem.idiomas = self.idiomas

        for k, v in list(self.atributos.items()):
            if k == "forca":
                personagem.FOR += v
            if k == "destreza":
                personagem.DES += v
            if k == "constituicao":
                personagem.CON += v
            if k == "inteligencia":
                personagem.INT += v
            if k == "sabedoria":
                personagem.SAB += v
            if k == "carisma":
                personagem.CAR += v


class Classe(Modificador):
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def modificar(self, personagem):
        personagem.classe['nome'] = self.nome
        personagem.classe['tabela'] = self.tabela[personagem.nivel]
        personagem.classe['dv'] = self.dado_vida


class Alinhamento(Modificador):
    def modificar(self, personagem):
        personagem.alinhamento = alinhamentos[random.randrange(0, len(alinhamentos))]


class EquipamentosKit(Modificador):
    def __init__(self):
        self.equipamentos = []

    def modificar(self, personagem):
        personagem.equipamentos.clear()

        random_kit = kits_hda[random.randrange(0, len(kits_hda))]
        for item in random_kit:
            self.equipamentos.append(item)

        random_arma = hda_armas[random.randrange(0, len(hda_armas))]
        self.equipamentos.append(random_arma)

        random_protecao = hda_protecao[random.randrange(0, len(hda_protecao))]
        self.equipamentos.append(random_protecao)

        for item in self.equipamentos:
            personagem.equipamentos.append(item)


class GeradorAleatorio(object):
    def __init__(self):
        self.personagem = Personagem()
        self.atributos = Atributos3d6()
        self.racas_disponiveis = [Raca(r) for r in tbl_racas]
        self.classes_disponiveis = [Classe(c) for c in tbl_classes]
        self.alinhamento = Alinhamento()
        self.equipamentos = EquipamentosKit()

    def rolar_atributos(self):
        self.atributos.modificar(self.personagem)

    def selecionar_raca(self):
        self.raca = self.racas_disponiveis[random.randrange(0, len(self.racas_disponiveis))]
        self.raca.modificar(self.personagem)

    def selecionar_classe(self):
        self.classe = self.classes_disponiveis[random.randrange(0, len(self.classes_disponiveis))]
        self.classe.modificar(self.personagem)

    def selecionar_alinhamento(self):
        self.alinhamento.modificar(self.personagem)

    def selecionar_inventario(self):
        self.equipamentos.modificar(self.personagem)

    def criar_personagem(self):
        self.rolar_atributos()
        self.selecionar_raca()
        self.selecionar_classe()
        self.selecionar_alinhamento()
        self.selecionar_inventario()

        return copy.deepcopy(self.personagem)
