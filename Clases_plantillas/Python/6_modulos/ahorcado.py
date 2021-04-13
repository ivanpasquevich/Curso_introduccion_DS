import random

def eleccion(lista):
    return random.choice(lista)

def  espacios(palabra):
    return ["_"]*len(palabra)

def  mostrar(lista):
    print(" ".join(lista))
    
def adivinar(palabra,lista):
    letra = input("ingrese una letra: ").lower()
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i]==letra:
                lista[i] = letra
                
def verificar_continuidad(lista):
    return "_" in lista

def main():

    with open("palabras_ahorcado.txt") as file:
        texto = file.read()

    lista_palabras = texto.split(",")

    palabra = eleccion(lista_palabras)

    lista_ = espacios(palabra)

    print (" Hora de jugar, esta es su palabra:")
    mostrar(lista_)

    while verificar_continuidad(lista_):
        adivinar(palabra,lista_)
        mostrar(lista_)

    print(f"Felicidades ha ganado la palabra es {palabra}")
    
    
main()