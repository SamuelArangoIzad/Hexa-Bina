def completar_con_ceros(cadena, longitud_deseada):
    if len(cadena) >= longitud_deseada:
        return cadena
    else:
        ceros_necesarios = longitud_deseada - len(cadena)
        return "0" * ceros_necesarios + cadena

def resta_hexadecimal(numero1, numero2):
    diccionario_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                       'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    longitud_maxima = max(len(numero1), len(numero2))

    numero1 = completar_con_ceros(numero1, longitud_maxima)


    numero2 = completar_con_ceros(numero2, longitud_maxima)

    resultado = ""

    prestamo = 0

    for ii in range(longitud_maxima - 1, -1, -1):
        digito1 = numero1[ii]


        digito2 = numero2[ii]

        valor1 = diccionario_hex[digito1]


        valor2 = diccionario_hex[digito2]

        """
        ACA ESTA LO INTERESANTE DONDE SI DIFERENCIA TEMPORAL SUS VALORES CALCULADOS
        TENIENDO EN CUENTA EL PRESTAMO ES NUMERO -NEGATIVO QUIERE DECIR QUE EL NUMERO 1 
        ES MENOR QUE EL NUMERO 2 Y COMO NO HAY SUFICIENTE ACARREO EN POSICIONES ANTERIOR 
        COMPENSA LA DIFERENCIA CON += 16 SOLICITANDO PRESTADO AL DE AL LADO
        PARA COMPENSAR DIFERENCIA NEGATIVA
        
        """



        diferencia_temporal = valor1 - valor2 - prestamo

        if diferencia_temporal < 0:


            prestamo = 1


            diferencia_temporal += 16

        else:
            prestamo = 0



        resultado = (hex(diferencia_temporal)[2:] + resultado)



    return resultado




numero1 = input("Ingrese el primer número hexadecimal: ")
numero2 = input("Ingrese el segundo número hexadecimal: ")

resultado_resta = resta_hexadecimal(numero1, numero2)
print("Resta:", resultado_resta)
