import time
print("Exceções e Try Except")
print("")

# estrutura basica do try except
try:
    pass
except:
    pass
finally:
    pass

opcao=0
while opcao != 4:
    print("super programa 9000")
    print("---------------------")
    print("1. cadastrar produto")
    print("---------------------")
    print("2. cadastrar cliente")
    print("---------------------")
    print("3. extrato de caixa")
    print("---------------------")
    print("4. sair")
    print("---------------------")

    try:
        opcao = int(input("digite sua escolha: "))
        print("")
        time.sleep(1)
    except:
        print("")
        print("digite um número")
        print("")
        time.sleep(1)
    else:
        if opcao == 1:
            print("produto cadastrado")
            print("")
            time.sleep(1)
        elif opcao == 2:
            print("cliente cadastrado")
            print("")
            time.sleep(1)
        elif opcao == 3:
            print("extrato de caixa enviado")
            print("")
            time.sleep(1)
        elif opcao == 4:
            print("tchau")
            print("")
            time.sleep(1)
            break
        else:
            print("opcao invalida")
            print("")
            time.sleep(1)