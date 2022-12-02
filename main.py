from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura') #jogadas possíveis
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

def leiaInt(msg): #Função que valida a entrada dos dados
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            if valor < 3:
                ok = True
            else:
                print('\033[0;31mJogada inválida\033[m')
        else:
            print('\033[0;31mJogada inválida\033[m')
        if ok:
            break
    return valor


jogador = leiaInt('Qual a sua jogada? ')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(0.5)
print('-=' * 11)
print('Você jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=' * 11)

if jogador == computador:
    print('EMPATE!')

elif jogador == 0:#Se o jogador escolher pedra
    if computador == 1:
        print('VOCÊ PERDEU!')
    if computador == 2:
        print('VOCÊ GANHOU!')

elif jogador == 1:#Se o jogador escolher papel
    if computador == 2:
        print('VOCÊ PERDEU!')
    if computador == 0:
        print('VOCÊ GANHOU!')

elif jogador == 2:#Se o jogador escolher tesoura
    if computador == 0:
        print('VOCÊ PERDEU!')
    if computador == 1:
        print('VOCÊ GANHOU!')