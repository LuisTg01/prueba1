def suma_recursiva(n,p,c=1):
    if  n == 0: #si n es 0, entonces multiplicará a P * 0 dando en todos los casos 0.
        return 0
    else:
        return (p * c) +  suma_recursiva(n-1,p,c + 1)

p=int(input('Ingrese el valor de P:  '))
n=int(input('Ingrese el valor de N:  '))
 
print(suma_recursiva(p,n))