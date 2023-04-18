import json

def load_config(filename):
    with open(filename) as f:
        config = json.load(f)
    return config

print(load_config('BMW_M3.json'))