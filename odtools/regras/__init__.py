# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

from .basicas.atributos import atributos
from .basicas.alinhamentos import alinhamentos
from .basicas.idiomas import idiomas
from .basicas.classes import classes as mb_classes
from .basicas.racas import racas as mb_racas

racas = mb_racas
classes = mb_classes

from .extras.kits import kits_hda, kits_clerigo, kits_ladrao, kits_mago
from .extras.kits import hda_armas, clerigo_armas, ladrao_armas, mago_armas
from .extras.kits import hda_protecao, clerigo_protecao, ladrao_protecao
