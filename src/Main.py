from Cliente import Cliente
from Conta import Conta
class Main:
    pass



conta1 = Conta("Luiz", 1234, 190.00)

conta1.sacar(100.00)
print(conta1.get_saldo)

print("""Bem vindo ao CLI da loja, deseja
      1 - Depositar dinheiro
      2 - Se cadastrar na loja
      3 - Cadastrar sua conta bancária
      4 - Depositar dinheiro
      5 - sacar dinheiro""")