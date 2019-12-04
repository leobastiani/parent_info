#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

import psutil
import json

process = [psutil.Process()]
while True:
    try:
        new = psutil.Process(process[-1].ppid())
        process.append(new)
    except Exception as e:
        break
with open('C:\\dev\\leo.txt', 'w', encoding='utf-8') as file:
    info = json.dumps([x.cmdline() for x in process])
    print(info)
    file.write(info)


import code
code.interact(local=dict(globals(), **locals()))
