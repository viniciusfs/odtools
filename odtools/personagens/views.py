# -*- coding: utf-8 -*-

# This file is part of ODtools project.
# (c) 2017, Vinicius Figueiredo <viniciusfs@gmail.com>

import ast
import copy
import dice
import random
import uuid
import pypdftk
import os

from flask import current_app, Blueprint, Response, request, render_template, json, current_app, redirect, url_for, send_file

from ..regras import atributos as tbl_atributos
from ..regras import racas as tbl_racas
from ..regras import classes as tbl_classes
from ..regras import alinhamentos as lst_alinhamentos
from ..regras import idiomas as lst_idiomas

from ..regras import kits_hda, kits_clerigo, kits_mago, kits_ladrao
from ..regras import hda_armas, clerigo_armas, mago_armas, ladrao_armas
from ..regras import hda_protecao, clerigo_protecao, ladrao_protecao

from .models import GeradorAleatorio


personagens = Blueprint('personagens', __name__, url_prefix='/personagens')


@personagens.route('/')
def index():
    return render_template('personagens/index.html')


@personagens.route('/aleatorio', methods=['GET'])
def criar_aleatorio():
    g = GeradorAleatorio()
    personagem = g.criar_personagem()

    return render_template('personagens/index.html', p=personagem)


@personagens.route('/pdf', methods=['POST'])
def pdf():
    if request.method == 'POST':
        data = request.form.get('personagem')
        personagem = ast.literal_eval(data)

        defaults = {
            'Classe e Especialização': personagem['classe']['nome'],
            'Raça': personagem['raca']['nome'],
            'Alinhamento': personagem['alinhamento'],
            'Atributos_0': personagem['atributos']['forca']['valor'],
            'Atributos_1': personagem['atributos']['destreza']['valor'],
            'Atributos_2': personagem['atributos']['constituicao']['valor'],
            'Atributos_3': personagem['atributos']['inteligencia']['valor'],
            'Atributos_4': personagem['atributos']['sabedoria']['valor'],
            'Atributos_5': personagem['atributos']['carisma']['valor'],
            'Bônus de Ataque': personagem['ba']['classe'],
            'Básico': personagem['ba']['forca'],
            'À Distância': personagem['ba']['destreza'],
            'Aramas e Ataques 0': personagem['armas'][0]['nome'],
            'Iniciativa 0': personagem['armas'][0]['iniciativa'],
            'Ataque 0': personagem['armas'][0]['ba'],
            'Dano 0': personagem['armas'][0]['dano'],
            'Alcance 0': personagem['armas'][0]['alcance'] if 'alcance' in personagem['armas'][0] else '-',
            'Tamanho 0': personagem['armas'][0]['tamanho'] if 'tamanho' in personagem['armas'][0] else '',
            'Classe Armadura': personagem['ca']['total'],
            'Mod Des': personagem['ca']['destreza'],
            'Armadura': personagem['ca']['equipamentos'],
            'Outro 0': personagem['ca']['raca'] if personagem['raca']['nome'] == 'Halfling' else '',
            'Jogada Proteção': personagem['jp']['base'],
            'JP Des': personagem['jp']['destreza'],
            'JP Con': personagem['jp']['constituicao'],
            'JP Sab': personagem['jp']['sabedoria'],
            'Movimento': personagem['movimento']['total'],
            'Pontos de Vida': personagem['classe']['dado_vida'],
            'Idiomas 0': personagem['idiomas'][0] if personagem['idiomas'][0] else '',
            'Idiomas 1': personagem['idiomas'][1] if len(personagem['idiomas']) >= 2 else '',
            'Idiomas 2': personagem['idiomas'][2] if len(personagem['idiomas']) >= 3 else '',
            'Idiomas 3': personagem['idiomas'][3] if len(personagem['idiomas']) >= 4 else '',
            'Idiomas 4': personagem['idiomas'][4] if len(personagem['idiomas']) >= 5 else '',
            'Idiomas 5': personagem['idiomas'][5] if len(personagem['idiomas']) >= 6 else '',
            'Nível': '1',
            'TL 0': personagem['classe']['tabela'][1]['abrir_fechaduras'] if personagem['classe']['nome'] == 'Ladrão' else '',
            'TL 1': personagem['classe']['tabela'][1]['desarmar_armadilhas'] if personagem['classe']['nome'] == 'Ladrão' else '',
            'TL 2': personagem['classe']['tabela'][1]['escalar_muros'] if personagem['classe']['nome'] == 'Ladrão' else '',
            'TL 3': personagem['classe']['tabela'][1]['mover_silencio'] if personagem['classe']['nome'] == 'Ladrão' else '',
            'TL 4': personagem['classe']['tabela'][1]['esconder_sombras'] if personagem['classe']['nome'] == 'Ladrão' else '',
            'TL 5': personagem['classe']['tabela'][1]['pungar'] if personagem['classe']['nome'] == 'Ladrão' else '',
            'TL 6': personagem['classe']['tabela'][1]['ouvir_barulhos'] if personagem['classe']['nome'] == 'Ladrão' else '',
            'TL 7': personagem['classe']['tabela'][1]['ataque_costas'] if personagem['classe']['nome'] == 'Ladrão' else '',
            'Afastar Mortos-Vivos 0': personagem['classe']['tabela'][1]['esqueleto'] if personagem['classe']['nome'] == 'Clérigo' else '',
            'Afastar Mortos-Vivos 1': personagem['classe']['tabela'][1]['zumbi'] if personagem['classe']['nome'] == 'Clérigo' else '',
            'Afastar Mortos-Vivos 2': personagem['classe']['tabela'][1]['carnical'] if personagem['classe']['nome'] == 'Clérigo' else '',
            'Afastar Mortos-Vivos 3': personagem['classe']['tabela'][1]['inumano'] if personagem['classe']['nome'] == 'Clérigo' else '',
            'Afastar Mortos-Vivos 4': personagem['classe']['tabela'][1]['aparicao'] if personagem['classe']['nome'] == 'Clérigo' else '',
            'Afastar Mortos-Vivos 5': personagem['classe']['tabela'][1]['mumia'] if personagem['classe']['nome'] == 'Clérigo' else '',
            'Afastar Mortos-Vivos 6': personagem['classe']['tabela'][1]['espectro'] if personagem['classe']['nome'] == 'Clérigo' else '',
            'Afastar Mortos-Vivos 7': personagem['classe']['tabela'][1]['vampiro'] if personagem['classe']['nome'] == 'Clérigo' else ''
        }

        equips = {}
        for i in range(0, len(personagem['equipamentos'])):
            key_name = 'Equipamentos %s' % i
            equips[key_name] = personagem['equipamentos'][i]['nome']

        mapping = {}
        mapping.update(defaults)
        mapping.update(equips)

        source = os.path.join(current_app.config['DATA_DIR'], 'od-ficha.pdf')
        destination = os.path.join(current_app.config['TMP_DIR'], 'ficha.pdf')

        generated_pdf = pypdftk.fill_form(source, mapping, out_file=destination)

        return send_file(destination, as_attachment=True)
