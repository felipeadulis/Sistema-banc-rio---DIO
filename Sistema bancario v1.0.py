# Sistema bancário v1.0
# Para fins de teste, utilize os dados da minha conta fictícia: ag 5422, conta 092766, senha 1234, nome Felipe

# Lista de dados

agencias = [
"5422",
      [
   "092766",["felipe","1234",0],
   "092767",["afonso","1235",0], 
      ],
"3750",
      [
   "284451",["ricardo","0000",0],
   "284469",["ivana","1111",0], 
      ]
          ]
      

# Lógica usuário
agencia = input("""
 Seja bem vindo ao Adulis Bank!
Digite a sua agência (4 digitos)
""")

while agencia not in agencias:
   agencia = input("""
        AGÊNCIA INVÁLIDA!
Digite a sua agência (4 digitos)
""")

contas_index = (agencias.index(agencia)+1)

conta = input("""
Digite a sua conta (6 digitos, apenas numerais)
""")

while conta not in agencias[contas_index]:
   conta = input("""
                 CONTA INVÁLIDA
Digite a sua conta (6 digitos, apenas numerais)
""")

dados_usuario_index = (agencias[contas_index].index(conta)+1)
nome = (agencias[contas_index][dados_usuario_index][0])
senha = (agencias[contas_index][dados_usuario_index][1])
saldo = (agencias[contas_index][dados_usuario_index][2])

tentativa = 1
acesso = False
senha_digitada = input(f"""
Seja bem vindo(a) {nome.title()}!
Digite a sua senha (tentativa {tentativa}/3):
""")

while tentativa < 3:
    tentativa = tentativa + 1
    if senha_digitada != senha:
       senha_digitada = input(f"""
Senha incorreta!
Digite a sua senha (tentativa {tentativa}/3):
""")
    else: 
       print(f"\nAcesso concedido! Felizes em vê-lo(a) novamente, {nome.title()}!")
       acesso = True
       break
       
else:
   print("Número de tentativas excedido, acesso negado!")


# Logica operações

limite_saque = 500
extrato = ""
numero_saques = 0
max_saques = 3

while acesso == True:
    operacao = ""
    while True:
       operacao = input("""
            Escolha uma operação: 
                 
[d] Depositar
[s] Sacar (máximo: 3 diários, limite: R$ 500,00)
[e] Extrato
[q] Sair
""")
       if operacao == "d":
          valor = float(input("Digite o valor desejado:\n"))

          if valor > 0: 
             agencias[contas_index][dados_usuario_index][2] += valor
             saldo = agencias[contas_index][dados_usuario_index][2]
             extrato += f"Depósito: R$ {valor:.2f}\n"
             print(f"Operação realizada com sucesso! Saldo: R$ {saldo:.2f}\n")
             
          else:
             print("Operação falhou! O valor digitado é inválido")
             
       elif operacao == "s":
        valor = float(input("Digite o valor desejado (máximo: 3 saques diários, limite: R$ 500,00):\n"))

        if valor > 0: 
           
           if valor <= agencias[contas_index][dados_usuario_index][2]:
              
              if valor <= limite_saque:
                 
                 if numero_saques < max_saques:
                    numero_saques += 1
                    agencias[contas_index][dados_usuario_index][2] -= valor
                    saldo = agencias[contas_index][dados_usuario_index][2]
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    print(f"Operação realizada com sucesso! Saldo: R$ {saldo:.2f}\n")

                 else: print("Operação falhou! Limite de saques excedido") 

              else: print("Operação falhou! O valor digitado é maior do que o máximo permitido")

           else: print("Operação falhou! O valor digitado é maior do que o saldo disponível na conta")

        else: print("Operação falhou! O valor digitado é inválido") 
           
           
       elif operacao == "e":   
           saldo = agencias[contas_index][dados_usuario_index][2]
           if not extrato:
              print(f"""
Nenhuma operação Realizada!
Saldo:  R$ {saldo:.2f}
""")
        
           else: 
              print(f"""
---------- EXTRATO ----------
{extrato}
Saldo:  R$ {saldo:.2f}
-----------------------------
""")   
              
       elif operacao == "q":
          print(f"Muito obrigado por usar o Adulis Bank, até a próxima {nome.title()}!\n")
          break
       
       else:
          print("\nOperação inválida!")
          






           
        


