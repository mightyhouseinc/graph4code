import json
import sys

with open(sys.argv[1]) as f:
    lines = f.read()

    data = {'repo': sys.argv[1], 'source': lines, 'indexName': 'expressions'}
    with open(sys.argv[2], 'w') as out:
        json.dump(data, out)
    
