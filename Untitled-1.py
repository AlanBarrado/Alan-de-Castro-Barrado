import os, time

print("aula de arquivos")

if os.path.isfile("login.txt"):
    print("cadastro ja existente")
    time.sleep(1)
    usuario = input("digite seu usuario: ")
    senha = input("digite sua senha: ")

    arquivo = open("login.txt", "r")
    conteudo = arquivo.read()
    time.sleep(.5)
    arquivo.close()

    partes = conteudo.split("|", 2)

    if usuario == partes[0] and senha == partes[1]:
        print("autenticado com sucesso!")
        time.sleep(.3)
        print(f"bem vindo {usuario}")
    else:
        print("usuario ou senha incorretos")
else:
    print("cadastro não existe, registre-se agora")
    usuario = input("digite seu usuario: ")
    senha = input("digite sua senha: ")

    arquivo = open("login.txt", "w")
    arquivo.write(f"{usuario}|{senha}")
    arquivo.close()

    print(f"usuario '{usuario}' cadastrado com sucesso")