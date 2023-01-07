def convertir_recursivo(n,p):
    conversión = '0123456789ABCDEF'

    if n < p:
        return conversión[n]
    else:
        return convertir_recursivo(n//p, p) + conversión[n % p]

numero =int(input("número: "))
base =int(input("Base: "))
resultado= convertir_recursivo(numero,base)
print(resultado)