
import json
import os


ARQUIVO_DADOS = "biblioteca_poo.json"


class Livro:
    def __init__(self, titulo, autor, ano, isbn,
                 disponivel=True, usuario=None):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn
        self.disponivel = disponivel
        self.usuario = usuario

    def exibir_dados(self):
        situacao = "Disponível" if self.disponivel else "Emprestado"

        print(f"\nTítulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"ISBN: {self.isbn}")
        print(f"Situação: {situacao}")

        if not self.disponivel:
            print(f"Usuário: {self.usuario}")

    def para_dicionario(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "isbn": self.isbn,
            "disponivel": self.disponivel,
            "usuario": self.usuario
        }


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(ARQUIVO_DADOS):
            try:
                with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)

                self.livros = [
                    Livro(
                        item["titulo"],
                        item["autor"],
                        item["ano"],
                        item["isbn"],
                        item.get("disponivel", True),
                        item.get("usuario")
                    )
                    for item in dados
                ]
            except (json.JSONDecodeError, OSError, KeyError):
                print("Aviso: não foi possível carregar os dados.")

    def salvar_dados(self):
        dados = [livro.para_dicionario() for livro in self.livros]

        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def cadastrar_livro(self):
        print("\n--- CADASTRAR LIVRO ---")

        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        ano = input("Ano de publicação: ").strip()
        isbn = input("ISBN: ").strip()

        if not titulo or not autor or not ano or not isbn:
            print("Erro: todos os campos são obrigatórios.")
            return

        if any(livro.isbn == isbn for livro in self.livros):
            print("Erro: já existe um livro com esse ISBN.")
            return

        novo_livro = Livro(titulo, autor, ano, isbn)
        self.livros.append(novo_livro)
        self.salvar_dados()

        print("Livro cadastrado com sucesso!")

    def listar_livros(self):
        print("\n--- TODOS OS LIVROS ---")

        if not self.livros:
            print("Nenhum livro cadastrado.")
            return

        for livro in self.livros:
            livro.exibir_dados()

    def pesquisar_livro(self):
        print("\n--- PESQUISAR LIVRO ---")
        termo = input("Digite título, autor ou ISBN: ").strip().lower()

        encontrados = [
            livro for livro in self.livros
            if termo in livro.titulo.lower()
            or termo in livro.autor.lower()
            or termo in livro.isbn.lower()
        ]

        if not encontrados:
            print("Nenhum livro encontrado.")
            return

        for livro in encontrados:
            livro.exibir_dados()

    def realizar_emprestimo(self):
        print("\n--- REALIZAR EMPRÉSTIMO ---")
        isbn = input("ISBN do livro: ").strip()

        for livro in self.livros:
            if livro.isbn == isbn:
                if not livro.disponivel:
                    print("Este livro já está emprestado.")
                    return

                usuario = input("Nome do usuário: ").strip()

                if not usuario:
                    print("O nome do usuário é obrigatório.")
                    return

                livro.disponivel = False
                livro.usuario = usuario
                self.salvar_dados()

                print("Empréstimo realizado com sucesso!")
                return

        print("Livro não encontrado.")

    def registrar_devolucao(self):
        print("\n--- REGISTRAR DEVOLUÇÃO ---")
        isbn = input("ISBN do livro: ").strip()

        for livro in self.livros:
            if livro.isbn == isbn:
                if livro.disponivel:
                    print("Este livro já está disponível.")
                    return

                livro.disponivel = True
                livro.usuario = None
                self.salvar_dados()

                print("Devolução registrada com sucesso!")
                return

        print("Livro não encontrado.")

    def listar_disponiveis(self):
        print("\n--- LIVROS DISPONÍVEIS ---")

        disponiveis = [
            livro for livro in self.livros if livro.disponivel
        ]

        if not disponiveis:
            print("Nenhum livro disponível no momento.")
            return

        for livro in disponiveis:
            livro.exibir_dados()

    def executar(self):
        while True:
            print("\n" + "=" * 38)
            print("      SISTEMA DE BIBLIOTECA")
            print("   ORIENTADO A OBJETOS (POO)")
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
                self.cadastrar_livro()
            elif opcao == "2":
                self.listar_livros()
            elif opcao == "3":
                self.pesquisar_livro()
            elif opcao == "4":
                self.realizar_emprestimo()
            elif opcao == "5":
                self.registrar_devolucao()
            elif opcao == "6":
                self.listar_disponiveis()
            elif opcao == "0":
                print("Programa encerrado. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.executar()

