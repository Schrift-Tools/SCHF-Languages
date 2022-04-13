import yaml

def saveData(data, filepath):
    with open(filepath, 'w') as yamlfile:
        print(yaml.dump(data, allow_unicode=True, width=float("inf"), indent=4), file=yamlfile)

def loadData(filepath):
    with open(filepath, 'r') as yamlfile:
        return yaml.safe_load(yamlfile)