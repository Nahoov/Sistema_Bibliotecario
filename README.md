Gestão de Biblioteca Full-Stack
É uma mini aplicação web desenvolvida para colocar em prática o fluxo completo de desenvolvimento de software (do Front, Back até o banco de dados). 
O projeto abrange desde a modelagem de dados e criação de uma API própria até o consumo de dados externos e a construção de uma interface responsiva.

🎯 Objetivo do Projeto
O foco principal deste repositório é o aprendizado técnico e a compreensão do ciclo de vida de uma aplicação:

- Construção de uma API RESTful do zero.

- Implementação de níveis de acesso (Admin vs. Usuário).

- Consumo da API pública Open Library para enriquecer o catálogo.

- Gerenciamento de estado no Front-End e persistência de dados no Back-End.

🛠️ Funcionalidades
👤 Perfil: Usuário Comum: 
   - Consulta de Acervo: Visualizar e pesquisar livros disponíveis na biblioteca.

  - Visualização de Detalhes: Ver informações detalhadas consumidas via Open Library.

🛡️ Perfil: Administrador (ADM)
  - Gestão de Livros: Adicionar, editar e excluir livros do acervo local.

  - Gestão de Usuários: Cadastro, atualização e remoção de usuários do sistema.

  - Controle de Empréstimos:  abrir solicitações de empréstimo, registrar a devolução.

📋 Fluxo de Dados

Autenticação: O sistema valida o nível de acesso no login.

Requisição: O Front-End solicita dados ao Back-End.

Processamento: O Back-End busca informações no Banco de Dados local ou na API da Open Library.

Resposta: Os dados são tratados e exibidos conforme a permissão do usuário.

🛠️ Tecnologias Utilizadas
Para garantir robustez e escalabilidade, o projeto utiliza:

- Linguagem: Python v3

- Framework Web (API): Flask

- Banco de Dados: PostgreSQL (Relacional)

- Integração: Open Library API

🚀 Como Executar (Em breve)

✍️ Autor
Desenvolvido por Nahomi como projeto de estudo e portfólio.
