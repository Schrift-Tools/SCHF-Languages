from datafile import loadData, saveData

data = loadData('data/characters.yaml')

idx = 0
for group in data:
    for char in data[group]:
        if data[group][char]['idx'] and data[group][char]['idx'] > idx:
            idx = data[group][char]['idx']
print((idx+1))
        
