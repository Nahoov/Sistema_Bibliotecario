CREATE TYPE status_emprestimo_enum AS ENUM('ativo','atrasado','devolvido');
CREATE TYPE usuario_enum AS ENUM('usuario','admin');
CREATE TYPE status_solicitacao_enum AS ENUM ('pendente','aprovado','negado');



CREATE TABLE usuarios(
    id_usuario SERIAL PRIMARY KEY,
    nome_usuario VARCHAR(55) NOT NULL,
    sobrenome_usuario VARCHAR(80) NOT NULL,
    email VARCHAR(80) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    tipo_usuario usuario_enum  NOT NULL DEFAULT 'usuario',
    data_conta_criada TIMESTAMP WITH TIME ZONE DEFAULT now()
);



CREATE TABLE autores(
    id_autor SERIAL PRIMARY KEY,
    nome_autor VARCHAR(150) NOT NULL
);



CREATE TABLE categoria_livros(
    id_categoria SERIAL PRIMARY KEY,
    nome_categoria VARCHAR(100) UNIQUE NOT NULL
);



CREATE TABLE livros(
    id_livro SERIAL PRIMARY KEY,
    id_categoria INT NOT NULL,
    nome_livro VARCHAR(100) NOT NULL,
    data_lancamento DATE NOT NULL,
    FOREIGN KEY(id_categoria) REFERENCES categoria_livros(id_categoria)
    
);



CREATE TABLE livro_autores(
    id_autor INT NOT NULL,
    id_livro INT NOT NULL,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro),
    PRIMARY KEY(id_autor, id_livro)
);



CREATE TABLE emprestimo_livro(
    id_emprestimo SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_livro INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE NOT NULL,
    data_devolucao_real DATE,
    status_emprestimo status_emprestimo_enum DEFAULT 'ativo',
    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY(id_livro) REFERENCES livros(id_livro),
    CHECK (data_devolucao_prevista >= data_emprestimo)
);


CREATE TABLE solicitacoes_admin(
    id_solicitacao SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    data_solicitacao TIMESTAMP WITH TIME ZONE DEFAULT now(),
    status_solicitacao status_solicitacao_enum DEFAULT 'pendente',
    observacoes TEXT,
    revisado_por INT,                        -- id do admin que aprovou/negou
    data_revisao TIMESTAMP WITH TIME ZONE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (revisado_por) REFERENCES usuarios(id_usuario)
);

--PARA UM FUTURO
--CREATE TABLE avaliacoes_livros(
--);

--CREATE TABLE estoque_livros(
    --id_estoque SERIAL PRIMARY KEY,
    --id_livro INT NOT NULL,
    --qtd_disponivel INT,
    --FOREIGN KEY(id_livro) REFERENCES livros(id_livro)
--);