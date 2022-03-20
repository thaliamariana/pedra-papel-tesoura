# Vamos criar um jogo de pedra, papel e tesoura!
# 1. O usuário irá escolher uma das 3 opções;
# 2. O robô irá, aleatoriamente, escolher uma das 3 opções;
# 3. Na primeira rodada, ganhando ou perdendo, o robô irá sugerir duas novas rodadas;
# 4. Caso o usuário ganhe, o robô irá parabenizá-lo;
# 5. Caso o robô ganhe, o robô irá tirar sarro com o usuário;
# 6. Caso empate, o robô irá fazer uma pergunta retórica.

from jogos import robo_contra_humano

print("Olá, você está iniciando um jogo de pedra, papel e tesoura.")
aceitacao = input("Podemos iniciar? [Responder com s|n]: ")

if aceitacao == "s":
    robo_contra_humano()

else:
    print("Até mais!")
