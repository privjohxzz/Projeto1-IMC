nome = (input("digite seu nome: "))

peso = float(input("digite seu peso: "))

altura = float(input("dgite sua altura: "))

imc = peso/(altura*altura)

if imc < 18.5:
    print(nome,'seu imc é',imc,'abaixo do peso')
elif imc  <24.9:
    print(nome,'seu imc é',imc,'peso normal')
elif imc  <29.9:
    print(nome,'seu imc é',imc,'sobrpeso')
elif imc  <34.9:
    print(nome,'seu imc é',imc,'obesidade grau 1')
elif imc  <39.9:
    print(nome,'seu imc é',imc,'obesidade grau 2')
else:
    print(nome,'seu imc é',imc,'obesidade grau 3')

