from random import randint

LISTA_OPCOES = ["pedra", "papel", "tesoura"]

def input_usuario():
    while True:
        escolha = input("\n\nEscolha uma opção [Pedra, Papel ou Tesoura]: ").lower()
        if escolha in LISTA_OPCOES:
            return escolha
        else:
            print("Opção inválida.")


def input_robo():
    escolha = randint(0,2)
    return LISTA_OPCOES[escolha]


def jogada(jogada1, jogada2): # 0 empate, 1 usuario ganha, 2 robo ganha
    if jogada1 == jogada2:
        return 0
    elif jogada1 == "pedra" and jogada2 == "tesoura":
        return 1
    elif jogada1 == "papel" and jogada2 == "pedra":
        return 1
    elif jogada1 == "tesoura" and jogada2 == "papel":
        return 1
    else:
        return 2


def robo_contra_humano():
    pontos_usuario = 0
    pontos_robo = 0
    rodada = 1

    while rodada <= 3:

        escolha_usuario = input_usuario()
        escolha_robo = input_robo()

        print(f"\n\nEscolha do usuário: {escolha_usuario}. Escolha do robô: {escolha_robo}.")

        match jogada(escolha_usuario, escolha_robo):
            case 0:
                print("\n\nEmpate nesta rodada!")
            case 1:
                print("\n\nVocê venceu esta rodada!")
                pontos_usuario += 1
            case 2:
                print("\n\nO robô venceu nesta rodada!")
                pontos_robo += 1
        
        if rodada == 1:
            nova_rodada = input("\n\nMelhor de três? [Responder com s|n]: ")
            if nova_rodada == "s":
                pass    
            else:
                break
        elif rodada == 3:
            if pontos_usuario > pontos_robo:
                print("\n\nResultado final: Ganhou do robô! Muito bem, não precisa mais selecionar o captcha.")
            elif pontos_robo > pontos_usuario:
                print("\n\nResultado final: Perdeu para o robô. Parabéns, nota 0.")
            else:
                print("\n\nResultado final: Empatou com o robô. Seria você, também, um robô? '-'")

        rodada += 1
