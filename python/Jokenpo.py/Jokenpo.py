import random
import time

opcoes = ["pedra", "papel", "tesoura"]
# Opções do jogo
print("JOGO DO JOKENPÔ")
print("Escolha: pedra, papel ou tesoura")

#Entrada do jogador
jogador =  input("Sua jogada: "). lower().strip()
print ("Jo")
time.sleep(1)
print("ken")
time.sleep(1)
print("pô")

    #Validação da entrada do jogador 
if jogador not in opcoes:
      print("Jogada invalida! Escolha entre pedra,papel, ou tesoura.")
else:
     #Escolha aleatória do computador 
    computador = random.choice(opcoes)
print(f"Computador escolheu: {computador}")
 #Lógica do jogo
if jogador == computador:
  print("Resultado: Empate!")
elif ((jogador == "pedra" and computador == "tesoura") or
          (jogador == "papel" and computador == "pedra") or
          (jogador == "tesoura" and computador == "papel")):
        print("Resultado: Você venceu!")
else:
        print("Resultado: Você perdeu, tente novamente!")


                                                                                                                                                                                                                                                     