import random

# Gera um número aleatório entre 1 e 10
n = random.randint(1, 10)

# Inicializa a variável para controle do jogo
acertou = False

# Loop para permitir várias tentativas
while not acertou:
    x = int(input("Escolha um número entre 1 e 10: "))
    
    if x == n:
        print("Parabéns, você acertou!")
        acertou = True  # Sai do loop
    elif x < n:
        print("Tente novamente, o número é maior.")
    else:  # Aqui, x deve ser maior que n
        print("Tente novamente, o número é menor.")