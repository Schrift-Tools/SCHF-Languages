from random import randint
from datafile import loadData, saveData

yaml_l = loadData('data/languages.yaml')
yaml_c = loadData('data/characters.yaml')

def checkQuit(query):
    if query.lower() == "q":
        print('See you later!')
        exit()

def typeIt(something, ask4change=False, can_quit=True):
    if ask4change and can_quit:
        typed = input(f'Warning: {something} is already in the data! Should we change it? — "y" for yes, "n" for no (or "q" for quit): ').strip()
        checkQuit(typed)
        return typed
    elif can_quit:
        typed = input(f'Enter {something} (or "q" for quit): ').strip()
        checkQuit(typed)
        return typed
    if not can_quit:
        typed = input(f'Enter {something}: ').strip()
        return typed

def isThere(query, yaml_dict, key1=None, key2=None, key3=None):
    report = False
    if key1 is None and key2 is None:
        for k_v0 in yaml_dict:
            if query == k_v0:
                report = k_v0
    elif key2 is None:
        for k_v0 in yaml_dict:
            for k_v1 in yaml_dict[k_v0][key1]:
                if query == k_v1:
                    report = k_v0
    elif key1 is None:
        for k_v0 in yaml_dict:
            for k_v1 in yaml_dict[k_v0]:
                for k_v2 in yaml_dict[k_v0][k_v1][key2]:
                    if query == k_v2 and '.' not in k_v1:
                        report = k_v1
    return report

def buildCharset(script):
    builded_charset = {'base': {}, 'extra': {}, 'modifiers': {}}
    for charset in builded_charset.keys():
        check_passed = False
        while not check_passed:
            characters = typeIt(f'{charset} characters for {script} script, space separated', can_quit=False).replace('\n', '')
            for glyph in characters.split(' '):
                if len(glyph) <= 1:
                    check_passed = True
                else:
                    check_passed = False
                    print(f'[{glyph}] is not a single character! Try again.')
        for glyph in characters.split(' '):
            if glyph != '':
                name = isThere(glyph, yaml_c, key2='glyph')
                if not name: name = f'unknown{randint(0, 9999):04}'
                builded_charset[charset][name] = glyph
    return builded_charset

name = typeIt('Language name').title()

check_passed = False
change_mode = False
while not check_passed:
    if name == '':
        name = typeIt('Language name').title()
    elif isThere(name, yaml_l):
        change_mode = typeIt(name, ask4change=True).title()
        if change_mode.lower() == 'n':
            change_mode = False
            name = typeIt('Language name').title()
        elif change_mode.lower() == 'y':
            change_mode = True
            check_passed = True
    else:
        check_passed = True

iso6393 = typeIt('ISO 639-3').casefold()
while isThere(iso6393, yaml_l, 'codes', 'ISO-6393') and not change_mode:
    print(f'"{iso6393}" already belongs to {isThere(iso6393, yaml_l, "codes", "ISO-6393")}')
    iso6393 = typeIt('ISO 639-3').casefold()

ot = typeIt('opentype tag').upper()
while isThere(ot, yaml_l, 'codes', 'opentype tag') and not change_mode:
    print(f'"{ot}" already belongs to {isThere(ot, yaml_l, "codes", "opentype tag")}')
    ot = typeIt('opentype tag').upper()

wiki = typeIt('wikicode').casefold()
while isThere(wiki, yaml_l, 'codes', 'wikicode') and not change_mode:
    print(f'"{wiki}" already belongs to {isThere(wiki, yaml_l, "codes", "wikicode")}')
    wiki = typeIt('wikicode').casefold()

altnames = [n.strip() for n in typeIt('alternative Language names if any, comma separated').title().split(',') if n != '']
family = typeIt('Language family').title()
while True:
    try:
        speakers = int(typeIt('count of speakers'))
        break
    except ValueError:
        print("Please enter a number!")
status = typeIt('status')
resources = [n.strip() for n in typeIt('internet resources as urls, comma separated').split(',') if n != '']

print(f'\
name:      {name}\n\
iso6393:   {iso6393}\n\
ot:        {ot}\n\
wiki:      {wiki}\n\
altnames:  {", ".join(altnames)}\n\
family:    {family}\n\
speakers:  {speakers}\n\
status:    {status}\n\
resources: {", ".join(resources)}\n')

scripts = typeIt('"l" for Latin script, "c" for Cyrillic, lc for both').casefold()
while scripts not in ['l', 'c', 'lc', 'cl']:
    scripts = typeIt('"l" for Latin script, "c" for Cyrillic, lc for both').casefold()

if scripts == 'l':
    scripts = {"Latin": buildCharset('Latin')}
elif scripts == 'c':
    scripts = {"Cyrillic": buildCharset('Cyrillic')}
else:
    scripts = {
        "Latin": buildCharset('Latin'),
        "Cyrillic": buildCharset('Cyrillic')
        }

check_passed = False
while not check_passed:
    print('\nCheck the names:')
    for script in scripts.keys():
        for charset in scripts[script]:
            print(f' {charset} {script}:')
            [print(f' | {char_name}: {glyph}') for char_name, glyph in scripts[script][charset].items()]
    y_or_n = 0
    while y_or_n not in ['y', 'n']:
        y_or_n = typeIt('"y" if character names are correct and "n" if you want to change them').casefold()
    if y_or_n == 'y':
        yaml_l[name] = {
            'codes': {
                'ISO-6393': iso6393,
                'opentype tag': ot,
                'wikicode': wiki},
            'info': {
                'alternative names': altnames,
                'language family': family,
                'speakers': speakers,
                'status': status,
                'wiki & other sourses': resources},
            'script': scripts,
        }
        check_passed = True
        saveData(yaml_l, 'data/languages.yaml')
        print(f'{name} was written into the data!\n')
    else:
        catched = False
        while not catched:
            charname = typeIt('character name you want to change').strip()
            for script in scripts.keys():
                for charset in scripts[script].keys():
                    if charname in scripts[script][charset].keys():
                        new_charname = typeIt('new character name').strip()
                        scripts[script][charset][new_charname] = scripts[script][charset][charname]
                        del(scripts[script][charset][charname])
                        catched = True
                        print('Done!\n')
            if not catched: print(f'Can\'t find "{charname}", try again!')