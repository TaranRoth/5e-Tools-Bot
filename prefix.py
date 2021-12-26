import json

prefix_path = "data/prefixes.json"
def get_prefix(server_id):
    with open(prefix_path, "r") as f:
        prefixes = json.load(f)
    print(prefixes[str(server_id)])
    return prefixes[str(server_id)]

def set_prefix(server_id, prefix):
    with open(prefix_path, "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(server_id)] = prefix

    with open(prefix_path, "w") as f:
        json.dump(prefixes, f)