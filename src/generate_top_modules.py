import json
from glob import glob
import sys
import bz2

analysis_modules = ['BaseException', 'DeprecationWarning', 'Exception',
                    'FutureWarning',
                    'NameError',
                    'None',
                    'RuntimeError',
                    'StopIteration',
                    'TypeError',
                    'UserWarning',
                    'ValueError',
                    '__doc__',
                    '__file__',
                    '__name__',
                    'abs',
                    'all',
                    'any',
                    'bin',
                    'bool',
                    'bytes',
                    'callable',
                    'chr',
                    'complex',
                    'del',
                    'dict',
                    'dir',
                    'divmod',
                    'eval',
                    'exec',
                    'exit',
                    'filter',
                    'float',
                    'format',
                    'frozenset',
                    'get_ipython',
                    'getattr',
                    'globals',
                    'hasattr',
                    'help',
                    'hex',
                    'id',
                    'input',
                    'isinstance',
                    'iter',
                    'locals',
                    'map',
                    'max',
                    'min',
                    'next',
                    'object',
                    'open',
                    'ord',
                    'pow',
                    'print',
                    'property',
                    'repr',
                    'reversed',
                    'set',
                    'super',
                    'tuple',
                    'vars',
                    'NotImplementedError',
                    'Warning',
                    'cd',
                    'clear',
                    'pylab',
                    'RuntimeWarning',
                    'hist',
                    'matplotlib',
                    'recall',
                    'history',
                    'time',
                    'KeyError',
                    'display']
# Arg 1 is the pattern to search for - can be dir/JSON or dir/RDF

for f in glob(sys.argv[1]):
    modules = {}
    if f.endswith('.json'):
        xf = open(f)
    elif f.endswith('.bz2'):
        xf = bz2.open(f)
    with xf as input:
        data = json.load(input)
        for node in data['turtle_analysis']:
            if node is None:
                continue

            if node["is_import"]:
                m = node["path_end"]
                if m in analysis_modules:
                    continue
                if m not in modules:
                    modules[m] = 0
                else:
                    modules[m] += 1

modules = dict(sorted(modules.items(), reverse=True, key=lambda item: item[1]))

max = int(sys.argv[3]) if len(sys.argv) == 4 else len(modules)
counter = 0
with open(sys.argv[2], 'w') as out:
    for m in modules:
        if counter >= max:
            break
        out.write(m + '\n')
        counter += 1


