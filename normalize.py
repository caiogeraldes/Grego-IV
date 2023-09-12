#! /bin/python3

import sys
import unicodedata

try:
    arquivo = sys.argv[1]
except IndexError as e:
    print("epa:", end="")
    sys.exit(e)

with open(arquivo, "r", encoding="utf8") as file:
    texto = file.read()

texto_normalizado = unicodedata.normalize("NFKC", texto)

with open(arquivo, "w", encoding="utf8") as file:
    file.write(texto_normalizado)
