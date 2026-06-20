import os




lista_restaurante = []




#title:
def titulo(texto):
    os.system("clear")
    espaco = " " * 100
    print(f"{espaco}{texto}")




#sub-title:
def subtitulo(texto):
    espaco = " " * 99
    print(f"{espaco}{texto}")
    print("\n")



#register:
def cadastrar_restaurante():
    def titulo_subtitulo():
        titulo("Cadastro de Restaurantes")
    titulo_subtitulo()
    nome_do_restaurante = input("\nDigite o nome do restaurante: ").upper()
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
    def titulo_subtitulo():
        titulo("Lista de Restaurantes")
    titulo_subtitulo()
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
    def titulo_subtitulo():
        titulo("Alternar status do Restaurante")
        subtitulo("       [Ativar/Desativar]")
    titulo_subtitulo()
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
    def titulo_subtitulo():
        titulo("Ajustar configurações do Restaurante")
        subtitulo("       [Modificação e Exclusão]")
    titulo_subtitulo()
    entrada = input("O que deseja fazer? (Alterar/Remover): ")

    match entrada:
        case "remover" | "Remover" | "REMOVER":
            titulo_subtitulo()
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

        case "Alterar" | "alterar" | "ALTERAR":
            chave = False
            titulo_subtitulo()
            opcao = input("O que deseja alterar? (Nome/Descrição/Categoria): ").upper()

            match opcao:
                case "NOME":
                    titulo_subtitulo()
                    print("Nome:")
                    for restaurante in lista_restaurante:
                        nome_restaurante = restaurante["Nome"]
                        print(f"{nome_restaurante}") 
                    old= input("\nQual restaurante você deseja alterar? ").upper()
                    for restaurante in lista_restaurante:
                        if old == restaurante["Nome"]:
                            chave = True
                            novo_nome = input("Digite o novo nome do restaurante: ").upper()
                            restaurante["Nome"] = novo_nome
                            input("\nAlteração feita com sucesso! ")
                            return
                    if not chave:   
                        input("\nRestaurante não encontrado, verifique e tente novamente. ")
                        listagem_restaurante()

                case "DESCRIÇÃO" | "DESCRICAO":
                    titulo_subtitulo()
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
                    titulo_subtitulo()
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

