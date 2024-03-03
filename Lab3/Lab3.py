def is_prime(numero):
    if numero <= 1:
        return False
    if numero == 2:#El numero especial 2
        return True
    if numero % 2 == 0: #ningun par es primo
        return False
    i = 3
    while i * i <= numero:#raiz cuadrada verificacion del numero
        if numero % i == 0:
            return False
        i += 2 #solo se necesita la verificacion de impares mayores que 2
    return True

def clasificar_numeros():
    enteros=[]
    racionales=[]
    primos=[]
    complejos=[]
    pares=[]
    for i in range(15):
        try:
            entrada = input(f"Numero {i + 1}: ")
            if 'i' in entrada:
                complejos.append(entrada)
            else:
                numero = float(entrada)
                if numero.is_integer():
                    entero = int(numero)
                    enteros.append(entero)
                    if entero % 2 == 0:
                        pares.append(entero)
                    if is_prime(entero):
                        primos.append(entero)
                else:
                    racionales.append(numero)
        except ValueError:
            print("Error: Debes ingresar un número válido.")
    print("Enteros:", enteros)
    print("Racionales:", racionales)
    print("Primos:", primos)
    print("Complejos:", complejos)
    print("Pares:", pares)

clasificar_numeros()
