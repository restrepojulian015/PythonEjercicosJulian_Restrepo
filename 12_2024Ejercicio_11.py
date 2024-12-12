# Scrip que reemplaza letras por vocales por simbolos para códificar una frase

texto = input("Digite la frase: ")
textoCifrado = ""

for letra in texto:
    if letra == "A" or letra == "a":
        textoCifrado += "$"
    elif letra == "E" or letra =="e":
        textoCifrado += "@"
    elif letra == "I" or letra =="i":
        textoCifrado += "?"
    elif letra == "O" or letra =="o":
        textoCifrado += "&"
    elif letra == "u" or letra =="u":
        textoCifrado += "#"
    elif letra ==" ":
        textoCifrado += "%"
    else:
        textoCifrado += letra
print(textoCifrado)