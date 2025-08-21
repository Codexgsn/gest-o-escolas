# 🏫 Sistema de Reserva de Salas

Sistema web para gerenciamento de reservas de salas de aula desenvolvido em Flask com PostgreSQL.

## 🚀 **Deploy no Render**

### **Deploy Automático (Recomendado)**
1. **Fazer commit das mudanças:**
   ```bash
   git add .
   git commit -m "Configuração PostgreSQL para Render"
   git push origin main
   ```

2. **No Render:**
   - Acesse [render.com](https://render.com)
   - Clique em "New +" → "Blueprint"
   - Conecte seu repositório GitHub
   - O `render.yaml` será detectado automaticamente
   - Clique em "Apply"

### **Deploy Manual**
1. **Criar serviço web** no Render
2. **Criar banco PostgreSQL** no Render
3. **Conectar banco ao serviço** via variável `DATABASE_URL`

## 🔧 **Configuração Local**

### **Instalar dependências:**
```bash
pip install -r requirements.txt
```

### **Executar aplicação:**
```bash
python app.py
```

### **Acessar:**
- **URL:** http://localhost:5000
- **Admin:** admin@gmail.com / @dm1n

## 📁 **Estrutura do Projeto**

```
gest-o-escolas/
├── app.py                 # Aplicação principal Flask
├── models.py              # Modelos do banco de dados
├── config.py              # Configuração por ambiente
├── wsgi.py                # Arquivo WSGI para produção
├── requirements.txt       # Dependências Python
├── Procfile               # Configuração do Gunicorn
├── render.yaml            # Configuração automática do Render
├── templates/             # Templates HTML
├── static/                # Arquivos estáticos (CSS, JS)
└── README.md              # Este arquivo
```

## 🎯 **Funcionalidades**

- ✅ **Sistema de usuários** com login/logout
- ✅ **Reserva de salas** com validação de conflitos
- ✅ **Painel administrativo** para gestão
- ✅ **Dashboard** com estatísticas
- ✅ **Banco PostgreSQL** para dados persistentes
- ✅ **Deploy automático** no Render

## 🔒 **Segurança**

- **Autenticação** via Flask-Login
- **Controle de acesso** por nível de usuário
- **Validação** de dados de entrada
- **Proteção** contra conflitos de horários

## 🌐 **Tecnologias**

- **Backend:** Flask, SQLAlchemy, PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **Deploy:** Render, Gunicorn
- **Banco:** PostgreSQL (produção) / SQLite (desenvolvimento)

## 📞 **Suporte**

Para dúvidas sobre deploy, consulte o arquivo `DEPLOY_RENDER.md`.

---

**🚀 Sistema pronto para produção com dados persistentes!**
