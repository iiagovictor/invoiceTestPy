#%%
from TestExercise import Invoice

#%% Sistema de input

item = int(input(f'Informe o número do item: '))
descricao = str(input(f'Informe a descrição do item {item}: '))
qtd = int(input(f'Qual a quantidade do produto {descricao}: '))
preco = float(input(f'Qual o valor unitário do produto {descricao}: '))

#%% Criando a classe Invoice

fatura = Invoice(item, descricao, qtd, preco)

#%% Teste do getters de cada atributo

print('Testando o getters')

fatura.item = item
fatura.descricao = descricao
fatura.qtd = qtd
fatura.preco = preco

#%% Teste do setters de cada atributo

print('Testando o setters')

item = int(input(f'Informe o número do item: '))
descricao = str(input(f'Informe a descrição do item {item}: '))
qtd = int(input(f'Qual a quantidade do produto {descricao}: '))
preco = float(input(f'Qual o valor unitário do produto {descricao}: '))

fatura.item = item
fatura.descricao = descricao
fatura.qtd = qtd
fatura.preco = preco