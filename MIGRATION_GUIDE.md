# 🚀 Guia Rápido de Migração para PostgreSQL (Neon)

## 📋 **Resumo da Migração:**

### **✅ O que já foi feito:**
- Dependências PostgreSQL configuradas
- Scripts de migração criados
- Schema PostgreSQL gerado
- Dados do SQLite exportados
- Configuração preparada para Neon

### **⚠️ O que ainda precisa ser feito:**
- Configurar variável de ambiente `DATABASE_URL` no Render
- Executar migração dos dados no Neon
- Fazer deploy da aplicação

## 🔧 **Passo a Passo da Migração:**

### **1. Configurar Variável de Ambiente no Render**

#### **No seu serviço web existente:**
1. Vá para a aba **"Environment"**
2. Adicione a variável de ambiente:
   ```
   DATABASE_URL = postgresql://neondb_owner:npg_taN7qXMnEGH0@ep-old-butterfly-adytodgp-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
   ```

3. **Adicionar outras variáveis importantes:**
   - **Key:** `FLASK_ENV`
   - **Value:** `production`

   - **Key:** `SECRET_KEY`
   - **Value:** Uma chave secreta forte (ex: `sua-chave-secreta-muito-segura-aqui`)

### **2. Migrar Dados para Neon PostgreSQL**

#### **2.1 Acessar o Console do Neon:**
1. Acesse o [dashboard do Neon](https://console.neon.tech)
2. Clique no seu projeto `neondb`
3. Clique em **"SQL Editor"** ou **"Console"**

#### **2.2 Executar Schema:**
1. No console SQL, cole e execute o conteúdo de `postgres_schema.sql`
2. Verifique se as tabelas foram criadas:
   ```sql
   \dt
   ```

#### **2.3 Migrar Dados:**
1. No mesmo console, cole e execute o conteúdo de `migration_data.sql`
2. Verifique se os dados foram inseridos:
   ```sql
   SELECT COUNT(*) FROM usuario;    -- Deve retornar 2
   SELECT COUNT(*) FROM sala;       -- Deve retornar 2
   SELECT COUNT(*) FROM reserva;    -- Deve retornar 4
   ```

### **3. Fazer Deploy**

1. **Commit e Push:**
   ```bash
   git add .
   git commit -m "Fix: Força uso do dialeto psycopg para PostgreSQL no Render"
   git push origin master
   ```

2. **O Render fará deploy automático**

### **4. Testar Aplicação**

1. Acesse sua aplicação
2. Faça login com as credenciais existentes
3. Crie uma nova reserva
4. Reinicie o serviço manualmente
5. Verifique se a reserva ainda existe

## 📊 **Dados que Serão Migrados:**

### **Usuários:**
- **Admin:** `admin@gmail.com` (Administrador do Sistema)
- **Professor:** `gugudograu@gmail.com` (gustavo professor)

### **Salas:**
- **3 A informática** (Capacidade: 30)
- **sala teste** (Capacidade: 20)

### **Reservas:**
- 4 reservas existentes com horários e datas

## 🔍 **Verificação da Migração:**

### **Comandos SQL para verificar:**
```sql
-- Verificar usuários
SELECT id, nome, email, is_admin FROM usuario;

-- Verificar salas
SELECT id, nome, capacidade FROM sala;

-- Verificar reservas
SELECT id, professor_id, sala_id, data, horario_inicio, horario_fim 
FROM reserva ORDER BY data, horario_inicio;
```

## ⚠️ **Problemas Comuns e Soluções:**

### **Erro: "relation does not exist"**
- **Solução:** Execute primeiro o `postgres_schema.sql`

### **Erro: "duplicate key value violates unique constraint"**
- **Solução:** Os dados já foram migrados, pode pular esta etapa

### **Erro: "connection refused"**
- **Solução:** Verifique se o Neon está ativo e a URL está correta

### **Erro: "authentication failed"**
- **Solução:** Verifique se a `DATABASE_URL` está correta no Render

### **Erro: "sslmode=require"**
- **Solução:** O Neon já inclui `sslmode=require` na URL, está correto

## 🎯 **Checklist Final:**

- [ ] Variável `DATABASE_URL` configurada no Render
- [ ] Variável `FLASK_ENV=production` configurada
- [ ] Variável `SECRET_KEY` configurada
- [ ] Schema executado no Neon PostgreSQL
- [ ] Dados migrados com sucesso
- [ ] Deploy da aplicação realizado
- [ ] Aplicação funcionando com dados persistentes

## 🚨 **Importante:**

- **Nunca delete** o banco Neon
- **Mantenha backup** das variáveis de ambiente
- **Monitore** o uso de recursos
- **Teste** sempre após mudanças
- **O Neon já inclui SSL** na URL fornecida

## 🔐 **Configuração Neon (JÁ FORNECIDA):**

```
DATABASE_URL=postgresql://neondb_owner:npg_taN7qXMnEGH0@ep-old-butterfly-adytodgp-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

---

**🎉 Após completar todos os passos, sua aplicação funcionará com dados persistentes no Neon PostgreSQL!**
