<<<<<<< HEAD
# Biblioteca_simples
=======
# 📚 Gestão de Biblioteca Full-Stack

Uma **mini aplicação web full-stack** desenvolvida com o objetivo de colocar em prática o **fluxo completo de desenvolvimento de software**, abrangendo **Front-End, Back-End e Banco de Dados**.

O projeto envolve desde a **modelagem de dados**, criação de uma **API própria**, controle de autenticação e permissões, até o **consumo de uma API externa** e a construção de uma interface preparada para uso real.

---

## 🎯 Objetivo do Projeto

O foco principal deste repositório é o **aprendizado técnico** e a compreensão do **ciclo de vida de uma aplicação web**, incluindo:

* Construção de uma **API RESTful** do zero
* Implementação de **níveis de acesso** (Administrador e Usuário)
* Consumo da API pública **Open Library** para enriquecer o catálogo
* Gerenciamento de estado no Front-End
* Persistência de dados no Back-End
* Integração entre diferentes camadas da aplicação

---

## 🛠️ Funcionalidades

### 👤 Perfil: Usuário Comum

* **Consulta de Acervo**: visualizar e pesquisar livros disponíveis na biblioteca
* **Visualização de Detalhes**: acessar informações detalhadas dos livros consumidas via Open Library API

---

### 🛡️ Perfil: Administrador (ADM)

* **Gestão de Livros**: adicionar, editar e remover livros do acervo local
* **Gestão de Usuários**: cadastrar, atualizar e excluir usuários do sistema
* **Controle de Empréstimos**:

  * Abrir solicitações de empréstimo
  * Registrar devoluções
  * Gerenciar o status dos livros

---

## 📋 Fluxo de Dados da Aplicação

1. **Autenticação**
   O sistema valida o login e identifica o nível de acesso do usuário.

2. **Requisição**
   O Front-End envia requisições para a API Back-End.

3. **Processamento**
   O Back-End processa a requisição, buscando dados no:

   * Banco de Dados local (PostgreSQL)
   * API externa Open Library

4. **Resposta**
   Os dados são tratados e retornados ao Front-End conforme as permissões do usuário.

---

## 🛠️ Tecnologias Utilizadas

Para garantir **robustez**, **organização** e **escalabilidade**, o projeto utiliza:

* **Linguagem:** Python 3
* **Framework Web (API):** Flask
* **Banco de Dados:** PostgreSQL (Relacional)
* **Integração Externa:** Open Library API
* **Arquitetura:** API REST
* **Controle de Acesso:** Autenticação com níveis de permissão

---

## 🚀 Como Executar o Projeto

> ⚠️ **Em desenvolvimento** — instruções de execução serão adicionadas em breve.

---

## 📌 Status do Projeto

🚧 Projeto em desenvolvimento, focado em aprendizado e construção de portfólio.

---

## ✍️ Autor

Desenvolvido por **Nahomi**
Projeto de estudo e portfólio para desenvolvimento **Full-Stack**.

---

Se você gostou do projeto ou tem sugestões, fique à vontade para contribuir ⭐

>>>>>>> develop
