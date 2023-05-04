#!/c/Users/z003btsx/AppData/Local/Programs/Python/Python311/python
"""Hello world multi linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python helloword.py
    ./helloword.py
"""
__version__ = "0.0.1"
__author__ = "TGM"
__license__ ="unlicense"
# dunder - dois underlines, nome sugestivo para facilitar.

import os

current_language =os.getenv("LANG","en_US")[:5]
msg="Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)