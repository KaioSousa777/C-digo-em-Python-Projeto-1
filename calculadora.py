numero1 = float (input("Digite o primeiro numero: "))
numero2 = float (input("Digite o segundo numero: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operação = input("Digite o número da operação desejada: ")

if operação == '1':
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")
elif operação == '2':
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operação == '3':
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operação == '4':
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")