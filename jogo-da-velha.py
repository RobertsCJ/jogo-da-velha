print('XO' * 10 + '#####  JOGO DA VELHA  #####' + 'OX' * 10,'\n')
print('JOGADOR 1 (X) \nJOGADOR 2 (O)\n')
from time import sleep
from random import randint

jogo = [
[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']]

	
def menu():
	while True:	
		print('JOGO DA VELHA')
		opcao = int(input('1) UM JOGADOR (COMPUTADOR) \n2) DOIS JOGADORES \n3) SAIR\n'))
		if opcao == 1:
			sleep(0.8)
			vsMaquina(jogo)
	
		elif opcao == 2:
			sleep(0.8)
			vsHumano(jogo)
	
		elif opcao == 3:
			print('Saindo...')
			sleep(1)
			break

def design(): #tabela do jogo da velha
	print(' '* 25, '# 1 2 3')
	print(' '* 25, '1', jogo[0][0] + '|' + jogo[0][1] + '|' + jogo[0][2]) 
	print(' '* 25, '2', jogo[1][0] + '|' + jogo[1][1] + '|' + jogo[1][2]) 
	print(' '* 25, '3', jogo[2][0] + '|' + jogo[2][1] + '|' + jogo[2][2])

def vsHumano(jogo): # 2 jogadores
	while ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]: #até os espaços vazios serem todos preenchidos
		design()
		print(' ' * 22 + 'VEZ DO JOGADOR 1')
		
		player1_linha = ' '
		while player1_linha not in '123':
			player1_linha = str(input('\nEm qual LINHA irá jogar (1/2/3)?\n')).strip()[0]
		
		player1_coluna = ' '
		while player1_coluna not in '123':
			player1_coluna = str(input('\nEm qual COLUNA irá jogar (1/2/3)?\n')).strip()[0]
		
		while jogo[int(player1_linha)-1][int(player1_coluna)-1] != ' ':
			print('\nESSE LUGAR JÁ ESTÁ PREENCHIDO, TENTE NOVAMENTE.\n')
			player1_linha = ' '
			while player1_linha not in '123':
				player1_linha = str(input('\nEm qual LINHA irá jogar (1/2/3)?\n')).strip()[0]
		
			player1_coluna = ' '
			while player1_coluna not in '123':
				player1_coluna = str(input('\nEm qual COLUNA irá jogar (1/2/3)?\n')).strip()[0]
		
		jogo[int(player1_linha)-1][int(player1_coluna)-1] = 'X'
			
		sleep(1)
		design()	
		
		if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'X' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'X' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'X' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'X' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'X' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'X' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'X' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'X':
			print('JOGADOR 1 VENCEU!')
			sleep(2)
			break
			
		if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'O' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'O' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'O' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'O' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'O' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'O' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'O' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'O':
			print('JOGADOR 2 VENCEU!')
			sleep(2)
			break

		if ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:
			print(' ' * 22, 'VEZ DO JOGADOR 2')
			
		else:               #se o jogo já estiver preenchido, não continuar
			print('\nACABOU O JOGO')
			break
		
		player2_linha = ' '
		while player2_linha not in '123':
			player2_linha = str(input('\nEm qual LINHA irá jogar (1/2/3)?\n')).strip()[0]
		
		player2_coluna = ' '
		while player2_coluna not in '123':
			player2_coluna = str(input('\nEm qual COLUNA irá jogar (1/2/3)?\n')).strip()[0]
			
		while jogo[int(player2_linha)-1][int(player2_coluna)-1] != ' ':
			print('\nESSE LUGAR JÁ ESTÁ PREENCHIDO, TENTE NOVAMENTE.\n')
			player2_linha = ' '
			while player2_linha not in '123':
				player2_linha = str(input('\nEm qual LINHA irá jogar (1/2/3)?\n')).strip()[0]
		
			player2_coluna = ' '
			while player2_coluna not in '123':
				player2_coluna = str(input('\nEm qual COLUNA irá jogar (1/2/3)?\n')).strip()[0]
		
		jogo[int(player2_linha)-1][int(player2_coluna)-1] = 'O'
		
		sleep(1)
		design()
		
		if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'X' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'X' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'X' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'X' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'X' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'X' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'X' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'X':
			print('JOGADOR 1 VENCEU!')
			sleep(2)
			break
			
		if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'O' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'O' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'O' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'O' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'O' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'O' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'O' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'O':
			print('JOGADOR 2 VENCEU!')
			sleep(2)
			break

def vsMaquina(jogo):
	while ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]: #até os espaços vazios serem todos preenchidos
		design()
		print(' ' * 22 + 'VEZ DO JOGADOR 1')
		
		player1_linha = ' '
		while player1_linha not in '123':
			player1_linha = str(input('\nEm qual LINHA irá jogar (1/2/3)?\n')).strip()[0]
		
		player1_coluna = ' '
		while player1_coluna not in '123':
			player1_coluna = str(input('\nEm qual COLUNA irá jogar (1/2/3)?\n')).strip()[0]
		
		while jogo[int(player1_linha)-1][int(player1_coluna)-1] != ' ':
			print('\nESSE LUGAR JÁ ESTÁ PREENCHIDO, TENTE NOVAMENTE.\n')
			player1_linha = ' '
			while player1_linha not in '123':
				player1_linha = str(input('\nEm qual LINHA irá jogar (1/2/3)?\n')).strip()[0]
		
			player1_coluna = ' '
			while player1_coluna not in '123':
				player1_coluna = str(input('\nEm qual COLUNA irá jogar (1/2/3)?\n')).strip()[0]
		
		jogo[int(player1_linha)-1][int(player1_coluna)-1] = 'X'
			
		sleep(1)
		design()	
		
		if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'X' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'X' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'X' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'X' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'X' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'X' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'X' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'X':
			print('JOGADOR 1 VENCEU!')
			sleep(2)
			break
			
		if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'O' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'O' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'O' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'O' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'O' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'O' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'O' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'O':
			print('COMPUTADOR VENCEU!')
			sleep(2)
			break
			
		if ' ' in jogo[0] or ' ' in jogo[1] or ' ' in jogo[2]:
			print(' ' * 22 + 'VEZ DO COMPUTADOR')
			
		else:               #se o jogo já estiver preenchido, não continuar
			print('\nACABOU O JOGO')
			break
			
		computador_linha = randint(0, 2)
		computador_coluna = randint(0, 2)
		while jogo[computador_linha][computador_coluna] != ' ':
			computador_linha = randint(0, 2)
			computador_coluna = randint(0, 2)
			
		jogo[computador_linha][computador_coluna] = 'O'
		
		sleep(1)
		design()	
		
		if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'X' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'X' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'X' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'X' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'X' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'X' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'X' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'X':
			print('JOGADOR 1 VENCEU!')
			sleep(2)
			print('\nACABOU O JOGO')
			break
			
		if jogo[0][0] == jogo[1][0] == jogo[2][0] == 'O' or jogo[0][1] == jogo[1][1] == jogo[2][1] == 'O' or jogo[0][2] == jogo[1][2] == jogo[2][2] == 'O' or jogo[0][0] == jogo[0][1] == jogo[0][2] == 'O' or jogo[1][0] == jogo[1][1] == jogo[1][2] == 'O' or jogo[2][0] == jogo[2][1] == jogo[2][2] == 'O' or jogo[0][0] == jogo[1][1] == jogo[2][2] == 'O' or jogo[2][0] == jogo[1][1] == jogo[0][2] == 'O':
			print('COMPUTADOR VENCEU!')
			sleep(2)
			print('\nACABOU O JOGO')
			break
		
menu()
'''
CHECKLIST:

#IDENTIFICAR QUEM GANHOU ## FEITO <---
#NÃO SOBRESCREVER O OUTRO ## CONCLUÍDO <-/
#PODER JOGAR CONTRA O COMPUTADOR 'PERFEITO!!'
'''
