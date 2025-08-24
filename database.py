#!/usr/bin/env python3
"""
Configuração específica para banco de dados PostgreSQL
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_database_url():
    """Retorna a URL do banco de dados configurada"""
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        # Render usa postgres:// mas SQLAlchemy espera postgresql://
        # Força o uso do dialeto psycopg (versão 3)
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql+psycopg://', 1)
        print(f"URL do banco configurada: {DATABASE_URL}")
        return DATABASE_URL
    
    return 'sqlite:///reserva_salas.db'

def create_database_engine():
    """Cria o engine do banco de dados"""
    database_url = get_database_url()
    
    if database_url.startswith('postgresql+psycopg://'):
        # Configurações específicas para PostgreSQL
        engine = create_engine(
            database_url,
            echo=False,  # Set to True for debug
            connect_args={
                'connect_timeout': 10,
                'application_name': 'gest-o-escolas'
            }
        )
        print("✅ Engine PostgreSQL criado com sucesso")
    else:
        # SQLite para desenvolvimento
        engine = create_engine(database_url, echo=False)
        print("✅ Engine SQLite criado com sucesso")
    
    return engine

def get_session_factory():
    """Retorna a factory de sessões do banco"""
    engine = create_database_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal

if __name__ == "__main__":
    # Teste da configuração
    print("🧪 Testando configuração do banco...")
    print("=" * 50)
    
    try:
        engine = create_database_engine()
        print(f"✅ Engine criado: {engine}")
        
        # Testa se consegue conectar (pode falhar se não houver banco)
        with engine.connect() as conn:
            print("✅ Conexão com banco estabelecida")
            
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        print("⚠️  Isso é normal se o banco PostgreSQL não estiver disponível")
