# -*- encoding: utf-8 -*-
"""

    iceaddr: Look up information about Icelandic street addresses and postcodes
    Copyright (c) 2018 Sveinbjorn Thordarson

"""

from __future__ import unicode_literals

postcodes = {
    101: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    103: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    104: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    105: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    107: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    108: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    109: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    110: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    111: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    112: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    113: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    116: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Þéttbýli'},
    121: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    123: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    124: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    125: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    127: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    128: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    129: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    130: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    132: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík',
             'type': 'Pósthólf'},
    162: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Reykjavík',
             'placename_tgf': 'Reykjavík - Dreifbýli',
             'type': 'Dreifbýli'},
    170: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Seltjarnarnes',
             'placename_tgf': 'Seltjarnarnesi',
             'type': 'Þéttbýli'},
    172: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Seltjarnarnes',
             'placename_tgf': 'Seltjarnarnesi',
             'type': 'Pósthólf'},
    190: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Vogar',
             'placename_tgf': 'Vogum',
             'type': 'Þéttbýli'},
    191: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Vogar',
             'placename_tgf': 'Vogum',
             'type': 'Dreifbýli'},
    200: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Kópavogur',
             'placename_tgf': 'Kópavogi',
             'type': 'Þéttbýli'},
    201: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Kópavogur',
             'placename_tgf': 'Kópavogi',
             'type': 'Þéttbýli'},
    202: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Kópavogur',
             'placename_tgf': 'Kópavogi',
             'type': 'Pósthólf'},
    203: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Kópavogur',
             'placename_tgf': 'Kópavogi',
             'type': 'Þéttbýli'},
    210: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Garðabær',
             'placename_tgf': 'Garðabæ',
             'type': 'Þéttbýli'},
    212: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Garðabær',
             'placename_tgf': 'Garðabæ',
             'type': 'Pósthólf'},
    220: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Hafnarfjörður',
             'placename_tgf': 'Hafnarfirði',
             'type': 'Þéttbýli'},
    221: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Hafnarfjörður',
             'placename_tgf': 'Hafnarfirði',
             'type': 'Þéttbýli'},
    222: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Hafnarfjörður',
             'placename_tgf': 'Hafnarfirði',
             'type': 'Pósthólf'},
    225: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Garðabær',
             'placename_tgf': 'Garðabær',
             'type': 'Þéttbýli'},
    230: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Reykjanesbær',
             'placename_tgf': 'Reykjanesbæ',
             'type': 'Þéttbýli'},
    232: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Reykjanesbær',
             'placename_tgf': 'Reykjanesbæ',
             'type': 'Pósthólf'},
    233: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Reykjanesbær',
             'placename_tgf': 'Reykjanesbæ',
             'type': 'Dreifbýli'},
    235: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Keflavíkurflugvöllur',
             'placename_tgf': 'Keflavíkurflugvöllur',
             'type': 'Þéttbýli'},
    240: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Grindavík',
             'placename_tgf': 'Grindavík',
             'type': 'Þéttbýli'},
    241: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Grindavík',
             'placename_tgf': 'Grindavík',
             'type': 'Dreifbýli'},
    245: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Sandgerði',
             'placename_tgf': 'Sandgerði',
             'type': 'Þéttbýli'},
    246: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Sandgerði',
             'placename_tgf': 'Sandgerði',
             'type': 'Dreifbýli'},
    250: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Garður',
             'placename_tgf': 'Garði',
             'type': 'Þéttbýli'},
    251: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Garður',
             'placename_tgf': 'Garði',
             'type': 'Dreifbýli'},
    260: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Reykjanesbær',
             'placename_tgf': 'Reykjanesbæ',
             'type': 'Þéttbýli'},
    262: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Reykjanesbær',
             'placename_tgf': 'Reykjanesbæ',
             'type': 'Þéttbýli'},
    270: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Mosfellsbær',
             'placename_tgf': 'Mosfellsbæ',
             'type': 'Þéttbýli'},
    271: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Mosfellsbær',
             'placename_tgf': 'Mosfellsbæ',
             'type': 'Dreifbýli'},
    276: {   'area': 'Höfuðborgarsvæðið',
             'placename_nf': 'Mosfellsbær',
             'placename_tgf': 'Mosfellsbæ',
             'type': 'Dreifbýli'},
    300: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Akranes',
             'placename_tgf': 'Akranesi',
             'type': 'Þéttbýli'},
    301: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Akranes',
             'placename_tgf': 'Akranesi',
             'type': 'Dreifbýli'},
    302: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Akranes',
             'placename_tgf': 'Akranesi',
             'type': 'Pósthólf'},
    310: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Borgarnes',
             'placename_tgf': 'Borgarnesi',
             'type': 'Þéttbýli'},
    311: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Borgarnes',
             'placename_tgf': 'Borgarnesi',
             'type': 'Dreifbýli'},
    320: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Reykholt í Borgarfirði',
             'placename_tgf': 'Reykholt í Borgarfirði',
             'type': 'Dreifbýli'},
    340: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Stykkishólmur',
             'placename_tgf': 'Stykkishólmi',
             'type': 'Þéttbýli'},
    341: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Stykkishólmur',
             'placename_tgf': 'Stykkishólmi',
             'type': 'Dreifbýli'},
    345: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Flatey á Breiðafirði',
             'placename_tgf': 'Flatey á Breiðafirði',
             'type': 'Dreifbýli'},
    350: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Grundarfjörður',
             'placename_tgf': 'Grundarfirði',
             'type': 'Þéttbýli'},
    351: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Grundarfjörður',
             'placename_tgf': 'Grundarfirði',
             'type': 'Dreifbýli'},
    355: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Ólafsvík',
             'placename_tgf': 'Ólafsvík',
             'type': 'Þéttbýli'},
    356: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Snæfellsbær',
             'placename_tgf': 'Snæfellsbæ',
             'type': 'Dreifbýli'},
    360: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Hellissandur',
             'placename_tgf': 'Hellissandi',
             'type': 'Þéttbýli'},
    370: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Búðardalur',
             'placename_tgf': 'Búðardal',
             'type': 'Þéttbýli'},
    371: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Búðardalur',
             'placename_tgf': 'Búðardal',
             'type': 'Dreifbýli'},
    380: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Reykhólahreppur',
             'placename_tgf': 'Reykhólahreppi',
             'type': 'Þéttbýli'},
    381: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Reykhólahreppur',
             'placename_tgf': 'Reykhólahreppi',
             'type': 'Dreifbýli'},
    400: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Ísafjörður',
             'placename_tgf': 'Ísafirði',
             'type': 'Þéttbýli'},
    401: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Ísafjörður',
             'placename_tgf': 'Ísafirði',
             'type': 'Dreifbýli'},
    410: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Hnífsdalur',
             'placename_tgf': 'Hnífsdal',
             'type': 'Þéttbýli'},
    415: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Bolungarvík',
             'placename_tgf': 'Bolungarvík',
             'type': 'Þéttbýli'},
    416: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Bolungarvík',
             'placename_tgf': 'Bolungarvík',
             'type': 'Dreifbýli'},
    420: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Súðavík',
             'placename_tgf': 'Súðavík',
             'type': 'Þéttbýli'},
    421: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Súðavík',
             'placename_tgf': 'Súðavík',
             'type': 'Dreifbýli'},
    425: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Flateyri',
             'placename_tgf': 'Flateyri',
             'type': 'Þéttbýli'},
    426: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Flateyri',
             'placename_tgf': 'Flateyri',
             'type': 'Dreifbýli'},
    430: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Suðureyri',
             'placename_tgf': 'Suðureyri',
             'type': 'Þéttbýli'},
    431: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Suðureyri',
             'placename_tgf': 'Suðureyri',
             'type': 'Dreifbýli'},
    450: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Patreksfjörður',
             'placename_tgf': 'Patreksfirði',
             'type': 'Þéttbýli'},
    451: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Patreksfjörður',
             'placename_tgf': 'Patreksfirði',
             'type': 'Dreifbýli'},
    460: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Tálknafjörður',
             'placename_tgf': 'Tálknafirði',
             'type': 'Þéttbýli'},
    461: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Tálknafjörður',
             'placename_tgf': 'Tálknafirði',
             'type': 'Dreifbýli'},
    465: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Bíldudalur',
             'placename_tgf': 'Bíldudal',
             'type': 'Þéttbýli'},
    466: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Bíldudalur',
             'placename_tgf': 'Bíldudal',
             'type': 'Dreifbýli'},
    470: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Þingeyri',
             'placename_tgf': 'Þingeyri',
             'type': 'Þéttbýli'},
    471: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Þingeyri',
             'placename_tgf': 'Þingeyri',
             'type': 'Dreifbýli'},
    500: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Staður',
             'placename_tgf': 'Stað',
             'type': 'Dreifbýli'},
    510: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Hólmavík',
             'placename_tgf': 'Hólmavík',
             'type': 'Þéttbýli'},
    511: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Hólmavík',
             'placename_tgf': 'Hólmavík',
             'type': 'Dreifbýli'},
    512: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Hólmavík',
             'placename_tgf': 'Hólmavík',
             'type': 'Dreifbýli'},
    520: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Drangsnes',
             'placename_tgf': 'Drangsnesi',
             'type': 'Þéttbýli'},
    524: {   'area': 'Vesturland og Vestfirðir',
             'placename_nf': 'Árneshreppur',
             'placename_tgf': 'Árneshreppi',
             'type': 'Dreifbýli'},
    530: {   'area': 'Norðurland',
             'placename_nf': 'Hvammstangi',
             'placename_tgf': 'Hvammstanga',
             'type': 'Þéttbýli'},
    531: {   'area': 'Norðurland',
             'placename_nf': 'Hvammstangi',
             'placename_tgf': 'Hvammstanga',
             'type': 'Dreifbýli'},
    540: {   'area': 'Norðurland',
             'placename_nf': 'Blönduós',
             'placename_tgf': 'Blönduósi',
             'type': 'Þéttbýli'},
    541: {   'area': 'Norðurland',
             'placename_nf': 'Blönduós',
             'placename_tgf': 'Blönduósi',
             'type': 'Dreifbýli'},
    545: {   'area': 'Norðurland',
             'placename_nf': 'Skagaströnd',
             'placename_tgf': 'Skagaströnd',
             'type': 'Þéttbýli'},
    546: {   'area': 'Norðurland',
             'placename_nf': 'Skagaströnd',
             'placename_tgf': 'Skagaströnd',
             'type': 'Dreifbýli'},
    550: {   'area': 'Norðurland',
             'placename_nf': 'Sauðárkrókur',
             'placename_tgf': 'Sauðárkróki',
             'type': 'Þéttbýli'},
    551: {   'area': 'Norðurland',
             'placename_nf': 'Sauðárkrókur',
             'placename_tgf': 'Sauðárkróki',
             'type': 'Dreifbýli'},
    560: {   'area': 'Norðurland',
             'placename_nf': 'Varmahlíð',
             'placename_tgf': 'Varmahlíð',
             'type': 'Þéttbýli'},
    561: {   'area': 'Norðurland',
             'placename_nf': 'Varmahlíð',
             'placename_tgf': 'Varmahlíð',
             'type': 'Dreifbýli'},
    565: {   'area': 'Norðurland',
             'placename_nf': 'Hofsós',
             'placename_tgf': 'Hofsós',
             'type': 'Þéttbýli'},
    566: {   'area': 'Norðurland',
             'placename_nf': 'Hofsós',
             'placename_tgf': 'Hofsós',
             'type': 'Dreifbýli'},
    570: {   'area': 'Norðurland',
             'placename_nf': 'Fljót',
             'placename_tgf': 'Fljótum',
             'type': 'Dreifbýli'},
    580: {   'area': 'Norðurland',
             'placename_nf': 'Siglufjörður',
             'placename_tgf': 'Siglufirði',
             'type': 'Þéttbýli'},
    581: {   'area': 'Norðurland',
             'placename_nf': 'Siglufjörður',
             'placename_tgf': 'Siglufirði',
             'type': 'Dreifbýli'},
    600: {   'area': 'Norðurland',
             'placename_nf': 'Akureyri',
             'placename_tgf': 'Akureyri',
             'type': 'Þéttbýli'},
    601: {   'area': 'Norðurland',
             'placename_nf': 'Akureyri',
             'placename_tgf': 'Akureyri',
             'type': 'Dreifbýli'},
    602: {   'area': 'Norðurland',
             'placename_nf': 'Akureyri',
             'placename_tgf': 'Akureyri',
             'type': 'Pósthólf'},
    603: {   'area': 'Norðurland',
             'placename_nf': 'Akureyri',
             'placename_tgf': 'Akureyri',
             'type': 'Þéttbýli'},
    610: {   'area': 'Norðurland',
             'placename_nf': 'Grenivík',
             'placename_tgf': 'Grenivík',
             'type': 'Þéttbýli'},
    611: {   'area': 'Norðurland',
             'placename_nf': 'Grímsey',
             'placename_tgf': 'Grímsey',
             'type': 'Þéttbýli'},
    616: {   'area': 'Norðurland',
             'placename_nf': 'Grenivík',
             'placename_tgf': 'Grenivík',
             'type': 'Dreifbýli'},
    620: {   'area': 'Norðurland',
             'placename_nf': 'Dalvík',
             'placename_tgf': 'Dalvík',
             'type': 'Þéttbýli'},
    621: {   'area': 'Norðurland',
             'placename_nf': 'Dalvík',
             'placename_tgf': 'Dalvík',
             'type': 'Dreifbýli'},
    625: {   'area': 'Norðurland',
             'placename_nf': 'Ólafsfjörður',
             'placename_tgf': 'Ólafsfirði',
             'type': 'Þéttbýli'},
    626: {   'area': 'Norðurland',
             'placename_nf': 'Ólafsfjörður',
             'placename_tgf': 'Ólafsfirði',
             'type': 'Dreifbýli'},
    630: {   'area': 'Norðurland',
             'placename_nf': 'Hrísey',
             'placename_tgf': 'Hrísey',
             'type': 'Þéttbýli'},
    640: {   'area': 'Norðurland',
             'placename_nf': 'Húsavík',
             'placename_tgf': 'Húsavík',
             'type': 'Þéttbýli'},
    641: {   'area': 'Norðurland',
             'placename_nf': 'Húsavík',
             'placename_tgf': 'Húsavík',
             'type': 'Dreifbýli'},
    645: {   'area': 'Norðurland',
             'placename_nf': 'Fosshólli',
             'placename_tgf': 'Fosshólli',
             'type': 'Dreifbýli'},
    650: {   'area': 'Norðurland',
             'placename_nf': 'Laugar',
             'placename_tgf': 'Laugum',
             'type': 'Þéttbýli'},
    660: {   'area': 'Norðurland',
             'placename_nf': 'Mývatn',
             'placename_tgf': 'Mývatni',
             'type': 'Dreifbýli'},
    670: {   'area': 'Norðurland',
             'placename_nf': 'Kópasker',
             'placename_tgf': 'Kópaskeri',
             'type': 'Þéttbýli'},
    671: {   'area': 'Norðurland',
             'placename_nf': 'Kópasker',
             'placename_tgf': 'Kópaskeri',
             'type': 'Dreifbýli'},
    675: {   'area': 'Norðurland',
             'placename_nf': 'Raufarhöfn',
             'placename_tgf': 'Raufarhöfn',
             'type': 'Þéttbýli'},
    676: {   'area': 'Norðurland',
             'placename_nf': 'Raufarhöfn',
             'placename_tgf': 'Raufarhöfn',
             'type': 'Dreifbýli'},
    680: {   'area': 'Norðurland',
             'placename_nf': 'Þórshöfn',
             'placename_tgf': 'Þórshöfn',
             'type': 'Þéttbýli'},
    681: {   'area': 'Norðurland',
             'placename_nf': 'Þórshöfn',
             'placename_tgf': 'Þórshöfn',
             'type': 'Dreifbýli'},
    685: {   'area': 'Norðurland',
             'placename_nf': 'Bakkafjörður',
             'placename_tgf': 'Bakkafirði',
             'type': 'Þéttbýli'},
    686: {   'area': 'Norðurland',
             'placename_nf': 'Bakkafjörður',
             'placename_tgf': 'Bakkafirði',
             'type': 'Dreifbýli'},
    690: {   'area': 'Norðurland',
             'placename_nf': 'Vopnafjörður',
             'placename_tgf': 'Vopnafirði',
             'type': 'Þéttbýli'},
    691: {   'area': 'Norðurland',
             'placename_nf': 'Vopnafjörður',
             'placename_tgf': 'Vopnafirði',
             'type': 'Dreifbýli'},
    700: {   'area': 'Austurland',
             'placename_nf': 'Egilsstaðir',
             'placename_tgf': 'Egilsstöðum',
             'type': 'Þéttbýli'},
    701: {   'area': 'Austurland',
             'placename_nf': 'Egilsstaðir',
             'placename_tgf': 'Egilsstöðum',
             'type': 'Dreifbýli'},
    710: {   'area': 'Austurland',
             'placename_nf': 'Seyðisfjörður',
             'placename_tgf': 'Seyðisfirði',
             'type': 'Þéttbýli'},
    711: {   'area': 'Austurland',
             'placename_nf': 'Seyðisfjörður',
             'placename_tgf': 'Seyðisfirði',
             'type': 'Dreifbýli'},
    715: {   'area': 'Austurland',
             'placename_nf': 'Mjóifjörður',
             'placename_tgf': 'Mjóafirði',
             'type': 'Dreifbýli'},
    720: {   'area': 'Austurland',
             'placename_nf': 'Borgarfjörður',
             'placename_tgf': 'Borgarfirði (eystri)',
             'type': 'Dreifbýli'},
    721: {   'area': 'Austurland',
             'placename_nf': 'Borgarfjörður',
             'placename_tgf': 'Borgarfirði (eystri)',
             'type': 'Dreifbýli'},
    730: {   'area': 'Austurland',
             'placename_nf': 'Reyðarfjörður',
             'placename_tgf': 'Reyðarfirði',
             'type': 'Þéttbýli'},
    731: {   'area': 'Austurland',
             'placename_nf': 'Reyðarfjörður',
             'placename_tgf': 'Reyðarfirði',
             'type': 'Dreifbýli'},
    735: {   'area': 'Austurland',
             'placename_nf': 'Eskifjörður',
             'placename_tgf': 'Eskifirði',
             'type': 'Þéttbýli'},
    736: {   'area': 'Austurland',
             'placename_nf': 'Eskifjörður',
             'placename_tgf': 'Eskifirði',
             'type': 'Dreifbýli'},
    740: {   'area': 'Austurland',
             'placename_nf': 'Neskaupstaður',
             'placename_tgf': 'Neskaupstað',
             'type': 'Þéttbýli'},
    741: {   'area': 'Austurland',
             'placename_nf': 'Neskaupsstaður',
             'placename_tgf': 'Neskaupsstað',
             'type': 'Dreifbýli'},
    750: {   'area': 'Austurland',
             'placename_nf': 'Fáskrúðsfjörður',
             'placename_tgf': 'Fáskrúðsfirði',
             'type': 'Þéttbýli'},
    751: {   'area': 'Austurland',
             'placename_nf': 'Fáskrúðsfjörður',
             'placename_tgf': 'Fáskrúðsfirði',
             'type': 'Dreifbýli'},
    755: {   'area': 'Austurland',
             'placename_nf': 'Stöðvarfjörður',
             'placename_tgf': 'Stöðvarfirði',
             'type': 'Þéttbýli'},
    756: {   'area': 'Austurland',
             'placename_nf': 'Stöðvarfjörður',
             'placename_tgf': 'Stöðvarfirði',
             'type': 'Dreifbýli'},
    760: {   'area': 'Austurland',
             'placename_nf': 'Breiðdalsvík',
             'placename_tgf': 'Breiðdalsvík',
             'type': 'Þéttbýli'},
    761: {   'area': 'Austurland',
             'placename_nf': 'Breiðdalsvík',
             'placename_tgf': 'Breiðdalsvík',
             'type': 'Dreifbýli'},
    765: {   'area': 'Austurland',
             'placename_nf': 'Djúpivogur',
             'placename_tgf': 'Djúpavogi',
             'type': 'Þéttbýli'},
    766: {   'area': 'Austurland',
             'placename_nf': 'Djúpivogur',
             'placename_tgf': 'Djúpavogi',
             'type': 'Dreifbýli'},
    780: {   'area': 'Austurland',
             'placename_nf': 'Höfn í Hornafirði',
             'placename_tgf': 'Höfn í Hornafirði',
             'type': 'Þéttbýli'},
    781: {   'area': 'Austurland',
             'placename_nf': 'Höfn í Hornafirði',
             'placename_tgf': 'Höfn í Hornafirði',
             'type': 'Dreifbýli'},
    785: {   'area': 'Austurland',
             'placename_nf': 'Öræfi',
             'placename_tgf': 'Öræfum',
             'type': 'Dreifbýli'},
    800: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Selfoss',
             'placename_tgf': 'Selfossi',
             'type': 'Þéttbýli'},
    801: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Selfoss',
             'placename_tgf': 'Selfossi',
             'type': 'Dreifbýli'},
    802: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Selfoss',
             'placename_tgf': 'Selfossi',
             'type': 'Pósthólf'},
    810: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Hveragerði',
             'placename_tgf': 'Hveragerði',
             'type': 'Þéttbýli'},
    815: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Þorlákshöfn',
             'placename_tgf': 'Þorlákshöfn',
             'type': 'Þéttbýli'},
    816: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Ölfus',
             'placename_tgf': 'Ölfus',
             'type': 'Dreifbýli'},
    820: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Eyrarbakki',
             'placename_tgf': 'Eyrarbakka',
             'type': 'Þéttbýli'},
    825: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Stokkseyri',
             'placename_tgf': 'Stokkseyri',
             'type': 'Þéttbýli'},
    840: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Laugarvatn',
             'placename_tgf': 'Laugarvatni',
             'type': 'Þéttbýli'},
    845: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Flúðir',
             'placename_tgf': 'Flúðum',
             'type': 'Þéttbýli'},
    846: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Flúðir',
             'placename_tgf': 'Flúðum',
             'type': 'Dreifbýli'},
    850: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Hella',
             'placename_tgf': 'Hellu',
             'type': 'Þéttbýli'},
    851: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Hella',
             'placename_tgf': 'Hellu',
             'type': 'Dreifbýli'},
    860: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Hvolsvöllur',
             'placename_tgf': 'Hvolsvelli',
             'type': 'Þéttbýli'},
    861: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Hvolsvöllur',
             'placename_tgf': 'Hvolsvelli',
             'type': 'Dreifbýli'},
    870: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Vík',
             'placename_tgf': 'Vík',
             'type': 'Þéttbýli'},
    871: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Vík',
             'placename_tgf': 'Vík',
             'type': 'Dreifbýli'},
    880: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Kirkjubæjarklaustur',
             'placename_tgf': 'Kirkjubæjarklaustri',
             'type': 'Þéttbýli'},
    881: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Kirkjubæjarklaustur',
             'placename_tgf': 'Kirkjubæjarklaustri',
             'type': 'Dreifbýli'},
    900: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Vestmannaeyjar',
             'placename_tgf': 'Vestmannaeyjum',
             'type': 'Þéttbýli'},
    902: {   'area': 'Suðurland og Reykjanes',
             'placename_nf': 'Vestmannaeyjar',
             'placename_tgf': 'Vestmannaeyjum',
             'type': 'Pósthólf'}
}

def postcodes_for_placename(pn):
    p = pn.lower()
    matches = list()
    
    for k,v in postcodes.items():
        n = v['placename_nf'].lower()
        t = v['placename_tgf'].lower()
        if n == p or t == p:
            matches.append(k)
    
    return matches

def postcodes_for_partial_placename(pn):
    p = pn.lower()
    matches = list()
    
    for k,v in postcodes.items():
        n = v['placename_nf'].lower()
        t = v['placename_tgf'].lower()
        if n.startswith(p) or t.startswith(p):
            matches.append(k)
            
    return matches
