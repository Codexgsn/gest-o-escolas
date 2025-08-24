-- Schema do banco PostgreSQL para Gestão de Escolas
-- Gerado em: 2025-08-24 11:31:34.012561

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);

-- Tabela de salas
CREATE TABLE IF NOT EXISTS sala (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    capacidade INTEGER NOT NULL
);

-- Tabela de reservas
CREATE TABLE IF NOT EXISTS reserva (
    id SERIAL PRIMARY KEY,
    professor_id INTEGER NOT NULL REFERENCES usuario(id),
    sala_id INTEGER NOT NULL REFERENCES sala(id),
    data DATE NOT NULL,
    horario_inicio TIME NOT NULL,
    horario_fim TIME NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para melhorar performance
CREATE INDEX IF NOT EXISTS idx_reserva_professor ON reserva(professor_id);
CREATE INDEX IF NOT EXISTS idx_reserva_sala ON reserva(sala_id);
CREATE INDEX IF NOT EXISTS idx_reserva_data ON reserva(data);
CREATE INDEX IF NOT EXISTS idx_usuario_email ON usuario(email);

-- Comentários das tabelas
COMMENT ON TABLE usuario IS 'Tabela de usuários do sistema';
COMMENT ON TABLE sala IS 'Tabela de salas disponíveis para reserva';
COMMENT ON TABLE reserva IS 'Tabela de reservas de salas';
