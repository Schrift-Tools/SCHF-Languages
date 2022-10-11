from datafile import loadData, saveData

yaml_c = loadData('data/characters.yaml')

g_list = ['grave', 'acute', 'cedilla', 'dotaccent', 'ring', 'tilde', 'commaturnedmod', 'apostrophemod', 'circumflex', 'caron', 'Ereversed', 'Schwa', 'Zstroke', 'LJ', 'NJ', 'DZ', 'Acaron', 'Dmacronbelow', 'Edotbelow', 'Gcaron', 'Hcaron', 'Hdotbelow', 'Hdieresis', 'Hcedilla', 'Icaron', 'Idotbelow', 'Ndotaccent', 'Ocaron', 'Oogonek', 'Odotbelow', 'Pdotaccent', 'Sdotbelow', 'Tdotbelow', 'Ucaron', 'Udotbelow', 'Xdieresis', 'Ymacron', 'Ytilde', 'Esdescender-cy.loclCHU', 'f_f', 'f_f_i', 'f_f_l', 's_t', 'lj', 'nj', 'eturned', 'schwa', 'fi', 'fl', 'acaron', 'dmacronbelow', 'edotbelow', 'gcaron', 'hcaron', 'hdotbelow', 'hdieresis', 'hcedilla', 'icaron', 'idotbelow', 'ndotaccent', 'ocaron', 'oogonek', 'odotbelow', 'pdotaccent', 'sdotbelow', 'tdotbelow', 'ucaron', 'udotbelow', 'xdieresis', 'ymacron', 'ytilde', 'en-cy.loclBGR', 'esdescender-cy.loclCHU', 'zero.tnum', 'one.tnum', 'two.tnum', 'three.tnum', 'four.tnum', 'five.tnum', 'six.tnum', 'seven.tnum', 'eight.tnum', 'nine.tnum', ]

flatglyphs = {}
for group in yaml_c:
    for char in yaml_c[group]:
        unicode = yaml_c[group][char]['unicode']
        if unicode: 
            flatglyphs[char] = unicode
        else:
            flatglyphs[char] = '----'

unicodes = [[name, f'{flatglyphs[name]:>04}'] for name in g_list]

[print(code[1]) for code in unicodes]
