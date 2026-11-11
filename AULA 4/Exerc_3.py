'''Exercício 3: Verifique se o usuário é maior de idade
e pode entrar no show, escreva um programa que peça
ao usuário a idade e decida se ele pode entrar no show.'''

usuario = int(input("Digite a sua idade : "))
show = 18

if usuario >= show:
    print("LEGAL!!! Voce pode ir ao Show!!!!")
elif usuario <= 0:
    print("OPA!!! Voce ainda NÃO nasceu logo não pode ir ao Show!!!!")
elif usuario <= 10:
    print("OPA!!! Voce é muito NOVO e não pode ir ao Show!!!!")
else:
    print("QUE PENA!!! Voce não pode ir ao Show!!!!")