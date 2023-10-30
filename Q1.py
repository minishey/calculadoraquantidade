print('Bem vindo a Loja de Sheila Hui Yi Chiu RU:4412400')
valor_produto = float(input('Digite o valor o produto:'))  #Variável para valor do produto
qtd = int(input('Digite a quantidade do produto:'))  #Variável para quantidade do produto
res = valor_produto * qtd  #Variável para a soma total do valor
print('Valor total é de {:.2f}:'.format(res))

if qtd < 10:  # Comando para quantidade sem desconto
    desconto = (res * 0) / 100  # Decidi por escrever o cálculo a ser feito ao invés da porcentagem já calculada
    print('Quantidade não possui desconto')
elif qtd < 100:  # Comando para quantidade com 5%  de desconto
    desconto = (res * 5) / 100
    print('Novo valor com desconto (5%) de {:.2f} é {:.2f}'.format(desconto, res - desconto))
elif qtd < 1000:  # Comando para quantidade com 10% de desconto
    desconto = (res * 10) / 100
    print('Novo valor com desconto (10%) de {:.2f} é {:.2f}'.format(desconto, res - desconto))
else:
    qtd > 1000  # Comando para quantidade com 15% de desconto
    desconto = (res * 15) / 100
    print('Novo valor com desconto (15%) de {:.2f} é {:.2f}'.format(desconto, res - desconto))
# Fim do Programa
