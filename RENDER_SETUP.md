# 🚀 Configuração do Render para Persistência de Dados

## ✅ **Status Atual:**
- ✅ Dependências PostgreSQL configuradas (`psycopg[binary]>=3.2.2`)
- ✅ Configuração do banco forçada para usar dialeto `psycopg`
- ✅ Scripts de migração criados
- ✅ Schema PostgreSQL gerado
- ✅ Dados do SQLite exportados

## ❌ **Problema Anterior (RESOLVIDO):**
- ~~Dados são perdidos quando o serviço é reiniciado~~
- ~~Banco SQLite local não persiste no Render~~
- ~~Sistema de arquivos efêmero do Render~~

## 🎯 **Próximos Passos Necessários:**

### **Passo 1: Criar Banco PostgreSQL no Render** ⚠️ **PENDENTE**

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

### **Passo 2: Configurar o Serviço Web** ⚠️ **PENDENTE**

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

### **Passo 3: Migrar Dados para PostgreSQL** ⚠️ **PENDENTE**

1. **Execute o schema no PostgreSQL do Render:**
   - Use o arquivo `postgres_schema.sql` para criar as tabelas
   - Copie e cole o conteúdo no console SQL do Render

2. **Migrar os dados existentes:**
   - Use o arquivo `migration_data.sql` para inserir os dados
   - Copie e cole o conteúdo no console SQL do Render

### **Passo 4: Deploy e Teste** ⚠️ **PENDENTE**

1. **Faça commit das alterações:**
   ```bash
   git add .
   git commit -m "Fix: Força uso do dialeto psycopg para PostgreSQL no Render"
   git push origin master
   ```

2. **O Render fará deploy automático**

3. **Verifique se está funcionando:**
   - Acesse sua aplicação
   - Crie uma reserva
   - Reinicie o serviço manualmente
   - Verifique se a reserva ainda existe

## 📁 **Arquivos Criados para Migração:**

### **`postgres_schema.sql`** ✅
- Schema completo do banco PostgreSQL
- Tabelas: `usuario`, `sala`, `reserva`
- Índices para performance
- Comentários das tabelas

### **`migration_data.sql`** ✅
- Dados exportados do SQLite:
  - **2 usuários** (incluindo admin)
  - **2 salas** (3 A informática, sala teste)
  - **4 reservas** existentes

## 🔧 **Configuração Técnica (JÁ FEITA):**

### **`requirements.txt`** ✅
```
psycopg[binary]>=3.2.2
psycopg>=3.2.2
```

### **`config.py`** ✅
- Ambiente padrão: `production`
- Força uso do dialeto `postgresql+psycopg://`
- Configurações específicas para PostgreSQL

### **`database.py`** ✅
- Configuração específica para banco PostgreSQL
- Força uso do dialeto correto

### **`app.py`** ✅
- Configuração forçada para usar `get_database_url()`

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

## 🎯 **Resumo dos Passos Pendentes:**

1. **Criar banco PostgreSQL no Render**
2. **Configurar variáveis de ambiente** (`DATABASE_URL`, `FLASK_ENV`, `SECRET_KEY`)
3. **Executar schema e migrar dados** usando os arquivos SQL
4. **Fazer deploy** da aplicação
5. **Testar persistência** dos dados

---

**Resultado:** Após completar esses passos, seus dados permanecerão intactos mesmo quando o serviço for reiniciado! 🎉
