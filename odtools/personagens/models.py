# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

import copy
import dice
import random
import uuid
import pypdftk

from flask import Blueprint, Response, render_template, json, current_app, redirect, url_for, send_file

from ..regras import atributos as tbl_atributos
from ..regras import racas as tbl_racas
from ..regras import classes as tbl_classes
from ..regras import alinhamentos as lst_alinhamentos
from ..regras import idiomas as lst_idiomas

from ..regras import kits_hda, kits_clerigo, kits_mago, kits_ladrao
from ..regras import hda_armas, clerigo_armas, mago_armas, ladrao_armas
from ..regras import hda_protecao, clerigo_protecao, ladrao_protecao



class Processador(object):
    def __init__(self, personagem):
        self.personagem = personagem

    def process(self):
        raise NotImplementedError


class Atributos(Processador):
    def process(self):
        rolagens = []

        for i in range(0, 6):
            rolagens.append(dice.roll('3d6t'))

        self.personagem.atributos = rolagens


class Raca(Processador):
    def process(self):
        raca = random.choice(tbl_racas)
        self.personagem.raca = raca['nome']



class Personagem(object):
    def __init__(self):
        self.nivel = 0
        self.atributos = []
        self.classe = ""
        self.raca = ""
        self.alinhamento = ""
        self.linguas = []
        self.equipamentos = []
        self.dinheiro = {}
        self.caracteristicas = ""

        processadores = [Atributos]

        for processador in processadores:
            processador(self).process()

    @property
    def FOR(self):
        return self.atributos[0]

    @FOR.setter
    def FOR(self, value):
        self.atributos[0] = value

    @property
    def DES(self):
        return self.atributos[1]

    @DES.setter
    def DES(self, value):
        self.atributos[1] = value

    @property
    def CON(self):
        return self.atributos[2]

    @CON.setter
    def CON(self, value):
        self.atributos[2] = value

    @property
    def INT(self):
        return self.atributos[3]

    @INT.setter
    def INT(self, value):
        self.atributos[3] = value

    @property
    def SAB(self):
        return self.atributos[4]

    @SAB.setter
    def SAB(self, value):
        self.atributos[4] = value

    @property
    def CAR(self):
        return self.atributos[5]

    @CAR.setter
    def CAR(self, value):
        self.atributos[5] = value
