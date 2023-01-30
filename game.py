from models.calcular import Calcular

print('\033[107;30;4mJogo feito por: Fernando de Souza Batista\033[40;97;0m')
print('\033[107;30;4mLinkedin: https://www.linkedin.com/in/fernando-batista-208048207/\033[40;97;0m')


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('\033[97mInforme o nivel de dificuldade desejado '
                                 '[\033[34m1 \033[32m2 \033[33m3 \033[31m4\033[97m]: '))

    calc: Calcular = Calcular(dificuldade)

    print(f'Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()  # 5 + 7 = ?

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).')
    while True:
        try:
            continuar: int = int(input('Deseja continuar no jogo?'
                                       ' [1 - \033[32msim\033[97m, 0 - \033[31mnão\033[97m]\n'))
            break
        except:
            print('Valor incorreto! Digite [1] para continuar ou [0] para sair.')

    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou com {pontos} ponto(s).')
        print('Até a proxima!')


if __name__ == '__main__':
    main()

# Feito em 30/01/2023
