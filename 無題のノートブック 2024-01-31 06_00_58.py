# Databricks notebook source

import __init__
import sys
import pprint

pprint.pprint("### sys.path ###")
pprint.pprint(sys.path)

pprint.pprint("### os.cwd() ###")
pprint.pprint(os.getcwd())

pprint.pprint("### PYTHONPATH ###")
pprint.pprint(os.environ["PYTHONPATH"])

pprint.pprint("### env ###")
pprint.pprint(os.environ)

list(os.environ)
print(os.environ.values)
# tmp = os.environ
# pprint.pprint(os.environ)

# print(tmp.keys)




# COMMAND ----------

print(__name__)

# COMMAND ----------

# MAGIC %md
# MAGIC
