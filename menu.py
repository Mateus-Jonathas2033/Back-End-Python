import os




lista_restaurante = []



#text
def texting(title, subtitle):

    #title:
    os.system("clear")
    espaco = " " * 100
    print(f"{espaco}{title}")
    
    #sub-title:
    if subtitle == "":
        return
    espaco = " " * 99
    print(f"{espaco}{subtitle}")
    print("\n")




#block's_repeated_entrys
def norepeated(lista, biblioteca, variavel):

    for i in lista:
        entidade = i[biblioteca]
        if entidade == variavel:
            chave = True
            input(f"\nO '{variavel}' já existe. Por favor verifique a lista de restaurantes.")
            return True

        return False



#register:
def cadastrar_restaurante():
    texting("Cadastro de Restaurantes", "")
    nome_do_restaurante = input("\nDigite o nome do restaurante: ").upper()
    if norepeated(lista_restaurante, "Nome", nome_do_restaurante) == True:
        return
    categoria_do_restaurante = input("Digite a categoria do restaurante: ").upper()
    descricao_do_restaurante =  input("Digite uma descrição para o seu restaurante: ").upper()
    cadastro_restaurante = {"Nome":nome_do_restaurante, "Categoria":categoria_do_restaurante, "Descricao":descricao_do_restaurante, "Status":"AGUARDANDO APROVAÇÃO", "Ativo":False}
    lista_restaurante.append(cadastro_restaurante)
    print(f"\nO restaurante '{nome_do_restaurante}' foi cadastrado com sucesso, e aguardará aprovação.\n")
    continuar = input("\nDeseja cadastrar mais? (Y/N): ").upper()
    match continuar:
        case "Y" | "S":
            cadastrar_restaurante()
        case _:
            return




#listing:
def listagem_restaurante():
    texting("Lista de Restaurantes", "")
    print(f"\n\n{"Nome:".ljust(44)}{"Categoria:".ljust(40)}{"Status:".ljust(40)}{"Descrição:".ljust(0)}\n")
    for restaurante in lista_restaurante:
        nome_restaurante = restaurante["Nome"]
        categoria_restaurante = restaurante["Categoria"]
        descricao_restaurante = restaurante["Descricao"]
        status_restaurante = restaurante["Status"]
        print(f"-{nome_restaurante.ljust(43)}-{categoria_restaurante.ljust(39)}-{status_restaurante.ljust(39)}-{descricao_restaurante.ljust(0)}\n")
    input("\nAperte para voltar ao menu principal. ")
    return




#modify status: [activate/disable]
def status_restaurante():
    chave = False
    texting("Alternar status do Restaurante","       [Ativar/Desativar]")
    print(f"{"Nome:".ljust(44)}{"Status:".ljust(40)}\n")
    for restaurante in lista_restaurante:
        nome_restaurante = restaurante["Nome"]
        status_restaurante = restaurante["Status"]
        print(f"-{nome_restaurante.ljust(43)}-{status_restaurante.ljust(39)}")
    nome_restaurante = input("\nDigite o nome do restaurante que você deseja alternar: ").upper()
    if ((nome_restaurante == "EXIT") or
        (nome_restaurante == "QUIT") or
        (nome_restaurante == "LEAVE") or
        (nome_restaurante == "SAIR") or
        (nome_restaurante == "S")):
        return
    for restaurante in lista_restaurante:
        if nome_restaurante == restaurante["Nome"]:
            chave = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            informacao = f"\nO restaurante {nome_restaurante} foi ativado com sucesso. " if restaurante["Ativo"]  else f"\nO restaurante {nome_restaurante} foi desativado com sucesso. "
            input(informacao)
            restaurante["Status"] = "ATIVADO" if restaurante["Ativo"] else "DESATIVADO"
            return
    if not chave:
         input(f"\nO restaurante '{nome_restaurante}' não foi encontrado no banco de dados. Voltando para o menu... ")
         return




