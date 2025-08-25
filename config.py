import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    """Configuração base da aplicação"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chave-temporaria-desenvolvimento')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = 0
    SESSION_PERMANENT = False

class DevelopmentConfig(Config):
    """Configuração para desenvolvimento local"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///reserva_salas.db'

class ProductionConfig(Config):
    """Configuração para produção (Render)"""
    DEBUG = False
    
    # Configuração do banco para produção
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Verificar se psycopg está disponível
    try:
        import psycopg
        psycopg_available = True
    except ImportError:
        psycopg_available = False
    
    if DATABASE_URL and (DATABASE_URL.startswith('postgres://') or DATABASE_URL.startswith('postgresql://')) and psycopg_available:
        # Render usa postgres:// mas SQLAlchemy espera postgresql://
        # FORÇA o uso do dialeto psycopg (versão 3)
        if DATABASE_URL.startswith('postgres://'):
            DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql+psycopg://', 1)
        elif DATABASE_URL.startswith('postgresql://'):
            DATABASE_URL = DATABASE_URL.replace('postgresql://', 'postgresql+psycopg://', 1)
        
        # Configurações específicas para PostgreSQL com psycopg
        SQLALCHEMY_ENGINE_OPTIONS = {
            'connect_args': {
                'connect_timeout': 10,
                'application_name': 'gest-o-escolas'
            }
        }
    else:
        # Usar SQLite se psycopg não estiver disponível
        DATABASE_URL = None
        SQLALCHEMY_ENGINE_OPTIONS = {}
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'sqlite:///reserva_salas.db'

# Configuração padrão baseada no ambiente
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig  # Mudei para development por padrão
}

def get_config():
    """Retorna a configuração baseada no ambiente"""
    env = os.environ.get('FLASK_ENV', 'development')  # Mudei para development por padrão
    print(f"Ambiente configurado: {env}")
    return config.get(env, config['default'])
