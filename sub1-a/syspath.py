%load_ext autoreload
%autoreload 2

import os
import sys
import pprint

import main

pprint.pprint("### main ###")
pprint.pprint(dir(main))

pprint.pprint("### sys.path ###")
pprint.pprint(sys.path)

pprint.pprint("### os.cwd() ###")
pprint.pprint(os.getcwd())

main.hoge()