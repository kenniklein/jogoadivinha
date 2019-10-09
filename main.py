import random
import os

def conteudo_num_tentados():
    str(num_tentados)
    return str(num_tentados)[1:-1]


while(True):
    os.system('clear')
    print('\n***** Jogo Advinha *****')
    print('\nInstruções: escolha o nível de dificuldade e tente adivinhar o número sorteado!')
    print('\nEscolha a dificuldade\n1 Fácil\n2 Médio\n3 Difícil')
    dificuldade = input('\nDificuldade: ')
    
    try:
      int(dificuldade)
      dificuldade = int(dificuldade)
      if(dificuldade < 1 or dificuldade > 3):
        continue
      break
    except:
      #print('Formato inválido')
      continue 

#dificuldade = int(dificuldade)

intervalo_numeros = []

while(True):
    if(dificuldade == 1):
        tentativas = 5
        num_maximo = 10
        intervalo_numeros.insert(1, num_maximo)
        os.system('clear')
        print('\nVocê escolheu o nível FÁCIL\nVocê tem {} tentativas para acertar o número secreto'.format(tentativas))
        break
    elif(dificuldade == 2):
        tentativas = 3
        num_maximo = 10
        intervalo_numeros.insert(1, num_maximo)
        os.system('clear')
        print('\nVocê escolheu o nível MÉDIO\nVocê tem {} tentativas para acertar o número secreto'.format(tentativas))
        break
    elif(dificuldade == 3):
        tentativas = 3
        num_maximo = 20
        intervalo_numeros.insert(1, num_maximo)
        os.system('clear')
        print('\nVocê escolheu o nível DIFÍCIL\nVocê tem {} tentativas para acertar o número secreto'.format(tentativas))
        break

num_minimo = 1
# num_maximo = 10
intervalo_numeros.insert(0, num_minimo)
intervalo_numeros.insert(1, num_maximo)

num_tentados = list([])

num_secreto = random.randint(num_minimo, num_maximo)

i = 1
while (i <= tentativas):

    while (True):
        chute = input('\nDigite seu chute entre {} a {}: '.format(intervalo_numeros[0], intervalo_numeros[1]))
        try:
            int(chute)
            break
        except:
            print('Formato inválido')

    chute = int(chute)  # transforma em int

    if (chute in num_tentados):
        print('Número já tentado')
        continue

    if (chute < num_minimo or chute > num_maximo):
        num_invalido = True
    else:
        num_invalido = False
        num_tentados.append(chute)

    if (num_invalido):
        print('Número inválido')
        continue

    if (chute == num_secreto):
        os.system('clear')
        print('\nPARABÉNS!\n\nVocê acertou o número secreto:', num_secreto)
        print('\nVocê acertou na tentativa n°', i)
        break

    if (i >= tentativas):
        os.system('clear')
        print('*** GAME OVER ***')
        print('\nVocê tentou {} vezes e não conseguiu acertar o número secreto.'.format(tentativas))
        print('\nNúmeros tentados: {}'.format(conteudo_num_tentados()))
        print('\nO número secreto era:', num_secreto)
        break

    os.system('clear')
    print('\nVocê errou o número secreto. Tente novamente.')

    if (chute < num_secreto):
        print('\nDica: O número secreto é MAIOR que', chute)
    elif (chute > num_secreto):
        print('\nDica: O número secreto é MENOR que', chute)

    print('Números tentados até o momento: {}'.format(conteudo_num_tentados()))

    print('Tentativa(s) restante(s): {}'.format((tentativas - i)))
    i += 1

print('\n***** FIM DO JOGO *****')