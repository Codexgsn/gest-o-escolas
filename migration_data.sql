-- Script de migração de dados do SQLite para PostgreSQL
-- Gerado em: 2025-08-24 00:26:26.691985
-- Execute este script no seu banco PostgreSQL do Render

-- Migração de usuários
INSERT INTO usuario (nome, email, senha, is_admin) VALUES ('Administrador do Sistema', 'admin@gmail.com', 'pbkdf2:sha256:600000$zB2UyK5sdQWVVdOn$270540664187c7cf36cb14485f6da5924659033a09e5c3d309ca069c86d658dc', True);
INSERT INTO usuario (nome, email, senha, is_admin) VALUES ('gustavo professor', 'gugudograu@gmail.com', 'pbkdf2:sha256:600000$khf1Mgj6IAwy26DK$26949e3b1c5de09261796245449c753ae8bc4847ea37661516a5d3a02a67474d', False);

-- Total de usuários migrados: 2

-- Migração de salas
INSERT INTO sala (nome, capacidade) VALUES ('3 A informática', 30);
INSERT INTO sala (nome, capacidade) VALUES ('sala teste', 20);

-- Total de salas migradas: 2

-- Migração de reservas
INSERT INTO reserva (professor_id, sala_id, data, horario_inicio, horario_fim, data_criacao) VALUES (3, 1, '2025-08-24', '08:20:00', '09:30:00', '2025-08-23 23:44:44.050131');
INSERT INTO reserva (professor_id, sala_id, data, horario_inicio, horario_fim, data_criacao) VALUES (3, 2, '2025-08-25', '13:20:00', '14:10:00', '2025-08-23 23:44:44.082646');
INSERT INTO reserva (professor_id, sala_id, data, horario_inicio, horario_fim, data_criacao) VALUES (3, 1, '2025-08-26', '15:20:00', '16:10:00', '2025-08-23 23:44:44.112542');
INSERT INTO reserva (professor_id, sala_id, data, horario_inicio, horario_fim, data_criacao) VALUES (3, 1, '2025-08-26', '07:30:00', '08:20:00', '2025-08-23 23:49:43.678585');

-- Total de reservas migradas: 4

-- Migração concluída!
