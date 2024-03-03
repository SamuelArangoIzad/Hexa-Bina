def decimalabinario(numero_decimal):
    numerobinario=0
    multiplicapor=1
    while numero_decimal!=0:
        numerobinario=numerobinario+numero_decimal%2*multiplicapor
        numero_decimal//=2
        multiplicapor*=10
    return numerobinario

print(decimalabinario(5))


def decimal_a_hexadecimal(decimal):
    guia = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = ''

    while decimal > 0:
        contador = decimal % 16

        if contador > 9:
            hex_digit = guia[contador]
        else:
            hex_digit = str(contador)


        hexadecimal = hex_digit + hexadecimal


        decimal //= 16

    return hexadecimal

numero_decimal = 255
print("El número decimal", numero_decimal, "en hexadecimal es:", decimal_a_hexadecimal(numero_decimal))
