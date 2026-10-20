# Atividade-pr-tica-de-paradigmas-de-programa-o-em-Python

# 📚 Sistema de Gerenciamento de Biblioteca

## 📌 Sobre o projeto

Este projeto foi desenvolvido para a atividade prática da disciplina de Fundamentos e Paradigmas de Programação.

O objetivo é implementar um sistema simples de gerenciamento de biblioteca utilizando três paradigmas de programação: imperativo, orientado a objetos e funcional.

## 🎯 Funcionalidades

O sistema permite:

- Cadastrar livros com título, autor, ano de publicação e ISBN.
- Listar todos os livros cadastrados.
- Realizar empréstimos informando o ISBN e o nome do usuário.
- Registrar a devolução de livros pelo ISBN.
- Listar os livros disponíveis.
- Salvar os dados em arquivos JSON para manter os registros entre execuções.

## 🛠️ Tecnologias utilizadas

- Python 3
- Visual Studio Code
- Git e GitHub
- Arquivos JSON para persistência de dados

## 📂 Estrutura do projeto

```text
fundamentos-paradigmas-programacao/
├── README.md
├── imperativo.py
├── orientado_objetos.py
├── funcional.py
├── biblioteca.json
├── biblioteca_poo.json
└── biblioteca_funcional.json
```

Os arquivos JSON são criados automaticamente quando os respectivos programas salvam dados. Eles podem não existir antes do primeiro cadastro.

## ▶️ Como executar

É necessário ter o Python 3 instalado.

Abra o terminal na pasta do projeto e execute o programa desejado:

### 1. Paradigma imperativo

```bash
py imperativo.py
```

### 2. Paradigma orientado a objetos

```bash
py orientado_objetos.py
```

### 3. Paradigma funcional

```bash
py funcional.py
```

Após executar o comando, siga as opções apresentadas no menu do sistema.

## 🧠 Paradigmas de programação

### 1. Imperativo

Organiza o programa por meio de instruções sequenciais, funções e alterações de estado. É uma abordagem direta para implementar as operações da biblioteca.

Arquivo: `imperativo.py`

### 2. Orientado a objetos (POO)

Organiza o código em classes e objetos. A classe `Livro` representa os livros, enquanto a classe `Biblioteca` reúne as operações de gerenciamento.

Arquivo: `orientado_objetos.py`

### 3. Funcional

Utiliza funções para pesquisar, filtrar e transformar dados. A implementação procura evitar alterações diretas nos objetos de livro, utilizando dados imutáveis nas operações principais.

Arquivo: `funcional.py`

## 💾 Persistência dos dados

Cada implementação utiliza seu próprio arquivo JSON:

- `biblioteca.json`
- `biblioteca_poo.json`
- `biblioteca_funcional.json`

Essa separação permite testar os três programas independentemente.

## 🧪 Testes realizados

Os testes devem verificar:

- Cadastro e listagem de livros.
- Pesquisa por título, autor ou ISBN.
- Empréstimo de livros.
- Devolução de livros.
- Listagem de livros disponíveis.
- Persistência dos dados após encerrar e executar novamente o programa.

## 📊 Comparação entre os paradigmas

O paradigma imperativo apresenta uma sequência de instruções simples e direta.

O paradigma orientado a objetos permite organizar os dados e comportamentos em classes, facilitando a estruturação do sistema.

O paradigma funcional favorece o uso de funções de transformação e consulta, buscando reduzir alterações de estado.

A facilidade de implementação, a legibilidade e a manutenção podem variar de acordo com a experiência do programador e a complexidade do sistema.

## 👨‍💻 Autor

Bruno Souza

## 📄 Finalidade

Projeto acadêmico desenvolvido para estudo e comparação de paradigmas de programação.
