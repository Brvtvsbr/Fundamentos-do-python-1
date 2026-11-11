'''Exercício 2: Classificação de Triângulos
Escreva um programa em Python que receba três comprimentos de 
lados de um triângulo e determine se o triângulo é equilátero, 
isósceles ou escaleno.'''

comp1 = int(input("Digite o comprimento lado 1 do triangulo = "))
comp2 = int(input("Digite o comprimento lado 2 do triangulo = "))
comp3 = int(input("Digite o comprimento lado 3 do triangulo = "))

if comp1 == comp2 == comp3 :
    print("O triangulo é EQUILATERO!!!")
    
if comp1 == comp2 and comp1!= comp3 or comp2 == comp3 and comp2 != comp1 or comp3 == comp1 and comp3 != comp2 :
    print("O triangulo é ISOCELES!!!")
    
if comp1 != comp2 and comp2 != comp3 and comp1!= comp3:
    print("O triangulo é ESCALENO!!!")
    
print(comp1, comp2, comp3, sep="*")