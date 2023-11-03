import random
from time import sleep


def wb(a):

    '''
    subir numeros para casas vazias na escolha w

    '''
    som = 0
    for c in range(0,4):
        if li[8+a] == 0:
            li[8+a] = li[12+a]
            li[12+a] = 0
            
        if li[4+a] == 0:
            li[4+a] = li[8+a]
            li[8+a] = 0
            
        if li[0+a] == 0:
            li[0+a] = li[4+a]
            li[4+a] = 0
            
    
def w():

    '''
    algoritmo da escolha 'w' para as 4 colunas
    
    '''
    print('-' * 15)
    
    for c in range(0,4):
        cont = 0
        x = 0
        if li[4+c] == li[0+c] and li[4+c] != 0 and li[0+c] != 0:
            li[0+c] += li[4+c]
            li[4+c] = 0
            
            cont += 1
            wb(c)
            
        if li[8+c] == li[4+c] and li[8+c] != 0 and li[4+c]!= 0:
            li[4+c] += li[8+c]
            li[8+c] = 0
            
            cont += 1
            wb(c)
            
        if li[12+c] ==  li[8+c] and li[12+c] != 0 and li[8+c] != 0:
            li[8+c] += li[12+c]
            li[12+c] = 0
            cont += 1
            wb(c)
            
        if li[12+c] == li[4+c] and li[12+c] != 0 and li[4+c] != 0 and li[8+c] == 0:
            li[4+c] += li[12+c]
            li[12+c] = 0
            
            cont += 1
            wb(c)
            
        if li[8+c] == li[0+c] and li[0+c] != 0 and li[8+c] != 0 and li[4+c] == 0:
            li[0+c] += li[8+c]
            li[8+c] = 0
            
               
            cont += 1
            wb(c)
            
        if li[12+c] == li[0+c] and li[12+c] != 0 and li[0+c] != 0 and li[4+c] == 0 and li[8+c] == 0:
            li[0+c] += li[12+c]
            li[12+c] = 0
            cont += 1
            wb(c)
        if cont == 0:
            wb(c)
        
    p = random.randint(0,len(li) - 1)
    while li[p] != 0:
        p = random.randint(0,len(li) - 1)
    li[p] = 2

        
            
        
    
            
    
            
    print(f'Pontuação:{sum(li)}')
    print(f'[{li[0]:^5}]  [{li[1]:^5}]  [{li[2]:^5}]  [{li[3]:^5}]\n[{li[4]:^5}]  [{li[5]:^5}]  [{li[6]:^5}]  [{li[7]:^5}]\n[{li[8]:^5}]  [{li[9]:^5}]  [{li[10]:^5}]  [{li[11]:^5}]\n[{li[12]:^5}]  [{li[13]:^5}]  [{li[14]:^5}]  [{li[15]:^5}]')


def sb(a):
    '''
    subir numeros para casas vazias na escolha s

    '''
    for c in range(0,4):
        if li[4+a] == 0:
            li[4+a] = li[0+a]
            li[0+a] = 0
        if li[8+a] == 0:
            li[8+a] = li[4+a]
            li[4+a] = 0
        if li[12+a] == 0:
            li[12+a] = li[8+a]
            li[8+a] = 0


def s():
    '''
    algoritmo da escolha 's' para as 4 colunas
    
    '''
    print('-' * 15)
    for c in range(0,4):
        cont = 0
        if li[8+c] == li[12+c] and li[8+c] != 0 and li[12+c] != 0:
            li[12+c] += li[8+c]
            li[8+c] = 0
            cont += 1
            sb(c)
            
        if li[8+c] == li[4+c] and li[8+c] != 0 and li[4+c]!= 0:
            li[8+c] += li[4+c]
            li[4+c] = 0
            cont += 1
            sb(c)
            
        
        if li[0+c] ==  li[4+c] and li[0+c] != 0 and li[4+c] != 0:
            li[4+c] += li[0+c]
            li[0+c] = 0
            cont += 1
            sb(c)
            
        if li[0+c] == li[8+c] and li[0+c] != 0 and li[8+c] != 0 and li[4+c] == 0:
            li[8+c] += li[0+c]
            li[0+c] = 0
            sb(c)
        if li[4+c] == li[12+c] and li[4+c] != 0 and li[12+c] != 0 and li[8+c] == 0:
            li[12+c] += li[4+c]
            li[4+c] = 0
            cont += 1
            sb(c)
        if li[12+c] == li[0+c] and li[12+c] != 0 and li[0+c] != 0 and li[4+c] == 0 and li[8+c] == 0:
            li[12+c] += li[0+c]
            li[0+c] = 0
            sb(c)
            cont += 1
        if cont == 0:
            sb(c)
    p = random.randint(0,len(li) - 1)
    while li[p] != 0:
        p = random.randint(0,len(li) - 1)
    li[p] = 2       





    print(f'Pontuação:{sum(li)}')
    print(f'[{li[0]:^5}]  [{li[1]:^5}]  [{li[2]:^5}]  [{li[3]:^5}]\n[{li[4]:^5}]  [{li[5]:^5}]  [{li[6]:^5}]  [{li[7]:^5}]\n[{li[8]:^5}]  [{li[9]:^5}]  [{li[10]:^5}]  [{li[11]:^5}]\n[{li[12]:^5}]  [{li[13]:^5}]  [{li[14]:^5}]  [{li[15]:^5}]')


