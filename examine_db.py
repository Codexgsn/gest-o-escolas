#!/usr/bin/env python3
"""
Script para examinar o conteúdo completo do banco de dados
"""

import sqlite3
import os
from datetime import datetime

def examine_database():
    """Examina o conteúdo completo do banco de dados."""
    
    db_path = 'instance/reserva_salas.db'
    
    if not os.path.exists(db_path):
        print("❌ Banco de dados não encontrado!")
        return
    
    print("=" * 60)
    print("           ANÁLISE COMPLETA DO BANCO DE DADOS")
    print("=" * 60)
    print()
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. ESTRUTURA DAS TABELAS
    print("📋 ESTRUTURA DAS TABELAS:")
    print("-" * 40)
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        print(f"\n🔸 TABELA: {table_name}")
        
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        for col in columns:
            col_id, col_name, col_type, not_null, default_val, pk = col
            pk_str = " (PRIMARY KEY)" if pk else ""
            not_null_str = " NOT NULL" if not_null else ""
            default_str = f" DEFAULT {default_val}" if default_val else ""
            
            print(f"   • {col_name}: {col_type}{not_null_str}{default_str}{pk_str}")
    
    # 2. CONTEÚDO DAS TABELAS
    print("\n\n📊 CONTEÚDO DAS TABELAS:")
    print("-" * 40)
    
    # Usuários
    print("\n👥 TABELA USUÁRIOS:")
    cursor.execute("SELECT id, nome, email, is_admin FROM usuario ORDER BY id")
    usuarios = cursor.fetchall()
    
    if usuarios:
        print(f"   Total de usuários: {len(usuarios)}")
        for user in usuarios:
            admin_status = "✅ ADMIN" if user[3] else "👤 USUÁRIO"
            print(f"   • ID {user[0]}: {user[1]} ({user[2]}) - {admin_status}")
    else:
        print("   Nenhum usuário cadastrado")
    
    # Salas
    print("\n🏫 TABELA SALAS:")
    cursor.execute("SELECT id, nome, capacidade FROM sala ORDER BY id")
    salas = cursor.fetchall()
    
    if salas:
        print(f"   Total de salas: {len(salas)}")
        for sala in salas:
            print(f"   • ID {sala[0]}: {sala[1]} (Capacidade: {sala[2]} lugares)")
    else:
        print("   Nenhuma sala cadastrada")
    
    # Reservas
    print("\n📅 TABELA RESERVAS:")
    cursor.execute('''
        SELECT r.id, r.data, r.horario_inicio, r.horario_fim, 
               u.nome as professor, s.nome as sala, r.data_criacao
        FROM reserva r 
        JOIN usuario u ON r.professor_id = u.id 
        JOIN sala s ON r.sala_id = s.id
        ORDER BY r.data DESC, r.horario_inicio DESC
    ''')
    reservas = cursor.fetchall()
    
    if reservas:
        print(f"   Total de reservas: {len(reservas)}")
        for reserva in reservas:
            data_str = reserva[1] if isinstance(reserva[1], str) else reserva[1].strftime('%d/%m/%Y')
            hora_inicio = reserva[2] if isinstance(reserva[2], str) else reserva[2].strftime('%H:%M')
            hora_fim = reserva[3] if isinstance(reserva[3], str) else reserva[3].strftime('%H:%M')
            
            print(f"   • ID {reserva[0]}: {reserva[5]} - {data_str} {hora_inicio}-{hora_fim} ({reserva[4]})")
    else:
        print("   Nenhuma reserva cadastrada")
    
    # 3. ESTATÍSTICAS
    print("\n\n📈 ESTATÍSTICAS:")
    print("-" * 40)
    
    # Contagem por tipo de usuário
    cursor.execute("SELECT is_admin, COUNT(*) FROM usuario GROUP BY is_admin")
    admin_stats = cursor.fetchall()
    
    total_users = len(usuarios)
    admin_count = sum(1 for user in usuarios if user[3])
    regular_users = total_users - admin_count
    
    print(f"   👥 Total de usuários: {total_users}")
    print(f"   👑 Administradores: {admin_count}")
    print(f"   👤 Usuários comuns: {regular_users}")
    print(f"   🏫 Total de salas: {len(salas)}")
    print(f"   📅 Total de reservas: {len(reservas)}")
    
    # 4. RELACIONAMENTOS
    print("\n\n🔗 RELACIONAMENTOS:")
    print("-" * 40)
    
    # Verificar chaves estrangeiras
    cursor.execute("PRAGMA foreign_key_list(reserva)")
    foreign_keys = cursor.fetchall()
    
    if foreign_keys:
        print("   Chaves estrangeiras na tabela RESERVA:")
        for fk in foreign_keys:
            print(f"   • {fk[3]} -> {fk[4]}.{fk[5]}")
    else:
        print("   Nenhuma chave estrangeira encontrada")
    
    # 5. ÍNDICES
    print("\n\n🔍 ÍNDICES:")
    print("-" * 40)
    
    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='index'")
    indexes = cursor.fetchall()
    
    if indexes:
        for index in indexes:
            print(f"   • {index[0]}: {index[1]}")
    else:
        print("   Nenhum índice personalizado encontrado")
    
    # 6. INFORMAÇÕES DO BANCO
    print("\n\n💾 INFORMAÇÕES DO BANCO:")
    print("-" * 40)
    
    # Tamanho do arquivo
    file_size = os.path.getsize(db_path)
    print(f"   📁 Tamanho do arquivo: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    
    # Data de modificação
    mod_time = os.path.getmtime(db_path)
    mod_date = datetime.fromtimestamp(mod_time)
    print(f"   📅 Última modificação: {mod_date.strftime('%d/%m/%Y %H:%M:%S')}")
    
    # Versão do SQLite
    cursor.execute("SELECT sqlite_version()")
    sqlite_version = cursor.fetchone()[0]
    print(f"   🔧 Versão do SQLite: {sqlite_version}")
    
    conn.close()
    
    print("\n" + "=" * 60)
    print("           ANÁLISE CONCLUÍDA")
    print("=" * 60)

if __name__ == "__main__":
    examine_database() 