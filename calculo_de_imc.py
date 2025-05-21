nome = input("Digite seu nome: ")

peso = float(input("Digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc =   peso / ( altura*altura )

if imc <= 18.5:
   print(f"{nome}, seu imc é {imc} e voce esta abaixo do peso")

elif imc >= 18.5 and imc <=24.9:

   print(f"{nome}, seu imc é {imc} e voce esta peso normal")

elif imc >= 25.0 and imc <=29.9:

    print(f"{nome}, seu imc é {imc} e voce esta sobrepeso")

elif imc >= 30.0 and imc <= 34.9:

    print(f"{nome}, seu imc é {imc} e voce esta obesidade grau I")

elif imc >= 35.0 and imc <= 39.9:

    print(f"{nome}, seu imc é {imc} e voce esta obesidade grau II")

elif imc >= 40.0 and imc <= 49.9:
    
    print(f"{nome}, seu imc é {imc} e voce estao besidade grau III")

print("-------------------------------------------------------------------------")

print(f"Paciente {nome} sua classificação de imc {imc} ")

print("-------------------------------------------------------------------------")