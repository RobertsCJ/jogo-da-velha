from time import sleep
from random import randint
X = '\033[1;31m'; O = '\033[1;36m'; tag = '\033[m'; destaque = '\033[1;7m'


def design(): #tabela do jogo da velha
	print()
	print(' ' * 25, '#       #')
	print(' ' * 25, ' ', tabela[0][0] + '|' + tabela[0][1] + '|' + tabela[0][2]) 
	print(' ' * 25, ' ', tabela[1][0] + '|' + tabela[1][1] + '|' + tabela[1][2], ' ') 
	print(' ' * 25, ' ', tabela[2][0] + '|' + tabela[2][1] + '|' + tabela[2][2])
	print(' ' * 25, '#       #\n')


def menu():
	global tabela
	while True:	
		tabela=[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
				
		print('\n', f'{X}X{tag}{O}O{tag}' * 10 + f' {destaque}  JOGO DA VELHA  {tag} ' + f'{O}O{tag}{X}X{tag}' * 10,'\n')
		print(f'JOGADOR 1 ({X}X{tag}) \nJOGADOR 2 ({O}O{tag})')
		print('Use o numpad para marcar')
		opcao = str(input('\n1) UM JOGADOR (COMPUTADOR) \n2) DOIS JOGADORES \n3) SAIR\n'))
		if opcao == '1':
			sleep(0.8)
			vsMaquina(tabela)
	
		elif opcao == '2':
			sleep(0.8)
			vsHumano(tabela)
	
		elif opcao == '3':
			print('Saindo...')
			sleep(1)
			break


def vsMaquina(jogo):
	while ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:#até os todos espaços vazios serem preenchidos
		design()
		print(' ' * 22 + f'{X}VEZ DO JOGADOR 1{tag}\n')	
			
		marca(jogo, X, 'X')
			
		sleep(1)
		design()
		
		if verifica(jogo, 'X'):
			print(' ' * 22 + f'\n{X}JOGADOR 1 VENCEU!{tag}\n')
			sleep(1)
			break
				
		if ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:
			print(' ' * 22 + f'{O}VEZ DO COMPUTADOR{tag}')			
		else:  #se o jogo já estiver preenchido, não continuar
			print(' ' * 22 + f'{destaque}ACABOU O JOGO!{tag}')
			break
			
		computador_linha = randint(0, 2)
		computador_coluna = randint(0, 2)
		while jogo[computador_linha][computador_coluna] != ' ': ##
			computador_linha = randint(0, 2)
			computador_coluna = randint(0, 2)
		jogo[computador_linha][computador_coluna] = f'{O}O{tag}'
		
		sleep(1)
		design()	
					
		if verifica(jogo, 'O'):
			print(' ' * 22 + f'{O}COMPUTADOR VENCEU!{tag}')	
			sleep(1)
			break
	

def vsHumano(jogo):
	while ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:
		design()
		print(' ' * 22 + f'{X}VEZ DO JOGADOR 1{tag}\n')	 
		
		marca(jogo, X, 'X')		
			
		sleep(1)
		design()
					
		if verifica(jogo, 'X'):
			print(' ' * 22 + f'\n{X}JOGADOR 1 VENCEU!{tag}\n')
			sleep(2)
			break
				
		if ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:
			print(' ' * 22 + f'{O}VEZ DO JOGADOR 2{tag}')
					
		else: #se o jogo já estiver preenchido, não continuar
			print(' ' * 22 + f'{destaque}ACABOU O JOGO!{tag}')
			break

		marca(jogo, O, 'O')
					
		sleep(1)
		design()	
			
		if verifica(jogo, 'O'):
			print(' ' * 22, f'\n{O}JOGADOR 2 VENCEU!{tag}\n')
			sleep(2)
			break
	
			
def marca(jogo, cor, A):
	while True: 
		player = str(input(f'\n{destaque}Jogue:{tag} ')).strip()[0]
		if player == '1':  x = 2; y = 0
		elif player == '2': x = 2; y = 1
		elif player == '3': x = 2; y = 2 
		elif player == '4': x = 1; y = 0
		elif player == '5': x = 1; y = 1
		elif player == '6': x = 1; y = 2
		elif player == '7': x = 0; y = 0
		elif player == '8': x = 0; y = 1
		elif player == '9': x = 0; y = 2
		if jogo[x][y] == ' ' and player in '123456789':
			jogo[x][y] = f'{cor}{A}{tag}'
			break
			
			
def verifica(jogo, A):
	if jogo[0][0] == jogo[1][0] == jogo[2][0] == f'{X}{A}{tag}' or jogo[0][1] == jogo[1][1] == jogo[2][1] == f'{X}{A}{tag}' or jogo[0][2] == jogo[1][2] == jogo[2][2] == f'{X}{A}{tag}' or jogo[0][0] == jogo[0][1] == jogo[0][2] == f'{X}{A}{tag}' or jogo[1][0] == jogo[1][1] == jogo[1][2] == f'{X}{A}{tag}' or jogo[2][0] == jogo[2][1] == jogo[2][2] == f'{X}{A}{tag}' or jogo[0][0] == jogo[1][1] == jogo[2][2] == f'{X}{A}{tag}' or jogo[2][0] == jogo[1][1] == jogo[0][2] == f'{X}{A}{tag}':
		return True
