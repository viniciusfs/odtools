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



personagens = Blueprint('personagens', __name__, url_prefix='/personagens')


@personagens.route('/')
def index():
    return render_template('personagens/index.html')


@personagens.route('/aleatorio', methods=['GET'])
def criar_aleatorio():
    personagem = False

    while personagem is False:
        personagem = criar_personagem()

    return render_template('personagens/index.html', p=personagem)


@personagens.route('/pdf', methods=['POST'])
def pdf():
    if request.method == 'POST':
        data = request.form.get('personagem')
        personagem = ast.literal_eval(data)

        defaults = {
            u'Classe e Especialização': personagem['classe']['nome'],
            u'Raça': personagem['raca']['nome'],
            u'Alinhamento': personagem['alinhamento'],
            u'Atributos_0': personagem['atributos']['forca']['valor'],
            u'Atributos_1': personagem['atributos']['destreza']['valor'],
            u'Atributos_2': personagem['atributos']['constituicao']['valor'],
            u'Atributos_3': personagem['atributos']['inteligencia']['valor'],
            u'Atributos_4': personagem['atributos']['sabedoria']['valor'],
            u'Atributos_5': personagem['atributos']['carisma']['valor'],
            u'Bônus de Ataque': personagem['ba']['classe'],
            u'Básico': personagem['ba']['forca'],
            u'À Distância': personagem['ba']['destreza'],
            u'Aramas e Ataques 0': personagem['armas'][0]['nome'],
            u'Iniciativa 0': personagem['armas'][0]['iniciativa'],
            u'Ataque 0': personagem['armas'][0]['ba'],
            u'Dano 0': personagem['armas'][0]['dano'],
            u'Alcance 0': personagem['armas'][0]['alcance'] if personagem['armas'][0].has_key('alcance') else '-',
            u'Tamanho 0': personagem['armas'][0]['tamanho'] if personagem['armas'][0].has_key('tamanho') else '',
            u'Classe Armadura': personagem['ca']['total'],
            u'Mod Des': personagem['ca']['destreza'],
            u'Armadura': personagem['ca']['equipamentos'],
            u'Outro 0': personagem['ca']['raca'] if personagem['raca']['nome'] == u'Halfling' else '',
            u'Jogada Proteção': personagem['jp']['base'],
            u'JP Des': personagem['jp']['destreza'],
            u'JP Con': personagem['jp']['constituicao'],
            u'JP Sab': personagem['jp']['sabedoria'],
            u'Movimento': personagem['movimento']['total'],
            u'Pontos de Vida': personagem['classe']['dado_vida'],
            u'Idiomas 0': personagem['idiomas'][0] if personagem['idiomas'][0] else '',
            u'Idiomas 1': personagem['idiomas'][1] if len(personagem['idiomas']) >= 2 else '',
            u'Idiomas 2': personagem['idiomas'][2] if len(personagem['idiomas']) >= 3 else '',
            u'Idiomas 3': personagem['idiomas'][3] if len(personagem['idiomas']) >= 4 else '',
            u'Idiomas 4': personagem['idiomas'][4] if len(personagem['idiomas']) >= 5 else '',
            u'Idiomas 5': personagem['idiomas'][5] if len(personagem['idiomas']) >= 6 else '',
            u'Nível': '1',
            u'TL 0': personagem['classe']['tabela'][1]['abrir_fechaduras'] if personagem['classe']['nome'] == u'Ladrão' else '',
            u'TL 1': personagem['classe']['tabela'][1]['desarmar_armadilhas'] if personagem['classe']['nome'] == u'Ladrão' else '',
            u'TL 2': personagem['classe']['tabela'][1]['escalar_muros'] if personagem['classe']['nome'] == u'Ladrão' else '',
            u'TL 3': personagem['classe']['tabela'][1]['mover_silencio'] if personagem['classe']['nome'] == u'Ladrão' else '',
            u'TL 4': personagem['classe']['tabela'][1]['esconder_sombras'] if personagem['classe']['nome'] == u'Ladrão' else '',
            u'TL 5': personagem['classe']['tabela'][1]['pungar'] if personagem['classe']['nome'] == u'Ladrão' else '',
            u'TL 6': personagem['classe']['tabela'][1]['ouvir_barulhos'] if personagem['classe']['nome'] == u'Ladrão' else '',
            u'TL 7': personagem['classe']['tabela'][1]['ataque_costas'] if personagem['classe']['nome'] == u'Ladrão' else '',
            u'Afastar Mortos-Vivos 0': personagem['classe']['tabela'][1]['esqueleto'] if personagem['classe']['nome'] == u'Clérigo' else '',
            u'Afastar Mortos-Vivos 1': personagem['classe']['tabela'][1]['zumbi'] if personagem['classe']['nome'] == u'Clérigo' else '',
            u'Afastar Mortos-Vivos 2': personagem['classe']['tabela'][1]['carnical'] if personagem['classe']['nome'] == u'Clérigo' else '',
            u'Afastar Mortos-Vivos 3': personagem['classe']['tabela'][1]['inumano'] if personagem['classe']['nome'] == u'Clérigo' else '',
            u'Afastar Mortos-Vivos 4': personagem['classe']['tabela'][1]['aparicao'] if personagem['classe']['nome'] == u'Clérigo' else '',
            u'Afastar Mortos-Vivos 5': personagem['classe']['tabela'][1]['mumia'] if personagem['classe']['nome'] == u'Clérigo' else '',
            u'Afastar Mortos-Vivos 6': personagem['classe']['tabela'][1]['espectro'] if personagem['classe']['nome'] == u'Clérigo' else '',
            u'Afastar Mortos-Vivos 7': personagem['classe']['tabela'][1]['vampiro'] if personagem['classe']['nome'] == u'Clérigo' else ''
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


def criar_personagem():
    personagem = {}
    personagem['id'] = uuid.uuid4().hex
    current_app.logger.info('%s iniciando criacao de personagem' % personagem['id'])

    # passo 1 atributos
    personagem['atributos'] = sortear_atributos()
    current_app.logger.debug('%s atributos sorteados %d %d %d %d %d %d' % (
        personagem['id'],
        personagem['atributos']['forca']['valor'],
        personagem['atributos']['destreza']['valor'],
        personagem['atributos']['constituicao']['valor'],
        personagem['atributos']['inteligencia']['valor'],
        personagem['atributos']['sabedoria']['valor'],
        personagem['atributos']['carisma']['valor']))

    # passo 2 raca
    raca = random.choice(tbl_racas)
    personagem['raca'] = copy.deepcopy(raca)
    current_app.logger.debug('%s raca %s' % (personagem['id'],
                                            personagem['raca']['nome']))

    ## quando humano, sorteia dois atributos para serem alterados
    if personagem['raca']['nome'] == u'Humano':
        lista_atributos = ['forca',
                           'destreza',
                           'constituicao',
                           'inteligencia',
                           'sabedoria']

        atributo1 = random.choice(lista_atributos)
        atributo2 = random.choice(lista_atributos)

        while atributo1 == atributo2:
            atributo2 = random.choice(lista_atributos)

        personagem['raca']['modificadores'] = { atributo1: 2, atributo2: -2 }
        current_app.logger.debug('%s atributos selecionados +2 %s, -2 %s' % (
            personagem['id'],
            atributo1,
            atributo2))

    ## aplica alteracao de atributos devido a raca selecionada
    for atributo in personagem['raca']['modificadores'].keys():
        novo_valor = personagem['atributos'][atributo]['valor'] + \
            personagem['raca']['modificadores'][atributo]
        personagem['atributos'][atributo] = copy.deepcopy(tbl_atributos[atributo]['tabela'][str(
            novo_valor)])

    current_app.logger.debug('%s atributos modificados %d %d %d %d %d %d' % (
        personagem['id'],
        personagem['atributos']['forca']['valor'],
        personagem['atributos']['destreza']['valor'],
        personagem['atributos']['constituicao']['valor'],
        personagem['atributos']['inteligencia']['valor'],
        personagem['atributos']['sabedoria']['valor'],
        personagem['atributos']['carisma']['valor']))

    personagem['ba'] = {}
    if personagem['raca']['nome'] == u'Elfo' or personagem['raca']['nome'] == u'Halfling':
        personagem['ba']['raca'] = 1
    else:
        personagem['ba']['raca'] = 0

    # passo 3 classe
    classes_possiveis = []

    for classe in tbl_classes:
        if classe_permitida(classe, personagem['atributos']):
            classes_possiveis.append(copy.deepcopy(classe))
    current_app.logger.debug('%s possiveis classes %s' % (
        personagem['id'],
        classes_possiveis))

    if len(classes_possiveis) == 0:
        current_app.logger.info('%s descartando personagem' %
                                personagem['id'])
        return False

    classe = random.choice(classes_possiveis)
    for key in (2, 3, 4, 5):
        del classe['tabela'][key]

    personagem['classe'] = classe
    current_app.logger.debug('%s classe selecionada %s' % (personagem['id'],
                                                          personagem['classe']['nome']))

    # jp
    personagem['jp'] = {}
    personagem['jp']['base'] = personagem['classe']['tabela'][1]['jogada_protecao']
    personagem['jp']['destreza'] = personagem['atributos']['destreza']['ajuste']
    personagem['jp']['constituicao'] = personagem['atributos']['constituicao']['ajuste']
    personagem['jp']['sabedoria'] = personagem['atributos']['sabedoria']['ajuste']

    # passo 4 bonus de ataque
    personagem['ba']['forca'] =  personagem['atributos']['forca']['ajuste']
    personagem['ba']['destreza'] = personagem['atributos']['destreza']['ajuste']
    personagem['ba']['classe'] = personagem['classe']['tabela'][1]['bonus_ataque']

    # passo 5 idiomas
    idiomas = []

    if personagem['raca']['nome'] == u'Anão':
        idiomas.append(u'Anão')

    if personagem['raca']['nome'] == u'Elfo':
        idiomas.append(u'Élfico')

    if personagem['raca']['nome'] == u'Halfling':
        idiomas.append(u'Comum')

    if personagem['raca']['nome'] == u'Humano':
        idiomas.append(u'Comum')

    if personagem['atributos']['inteligencia']['idiomas_adicionais'] > 0:
        for i in range(0, personagem['atributos']['inteligencia']['idiomas_adicionais']):
            idioma = random.choice(lst_idiomas)
            if idioma not in idiomas:
                idiomas.append(idioma)

    personagem['idiomas'] = copy.deepcopy(idiomas)
    current_app.logger.debug('%s idiomas %s' % (personagem['id'],
                                                          personagem['idiomas']))

    # passo 6 alinhamento
    alinhamentos = copy.deepcopy(lst_alinhamentos)

    if personagem['raca']['nome'] == u'Anão':
        alinhamentos.append(u'Ordeiro')

    if personagem['raca']['nome'] == u'Elfo':
        alinhamentos.append(u'Neutro')

    if personagem['raca']['nome'] == u'Halfling':
        alinhamentos.append(u'Neutro')
        alinhamentos.append(u'Caótico')

    personagem['alinhamento'] = random.choice(alinhamentos)

    # passo 7 equipamentos e carga
    personagem['dinheiro'] = {}
    personagem['dinheiro']['po'] = dice.roll('3d6t')

    personagem['armas'] = []
    personagem['protecao'] = []

    if personagem['classe']['nome'] == u'Clérigo':
        equipamentos = random.choice(kits_clerigo)
        personagem['equipamentos'] = copy.deepcopy(equipamentos)

        arma = random.choice(clerigo_armas)
        personagem['armas'].append(copy.deepcopy(arma))

        sorte = random.choice(range(1,11)) % 2

        if sorte == 0:
            protecao = random.choice(clerigo_protecao)
            personagem['protecao'].append(copy.deepcopy(protecao))

    if personagem['classe']['nome'] == u'Homem de armas':
        equipamentos = random.choice(kits_hda)
        personagem['equipamentos'] = copy.deepcopy(equipamentos)

        arma = random.choice(hda_armas)
        personagem['armas'].append(copy.deepcopy(arma))

        sorte = random.choice(range(1,11)) % 2

        if sorte == 0:
            protecao = random.choice(hda_protecao)
            personagem['protecao'].append(copy.deepcopy(protecao))

    if personagem['classe']['nome'] == u'Ladrão':
        equipamentos = random.choice(kits_ladrao)
        personagem['equipamentos'] = copy.deepcopy(equipamentos)

        arma = random.choice(ladrao_armas)
        personagem['armas'].append(copy.deepcopy(arma))

        sorte = random.choice(range(1,11)) % 2

        if sorte == 0:
            protecao = random.choice(ladrao_protecao)
            personagem['protecao'].append(copy.deepcopy(protecao))

    if personagem['classe']['nome'] == u'Mago':
        equipamentos = random.choice(kits_mago)
        personagem['equipamentos'] = copy.deepcopy(equipamentos)

        arma = random.choice(mago_armas)
        personagem['armas'].append(copy.deepcopy(arma))


    carga = 0
    for item in personagem['equipamentos']:
        carga += item['peso']

    for item in personagem['armas']:
        carga += item['peso']

    for item in personagem['protecao']:
        carga += item['peso']

    personagem['carga'] = carga

    personagem['movimento'] = {}
    personagem['movimento']['raca'] = personagem['raca']['movimento']
    personagem['movimento']['armadura'] = 0
    personagem['movimento']['carga'] = 0

    if personagem['carga'] < personagem['atributos']['forca']['sem_carga']:
        personagem['movimento']['carga'] = 0
    elif personagem['carga'] < personagem['atributos']['forca']['carga_leve']:
        personagem['movimento']['carga'] = -1
    elif personagem['carga'] < personagem['atributos']['forca']['carga_pesada']:
        personagem['movimento']['carga'] = -2

    personagem['movimento']['total'] = personagem['movimento']['raca'] + personagem['movimento']['armadura'] + personagem['movimento']['carga']

    for item in personagem['armas']:
        if item['categoria'] == 'corpo-a-corpo':
            item['ba'] = personagem['ba']['classe'] + personagem['ba']['forca']
            if 'alcance' in item:
                item['ba'] = personagem['ba']['classe'] + personagem['ba']['destreza']
        elif item['categoria'] == 'distancia':
            item['ba'] = personagem['ba']['classe'] + personagem['ba']['destreza']
            if personagem['raca']['nome'] == 'Halfling':
                item['ba'] += 1
            if personagem['raca']['nome'] == 'Elfo' and item['nome'] == 'Arco curto, flecha de caça':
                item['ba'] += 1


    # passo 8 classe de armadura
    personagem['ca'] = {}
    personagem['ca']['destreza'] = personagem['atributos']['destreza']['ajuste']

    ca_equip = 0

    for item in personagem['protecao']:
        ca_equip += item['bonus']

    personagem['ca']['equipamentos'] = ca_equip

    if personagem['raca']['nome'] == 'Halfling':
        personagem['ca']['raca'] = 2
    else:
        personagem['ca']['raca'] = 0

    personagem['ca']['total'] = 10 + personagem['ca']['destreza'] + personagem['ca']['equipamentos']


    # passo 9 magia
    # passo 10 detalhes

    # fiiiiimmm
    current_app.logger.info('%s criacao concluida' %
                                personagem['id'])
    return personagem


def sortear_atributos():
    rolagens = []
    atributos = {
        'forca': {},
        'destreza': {},
        'constituicao': {},
        'inteligencia': {},
        'sabedoria': {},
        'carisma': {}
    }

    for i in range(0, 6):
        rolagens.append(dice.roll('3d6t'))

    forca = str(rolagens[0])
    destreza = str(rolagens[1])
    constituicao = str(rolagens[2])
    inteligencia = str(rolagens[3])
    sabedoria = str(rolagens[4])
    carisma = str(rolagens[5])

    atributos['forca'] = copy.deepcopy(tbl_atributos['forca']['tabela'][forca])
    atributos['destreza'] = copy.deepcopy(tbl_atributos['destreza']['tabela'][destreza])
    atributos['constituicao'] = copy.deepcopy(tbl_atributos['constituicao']['tabela'][constituicao])
    atributos['inteligencia'] = copy.deepcopy(tbl_atributos['inteligencia']['tabela'][inteligencia])
    atributos['sabedoria'] = copy.deepcopy(tbl_atributos['sabedoria']['tabela'][sabedoria])
    atributos['carisma'] = copy.deepcopy(tbl_atributos['carisma']['tabela'][carisma])

    return atributos


def classe_permitida(classe, atributos):
    for atributo in classe['atributos_minimos'].keys():
        if atributos[atributo]['valor'] <= classe['atributos_minimos'][atributo]:
            return False
    return True
