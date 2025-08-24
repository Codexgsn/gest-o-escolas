import os

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
    # Usa PostgreSQL se disponível, senão SQLite
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        # Render usa postgres:// mas SQLAlchemy espera postgresql://
        # Força o uso do dialeto psycopg (versão 3)
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql+psycopg://', 1)
        print(f"URL do banco configurada: {DATABASE_URL}")
        
        # Configurações específicas para PostgreSQL
        SQLALCHEMY_ENGINE_OPTIONS = {
            'connect_args': {
                'connect_timeout': 10,
                'application_name': 'gest-o-escolas'
            }
        }
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'sqlite:///reserva_salas.db'
    print(f"SQLALCHEMY_DATABASE_URI final: {SQLALCHEMY_DATABASE_URI}")

# Configuração padrão baseada no ambiente
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': ProductionConfig  # Mudei para production por padrão
}

def get_config():
    """Retorna a configuração baseada no ambiente"""
    env = os.environ.get('FLASK_ENV', 'production')  # Mudei para production por padrão
    print(f"Ambiente configurado: {env}")
    return config.get(env, config['default'])
