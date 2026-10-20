
import json
import os
from dataclasses import dataclass, asdict, replace


ARQUIVO_DADOS = "biblioteca_funcional.json"


@dataclass(frozen=True)
class Livro:
    titulo: str
    autor: str
    ano: str
    isbn: str
    disponivel: bool = True
    usuario: str = None


# Funções de transformação e consulta

def criar_livro(titulo, autor, ano, isbn):
    return Livro(titulo, autor, ano, isbn)


def buscar_livro_por_isbn(livros, isbn):
    return next(
        (livro for livro in livros if livro.isbn == isbn),
        None
    )


def pesquisar_livros(livros, termo):
    termo = termo.lower()

    return list(filter(
        lambda livro:
            termo in livro.titulo.lower()
            or termo in livro.autor.lower()
            or termo in livro.isbn.lower(),
        livros
    ))


def livros_disponiveis(livros):
    return list(filter(lambda livro: livro.disponivel, livros))


def cadastrar_livro(livros, novo_livro):
    if buscar_livro_por_isbn(livros, novo_livro.isbn):
        return livros, False

    return livros + [novo_livro], True


def emprestar_livro(livros, isbn, usuario):
    livro = buscar_livro_por_isbn(livros, isbn)

    if livro is None or not livro.disponivel or not usuario.strip():
        return livros, False

    novos_livros = [
        replace(item, disponivel=False, usuario=usuario.strip())
        if item.isbn == isbn else item
        for item in livros
    ]

    return novos_livros, True


def devolver_livro(livros, isbn):
    livro = buscar_livro_por_isbn(livros, isbn)

    if livro is None or livro.disponivel:
        return livros, False

    novos_livros = [
        replace(item, disponivel=True, usuario=None)
        if item.isbn == isbn else item
        for item in livros
    ]

    return novos_livros, True


# Funções de armazenamento

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return [Livro(**item) for item in dados]

    except (json.JSONDecodeError, OSError, TypeError, KeyError):
        print("Aviso: não foi possível carregar os dados.")
        return []


def salvar_dados(livros):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(
            [asdict(livro) for livro in livros],
            arquivo,
            ensure_ascii=False,
            indent=4
        )


# Funções de apresentação

def exibir_livro(livro):
    situacao = "Disponível" if livro.disponivel else "Emprestado"

    print(f"\nTítulo: {livro.titulo}")
    print(f"Autor: {livro.autor}")
    print(f"Ano: {livro.ano}")
    print(f"ISBN: {livro.isbn}")
    print(f"Situação: {situacao}")

    if not livro.disponivel:
        print(f"Usuário: {livro.usuario}")


def exibir_lista(livros):
    if not livros:
        print("Nenhum livro encontrado.")
        return

    for livro in livros:
        exibir_livro(livro)


# Menu do programa

def menu():
    livros = carregar_dados()

    while True:
        print("\n" + "=" * 40)
        print("       SISTEMA DE BIBLIOTECA")
        print("         PARADIGMA FUNCIONAL")
        print("=" * 40)
        print("1. Cadastrar livro")
        print("2. Listar todos os livros")
        print("3. Pesquisar livro")
        print("4. Realizar empréstimo")
        print("5. Registrar devolução")
        print("6. Listar livros disponíveis")
        print("0. Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\n--- CADASTRAR LIVRO ---")
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            ano = input("Ano de publicação: ").strip()
            isbn = input("ISBN: ").strip()

            if not all([titulo, autor, ano, isbn]):
                print("Erro: todos os campos são obrigatórios.")
                continue

            novo_livro = criar_livro(titulo, autor, ano, isbn)
            livros, sucesso = cadastrar_livro(livros, novo_livro)

            if sucesso:
                salvar_dados(livros)
                print("Livro cadastrado com sucesso!")
            else:
                print("Erro: já existe um livro com esse ISBN.")

        elif opcao == "2":
            print("\n--- TODOS OS LIVROS ---")
            exibir_lista(livros)

        elif opcao == "3":
            termo = input("Digite título, autor ou ISBN: ").strip()
            exibir_lista(pesquisar_livros(livros, termo))

        elif opcao == "4":
            isbn = input("ISBN do livro: ").strip()
            usuario = input("Nome do usuário: ").strip()

            livros, sucesso = emprestar_livro(livros, isbn, usuario)

            if sucesso:
                salvar_dados(livros)
                print("Empréstimo realizado com sucesso!")
            else:
                print("Não foi possível realizar o empréstimo.")

        elif opcao == "5":
            isbn = input("ISBN do livro: ").strip()
            livros, sucesso = devolver_livro(livros, isbn)

            if sucesso:
                salvar_dados(livros)
                print("Devolução registrada com sucesso!")
            else:
                print("Não foi possível realizar a devolução.")

        elif opcao == "6":
            print("\n--- LIVROS DISPONÍVEIS ---")
            exibir_lista(livros_disponiveis(livros))

        elif opcao == "0":
            print("Programa encerrado. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
