try:
    nome = input("Digite seu nome: ")

    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))

    imc = peso / (altura * altura)

    if imc <= 18.5:
        print(f"{nome}, seu IMC é {imc:.2f} e você está abaixo do peso.")
    elif 18.5 < imc <= 24.9:
        print(f"{nome}, seu IMC é {imc:.2f} e você está com peso normal.")
    elif 25.0 <= imc <= 29.9:
        print(f"{nome}, seu IMC é {imc:.2f} e você está com sobrepeso.")
    elif 30.0 <= imc <= 34.9:
        print(f"{nome}, seu IMC é {imc:.2f} e você está com obesidade grau I.")
    elif 35.0 <= imc <= 39.9:
        print(f"{nome}, seu IMC é {imc:.2f} e você está com obesidade grau II.")
    elif imc >= 40.0:
        print(f"{nome}, seu IMC é {imc:.2f} e você está com obesidade grau III.")

    print("-------------------------------------------------------------------------")
    print(f"Paciente {nome}, sua classificação de IMC é {imc:.2f}")
    print("-------------------------------------------------------------------------")

except ZeroDivisionError:
    print("Erro: Certifique-se de digitar números válidos para peso e altura.")
    
with open ("cadastro_imc.txt", "a") as arquivo:
    arquivo.write(f"nome: {nome}\nIMC: {imc:.2f}")
    arquivo.write("\n---------------------------")
