#Agenda de Contatos
def adicionar_contato(contatos):
    contato = {"nome": nome_contato, "telefone": int(telefone), "email": email, "favorito": False}
    contatos.append(contato)
    print("\nContato adicionado")
    return 

def  ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} / Telefone: ({telefone}) / E-mail: ({email})")
    return

def info_editavel():
    print("Opções:")
    print("[a] Nome do contato")
    print("[b] Telefone do contato")
    print("[c] E-mail do contato")
    print("[d] Tudo")
    return

def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_int = int(indice_contato) - 1
    if indice_contato_int > len(contatos):
        print("\nATENÇAO: Número de contato inválido")
    else:
        if novo_nome is not None:
            contatos[indice_contato_int]["nome"] = novo_nome
        if novo_telefone is not None:
            contatos[indice_contato_int]["telefone"] = novo_telefone
        if novo_email is not None:
            contatos[indice_contato_int]["email"] = novo_email
        print (f"Contato {indice_contato} atualizado com sucesso.")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_int = int(indice_contato) - 1
    if indice_contato_int > len(contatos):
        print("\nATENÇAO: Número de contato inválido")
    else:
        contatos[indice_contato_int]["favorito"] = True
        print(f"Contato {indice_contato} favoritado com sucesso.")
    return

def ver_contatos_favoritos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        if contato ["favorito"]:
            status = "★"
            nome_contato = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. [{status}] {nome_contato} / Telefone: ({telefone}) / E-mail: ({email})")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_int = int(indice_contato) - 1
    if indice_contato_int > len(contatos):
        print("\nATENÇAO: Número de contato inválido")
    else:
        contatos.remove(contatos[indice_contato_int])
        print(f"Contato {indice_contato} deletado com sucesso.")
    return

contatos = []
while True:
    print("\nSua agenda de contatos")
    print("\nMenu:\n")
    print("1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar contato")

    escolha = input("\nDigite o número da sua opção: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone de contato (apenas números): ")
        email = input("Digite o e-mail de contato: ")
        adicionar_contato(contatos)
    
    if escolha == "2":
        ver_contatos(contatos)
    
    if escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja editar: ")
        info_editavel()
        opcao = input ("Informe qual informação quer editar: ")
        if opcao == "a":
           novo_nome = input("Digite o novo nome do contato: ")
           novo_telefone = None
           novo_email = None
        elif opcao == "b":
            novo_nome = None
            novo_telefone = input("Digite o novo telefone de contato (apenas números): ")
            novo_email = None
        elif opcao == "c":
            novo_nome = None
            novo_telefone = None
            novo_email = input("Digite o novo e-mail de contato: ")
        elif opcao == "d":
           novo_nome = input("Digite o novo nome do contato: ")
           novo_telefone = input("Digite o novo telefone de contato (apenas números): ")
           novo_email = input("Digite o novo e-mail de contato: ")
        editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
    
    if escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)
    
    if escolha == "5":
        ver_contatos_favoritos(contatos)

    if escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja apagar: ")
        apagar_contato(contatos,indice_contato)