from copy import deepcopy
import random
import os
import time
def mostrarTablero(tablero):
    print()
    for i in range(8):
        print('                         +----+----+----+----+----+----+----+----+')
        print('                         |',tablero[i][0],'|',tablero[i][1],'|',tablero[i][2],'|',tablero[i][3],'|',tablero[i][4],'|',tablero[i][5],'|',tablero[i][6],'|',tablero[i][7],'|')
    print('                         +----+----+----+----+----+----+----+----+')
    print()

def asignarMinas(tablero):
    cont=0
    while cont!=10:
        num1=random.randrange(0,8)
        num2=random.randrange(0,8)
        if tablero[num1][num2] =='💣':
            continue
        else:
            tablero[num1][num2]='💣'
            cont+=1

def contMinas(tablero,fila,columna):
    contMinas = 0 
    for i in range(-1,2):
        for x in range(-1,2):
            if fila+i > 7 or columna+x > 7 or fila+i < 0 or columna+x < 0:
                continue
            elif tablero[fila+i][columna+x] == '💣':
                contMinas+=1
    if fila > 7 or columna > 7 or fila < 0 or columna < 0:
        pass
    else:
        if tablero[fila][columna] != '💣' and tablero[fila][columna] != '  ':
            pass 
        else:
            return contMinas



def autoPoner(tablero,tableroSinMinas,columna,fila):
    ceros = [(fila,columna)]
    while len(ceros) > 0:
        fila,columna = ceros.pop()
        for i in range(-1,2):
            for x in range(-1,2):
                if fila+i > 7 or columna+x > 7 or fila+i < 0 or columna+x < 0:
                    continue
                elif tablero[fila+i][columna+x] == '  ':
                    if contMinas(tablero,fila+i,columna+x) == 0:
                        tablero[fila+i][columna+x]=' 0'
                        tableroSinMinas[fila+i][columna+x]=' 0'
                        if (fila+i,columna+x)not in ceros:
                            ceros.append((fila+i,columna+x))
                    else:
                        tableroSinMinas[fila+i][columna+x] = ' '+str(contMinas(tablero,fila+i,columna+x))
                        tablero[fila+i][columna+x] = ' '+str(contMinas(tablero,fila+i,columna+x))
                else:
                    continue

tablero = [[ '  ' for i in range(8)] for i in range(8)]
tableroSinMinas = deepcopy(tablero)
asignarMinas(tablero)
os.system('cls')
print('''
                                    . . .                         
                                     \|/                          
                                   `--+--'                        
                                     /|\                          
                                    ' | '                         
                                      |                           
                                  ,--'#`--.                       
                                  |#######|                       
                               _.-'#######`-._                    
                            ,-'###############`-.                 
                          ,'#####################`,               
                         /#########################\              
                        |###########################|             
                       |#############################|                        
                       |#############################|            
                       |#############################|            
                        |###########################/             
                         \#########################/              
                          `.#####################,'               
                            `._###############_,'                 
                               `--..#####..--'             
         ____  _    _  _____  _____          __  __ _____ _   _           _____ 
        |  _ \| |  | |/ ____|/ ____|   /\   |  \/  |_   _| \ | |   /\    / ____|
        | |_) | |  | | (___ | |       /  \  | \  / | | | |  \| |  /  \  | (___  
        |  _ <| |  | |\___ \| |      / /\ \ | |\/| | | | |     | / /\ \  \___ \ 
        | |_) | |__| |____) | |____ / ____ \| |  | |_| |_| |\  |/ ____ \ ____) |
        |____/ \____/|_____/ \_____/_/    \_\_|  |_|_____|_| \_/_/    \_\_____/ 

    ''')
