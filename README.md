# 🏫 Sistema de Reserva de Salas - Documentação Completa

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Instalação e Configuração](#instalação-e-configuração)
6. [Como Usar](#como-usar)
7. [Deploy Gratuito na Internet](#deploy-gratuito-na-internet)
8. [Arquitetura do Sistema](#arquitetura-do-sistema)
9. [Banco de Dados](#banco-de-dados)
10. [Segurança](#segurança)
11. [Personalização](#personalização)
12. [Troubleshooting](#troubleshooting)

---

## 🎯 Visão Geral

O **Sistema de Reserva de Salas** é uma aplicação web desenvolvida em Python/Flask que permite gerenciar reservas de salas de aula de forma eficiente e organizada. Ideal para escolas, universidades, empresas ou qualquer instituição que precise gerenciar o uso de espaços físicos.

### 🎯 Objetivos do Sistema
- ✅ **Facilitar reservas** de salas de forma simples e intuitiva
- ✅ **Evitar conflitos** de horários automaticamente
- ✅ **Gerenciar usuários** com diferentes níveis de acesso
- ✅ **Fornecer relatórios** de uso das salas
- ✅ **Interface responsiva** para uso em qualquer dispositivo

---

## 🚀 Funcionalidades

### 👤 **Para Usuários Comuns:**
- 🔐 **Login/Cadastro** com email e senha
- 📅 **Fazer reservas** de salas para datas futuras
- 🕐 **Escolher horários** dentro do período permitido
- 👀 **Visualizar suas reservas** ativas
- ❌ **Cancelar reservas** próprias
- 🔍 **Ver todas as reservas** do sistema (somente ativas)

### 👨‍💼 **Para Administradores:**
- 👥 **Gerenciar usuários** (criar, editar, excluir)
- 🏢 **Gerenciar salas** (adicionar, remover)
- 📝 **Criar reservas** para qualquer usuário
- ✏️ **Editar reservas** existentes
- 🗑️ **Excluir reservas** de qualquer usuário
- 📊 **Visualizar todas as reservas** (ativas e passadas)
- 🔧 **Configurar permissões** de administrador

### 🛡️ **Sistema de Segurança:**
- 🔐 **Autenticação** obrigatória para todas as operações
- 👮‍♂️ **Controle de acesso** baseado em roles
- 🛡️ **Proteção contra conflitos** de horários
- 🔒 **Senhas criptografadas** com hash seguro
- ⏰ **Validação de datas** e horários

---

## 🛠️ Tecnologias Utilizadas

### **Backend:**
- **Python 3.8+** - Linguagem principal
- **Flask 3.0.0** - Framework web
- **Flask-Login 0.6.3** - Sistema de autenticação
- **Flask-SQLAlchemy 3.1.1** - ORM para banco de dados
- **SQLite** - Banco de dados (pode ser migrado para PostgreSQL/MySQL)

### **Frontend:**
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização responsiva
- **JavaScript** - Interatividade
- **Bootstrap** - Framework CSS (opcional)

### **Ferramentas de Desenvolvimento:**
- **Git** - Controle de versão
- **pip** - Gerenciador de pacotes Python
- **SQLite Browser** - Visualização do banco de dados

---

## 📁 Estrutura do Projeto

```
reserva_salas/
├── 📄 app.py                 # Aplicação principal Flask
├── 📄 models.py              # Modelos do banco de dados
├── 📄 requirements.txt       # Dependências Python
├── 📁 templates/             # Templates HTML
│   ├── 📄 base.html          # Template base
│   ├── 📄 index.html         # Página inicial
│   ├── 📄 login.html         # Página de login
│   ├── 📄 register.html      # Página de cadastro
│   ├── 📄 reservas.html      # Página de reservas
│   ├── 📄 todas_reservas.html # Lista de todas as reservas
│   ├── 📄 admin.html         # Painel administrativo
│   ├── 📄 novo_usuario.html  # Criar usuário
│   ├── 📄 editar_usuario.html # Editar usuário
│   ├── 📄 editar_reserva.html # Editar reserva
│   └── 📄 README_ADMIN.md    # Documentação do admin
├── 📁 static/                # Arquivos estáticos
│   └── 📄 style.css          # Estilos CSS
├── 📁 instance/              # Banco de dados SQLite
│   └── 📄 reserva_salas.db   # Arquivo do banco
├── 📄 start_server.bat       # Script para iniciar servidor
├── 📄 stop_server.bat        # Script para parar servidor
└── 📄 setup_admin.bat        # Script de configuração
```

---

## ⚙️ Instalação e Configuração

### **Pré-requisitos:**
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

### **Passo a Passo:**

#### 1. **Baixar o Projeto**
```bash
# Opção 1: Clonar do Git
git clone [URL_DO_REPOSITORIO]
cd reserva_salas

# Opção 2: Baixar arquivo ZIP e extrair
```

#### 2. **Instalar Dependências**
```bash
pip install -r requirements.txt
```

#### 3. **Executar o Sistema**
```bash
python app.py
```

#### 4. **Acessar o Sistema**
- Abra o navegador
- Acesse: `http://localhost:5000`
- Use as credenciais padrão:
  - **Email:** admin@gmail.com
  - **Senha:** @dm1n

### **Scripts Automatizados (Windows):**
- **`setup_admin.bat`** - Instala dependências e inicia o sistema
- **`start_server.bat`** - Inicia o servidor
- **`stop_server.bat`** - Para o servidor

---

## 📖 Como Usar

### **Primeiro Acesso:**
1. Acesse o sistema pela primeira vez
2. O usuário administrador é criado automaticamente
3. Faça login com as credenciais padrão
4. Altere a senha do administrador por segurança

### **Para Usuários Comuns:**
1. **Cadastro:** Clique em "Cadastrar" na página inicial
2. **Login:** Use email e senha para acessar
3. **Fazer Reserva:**
   - Selecione a data
   - Escolha a sala
   - Defina horário de início e fim
   - Clique em "Fazer Reserva"
4. **Gerenciar Reservas:** Veja, edite ou cancele suas reservas

### **Para Administradores:**
1. **Login:** Use credenciais de administrador
2. **Painel Admin:** Acesse automaticamente o painel administrativo
3. **Gerenciar Usuários:** Crie, edite ou exclua usuários
4. **Gerenciar Salas:** Adicione ou remova salas
5. **Gerenciar Reservas:** Crie, edite ou exclua reservas de qualquer usuário

---

## 🌐 Deploy Gratuito na Internet

### **Opção 1: Render (Recomendado)**
**Vantagens:** Gratuito, fácil, suporte a Python/Flask

#### Passos:
1. **Criar conta:** Acesse [render.com](https://render.com)
2. **Conectar repositório:** Conecte seu GitHub/GitLab
3. **Configurar build:**
   ```bash
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   ```
4. **Variáveis de ambiente:**
   ```
   SECRET_KEY=sua_chave_secreta_aqui
   ```
5. **Deploy:** Clique em "Deploy"

#### Arquivo `requirements.txt` necessário:
```
Flask==3.0.0
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.1
gunicorn==21.2.0
```

### **Opção 2: Railway**
**Vantagens:** Gratuito, muito fácil, suporte nativo a Python

#### Passos:
1. Acesse [railway.app](https://railway.app)
2. Conecte seu repositório GitHub
3. Railway detecta automaticamente que é um projeto Python
4. Deploy automático

### **Opção 3: Heroku (Limitado)**
**Vantagens:** Confiável, mas plano gratuito limitado

#### Passos:
1. Crie conta no [heroku.com](https://heroku.com)
2. Instale Heroku CLI
3. Execute:
   ```bash
   heroku create seu-app-name
   git push heroku main
   ```

### **Opção 4: PythonAnywhere**
**Vantagens:** Especializado em Python, muito fácil

#### Passos:
1. Crie conta em [pythonanywhere.com](https://pythonanywhere.com)
2. Faça upload dos arquivos
3. Configure o WSGI file
4. Deploy automático

### **Configurações para Deploy:**

#### 1. **Arquivo `requirements.txt`:**
```
Flask==3.0.0
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
Werkzeug==3.0.1
gunicorn==21.2.0
```

#### 2. **Arquivo `Procfile` (para Heroku):**
```
web: gunicorn app:app
```

#### 3. **Modificar `app.py` para produção:**
```python
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_default_admin_if_not_exists()
    # Para produção, use:
    # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    # Para desenvolvimento:
    app.run(debug=True)
```

---

## 🏗️ Arquitetura do Sistema

### **Padrão MVC (Model-View-Controller):**

#### **Model (Modelos):**
- **`Usuario`** - Gerencia usuários e autenticação
- **`Sala`** - Gerencia salas disponíveis
- **`Reserva`** - Gerencia reservas e relacionamentos

#### **View (Templates):**
- **HTML Templates** - Interface do usuário
- **CSS** - Estilização responsiva
- **JavaScript** - Interatividade

#### **Controller (Rotas):**
- **Rotas de Autenticação** - Login, logout, registro
- **Rotas de Reservas** - Criar, editar, cancelar reservas
- **Rotas Administrativas** - Gerenciamento do sistema

### **Fluxo de Dados:**
1. **Usuário** acessa uma página
2. **Flask** processa a requisição
3. **Modelo** consulta/atualiza o banco de dados
4. **Template** renderiza a resposta
5. **Usuário** recebe a página atualizada

---

## 🗄️ Banco de Dados

### **Estrutura das Tabelas:**

#### **Tabela `usuario`:**
```sql
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE
);
```

#### **Tabela `sala`:**
```sql
CREATE TABLE sala (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    capacidade INTEGER NOT NULL
);
```

#### **Tabela `reserva`:**
```sql
CREATE TABLE reserva (
    id INTEGER PRIMARY KEY,
    professor_id INTEGER NOT NULL,
    sala_id INTEGER NOT NULL,
    data DATE NOT NULL,
    horario_inicio TIME NOT NULL,
    horario_fim TIME NOT NULL,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (professor_id) REFERENCES usuario(id),
    FOREIGN KEY (sala_id) REFERENCES sala(id)
);
```

### **Relacionamentos:**
- **Usuario** → **Reserva** (1:N) - Um usuário pode ter várias reservas
- **Sala** → **Reserva** (1:N) - Uma sala pode ter várias reservas
- **Reserva** → **Usuario** (N:1) - Uma reserva pertence a um usuário
- **Reserva** → **Sala** (N:1) - Uma reserva pertence a uma sala

---

## 🔒 Segurança

### **Medidas Implementadas:**

#### **Autenticação:**
- ✅ **Login obrigatório** para todas as operações
- ✅ **Senhas criptografadas** com Werkzeug
- ✅ **Sessões seguras** com chave secreta
- ✅ **Logout automático** ao fechar navegador

#### **Autorização:**
- ✅ **Controle de acesso** baseado em roles
- ✅ **Decorator `@admin_required`** para rotas administrativas
- ✅ **Validação de propriedade** (usuário só edita suas reservas)

#### **Validação de Dados:**
- ✅ **Validação de email** com regex
- ✅ **Validação de datas** (não permite datas passadas)
- ✅ **Validação de horários** (não permite conflitos)
- ✅ **Sanitização de inputs** para prevenir SQL injection

#### **Proteção contra Ataques:**
- ✅ **CSRF Protection** (Flask-WTF opcional)
- ✅ **SQL Injection** (prevenido pelo ORM)
- ✅ **XSS Protection** (escape automático nos templates)

---

## 🎨 Personalização

### **Cores e Estilo:**
Edite o arquivo `static/style.css`:
```css
:root {
    --primary-color: #4CAF50;    /* Cor principal */
    --secondary-color: #2196F3;  /* Cor secundária */
    --accent-color: #FF9800;     /* Cor de destaque */
    --text-color: #333;          /* Cor do texto */
    --background-color: #f5f5f5; /* Cor de fundo */
}
```

### **Horários Permitidos:**
Edite no arquivo `app.py`:
```python
HORARIOS_PERMITIDOS = [
    ("07:30", "manhã"),
    ("08:20", "manhã"),
    ("09:30", "manhã"),
    # Adicione ou remova horários conforme necessário
]
```

### **Salas Padrão:**
Edite na função `popular_salas()`:
```python
nomes = [
    'Sala 101', 'Sala 102', 'Sala 103',
    'Laboratório 1', 'Laboratório 2',
    'Auditório', 'Sala de Reunião'
]
```

### **Configurações do Sistema:**
```python
# Em app.py
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reserva_salas.db'
app.config['REMEMBER_COOKIE_DURATION'] = 0  # Sessão expira ao fechar
```

---

## 🔧 Troubleshooting

### **Problemas Comuns:**

#### **1. Erro de Dependências:**
```bash
# Solução: Instalar dependências
pip install -r requirements.txt
```

#### **2. Erro de Banco de Dados:**
```bash
# Solução: Recriar banco
rm instance/reserva_salas.db
python app.py  # Banco será criado automaticamente
```

#### **3. Erro de Porta em Uso:**
```bash
# Solução: Mudar porta
python app.py --port 5001
```

#### **4. Erro de Permissões:**
```bash
# Solução: Dar permissões de escrita
chmod 755 reserva_salas/
```

#### **5. Erro de Python 3.13:**
```bash
# Solução: Usar Python 3.8-3.11
# Ou atualizar dependências:
pip install --upgrade Flask-SQLAlchemy
```

### **Logs de Erro:**
- Verifique o console onde o servidor está rodando
- Logs aparecem em tempo real
- Erros são exibidos com detalhes

---

## 📚 Recursos Adicionais

### **Documentação Técnica:**
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)

### **Tutoriais Relacionados:**
- [Deploy Flask no Render](https://render.com/docs/deploy-flask)
- [Deploy Flask no Railway](https://docs.railway.app/deploy/deployments)
- [Deploy Flask no Heroku](https://devcenter.heroku.com/articles/python)

### **Ferramentas Úteis:**
- [SQLite Browser](https://sqlitebrowser.org/) - Visualizar banco de dados
- [Postman](https://www.postman.com/) - Testar APIs
- [GitHub](https://github.com/) - Controle de versão

---

## 🤝 Contribuição

### **Como Contribuir:**
1. **Fork** o projeto
2. **Crie** uma branch para sua feature
3. **Commit** suas mudanças
4. **Push** para a branch
5. **Abra** um Pull Request

### **Padrões de Código:**
- Use **PEP 8** para estilo Python
- Documente funções e classes
- Teste suas mudanças
- Mantenha compatibilidade

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo `LICENSE` para detalhes.

### **Permissões:**
- ✅ **Usar** comercialmente
- ✅ **Modificar** o código
- ✅ **Distribuir** livremente
- ✅ **Usar** privadamente
- ❌ **Responsabilidade** do autor

---

## 📞 Suporte

### **Canais de Ajuda:**
- 📧 **Email:** seu-email@exemplo.com
- 💬 **Discord:** [Link do servidor]
- 📱 **WhatsApp:** [Seu número]
- 🌐 **Website:** [Seu site]

### **FAQ:**
**Q: Como mudar a senha do administrador?**
A: Acesse o painel admin → Editar usuário → Alterar senha

**Q: Como adicionar mais salas?**
A: Acesse o painel admin → Gerenciar salas → Adicionar sala

**Q: Como fazer backup do banco?**
A: Copie o arquivo `instance/reserva_salas.db`

---

**🎉 Parabéns! Agora você tem um sistema completo de reserva de salas pronto para uso e deploy!** 