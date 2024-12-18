# Solicitar ao usuário para digitar dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicitar ao usuário para escolher a operação usando sinais (+, -, *, /)
operacao = input("Escolha a operação (+, -, *, /): ")

# Realizar a operação escolhida e mostrar apenas o resultado
if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida.")
