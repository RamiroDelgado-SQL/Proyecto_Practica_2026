# Pedimos la fecha de nacimiento
anio_nac = int(input("Ingrese su año de nacimiento: "))
mes_nac = int(input("Ingrese su mes de nacimiento (1-12): "))
dia_nac = int(input("Ingrese su día de nacimiento: "))

# Pedimos la fecha actual
anio_actual = int(input("Ingrese el año actual: "))
mes_actual = int(input("Ingrese el mes actual (1-12): "))
dia_actual = int(input("Ingrese el día actual: "))

# Calculamos la edad
edad = anio_actual - anio_nac

# Ajustamos si todavía no cumplió años este año
if (mes_actual < mes_nac) or (mes_actual == mes_nac and dia_actual < dia_nac):
    edad = edad - 1

# Mostramos el resultado
print("Tu edad es:", edad)