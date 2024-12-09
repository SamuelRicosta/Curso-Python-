#fazer a funçao para calcualar raizes de uma funçao ax^2 + bx + c
#
#ter os valores a b c 
#calcular a raizes 
#




def calcula_delta(a , b, c):
    return (b**2) - (4*a*c)

def calcula_x1(a , b, delta):
    return (-b + (delta ** 0.5)) / (2 * a)

def calcula_x2(a , b, delta):
    return (-b - (delta ** 0.5)) / (2 * a)




def calcular_raizes(a, b, c ):
    delta = calcula_delta(a, b, c)

    if delta < 0:
        print('nao a raizes reuas')

    if delta == 0:
        x = calcula_x1(a, b, delta)
        print(f'x = {x}')

    if delta > 0: 
        x1 = calcula_x1(a, b, delta)
        x2 = calcula_x2(a, b, delta)
        print(f'x1 = {x1}, x2 = {x2}')




print('Vamos calcular as raizes de uma funcao quadratica ax^2 + bx + c.')

a = float(input('coloque o valor de a: '))
b = float(input("coloque o valor de b: "))
c = float(input("coloque o valor de c: "))

print()

calcular_raizes(a, b, c)

