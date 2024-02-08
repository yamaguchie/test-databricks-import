# %load_ext autoreload
# %autoreload 2

import os
import sys
import pprint
from os.path import abspath
import os
from pathlib import Path
import main

# path = os.path.dirname(os.path.abspath("__file__"))
print("このファイルの場所は？:" , os.path.abspath(''))
# print(Path().resolve())

pprint.pprint("### current1 ###")
pprint.pprint(os.getcwd())

pprint.pprint("### main ###")
pprint.pprint(dir(main))

pprint.pprint("### sys.path ###")
pprint.pprint(sys.path)

pprint.pprint("### os.cwd() ###")
pprint.pprint(os.getcwd())

main.hoge()

print(__name__)