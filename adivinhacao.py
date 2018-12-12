print("**********************************")
print("*bem vindo ao jogo de adivinhação*")
print("**********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1

# while - início
# while(rodada <= total_tentativas):
for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {} ".format(rodada,total_tentativas))
    chute = input("Digite um número entre 1 e 100: \n")
    chute = int(chute)

    if (chute < 1 or chute > 100):
        print("Número fora da área de tentativas")
        continue

    print("Você digitou ", chute)

    if(numero_secreto == chute):
        print("Você acertou")
        break
    else: 
        if(chute > numero_secreto):
            print("Você errou, o seu chute foi maior que o número secreto")
        elif(chute < numero_secreto):
            print("Você errou, o seu chute foi menor que o número secreto")
# while - fim

