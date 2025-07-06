# Sistema de Administração - Reserva de Salas

## 🔐 Credenciais do Administrador Padrão

**Email:** admin@gmail.com  
**Senha:** @dm1n

## 🚀 Como Configurar o Sistema

### 1. Criar o Usuário Administrador

O usuário administrador padrão é criado automaticamente quando o sistema é iniciado pela primeira vez.

**Credenciais padrão:**
- Email: admin@gmail.com
- Senha: @dm1n

### 2. Iniciar o Servidor

```bash
python app.py
```

### 3. Acessar o Sistema

1. Acesse: http://localhost:5000
2. Faça login com as credenciais do administrador
3. Você será redirecionado automaticamente para o painel de administração

## 🛠️ Funcionalidades do Painel de Administração

### Gerenciamento de Usuários
- ✅ **Visualizar todos os usuários** cadastrados no sistema
- ✅ **Criar novos usuários** com permissões de admin ou usuário comum
- ✅ **Editar informações** dos usuários existentes
- ✅ **Excluir usuários** (exceto o próprio administrador)
- ✅ **Definir permissões** de administrador para qualquer usuário

### Gerenciamento de Reservas
- ✅ **Visualizar todas as reservas** do sistema
- ✅ **Criar reservas** para qualquer usuário
- ✅ **Editar reservas** existentes
- ✅ **Excluir reservas** de qualquer usuário
- ✅ **Gerenciar conflitos** de horários automaticamente

### Funcionalidades Especiais
- ✅ **Acesso exclusivo** - apenas administradores podem acessar o painel
- ✅ **Redirecionamento automático** - admins são direcionados para o painel após login
- ✅ **Interface intuitiva** com botões de ação claros
- ✅ **Confirmações de segurança** antes de excluir dados

## 📋 Estrutura do Sistema

### Rotas de Administração
- `/admin` - Painel principal de administração
- `/admin/usuario/novo` - Criar novo usuário
- `/admin/usuario/<id>/editar` - Editar usuário
- `/admin/usuario/<id>/excluir` - Excluir usuário
- `/admin/reserva/nova` - Criar nova reserva
- `/admin/reserva/<id>/editar` - Editar reserva
- `/admin/reserva/<id>/excluir` - Excluir reserva

### Proteções de Segurança
- ✅ **Decorator `@admin_required`** - verifica se o usuário é admin
- ✅ **Validação de dados** - verifica formatos e conflitos
- ✅ **Proteção contra auto-exclusão** - admin não pode excluir a si mesmo
- ✅ **Verificação de conflitos** - impede reservas duplicadas

## 🎨 Interface do Usuário

### Design Responsivo
- ✅ **Layout moderno** com gradientes e sombras
- ✅ **Botões intuitivos** com efeitos hover
- ✅ **Tabelas organizadas** para visualização de dados
- ✅ **Formulários bem estruturados** para entrada de dados

### Elementos Visuais
- ✅ **Status coloridos** para identificar admins e usuários
- ✅ **Botões de ação** com cores distintas (editar/excluir)
- ✅ **Seções organizadas** para diferentes funcionalidades
- ✅ **Feedback visual** para ações do usuário

## 🔧 Comandos Úteis

### Popular Salas (se necessário)
```bash
# Acesse: http://localhost:5000/popular_salas
```

## 📝 Notas Importantes

1. **Segurança**: O sistema verifica permissões em todas as rotas administrativas
2. **Dados**: Todas as ações são registradas no banco de dados SQLite
3. **Backup**: Recomenda-se fazer backup regular do arquivo `reserva_salas.db`
4. **Logs**: O sistema exibe mensagens de sucesso/erro para todas as ações

## 🆘 Suporte

Se encontrar problemas:
1. Verifique se o banco de dados foi criado corretamente
2. Confirme se o usuário admin foi criado
3. Verifique os logs do servidor para mensagens de erro
4. Certifique-se de que todas as dependências estão instaladas 