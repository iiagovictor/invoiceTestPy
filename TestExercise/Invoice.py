# Classe Invoice, representa uma fatura de um item vendido na loja
class Invoice:

  #Método construtor
  def __init__(self, item, descricao, qtd, preco): 
    self.item = item
    self.descricao = descricao

    # Valida número de itens
    if type(qtd) == type(int()):
      if qtd > 0:
        self.qtd = qtd
      else:
        raise Exception('Quantidade não pode ser vazio, menor ou igual a 0.')
    else:
      raise Exception('A "quantidade" deve ser do tipo inteiro e não pode ser vazio.')

    # Valida preço do item
    if type(preco) == type(float()) or type(preco) == type(int()):
      self.preco = 0 if preco < 0 else preco 
    else:
      raise Exception('O "preço" deve ser do tipo int ou float.')
    
    print('Fatura criada com sucesso!')

   #Calcula o valor da fatura (multiplica a quantidade pelo preço por item) e depois retorna o valor como um double
  def getInvoiceAmount(self):
    total = self.qtd * self.preco
    return total

  @property
  def item(self):
    return self.__item

  @property
  def descricao(self):
    return self.__descricao

  @property
  def qtd(self):
    return self.__qtd

  @property
  def preco(self):
    return self.__preco

  @item.setter
  def item(self, value):
    if type(value) == type(int()):
      self.__item = value
    else:
      raise Exception('"Item" deve ser do tipo int.')

  @descricao.setter
  def descricao(self, value):
    if type(value) == type(str()):
      self.__descricao = value
    else:
      raise Exception('"Descrição" deve ser do tipo string.')

  @qtd.setter
  def qtd(self, value):
    # Valida número de itens
    if type(value) == type(int()):
      if value > 0:
        self.__qtd = value
      else:
        raise Exception('Quantidade não pode ser vazio, menor ou igual a 0.')
    else:
      raise Exception('A "quantidade" deve ser do tipo inteiro e não pode ser vazio.')

  @preco.setter
  def preco(self, value):
    # Valida preço do item
    if type(value) == type(float()) or type(value) == type(int()):
      self.__preco = 0 if value < 0 else value 
    else:
      raise Exception('O "preço" deve ser do tipo int ou float.')