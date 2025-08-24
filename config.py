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
    # O banco será configurado pelo database_config.py
    # Não definimos SQLALCHEMY_DATABASE_URI aqui para evitar conflitos

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