print('El objetivo del juego Buscaminas es liberar todas las casillas que no tienen una mina.\nEl tablero es de 8x8 y en el habran 10 minas que deberas de evitar.\nLas casillas con número indican la cantidad de minas en las casillas que la rodean.\nLas banderas te serviran de referencia a ti mismo para saber donde puede haber una mina, estas las podras desplegar por todo el tablero.\nPara poder moverte por el tablero necesitaras de las teclas W/A/S/D, pero no se leeran automaticamente tendras que pulsar el enter para moverte.\nPara confirmar la posicion que quieres elejir deberas pular espacio y luego enter\nMucha suerte!!!')
print()
input('Dale a enter para empezar: ')
os.system('cls')
while True:   
    tableroFlecha = deepcopy(tableroSinMinas)
    os.system('cls')
    print('''
         ____  _    _  _____  _____          __  __ _____ _   _           _____ 
        |  _ \| |  | |/ ____|/ ____|   /\   |  \/  |_   _| \ | |   /\    / ____|
        | |_) | |  | | (___ | |       /  \  | \  / | | | |  \| |  /  \  | (___  
        |  _ <| |  | |\___ \| |      / /\ \ | |\/| | | | |     | / /\ \  \___ \ 
        | |_) | |__| |____) | |____ / ____ \| |  | |_| |_| |\  |/ ____ \ ____) |
        |____/ \____/|_____/ \_____/_/    \_\_|  |_|_____|_| \_/_/    \_\_____/ 

    ''')
    mostrarTablero(tableroSinMinas)                                                        
    bandera=input('Quieres poner una bandera?:\ns = Poner Bandera\nn = Quitar Bandera\nj = Juagar\nsalir = Sales del buscaminas\nElije: ').lower()
    os.system('cls')
    emojisList=['😀','😃','😄','😁','😆','😅','😂','🤣','🥲','☺️','😊','😇','🙂','🙃','😉','😌','😍','🥰','😘','😗','😙','😚','😋','😛','😝','😜','🤪','🤨','🧐','🤓','😎','🥸','🤩','🥳','😏','😒','😞','😔','😟','😕','🙁','☹️','😣','😖','😫','😩','🥺','😢','😭','😤','😠','😡','🤬','🤯','😳','🥵','🥶','😱','😨','😰','😥','😓','🤗','🤔','🤭','🤫','🤥','😶','😐','😑','😬','🙄','😯','😦','😧','😮','😲','🥱','😴','🤤','😪','😵','🤐','🥴','🤢','🤮','🤧','😷','🤒','🤕','🤑','🤠','😈','👿','👹','👺','🤡','💩','👻','💀','☠️','👽','👾','🤖','🎃','😺','😸','😹','😻','😼','😽','🙀','😿','😾']
    if bandera == 's':
        fila = 0
        columna = 0
        posAnterior=tableroFlecha[fila][columna]
        movFich = 0
        emojiRandom=emojisList[random.randrange(0,len(emojisList))]
        tableroFlecha[fila][columna] = emojiRandom
        print('''
         ____  _    _  _____  _____          __  __ _____ _   _           _____ 
        |  _ \| |  | |/ ____|/ ____|   /\   |  \/  |_   _| \ | |   /\    / ____|
        | |_) | |  | | (___ | |       /  \  | \  / | | | |  \| |  /  \  | (___  
        |  _ <| |  | |\___ \| |      / /\ \ | |\/| | | | |     | / /\ \  \___ \ 
        | |_) | |__| |____) | |____ / ____ \| |  | |_| |_| |\  |/ ____ \ ____) |
        |____/ \____/|_____/ \_____/_/    \_\_|  |_|_____|_| \_/_/    \_\_____/ 

        ''')          
        mostrarTablero(tableroFlecha)
        while movFich != ' ':
            emojiRandom=emojisList[random.randrange(0,len(emojisList))]
            tableroFlecha[fila][columna] = posAnterior
            movFich = input('Donde quieres moverte usando W/A/S/D: ').lower()
            if movFich == 'w' and fila <= 7 and fila >= 0:
                fila-=1
            elif movFich == 's' and fila <= 7 and fila >= 0:
                fila+=1
            elif movFich == 'a' and columna <= 7 and columna >= 0:
                columna-=1
            elif movFich == 'd' and columna <= 7 and columna >= 0:
                columna+=1
            else:
                continue
            posAnterior=tableroFlecha[fila][columna]
            tableroFlecha[fila][columna] = emojiRandom
            os.system('cls')
            print('''
         ____  _    _  _____  _____          __  __ _____ _   _           _____ 
        |  _ \| |  | |/ ____|/ ____|   /\   |  \/  |_   _| \ | |   /\    / ____|
        | |_) | |  | | (___ | |       /  \  | \  / | | | |  \| |  /  \  | (___  
        |  _ <| |  | |\___ \| |      / /\ \ | |\/| | | | |     | / /\ \  \___ \ 
        | |_) | |__| |____) | |____ / ____ \| |  | |_| |_| |\  |/ ____ \ ____) |
        |____/ \____/|_____/ \_____/_/    \_\_|  |_|_____|_| \_/_/    \_\_____/ 

            ''')          
            mostrarTablero(tableroFlecha)
            tableroFlecha[fila][columna] = '  '
        tableroSinMinas[fila][columna]='🚩'
        tablero[fila][columna]='🚩'
    elif bandera == 'n':
        fila = 0
        columna = 0
        posAnterior=tableroFlecha[fila][columna]
        movFich = 0
        emojiRandom=emojisList[random.randrange(0,len(emojisList))]
        tableroFlecha[fila][columna] = emojiRandom
        print('''
         ____  _    _  _____  _____          __  __ _____ _   _           _____ 
        |  _ \| |  | |/ ____|/ ____|   /\   |  \/  |_   _| \ | |   /\    / ____|
        | |_) | |  | | (___ | |       /  \  | \  / | | | |  \| |  /  \  | (___  
        |  _ <| |  | |\___ \| |      / /\ \ | |\/| | | | |     | / /\ \  \___ \ 
        | |_) | |__| |____) | |____ / ____ \| |  | |_| |_| |\  |/ ____ \ ____) |
        |____/ \____/|_____/ \_____/_/    \_\_|  |_|_____|_| \_/_/    \_\_____/ 

        ''')          
        mostrarTablero(tableroFlecha)
        while movFich != ' ':
            emojiRandom=emojisList[random.randrange(0,len(emojisList))]
            tableroFlecha[fila][columna] = posAnterior
            movFich = input('Donde quieres moverte usando W/A/S/D: ').lower()
            if movFich == 'w' and fila <= 7 and fila >= 0:
                fila-=1
            elif movFich == 's' and fila <= 7 and fila >= 0:
                fila+=1
            elif movFich == 'a' and columna <= 7 and columna >= 0:
                columna-=1
            elif movFich == 'd' and columna <= 7 and columna >= 0:
                columna+=1
            else:
                continue
            posAnterior=tableroFlecha[fila][columna]
            tableroFlecha[fila][columna] = emojiRandom
            os.system('cls')
            print('''
         ____  _    _  _____  _____          __  __ _____ _   _           _____ 
        |  _ \| |  | |/ ____|/ ____|   /\   |  \/  |_   _| \ | |   /\    / ____|
        | |_) | |  | | (___ | |       /  \  | \  / | | | |  \| |  /  \  | (___  
        |  _ <| |  | |\___ \| |      / /\ \ | |\/| | | | |     | / /\ \  \___ \ 
        | |_) | |__| |____) | |____ / ____ \| |  | |_| |_| |\  |/ ____ \ ____) |
        |____/ \____/|_____/ \_____/_/    \_\_|  |_|_____|_| \_/_/    \_\_____/ 

            ''')          
            mostrarTablero(tableroFlecha)
            tableroFlecha[fila][columna] = '  '
        if tableroSinMinas[fila][columna] == '🚩':
            tableroSinMinas[fila][columna] = '  '
            tablero[fila][columna] = '  '
        else:
            print('NO HAY BANDERA')
            time.sleep(2)
        os.system('cls')
    elif bandera == 'j':
        fila = 0
        columna = 0
        posAnterior=tableroFlecha[fila][columna]
        movFich = 0
        emojiRandom=emojisList[random.randrange(0,len(emojisList))]
        tableroFlecha[fila][columna] = emojiRandom
        print('''
         ____  _    _  _____  _____          __  __ _____ _   _           _____ 
        |  _ \| |  | |/ ____|/ ____|   /\   |  \/  |_   _| \ | |   /\    / ____|
        | |_) | |  | | (___ | |       /  \  | \  / | | | |  \| |  /  \  | (___  
        |  _ <| |  | |\___ \| |      / /\ \ | |\/| | | | |     | / /\ \  \___ \ 
        | |_) | |__| |____) | |____ / ____ \| |  | |_| |_| |\  |/ ____ \ ____) |
        |____/ \____/|_____/ \_____/_/    \_\_|  |_|_____|_| \_/_/    \_\_____/ 

        ''')          
        mostrarTablero(tableroFlecha)
        while movFich != ' ':
            emojiRandom=emojisList[random.randrange(0,len(emojisList))]
            tableroFlecha[fila][columna] = posAnterior
            movFich = input('Donde quieres moverte usando W/A/S/D: ').lower()
            if movFich == 'w' and fila <= 7 and fila >= 0:
                fila-=1
            elif movFich == 's' and fila <= 7 and fila >= 0:
                fila+=1
            elif movFich == 'a' and columna <= 7 and columna >= 0:
                columna-=1
            elif movFich == 'd' and columna <= 7 and columna >= 0:
                columna+=1
            else:
                continue
            posAnterior=tableroFlecha[fila][columna]
            tableroFlecha[fila][columna] = emojiRandom
            os.system('cls')
            print('''
         ____  _    _  _____  _____          __  __ _____ _   _           _____ 
        |  _ \| |  | |/ ____|/ ____|   /\   |  \/  |_   _| \ | |   /\    / ____|
        | |_) | |  | | (___ | |       /  \  | \  / | | | |  \| |  /  \  | (___  
        |  _ <| |  | |\___ \| |      / /\ \ | |\/| | | | |     | / /\ \  \___ \ 
        | |_) | |__| |____) | |____ / ____ \| |  | |_| |_| |\  |/ ____ \ ____) |
        |____/ \____/|_____/ \_____/_/    \_\_|  |_|_____|_| \_/_/    \_\_____/ 

            ''')          
            mostrarTablero(tableroFlecha)
            tableroFlecha[fila][columna] = '  '
        os.system('cls')
        cont=0
        if tablero[fila][columna] == '💣':
            os.system('cls')
            print('''
             _____    ______   _____    _____    _____    _____   _______   ______ 
            |  __ \  |  ____| |  __ \  |  __ \  |_   _|  / ____| |__   __| |  ____|
            | |__) | | |__    | |__) | | |  | |   | |   | (___      | |    | |__   
            |  ___/  |  __|   |  _  /  | |  | |   | |    \___ \     | |    |  __|  
            | |      | |____  | | \ \  | |__| |  _| |_   ____) |    | |    | |____ 
            |_|      |______| |_|  \_\ |_____/  |_____| |_____/     |_|    |______|
                ''')
            mostrarTablero(tablero)
            break
        elif contMinas(tablero,fila,columna) == 0 and tablero[fila][columna] == '  ':
            tablero[fila][columna]=' 0'
            tableroSinMinas[fila][columna]=' 0'
            autoPoner(tablero,tableroSinMinas,columna,fila)
        elif contMinas(tablero,fila,columna) != '🚩' and tablero[fila][columna] == '  ':
            tableroSinMinas[fila][columna] = ' '+str(contMinas(tablero,fila,columna))
            tablero[fila][columna] = ' '+str(contMinas(tablero,fila,columna))
    
        for i in range(8):
            for x in range(8):
                if tableroSinMinas[i][x] != '  ' and tableroSinMinas[i][x] != '💣' and tableroSinMinas[i][x] != '🚩':
                    cont+=1
        time.sleep(0.001)
        if cont==54:
            os.system('cls')
            print('''
          _____              _   _               _____   _______   ______ 
         / ____|     /\     | \ | |     /\      / ____| |__   __| |  ____|
        | |  __     /  \    |  \| |    /  \    | (___      | |    | |__   
        | | |_ |   / /\ \   |     |   / /\ \    \___ \     | |    |  __|  
        | |__| |  / ____ \  | |\  |  / ____ \   ____) |    | |    | |____ 
         \_____| /_/    \_\ |_| \_| /_/    \_\ |_____/     |_|    |______|
                                                                                                            
            ''')
            mostrarTablero(tablero)
            break
        mostrarTablero(tableroSinMinas)
    elif bandera == 'salir':
        os.system('cls')
        print()
        print('''
          _____  _____             _____  _____             _____   _____    ____   _____         _  _    _  ______  _____            _____  
         / ____||  __ \     /\    / ____||_   _|    /\     / ____| |  __ \  / __ \ |  __ \       | || |  | ||  ____|/ ____|    /\    |  __ \ 
        | |  __ | |__) |   /  \  | |       | |     /  \   | (___   | |__) || |  | || |__) |      | || |  | || |__  | |  __    /  \   | |__) |
        | | |_ ||  _  /   / /\ \ | |       | |    / /\ \   \___ \  |  ___/ | |  | ||  _  /   _   | || |  | ||  __| | | |_ |  / /\ \  |  _  / 
        | |__| || | \ \  / ____ \| |____  _| |_  / ____ \  ____) | | |     | |__| || | \ \  | |__| || |__| || |____| |__| | / ____ \ | | \ \ 
         \_____||_|  \_\/_/    \_\\_____||_____|/_/    \_\|_____/  |_|      \____/ |_|  \_\  \____/  \____/ |______|\_____|/_/    \_\|_|  \_\
        ''')
        break
    else:
        print('Podrias elejir una de las opciones que te pide porfavor?')
        time.sleep(2)
