def seguridad(A, B, C):

    acceso_autorizado = A and not B and not C
    alerta_seguridad = not A or C
    evacuacion_obligatoria = B or C

    X = acceso_autorizado
    Y = alerta_seguridad
    Z = evacuacion_obligatoria
    return X, Y, Z
A = True
B = False
C = False

X, Y, Z = seguridad(A, B, C)

print("Acceso autorizado:", X)
print("Alerta de seguridad:", Y)
print("Evacuación obligatoria:", Z)
