'''Exercício 1: Verificação de Número Positivo
Escreva um programa em Python que solicite ao usuário
um número inteiro e verifique 
se o número é positivo, negativo ou zero.'''

num = int(input("Digite um numero: "))
          
if num > 0:
          print(f"O numero {num} é Positivo!!!")
if num < 0:
          print(f"O numero {num} é Negativo!!!")
if num == 0:
          print(f"O numero {num} é ZERO!!!") 