from datafile import loadData, saveData

characters = loadData('data/characters.yaml')
languages = loadData('data/languages.yaml')

key = 'glyph'
query = 'Ӱ'

catched = False
for group in characters:
    for char in characters[group]:
        if characters[group][char][key] == query or char == query:
            print('-', group)
            print('-', char, )
            [print(f'\t{k}: {v}') for k, v in characters[group][char].items()]
            catched = char

appears_cyr = set()
appears_lat = set()
for lang in languages:
    for script in languages[lang]['script']:
        for charset in languages[lang]['script'][script]:
            if catched in languages[lang]['script'][script][charset].keys():
                if script == "Latin":
                    appears_lat.add(lang)
                if script == "Cyrillic":
                    appears_cyr.add(lang)

if len(appears_lat): print(f"Latin ({len(appears_lat)}): {', '.join(sorted(appears_lat))}")
if len(appears_cyr): print(f"Cyrillic ({len(appears_cyr)}): {', '.join(sorted(appears_cyr))}")

if not catched:
    print('Nothing was found.')