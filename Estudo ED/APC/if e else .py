# programa que avalia a sua altura e peso 





def compara_altura_media(sexo, altura):

    if sexo == 'f':
       
       if altura < 1.62:
           saida = 'baixa'
       else:
           saida = 'alta'
    else:
        if altura < 1.74:
           saida = 'baixo'
        else:
           saida = 'alto'

    return saida

def classifica_imc(peso, altura):

    imc = peso / (altura ** 2)

    if imc < 18.5:
        saida = 'magreza'
    elif 18.5 <= imc <=  24.9:
        saida = 'normal'
    elif 25.0 <= imc <= 29.9 :
        saida = 'sobrepeso'
    elif 30.0 <= imc <= 30.9:
        saida = 'obesidade'
    elif imc > 40.0:
        saida = 'obesidade grave'

    return saida


#entrada de dados 

nome = input("Digire seu nome: ")
sexo = input("Digite seu sexo (m/f): ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso em (KG): "))

print()

print(f" ola {nome}")
print(f" Voce e mais {compara_altura_media(sexo, altura)} do que a media ")
print(f" A sua classifcacao de peso e {classifica_imc(peso, altura)}")
