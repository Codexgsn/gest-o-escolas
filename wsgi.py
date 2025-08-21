#!/usr/bin/env python3
"""
Arquivo WSGI para produção no Render
Este arquivo é usado pelo Gunicorn para iniciar a aplicação
"""

import os
from app import app, db, create_default_admin_if_not_exists

# Configurar ambiente de produção
os.environ['FLASK_ENV'] = 'production'

# Criar tabelas e admin padrão se necessário
with app.app_context():
    db.create_all()
    create_default_admin_if_not_exists()

# Aplicação para o Gunicorn
application = app

if __name__ == '__main__':
    # Para desenvolvimento local
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
