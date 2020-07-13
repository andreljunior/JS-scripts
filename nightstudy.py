#nome = 'andre'
#nome_maiusculo = nome.capitalize()
#mensagem = f'olá {nome_maiusculo}!'
#print('ola {nome_maiusculo}!')
#print(mensagem)
#print(nome)


#nomes = []
#nome1 = input('insira o primeiro nome')
#nome2 = input('insira o segundo nome')
#nome3 = input('insira o terceiro nome')
#nome4 = input('insira o quarto nome')
#nome5 = input('insira o quinto nome')
#nomes.append(nome1)
#nomes.append(nome2)
#nomes.append(nome3)
#nomes.append(nome4)
#nomes.append(nome5)
#print(nomes)
#number = int(input('insira um numero de 1 a 4'))
#del nomes[number]
#print(nomes)


#valor = 0
#for valor in range (5):
#    valor +=5
#    print(valor)




par = []
impar = []
for valor in range(50,100):
    if valor % 2 > 0:
        impar.append(valor)
    else:
        par.append(valor)

print('Vetor de numeros impares: ')
print(impar)
print('Vetor de numeros pares: ')
print(par)





