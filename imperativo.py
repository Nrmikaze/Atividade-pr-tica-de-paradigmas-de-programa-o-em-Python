
import json
import os

ARQUIVO_DADOS = "biblioteca.json"


def carregar_dados():
    """Carrega os livros salvos ou inicia uma lista vazia."""
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            print("Aviso: não foi possível ler os dados salvos.")

    return []


def salvar_dados(livros):
    """Salva os livros em um arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)


def cadastrar_livro(livros):
    print("\n--- CADASTRAR LIVRO ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()
    isbn = input("ISBN: ").strip()

    if not titulo or not autor or not ano or not isbn:
        print("Erro: todos os campos são obrigatórios.")
        return

    if any(livro["isbn"] == isbn for livro in livros):
        print("Erro: já existe um livro com esse ISBN.")
        return

    livros.append({
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "disponivel": True,
        "usuario": None
    })

    salvar_dados(livros)
    print("Livro cadastrado com sucesso!")


def listar_livros(livros):
    print("\n--- LIVROS CADASTRADOS ---")

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        situacao = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"\nTítulo: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Situação: {situacao}")

        if not livro["disponivel"]:
            print(f"Usuário: {livro['usuario']}")


def pesquisar_livro(livros):
    print("\n--- PESQUISAR LIVRO ---")
    termo = input("Digite o título, autor ou ISBN: ").strip().lower()

    encontrados = [
        livro for livro in livros
        if termo in livro["titulo"].lower()
        or termo in livro["autor"].lower()
        or termo in livro["isbn"].lower()
    ]

    if not encontrados:
        print("Nenhum livro encontrado.")
        return

    for livro in encontrados:
        situacao = "Disponível" if livro["disponivel"] else "Emprestado"
        print(
            f"{livro['titulo']} | {livro['autor']} | "
            f"ISBN: {livro['isbn']} | {situacao}"
        )


def realizar_emprestimo(livros):
    print("\n--- REALIZAR EMPRÉSTIMO ---")
    isbn = input("ISBN do livro: ").strip()

    for livro in livros:
        if livro["isbn"] == isbn:
            if not livro["disponivel"]:
                print("Este livro já está emprestado.")
                return

            usuario = input("Nome do usuário: ").strip()

            if not usuario:
                print("O nome do usuário é obrigatório.")
                return

            livro["disponivel"] = False
            livro["usuario"] = usuario
            salvar_dados(livros)
            print("Empréstimo realizado com sucesso!")
            return

    print("Livro não encontrado.")


def registrar_devolucao(livros):
    print("\n--- REGISTRAR DEVOLUÇÃO ---")
    isbn = input("ISBN do livro: ").strip()

    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["disponivel"]:
                print("Este livro já está disponível.")
                return

            livro["disponivel"] = True
            livro["usuario"] = None
            salvar_dados(livros)
            print("Devolução registrada com sucesso!")
            return

    print("Livro não encontrado.")


def listar_disponiveis(livros):
    print("\n--- LIVROS DISPONÍVEIS ---")
    disponiveis = [livro for livro in livros if livro["disponivel"]]

    if not disponiveis:
        print("Nenhum livro disponível no momento.")
        return

    for livro in disponiveis:
        print(
            f"{livro['titulo']} | {livro['autor']} | "
            f"Ano: {livro['ano']} | ISBN: {livro['isbn']}"
        )


def menu():
    livros = carregar_dados()

    while True:
        print("\n" + "=" * 38)
        print("      SISTEMA DE BIBLIOTECA")
        print("       PARADIGMA IMPERATIVO")
        print("=" * 38)
        print("1. Cadastrar livro")
        print("2. Listar todos os livros")
        print("3. Pesquisar livro")
        print("4. Realizar empréstimo")
        print("5. Registrar devolução")
        print("6. Listar livros disponíveis")
        print("0. Sair")
        print("=" * 38)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            pesquisar_livro(livros)
        elif opcao == "4":
            realizar_emprestimo(livros)
        elif opcao == "5":
            registrar_devolucao(livros)
        elif opcao == "6":
            listar_disponiveis(livros)
        elif opcao == "0":
            print("Programa encerrado. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
