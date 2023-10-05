import json
from sys import argv

with open(argv[1]) as f:
    code = f.read()

obj = {"source": code, "repo": argv[1], "indexName": "index"}
with open(argv[2], "w") as f:
    json.dump(obj, f)

