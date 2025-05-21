filmes = [[], [], [], []]
categorias = ["Drama", "Comedia", "Ficção", "Fantasia", "Terror", "Suspense", "Faroeste", "Musical"]

def cadastro():
    nome = str(input("Nome do Filme: "))
    print("Gêneros: 'Drama', 'Comedia', 'Ficção', 'Fantasia', 'Terror'', 'Suspense', 'Faroeste', 'Musical', 'Ação', 'Policial'")
    genero = str(input("Gênero: "))
    if genero.capitalize() not in categorias:
        print("Gênero inexistente!")
        return
    while True:
        try:
            nota = float(input('Nota (0 a 10): '))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")
    filmes[2].append([nota])
    anoL = int(input("Ano de Lançamento: "))

    filmes[0].append(nome)
    filmes[1].append(genero)
    filmes[2].append(nota)
    filmes[3].append(anoL)
    print('Filme cadastrado realizado com sucesso')

def lista():
    if len(filmes[0]) == 0:
        print('Não há filmes cadastrados.')
    else:
        for i in range(len(filmes[0])):
            media = sum(filmes[2][i]) / len(filmes[2][i])
            print(f'{i + 1}. Filme: {filmes[0][i]}, Gênero: {filmes[1][i]}, Média das Notas: {media:.2f}')

def buscar_filmes():
    if len(filmes[0]) == 0:
        print('Não há filmes cadastrados.')
    else:
        buscar = input("Nome do Filme: ")
        for i in range(len(filmes[0])):
            if filmes[0][i].lower() == buscar.lower():
                media = sum(filmes[2][i]) / len(filmes[2][i])
                print(f'Filme: {filmes[0][i]}, Gênero: {filmes[1][i]}, Média das Notas: {media:.2f}')
                return i
        print("Filme não encontrado.")
        return None

def avaliar_filmes():
    while True:
        if len(filmes[0]) == 0:
            print('Não há filmes cadastrados.')
        else:
            indice = buscar_filmes()
            if indice is not None:
                while True:
                    try:
                        nova_nota = float(input("Digite uma nova nota para o filme (0 a 10): "))
                        if 0 <= nova_nota <= 10:
                            break
                        else:
                            print("Nota inválida! Digite um valor entre 0 e 10.")
                    except ValueError:
                        print("Entrada inválida! Digite um número.")
                filmes[2][indice].append(nova_nota)
                media = sum(filmes[2][indice]) / len(filmes[2][indice])
                print("Nova nota registrada com sucesso!")
                print(f"Média de Notas: {media:.2f}")
                return
            else:
                print("Tente novamente.")

def remover_filme():
    if len(filmes[0]) == 0:
        print("Nenhum filme cadastrado para remover.")
        return
    nome = input("Digite o nome do filme que deseja remover: ").strip()
    for i in range(len(filmes[0])):
        if filmes[0][i].lower() == nome.lower():
                filmes[0].pop(i)
                filmes[1].pop(i)
                filmes[2].pop(i)
                filmes[3].pop(i)

                print(f"{nome} foi removido.")
        else:
            print("Filme não encontrado.")

def stats():
    if len(filmes[0]) == 0:
        print('Não há filmes cadastrados.')
    else:
        while True:
            print("===ESTATÍSTICAS===")
            print("1. Qtd. de Filmes")
            print("2. Média de Notas")
            print("3. Melhores Filmes")
            print("4. Gênero mais cadastrados")
            print("5. Voltar ao Menu")
            print()
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                print(f"Quantidade total de filmes cadastrados: {len(filmes[0])}")

            elif opcao == "2":
                total_notas = 0
                total_avaliacoes = 0
                for notas in filmes[2]:
                    total_notas += sum(notas)
                    total_avaliacoes += len(notas)
                if total_avaliacoes > 0:
                    media_geral = total_notas / total_avaliacoes
                    print(f"Média geral das notas: {media_geral:.2f}")
                else:
                    print("Nenhuma nota registrada ainda.")

            elif opcao == "3":
                if len(filmes[0]) == 0:
                    print("Nenhum filme cadastrado.")
                else:
                    melhores = []
                    maior_media = 0
                    for i in range(len(filmes[0])):
                        media = sum(filmes[2][i]) / len(filmes[2][i])
                        if media > maior_media:
                            maior_media = media
                            melhores = [i]
                        elif media == maior_media:
                            melhores.append(i)
                    print(f"Melhor(es) filme(s) com média {maior_media:.2f}:")
                    for i in melhores:
                        print(f"- {filmes[0][i]} ({filmes[1][i]})")

            elif opcao == "4":
                if len(filmes[1]) == 0:
                    print("Nenhum gênero cadastrado.")
                else:
                    from collections import Counter
                    contagem = Counter(filmes[1])
                    genero_mais_comum = contagem.most_common(1)[0]
                    print(f"Gênero mais cadastrado: {genero_mais_comum[0]} ({genero_mais_comum[1]} filmes)")

            elif opcao == "5":
                break

            else:
                print("Opção inválida. Tente novamente.")

def menu():
    while True:
        print("===MENU===")
        print("1. CADASTRAR FILMES")
        print("2. LISTAR FILMES")
        print("3. BUSCAR FILMES")
        print("4. AVALIAR FILMES")
        print("5. REMOVER FILMES")
        print("6. ESTATÍSTICAS")
        print("7. Encerrar SistemA")
        print()
        opcao = input("Digite uma opção: ")
        if opcao == "1":
            cadastro()
        elif opcao == "2":
            lista()
        elif opcao == "3":
            buscar_filmes()
        elif opcao == "4":
            avaliar_filmes()
        elif opcao == "5":
            remover_filme()
        elif opcao == "6":
            stats()
        elif opcao == "7":
            break
        else:
            print("opcção inválida. tente novamente.")
menu()
