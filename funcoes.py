from time import sleep
from random import randint


def design(): #tabela do jogo da velha
	print(' ' * 25, '# 7 8 9 #')
	print(' ' * 25, ' ', tabela[0][0] + '|' + tabela[0][1] + '|' + tabela[0][2]) 
	print(' ' * 25, '4', tabela[1][0] + '|' + tabela[1][1] + '|' + tabela[1][2], '6') 
	print(' ' * 25, ' ', tabela[2][0] + '|' + tabela[2][1] + '|' + tabela[2][2])
	print(' ' * 25, '# 1 2 3 #\n')


def menu():
	global tabela
	while True:	
		tabela = [
				[' ', ' ', ' '],
				[' ', ' ', ' '],
				[' ', ' ', ' ']]
				
		print('XO' * 10 + ' JOGO DA VELHA  ' + 'OX' * 10,'\n')
		print('JOGADOR 1 (X) \nJOGADOR 2 (O)')
		print('Use o numpad para marcar')
		opcao = int(input('\n1) UM JOGADOR (COMPUTADOR) \n2) DOIS JOGADORES \n3) SAIR\n'))
		if opcao == 1:
			sleep(0.8)
			vsMaquina(tabela)
	
		elif opcao == 2:
			sleep(0.8)
			vsHumano(tabela)
	
		elif opcao == 3:
			print('Saindo...')
			sleep(1)
			break


def vsMaquina(jogo):
	while ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:#até os todos espaços vazios serem preenchidos
		design()
		print(' ' * 22 + 'VEZ DO JOGADOR 1\n')	
		while True: 
			player1 = str(input('\nJogue: ')).strip()[0]
			if player1 == '1':  x = 2; y = 0
			elif player1 == '2': x = 2; y = 1
			elif player1 == '3': x = 2; y = 2 
			elif player1 == '4': x = 1; y = 0
			elif player1 == '5': x = 1; y = 1
			elif player1 == '6': x = 1; y = 2
			elif player1 == '7': x = 0; y = 0
			elif player1 == '8': x = 0; y = 1
			elif player1 == '9': x = 0; y = 2
			
			if jogo[x][y] == ' ' and player1 in '123456789':
				jogo[x][y] = 'X'
				break
		
		sleep(1)
		design()
		
		if verifica_X(jogo):
			print('\nJOGADOR 1 VENCEU!\n')
			sleep(0.8)
			break
				
		if ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:
			print(' ' * 22 + 'VEZ DO COMPUTADOR')			
		else:  #se o jogo já estiver preenchido, não continuar
			break
			
		computador_linha = randint(0, 2)
		computador_coluna = randint(0, 2)
		while jogo[computador_linha][computador_coluna] != ' ': ##
			computador_linha = randint(0, 2)
			computador_coluna = randint(0, 2)
		jogo[computador_linha][computador_coluna] = 'O'
		
		sleep(1)
		design()	
					
		if verifica_O(jogo):
			print('COMPUTADOR VENCEU!')	
			sleep(0.8)
			break
	

def vsHumano(jogo):
	while ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:
		design()
		for i in range(2):
			print(' ' * 22 + f'VEZ DO JOGADOR {i+1}\n')	
			while True: 
				player1 = str(input('\nJogue: ')).strip()[0]
				if player1 == '1':  x = 2; y = 0
				elif player1 == '2': x = 2; y = 1
				elif player1 == '3': x = 2; y = 2 
				elif player1 == '4': x = 1; y = 0
				elif player1 == '5': x = 1; y = 1
				elif player1 == '6': x = 1; y = 2
				elif player1 == '7': x = 0; y = 0
				elif player1 == '8': x = 0; y = 1
				elif player1 == '9': x = 0; y = 2
			
				if jogo[x][y] == ' ' and player1 in '123456789':
					if i == 0:
						jogo[x][y] = 'X'
					elif i == 1:
						jogo[x][y] = 'O'
					break
				
			sleep(1)
			design()
			
			if verifica_X(jogo):
				print(f'\nJOGADOR {i+1} VENCEU!\n')
				sleep(0.8)
				break
			if verifica_O(jogo):
				print(f'\nJOGADOR {i+1} VENCEU!\n')
				sleep(0.8)
				break
			

def verifica_X(jogo):
	if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'X' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'X' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'X' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'X' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'X' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'X' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'X' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'X':
		return True
		
			
def verifica_O(jogo):
	if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'O' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'O' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'O' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'O' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'O' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'O' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'O' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'O':
		return True
		
