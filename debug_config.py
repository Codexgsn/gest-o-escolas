    #!/usr/bin/env python3
"""
Debug da configuração do banco de dados
"""

import os

def debug_environment():
    """Debug das variáveis de ambiente"""
    
    print("🔍 DEBUG DAS VARIÁVEIS DE AMBIENTE")
    print("=" * 50)
    
    # Verificar variáveis importantes
    database_url = os.environ.get('DATABASE_URL')
    flask_env = os.environ.get('FLASK_ENV')
    secret_key = os.environ.get('SECRET_KEY')
    
    print(f"🔗 DATABASE_URL: {database_url}")
    print(f"🌍 FLASK_ENV: {flask_env}")
    print(f"🔐 SECRET_KEY: {'✅ Configurada' if secret_key else '❌ Não configurada'}")
    
    if database_url:
        if database_url.startswith('postgresql://'):
            print("✅ Usando PostgreSQL (formato correto)")
        elif database_url.startswith('postgres://'):
            print("⚠️  Usando postgres:// (precisa ser convertido)")
        else:
            print("❌ Formato de URL desconhecido")
    else:
        print("❌ DATABASE_URL não encontrada!")

def debug_config_file():
    """Debug do arquivo de configuração"""
    
    print("\n🔧 DEBUG DO ARQUIVO DE CONFIGURAÇÃO")
    print("=" * 50)
    
    try:
        from config import get_config
        
        config = get_config()
        print(f"✅ Configuração carregada: {config.__class__.__name__}")
        print(f"🔗 SQLALCHEMY_DATABASE_URI: {config.SQLALCHEMY_DATABASE_URI}")
        
        if hasattr(config, 'SQLALCHEMY_ENGINE_OPTIONS'):
            print(f"⚙️  SQLALCHEMY_ENGINE_OPTIONS: {config.SQLALCHEMY_ENGINE_OPTIONS}")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao carregar configuração: {e}")
        return False

def debug_database_url():
    """Debug da função get_database_url"""
    
    print("\n🔗 DEBUG DA FUNÇÃO GET_DATABASE_URL")
    print("=" * 50)
    
    try:
        from database import get_database_url
        
        url = get_database_url()
        print(f"🔗 URL retornada: {url}")
        
        if url.startswith('postgresql+psycopg://'):
            print("✅ Usando dialeto psycopg (PostgreSQL)")
        elif url.startswith('sqlite://'):
            print("⚠️  Usando SQLite (local)")
        else:
            print("❌ Formato de URL desconhecido")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao executar get_database_url: {e}")
        return False

if __name__ == "__main__":
    print("🚀 DEBUG COMPLETO DA CONFIGURAÇÃO")
    print("=" * 50)
    
    # Debug das variáveis de ambiente
    debug_environment()
    
    # Debug do arquivo de configuração
    config_ok = debug_config_file()
    
    # Debug da função get_database_url
    database_ok = debug_database_url()
    
    print("\n" + "=" * 50)
    print("📊 RESUMO DO DEBUG:")
    print("=" * 50)
    
    print(f"🔧 Configuração: {'✅ OK' if config_ok else '❌ FALHOU'}")
    print(f"🔗 Database URL: {'✅ OK' if database_ok else '❌ FALHOU'}")
    
    # Verificar se está tudo configurado
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgresql://'):
        print("🎉 Configuração PostgreSQL está correta!")
    else:
        print("⚠️  Configuração PostgreSQL precisa ser ajustada!")