def db(a):
    '''
    subir numeros para casas vazias na escolha d

    '''
    for c in range(0,4):
        if li[3+a] == 0:
            li[3+a] = li[2+a]
            li[2+a] = 0
        if li[2+a] == 0:
            li[2+a] = li[1+a]
            li[1+a] = 0
        if li[1+a] == 0:
            li[1+a] = li[0+a]
            li[0+a] = 0


def d():

    '''
    algoritmo da escolha 'd' para as 4 colunas
    
    '''
    print('-' * 15)
    
    for c in range(0,13,4):
        cont = 0
        if li[3+c] == li[2+c] and li[3+c] != 0 and li[2+c] != 0:
            li[3+c] += li[2+c]
            li[2+c] = 0
            
            cont += 1
            db(c)
            
        if li[1+c] == li[2+c] and li[1+c] != 0 and li[2+c]!= 0:
            li[2+c] += li[1+c]
            li[1+c] = 0
            
            cont += 1
            db(c)
            
        if li[1+c] ==  li[0+c] and li[1+c] != 0 and li[0+c] != 0:
            li[1+c] += li[0+c]
            li[0+c] = 0
            cont += 1
            db(c)
            
        if li[0+c] == li[2+c] and li[0+c] != 0 and li[2+c] != 0 and li[1+c] == 0:
            li[2+c] += li[0+c]
            li[0+c] = 0
            
            cont += 1
            db(c)
            
        if li[1+c] == li[3+c] and li[1+c] != 0 and li[3+c] != 0 and li[2+c] == 0:
            li[3+c] += li[1+c]
            li[1+c] = 0
            
               
            cont += 1
            db(c)
            
        if li[0+c] == li[3+c] and li[0+c] != 0 and li[3+c] != 0 and li[1+c] == 0 and li[2+c] == 0:
            li[3+c] += li[0+c]
            li[0+c] = 0
            cont += 1
            db(c)
        if cont == 0:
            db(c)
    p = random.randint(0,len(li) - 1)
    while li[p] != 0:
        p = random.randint(0,len(li) - 1)
    li[p] = 2


    print(f'Pontuação:{sum(li)}')
    print(f'[{li[0]:^5}]  [{li[1]:^5}]  [{li[2]:^5}]  [{li[3]:^5}]\n[{li[4]:^5}]  [{li[5]:^5}]  [{li[6]:^5}]  [{li[7]:^5}]\n[{li[8]:^5}]  [{li[9]:^5}]  [{li[10]:^5}]  [{li[11]:^5}]\n[{li[12]:^5}]  [{li[13]:^5}]  [{li[14]:^5}]  [{li[15]:^5}]')


def ab(a):
    '''
    subir numeros para casas vazias na escolha d

    '''
    for c in range(0,4):
        if li[0+a] == 0:
            li[0+a] = li[1+a]
            li[1+a] = 0
        if li[1+a] == 0:
            li[1+a] = li[2+a]
            li[2+a] = 0
        if li[2+a] == 0:
            li[2+a] = li[3+a]
            li[3+a] = 0