#modify or remove:
def configurar_restaurante():
    def reply_text():
        texting("Ajustar configurações do Restaurante","       [Modificação e Exclusão]")
    reply_text()
    entrada = input("O que deseja fazer? (Alterar/Remover): ").upper()

    match entrada:
        case "REMOVER":
            reply_text()
            print(f"{"Nome:".ljust(44)}\n")
            for restaurante in lista_restaurante:
                nome_restaurante = restaurante["Nome"]
                print(f"-{nome_restaurante}")
            nome_remocao = input("\nDigite o nome do restaurante que deseja remover: ").upper()
            for restaurante in lista_restaurante:
                if nome_remocao == restaurante["Nome"]:
                    lista_restaurante.remove(restaurante)
                    input("\nRestaurante removido com sucesso!\n")
                    return
                else:
                    input("\nNome inválido, saindo...!\n")
                    return

        case "ALTERAR":
            chave = False
            reply_text()
            opcao = input("O que deseja alterar? (Nome/Descrição/Categoria): ").upper()

            match opcao:
                case "NOME":
                    reply_text()
                    print("Nome:")
                    for restaurante in lista_restaurante:
                        nome_restaurante = restaurante["Nome"]
                        print(f"-{nome_restaurante}") 
                    verifying_name = input("\nQual restaurante você deseja alterar? ").upper()
                    for restaurante in lista_restaurante:
                        if verifying_name == restaurante["Nome"]:
                            chave = True
                            novo_nome = input("Digite o novo nome do restaurante: ").upper()
                            restaurante["Nome"] = novo_nome
                            input("\nAlteração feita com sucesso! ")
                            return
                    if not chave:   
                        input("\nRestaurante não encontrado, verifique e tente novamente. ")
                        listagem_restaurante()

                case "DESCRIÇÃO" | "DESCRICAO":
                    reply_text()
                    print(f"{"Nome:".ljust(44)}Descrição:")
                    for restaurante in lista_restaurante:
                        nome_restaurante = restaurante["Nome"]
                        descricao_restaurante = restaurante["Descricao"]
                        print(f"-{nome_restaurante.ljust(43)}-{descricao_restaurante}")
                    restaurante = input("\nQual restaurante você deseja alterar? ").upper()
                    for restaurantes in lista_restaurante:
                        if restaurante == restaurantes["Nome"]:
                            chave = True
                            nova_descricao = input("Digite sua nova descrição: ").upper()
                            restaurantes["Descricao"] = nova_descricao
                            input("\nAlteração feita com sucesso! ")
                            return
                    if not chave:
                            input("\nRestaurante não encontrado, verifique e tente novamente. ")
                            listagem_restaurante()

                case "CATEGORIA":
                    reply_text()
                    print(f"{"Nome:".ljust(44)}Categoria:")
                    for restaurante in lista_restaurante:
                        nome_restaurante = restaurante["Nome"]
                        categoria_restaurante = restaurante["Categoria"]
                        print(f"-{nome_restaurante.ljust(43)}-{categoria_restaurante}")
                    restaurante = input("\nQual restaurante você deseja alterar? ").upper()
                    for restaurantes in lista_restaurante:
                        if restaurante == restaurantes["Nome"]:
                            chave = True
                            nova_categoria = input("Digite sua nova categoria: ").upper()
                            restaurantes["Categoria"] = nova_categoria
                            input("\nAlteração feita com sucesso! ")
                            return
                    if not chave:
                            input("\nRestaurante não encontrado, verifique e tente novamente. ")
                            listagem_restaurante()

                case _:
                    input("Opção inválida! Saindo...")
                    return

        case _:
            input("\nSaindo...!")
            return



#Selling
def anuncio():
    texting("Anuncie seus pratos", "")
    verifying_name = input("Digite o nome do seu restaurante: ").upper()
    for restaurante in lista_restaurante:
        if verifying_name == restaurante["Nome"]:
            nome_restaurante = verifying_name
            texting("Anuncie seus pratos", f" Restaurante: {nome_restaurante}")
            prato = input("Digite o nome do prato que deseja cadastrar: ").upper()
            try:
                valor = float(input("Digite o valor deste prato: "))
                quantidade = float(input("Digite a quantidade disponível por cliente: "))
            except:
                input("Argumento inválido! Saindo...")
                return
            valor = float(valor)
            quantidade = float(quantidade)
        else:
            input(f"O restaurante '{verifying_name}' não foi encontrado! Por favor, tente novamente.")
            return


