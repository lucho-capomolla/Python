desplazamiento = 3 # ROT3

def codifica(texto):
    cifrado = ""
    if texto == texto.upper():
        lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    else:
        lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    for caracter in texto:
        if caracter in lista:
            cifrado += lista[(lista.index(caracter) + desplazamiento % (len(lista)))] 
        else:
            cifrado += caracter
    print(cifrado)
    return cifrado


def descodifica(texto):
    descifrado = ""
    if texto == texto.upper():
        lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    else:
        lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    for caracter in texto:
        if caracter in lista:
            descifrado += lista[(lista.index(caracter) - desplazamiento % (len(lista)))]
        else:
            descifrado += caracter
    print(descifrado)
    return descifrado


if __name__  == '__main__':
    cifrado = codifica("hola mundo")
    descifrado = descodifica(cifrado)