def a():

    '''
    algoritmo da escolha 'a' para as 4 colunas
    
    '''
    print('-' * 15)
    
    for c in range(0,13,4):
        cont = 0
        if li[0+c] == li[1+c] and li[0+c] != 0 and li[1+c] != 0:
            li[0+c] += li[1+c]
            li[1+c] = 0
            
            cont += 1
            ab(c)
            
        if li[1+c] == li[2+c] and li[1+c] != 0 and li[2+c]!= 0:
            li[1+c] += li[2+c]
            li[2+c] = 0
            
            cont += 1
            ab(c)
            
        if li[2+c] ==  li[3+c] and li[2+c] != 0 and li[3+c] != 0:
            li[2+c] += li[3+c]
            li[3+c] = 0
            cont += 1
            ab(c)
            
        if li[3+c] == li[1+c] and li[3+c] != 0 and li[1+c] != 0 and li[2+c] == 0:
            li[1+c] += li[3+c]
            li[3+c] = 0
            
            cont += 1
            ab(c)
            
        if li[2+c] == li[0+c] and li[2+c] != 0 and li[0+c] != 0 and li[1+c] == 0:
            li[0+c] += li[2+c]
            li[2+c] = 0
            
               
            cont += 1
            ab(c)
            
        if li[0+c] == li[3+c] and li[0+c] != 0 and li[3+c] != 0 and li[1+c] == 0 and li[2+c] == 0:
            li[0+c] += li[3+c]
            li[3+c] = 0
            cont += 1
            ab(c)
        if cont == 0:
            ab(c)
    p = random.randint(0,len(li) - 1)
    while li[p] != 0:
        p = random.randint(0,len(li) - 1)
    li[p] = 2


    print(f'Pontuação:{sum(li)}')
    print(f'[{li[0]:^5}]  [{li[1]:^5}]  [{li[2]:^5}]  [{li[3]:^5}]\n[{li[4]:^5}]  [{li[5]:^5}]  [{li[6]:^5}]  [{li[7]:^5}]\n[{li[8]:^5}]  [{li[9]:^5}]  [{li[10]:^5}]  [{li[11]:^5}]\n[{li[12]:^5}]  [{li[13]:^5}]  [{li[14]:^5}]  [{li[15]:^5}]')


# sistema principal
print('_' * 55)
print('        -BEM VINDO AO 2048-          ')
reset = '1'
while reset == '1':
    print()
    opc = input('''Digite qual opcção de jogo voce deseja:
[1] até chegar em 2048
[2] jogo livre
opcao:''').lower().strip()[0]
    while opc not in '12':
        print('opção invalida . . . ')
        opc = input('pfv digite [1] ou [2]:').lower().strip()[0]
    li = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for c in range(0,3):
        p = random.randint(0,len(li) - 1)
        while li[p] != 0:
            p = random.randint(0,len(li) - 1)
        li[p] = 2
    print(f'Pontuação:{sum(li)}')
    print(f'[{li[0]:^5}]  [{li[1]:^5}]  [{li[2]:^5}]  [{li[3]:^5}]\n[{li[4]:^5}]  [{li[5]:^5}]  [{li[6]:^5}]  [{li[7]:^5}]\n[{li[8]:^5}]  [{li[9]:^5}]  [{li[10]:^5}]  [{li[11]:^5}]\n[{li[12]:^5}]  [{li[13]:^5}]  [{li[14]:^5}]  [{li[15]:^5}]')

    if opc == '2':
            while sum(li) != 10000:
                jogada = input('jogada [W/A/S/D]:').lower().strip()
                while jogada not in 'wasd':
                    print('essa jogada não é valida... pfv digite [W/A/S/D]')
                    jogada = input('jogada:').lower().strip()
                if jogada == 'w':
                    w()
                if jogada == 's':
                    s()
                if jogada == 'd':
                    d()
                if jogada == 'a':
                    a()
                if li.count(0) == 0:
                    break
            print('=' * 15)
            print('''não tem mais opções de jogadas
voce perdeu !'''.title())
            sleep(1)
            print()
            reset = input('''[ 1 ] reiciniar
[ 2 ] sair
        opção:''')
            while reset not in '12':
                print('opção invalida . . . ')
                reset = input('pfv digite [1] ou [2]:').lower().strip()[0]
            if reset == '2':
                print()
                print('Obrigado por jogar ! s2')
                print()
    if opc == '1':
        while sum(li) != 50000:
            if 2048 in li:
                print('Parabens ! voce conseguiu vencer o jogo !')
                print('s2 ' * 20)
                break
            jogada = input('jogada [W/A/S/D]:').lower().strip()
            while jogada not in 'wasd':
                print('essa jogada não é valida... pfv digite [W/A/S/D]')
                jogada = input('jogada:').lower().strip()
            if jogada == 'w':
                w()
            if jogada == 's':
                s()
            if jogada == 'd':
                d()
            if jogada == 'a':
                a()
            if li.count(0) == 0:
                print('=' * 15)
                print('''não tem mais opções de jogadas
        voce perdeu !'''.title())
                sleep(1)
                print()
                break
        reset = input('''[ 1 ] reiciniar
[ 2 ] sair
opção:''')
        while reset not in '12':
            print('opção invalida . . . ')
            reset = input('pfv digite [1] ou [2]:').lower().strip()[0]
        if reset == '2':
            print()
            print('Obrigado por jogar ! s2')
            print()
