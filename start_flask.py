import subprocess
import sys
import os

if os.path.exists('flask.pid'):
    print('Já existe um servidor rodando (flask.pid encontrado). Use o stop_server.bat antes de iniciar outro.')
    sys.exit(1)

# Inicia o servidor Flask em background
proc = subprocess.Popen([sys.executable, 'app.py'])

# Salva o PID
with open('flask.pid', 'w') as f:
    f.write(str(proc.pid))

print(f'Servidor Flask iniciado em background (PID: {proc.pid})!')
print('Para parar o servidor, use o arquivo stop_server.bat') 