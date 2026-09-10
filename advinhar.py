import random

numero_secreto = random.randint(1, 10)
acertou = False

while not acertou:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    
    if chute == numero_secreto:
        print("Parabéns! Você acertou!")
        acertou = True
    else:
        print("Tente novamente!")