Class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.ldade = idade
  def apresentar(self):
    print(f"Olá, meu nome é {self.nome} e {self.idade) anos.")
  def fazer_aniversario(self):
    self.idade += 1
pessoa = Pessoa("Ana", 17)
pessoa.apresentar()
