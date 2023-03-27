from datafile import loadData
from os import listdir

languages = loadData('data/languages.yaml')
texts = [tuple(file[:-4].split(', ')) for file in listdir('texts') if file[-3:] == 'txt']

scripts = {script: set() for language in languages for script in languages[language]['script']}

languages_with_text    = {script: [] for script in scripts}
languages_without_text = {script: [] for script in scripts}

for language, script in texts:
    languages_with_text[script].append(language)

for language in languages:
    for script in languages[language]['script']:
        if language not in languages_with_text[script]:
            languages_without_text[script].append(language)

with open('Languages-with-text-Report.txt', 'w+') as file:
    print('Languages in data with text', file=file)
    for script in languages_with_text:
        print(f'\n{script} ({len(languages_with_text[script])})', file=file)
        for language in sorted(languages_with_text[script]):
            print(f'\t{language}', file=file)

with open('Languages-without-text-Report.txt', 'w+') as file:
    print('Languages in data without text', file=file)
    for script in languages_without_text:
        print(f'\n{script} ({len(languages_without_text[script])})', file=file)
        for language in sorted(languages_without_text[script]):
            print(f'\t{language}', file=file)
