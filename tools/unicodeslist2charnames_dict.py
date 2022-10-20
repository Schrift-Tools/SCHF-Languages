from datafile import loadData, saveData

yaml_c = loadData('data/characters.yaml')

unicodes_set = ['0410', '0411', '0412', '0413', '0414', '0415', '0400', '0401', '0416', '0417', '0418', '0419', '040D', '041A', '040C', '041B', '041C', '041D', '041E', '041F', '0420', '0421', '0422', '0423', '040E', '0424', '0425', '0427', '0426', '0428', '0429', '040F', '042C', '042A', '042B', '0409', '040A', '0405', '042D', '042E', '042F', '0462', '0472', '0474', '3008', '3009', '2116', '0494', '0495', '049E', '049F', '04A4', '04A5', '04A6', '04A7', '04A8', '04A9', '04AC', '04AD', '04B4', '04B5', '04BC', '04BD', '04BE', '04BF', '04CB', '04CC', '04D2', '04D3', '04DC', '04DD', '04DE', '04DF', '04E0', '04E1', '04E4', '04E5', '04F0', '04F1', '04F4', '04F5', '04F8', '04F9', '04F6', '04F7',]

unicodes_dict = {}

for unicode in unicodes_set:
    for group in yaml_c:
        for char in yaml_c[group]:
            if str(yaml_c[group][char]['unicode']).zfill(4) == unicode:
                unicodes_dict[unicode] = char

[print(f'{k}: {v}') for k, v in unicodes_dict.items()]
