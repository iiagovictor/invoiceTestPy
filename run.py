#%%
from TestExercise.Invoice import Invoice

#%% Sistema de input

item = int(input(f'Informe o número do item: '))
descricao = str(input(f'Informe a descrição do item {item}: '))
qtd = int(input(f'Qual a quantidade do produto {descricao}: '))
preco = float(input(f'Qual o valor unitário do produto {descricao}: '))

#%% Criando a classe Invoice

fatura = Invoice(item, descricao, qtd, preco)

#%% Teste do getters de cada atributo

print('\nTestando o getters')

fatura.item = item
print(f'Item: {fatura.item}')
fatura.descricao = descricao
print(f'Descrição: {fatura.descricao}')
fatura.qtd = qtd
print(f'Quantidade: {fatura.qtd}')
fatura.preco = preco
print(f'Preço: {fatura.preco}')

#%% Teste do setters de cada atributo

print('\nTestando o setters')

item = int(input(f'Informe o número do item: '))
descricao = str(input(f'Informe a descrição do item {item}: '))
qtd = int(input(f'Qual a quantidade do produto {descricao}: '))
preco = float(input(f'Qual o valor unitário do produto {descricao}: '))

fatura.item = item
print(f'\nItem: {fatura.item}')
fatura.descricao = descricao
print(f'Descrição: {fatura.descricao}')
fatura.qtd = qtd
print(f'Quantidade: {fatura.qtd}')
fatura.preco = preco
print(f'Preço: {fatura.preco}')