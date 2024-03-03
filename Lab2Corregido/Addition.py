def completar_con_ceros(cadena, longitud_deseada):



    if len(cadena) >= longitud_deseada:


        return cadena
    else:

        ceros_necesarios = longitud_deseada - len(cadena)


        return "0" * ceros_necesarios + cadena
def hex_addition(numero1, numero2):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}



    max_length = max(len(numero1), len(numero2))



    numero1 = completar_con_ceros(numero1, max_length)



    numero2 = completar_con_ceros(numero2, max_length)


    result = ""


    carry = 0

    """
    Lo que hace el bucle for es recorrer la longitud maxima de los numeros usando
    el -1 donde os indices comienzan desde 0 y se quiere empezar desde el ultimo dato
    -1 es limite inferior entonces con -1 queremos indicar que queremos llegar hasta el 0
    -1 es el paso o decremento entre cada numero del rango indicando que queremos ir
    disminuyendo de unidad en unidad en las itaraciones
    """

    for ii in range(max_length - 1, -1, -1):


        digit1 = numero1[ii]

        digit2 = numero2[ii]



        val1 = hex_dict[digit1]

        val2 = hex_dict[digit2]



        temp_sum = val1 + val2 + carry


        if temp_sum >= 16:
            carry = 1
            temp_sum -= 16


        else:


            carry = 0



        result = (hex(temp_sum)[2:] + result)


    if carry == 1:


        result = '1' + result


    return result


numero1 = input("Ingrese el primer número hexadecimal: ")
numero2 = input("Ingrese el segundo número hexadecimal: ")



resultado_suma = hex_addition(numero1, numero2)
print("Suma:", resultado_suma)