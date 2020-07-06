import toml

def importToml(filename):
    return toml.load(filename)

def merge(dict1, dict2):
    keySet = set(dict1.keys())
    for k, v in dict2.items():
        if k in keySet:
            if dict1[k] == v:
                continue
            elif isinstance(dict1[k], list):
                if v in dict1[k] or (hasattr(v, '__len__') and len(v) == 0):
                    continue
                else:
                    dict1[k].append(v)
            elif isinstance(dict1[k], dict):
                if v == dict1[k] or (hasattr(v, '__len__') and len(v) == 0):
                    continue
                else:
                    dict1[k] = merge(dict1[k], v)
            else:
                dict1[k] = [dict1[k], v]
        else:
            dict1[k] = v
    return dict1


if __name__ == '__main__':
    filenames = ["Pipfile1", "Pipfile"]
    tomlData = {}
    for f in filenames:
        tomlData = merge(tomlData, toml.load(f))
        print(tomlData)