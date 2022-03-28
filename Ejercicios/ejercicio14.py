# 14. Dada una cadena indicar si es palindromo o no.

def esPalindromo(palabra):
    palabraReves = palabra[::-1]
    if(palabra == palabraReves):
        return True
    else:
        return False
    
def ejercicio14():
    palabra = input("Ingrese una palabra: ")
    
    if esPalindromo(palabra):
        print("Es palíndromo.")
    else:
        print("No es palíndromo.")
        

ejercicio14()
    