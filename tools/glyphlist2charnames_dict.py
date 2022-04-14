from datafile import loadData, saveData

yaml_c = loadData('data/characters.yaml')

glyphs_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZĆČŁŃŚŠŬŹŽabcdefghijklmnopqrstuvwxyzćčłńśšŭźž'
charnames_dict = {}

for glyph in glyphs_set:
    for group in yaml_c:
        for char in yaml_c[group]:
            if yaml_c[group][char]['glyph'] == glyph:
                charnames_dict[char] = glyph

[print(f'{k}: {v}') for k, v in charnames_dict.items()]
