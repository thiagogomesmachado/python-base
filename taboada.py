#!/c/Users/z003btsx/AppData/Local/Programs/Python/Python311/python

"""imprime a tabuada do 1 ao 10"""
__version__ ="0.1.0"
__author__ ="thiago"

numeros = list(range(1,11))

for numero in numeros:
    print ("Tabuada do : " ,numero)
    for outro_numero in numeros:
        print(numero, "x" ,outro_numero, "=" ,numero * outro_numero)
    print ("-----------------")


    