# 🚀 Configuração do Render para Persistência de Dados

## ❌ **Problema Atual:**
- Dados são perdidos quando o serviço é reiniciado
- Banco SQLite local não persiste no Render
- Sistema de arquivos efêmero do Render

## ✅ **Solução: Banco PostgreSQL Persistente**

### **Passo 1: Criar Banco PostgreSQL no Render**

1. **Acesse o Dashboard do Render:**
   - Vá para [dashboard.render.com](https://dashboard.render.com)
   - Faça login na sua conta

2. **Criar Novo Banco de Dados:**
   - Clique em **"New +"**
   - Selecione **"PostgreSQL"**
   - Escolha um nome para o banco (ex: `gestao-escolas-db`)
   - Selecione a região mais próxima
   - Escolha o plano **"Free"** (gratuito)
   - Clique em **"Create Database"**

3. **Configurar Variáveis de Ambiente:**
   - Após criar o banco, vá para a aba **"Environment"**
   - Copie a **"External Database URL"**
   - Esta URL será algo como: `postgres://user:password@host:port/database`

### **Passo 2: Configurar o Serviço Web**

1. **No seu serviço web existente:**
   - Vá para a aba **"Environment"**
   - Adicione a variável de ambiente:
     - **Key:** `DATABASE_URL`
     - **Value:** Cole a URL do PostgreSQL copiada anteriormente

2. **Adicionar outras variáveis importantes:**
   - **Key:** `FLASK_ENV`
   - **Value:** `production`

   - **Key:** `SECRET_KEY`
   - **Value:** Uma chave secreta forte (ex: `sua-chave-secreta-muito-segura-aqui`)

### **Passo 3: Instalar Dependências PostgreSQL**

Adicione ao seu `requirements.txt`:
```
psycopg2-binary==2.9.9
```

### **Passo 4: Migrar Dados (Opcional)**

Se você quiser migrar os dados existentes do SQLite para PostgreSQL:

1. **Exportar dados do SQLite:**
   ```bash
   # No seu ambiente local
   python -c "
   from app import app, db
   from models import Usuario, Sala, Reserva
   
   with app.app_context():
       # Exportar usuários
       usuarios = Usuario.query.all()
       for u in usuarios:
           print(f'INSERT INTO usuario (nome, email, senha, is_admin) VALUES (\"{u.nome}\", \"{u.email}\", \"{u.senha}\", {u.is_admin});')
       
       # Exportar salas
       salas = Sala.query.all()
       for s in salas:
           print(f'INSERT INTO sala (nome, capacidade) VALUES (\"{s.nome}\", {s.capacidade});')
       
       # Exportar reservas
       reservas = Reserva.query.all()
       for r in reservas:
           print(f'INSERT INTO reserva (professor_id, sala_id, data, horario_inicio, horario_fim, data_criacao) VALUES ({r.professor_id}, {r.sala_id}, \"{r.data}\", \"{r.horario_inicio}\", \"{r.horario_fim}\", \"{r.data_criacao}\");')
   "
   ```

2. **Executar os comandos SQL no PostgreSQL do Render**

### **Passo 5: Verificar Configuração**

A configuração já está correta no `config.py`:

```python
class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        # Render usa postgres:// mas SQLAlchemy espera postgresql://
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or 'sqlite:///reserva_salas.db'
```

### **Passo 6: Deploy e Teste**

1. **Faça commit das alterações:**
   ```bash
   git add .
   git commit -m "Adiciona suporte ao PostgreSQL para Render"
   git push
   ```

2. **O Render fará deploy automático**

3. **Verifique se está funcionando:**
   - Acesse sua aplicação
   - Crie uma reserva
   - Reinicie o serviço manualmente
   - Verifique se a reserva ainda existe

## 🔧 **Alternativa: Sistema de Backup Automático**

Se preferir manter o SQLite, você pode implementar um sistema de backup:

1. **Backup para serviço de armazenamento externo** (AWS S3, Google Cloud Storage)
2. **Backup para repositório Git** (não recomendado para dados sensíveis)
3. **Sincronização com banco local** via API

## 📊 **Vantagens do PostgreSQL:**

- ✅ **Dados persistentes** entre reinicializações
- ✅ **Melhor performance** para múltiplos usuários
- ✅ **Backup automático** do Render
- ✅ **Escalabilidade** para crescimento futuro
- ✅ **Conformidade** com padrões empresariais

## ⚠️ **Limitações do Plano Gratuito:**

- **512MB de RAM** (suficiente para desenvolvimento)
- **1GB de armazenamento** (suficiente para milhares de reservas)
- **Conexões limitadas** (adequado para uso moderado)

## 🚨 **Importante:**

- **Nunca commite** credenciais de banco no Git
- **Use variáveis de ambiente** para configurações sensíveis
- **Teste localmente** antes de fazer deploy
- **Monitore** o uso de recursos no dashboard do Render

---

**Resultado:** Após essa configuração, seus dados permanecerão intactos mesmo quando o serviço for reiniciado! 🎉
