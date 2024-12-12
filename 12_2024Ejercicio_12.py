#strip que me perimite ingresar una palabra y valida si es palindroma

palabra = input("Dime una palabra ").replace(" ","")
texto = ""
for i in palabra:
    texto = i + texto
    
if(palabra == texto):
    print("Es palindromo")
else:
    print("No es palindroma")