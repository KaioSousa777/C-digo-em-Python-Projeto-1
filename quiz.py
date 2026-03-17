print("Seja muito bem vindo ao quiz do Kaio!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0 

print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A)Rockstar Games \n (B)Ubisoft \n (C)EA Esports \n (D)Activision \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")


print("Quem é o protagonista do jogo Grand Theft Auto San Andreas? \n (A)Carlos Miguel \n (B)Michael Bieber \n (C)Jonathan James \n (D)Carl Jonhson \n")
answer_1 = input("Resposta: ")

if answer_1 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/2")