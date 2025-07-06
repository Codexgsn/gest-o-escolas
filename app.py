from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
from datetime import datetime, timedelta, time
from models import db, Usuario, Sala, Reserva
import re
from functools import wraps
from werkzeug.security import generate_password_hash


# Constantes globais para horários
HORARIOS_PERMITIDOS = [
    ("07:30", "manhã"),
    ("08:20", "manhã"),
    ("09:30", "manhã"),
    ("10:20", "manhã"),
    ("11:10", "manhã"),
    ("13:20", "tarde"),
    ("14:10", "tarde"),
    ("15:20", "tarde"),
    ("16:10", "tarde"),
]

HORARIOS_FIM = HORARIOS_PERMITIDOS + [("17:00", "tarde")]

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave-temporaria-desenvolvimento')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reserva_salas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['REMEMBER_COOKIE_DURATION'] = 0  # Não lembrar login
app.config['SESSION_PERMANENT'] = False     # Sessão expira ao fechar o navegador

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = None  # Remove a mensagem padrão

@app.context_processor
def inject_now():
    return {'now': datetime.now}

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html', now=datetime.now)

def email_valido(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def verificar_conflito_horarios(sala_id, data, horario_inicio, horario_fim, reserva_id=None):
    """
    Verifica se há conflito de horários para uma sala em uma data específica.
    
    Args:
        sala_id: ID da sala
        data: Data da reserva
        horario_inicio: Horário de início
        horario_fim: Horário de fim
        reserva_id: ID da reserva atual (para edição, excluir da verificação)
    
    Returns:
        tuple: (tem_conflito, mensagem_erro)
    """
    # Verificar se horário de início é igual ao de fim
    if horario_inicio >= horario_fim:
        return True, "O horário de início deve ser anterior ao horário de fim!"
    
    # Buscar reservas existentes para a mesma sala e data
    query = Reserva.query.filter(
        Reserva.sala_id == sala_id,
        Reserva.data == data
    )
    
    # Se for uma edição, excluir a reserva atual da verificação
    if reserva_id:
        query = query.filter(Reserva.id != reserva_id)
    
    reservas_existentes = query.all()
    
    for reserva in reservas_existentes:
        # Verificar sobreposição de horários
        # Conflito ocorre quando:
        # 1. Início da nova reserva está dentro de uma reserva existente
        # 2. Fim da nova reserva está dentro de uma reserva existente  
        # 3. Nova reserva engloba completamente uma reserva existente
        # 4. Horários são exatamente iguais
        
        # Caso 1: Início da nova reserva está dentro da existente
        if reserva.horario_inicio <= horario_inicio < reserva.horario_fim:
            return True, f"Conflito: horário de início ({horario_inicio.strftime('%H:%M')}) está dentro da reserva existente ({reserva.horario_inicio.strftime('%H:%M')} - {reserva.horario_fim.strftime('%H:%M')})"
        
        # Caso 2: Fim da nova reserva está dentro da existente
        if reserva.horario_inicio < horario_fim <= reserva.horario_fim:
            return True, f"Conflito: horário de fim ({horario_fim.strftime('%H:%M')}) está dentro da reserva existente ({reserva.horario_inicio.strftime('%H:%M')} - {reserva.horario_fim.strftime('%H:%M')})"
        
        # Caso 3: Nova reserva engloba completamente a existente
        if horario_inicio <= reserva.horario_inicio and horario_fim >= reserva.horario_fim:
            return True, f"Conflito: sua reserva engloba completamente a reserva existente ({reserva.horario_inicio.strftime('%H:%M')} - {reserva.horario_fim.strftime('%H:%M')})"
        
        # Caso 4: Horários são exatamente iguais
        if horario_inicio == reserva.horario_inicio and horario_fim == reserva.horario_fim:
            return True, f"Conflito: horários idênticos à reserva existente ({reserva.horario_inicio.strftime('%H:%M')} - {reserva.horario_fim.strftime('%H:%M')})"
    
    return False, ""

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        if not email_valido(email):
            flash('Formato de e-mail incorreto!', 'error')
            return redirect(url_for('register'))
        if Usuario.query.filter_by(email=email).first():
            flash('Email já cadastrado!')
            return redirect(url_for('register'))
        usuario = Usuario(nome=nome, email=email)
        usuario.set_password(senha)
        db.session.add(usuario)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.check_password(senha):
            login_user(usuario, remember=False)
            flash('Login realizado com sucesso!', 'success')
            
            # Redirecionar admin para página de administração
            if usuario.is_admin:
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('reservas'))
        else:
            flash('E-mail ou senha incorretos!', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/popular_salas')
@login_required
def popular_salas():
    # Salas para cada ano e tipo
    nomes = [
        '3º Ano Informática', '3º Ano PCP A', '3º Ano PCP B',
        '2º Ano Informática', '2º Ano PCP A', '2º Ano PCP B',
        '1º Ano Informática', '1º Ano PCP A', '1º Ano PCP B',
    ]
    for nome in nomes:
        if not Sala.query.filter_by(nome=nome).first():
            db.session.add(Sala(nome=nome, capacidade=30))
    db.session.commit()
    return 'Salas populadas com sucesso!'

@app.route('/reservas', methods=['GET', 'POST'])
@login_required
def reservas():
    try:
        salas = Sala.query.all()
        horarios_permitidos = HORARIOS_PERMITIDOS
        horarios_fim = HORARIOS_FIM

        agora = datetime.now()
        data_atual = agora.date()
        hora_atual = agora.time()

        # Reservas ativas apenas do usuário atual
        reservas_ativas = Reserva.query.filter(
            Reserva.professor_id == current_user.id,
            (Reserva.data > data_atual) |
            ((Reserva.data == data_atual) & (Reserva.horario_fim > hora_atual))
        ).order_by(Reserva.data.asc(), Reserva.horario_inicio.asc()).all()

        if request.method == 'POST':
            data = datetime.strptime(request.form['data'], '%Y-%m-%d').date()
            
            # Validar data
            if data < data_atual:
                flash('Não é possível fazer reservas para datas passadas!')
                return redirect(url_for('reservas'))
            
            # Se for hoje, validar horário
            if data == data_atual and datetime.strptime(request.form['horario_inicio'], '%H:%M').time() <= hora_atual:
                flash('Não é possível fazer reservas para horários passados!')
                return redirect(url_for('reservas'))
            
            sala_id = request.form['sala_id']
            sala = Sala.query.get_or_404(sala_id)
            
            horario_inicio_str = request.form['horario_inicio']
            horario_fim_str = request.form['horario_fim']
            
            try:
                horario_inicio = datetime.strptime(horario_inicio_str, '%H:%M').time()
                horario_fim = datetime.strptime(horario_fim_str, '%H:%M').time()
            except ValueError:
                flash('Formato de horário inválido!')
                return redirect(url_for('reservas'))
            
            # Verificar se horário de início é igual ou posterior ao de fim
            if horario_inicio >= horario_fim:
                flash('O horário de início deve ser anterior ao horário de fim!')
                return redirect(url_for('reservas'))
            
            # Validar horário de fim do dia
            if horario_fim > datetime.strptime('17:00', '%H:%M').time():
                flash('O horário de fim não pode ser após 17:00!')
                return redirect(url_for('reservas'))
            
            # Verificar conflito de horários usando a função auxiliar
            tem_conflito, mensagem_erro = verificar_conflito_horarios(sala_id, data, horario_inicio, horario_fim)
            
            if tem_conflito:
                flash(mensagem_erro, 'error')
                return redirect(url_for('reservas'))
            
            # Se não houver conflitos, criar a reserva
            nova_reserva = Reserva(
                data=data,
                sala_id=sala_id,
                professor_id=current_user.id,
                horario_inicio=horario_inicio,
                horario_fim=horario_fim
            )
            db.session.add(nova_reserva)
            db.session.commit()
            flash('Reserva realizada com sucesso!', 'success')
            return redirect(url_for('reservas'))
        return render_template('reservas.html', 
                             salas=salas, 
                             reservas=reservas_ativas, 
                             horarios_permitidos=horarios_permitidos, 
                             horarios_fim=horarios_fim,
                             data_atual=data_atual,
                             hora_atual=hora_atual,
                             now=datetime.now)
    except Exception as e:
        flash(f'Ocorreu um erro: {str(e)}')
        return redirect(url_for('index'))

@app.route('/cancelar_reserva/<int:reserva_id>')
@login_required
def cancelar_reserva(reserva_id):
    reserva = Reserva.query.get_or_404(reserva_id)
    if reserva.professor_id != current_user.id:
        flash('Você não pode cancelar esta reserva!')
        return redirect(url_for('reservas'))
    db.session.delete(reserva)
    db.session.commit()
    flash('Reserva cancelada!')
    return redirect(url_for('reservas'))

@app.route('/todas_reservas')
@login_required
def todas_reservas():
    salas = Sala.query.all()
    agora = datetime.now()
    data_atual = agora.date()
    hora_atual = agora.time()

    # Filtros
    dia = request.args.get('dia')
    mes = request.args.get('mes')
    ano = request.args.get('ano')
    hora = request.args.get('hora')

    reservas_query = Reserva.query

    # Filtro por dia
    if dia:
        try:
            data_filtro = datetime.strptime(dia, '%Y-%m-%d').date()
            reservas_query = reservas_query.filter(Reserva.data == data_filtro)
        except Exception:
            pass
    # Filtro por mês
    if mes:
        try:
            mes = int(mes)
            reservas_query = reservas_query.filter(db.extract('month', Reserva.data) == mes)
        except Exception:
            pass
    # Filtro por ano
    if ano:
        try:
            ano = int(ano)
            reservas_query = reservas_query.filter(db.extract('year', Reserva.data) == ano)
        except Exception:
            pass
    # Filtro por hora do dia
    if hora == 'manha':
        reservas_query = reservas_query.filter(Reserva.horario_inicio < time(12,0))
    elif hora == 'tarde':
        reservas_query = reservas_query.filter(Reserva.horario_inicio >= time(12,0))

    # Apenas reservas ativas (futuras ou em andamento)
    reservas_ativas = reservas_query.filter(
        (Reserva.data > data_atual) |
        ((Reserva.data == data_atual) & (Reserva.horario_fim > hora_atual))
    ).order_by(Reserva.data.asc(), Reserva.horario_inicio.asc()).all()

    return render_template('todas_reservas.html', 
        reservas=reservas_ativas, 
        salas=salas, 
        data_atual=data_atual, 
        hora_atual=hora_atual)



def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route('/admin')
@login_required
@admin_required
def admin():
    usuarios = Usuario.query.all()
    salas = Sala.query.all()
    todas_reservas = Reserva.query.order_by(Reserva.data.desc()).all()
    data_atual = datetime.now().date()
    hora_atual = datetime.now().time()
    
    return render_template('admin.html', 
                         usuarios=usuarios,
                         salas=salas,
                         todas_reservas=todas_reservas,
                         data_atual=data_atual,
                         hora_atual=hora_atual,
                         horarios_permitidos=HORARIOS_PERMITIDOS,
                         horarios_fim=HORARIOS_FIM)

@app.route('/admin/usuario/<int:user_id>/editar', methods=['GET', 'POST'])
@login_required
@admin_required
def editar_usuario(user_id):
    usuario = Usuario.query.get_or_404(user_id)
    if request.method == 'POST':
        usuario.nome = request.form['nome']
        usuario.email = request.form['email']
        if request.form.get('is_admin'):
            usuario.is_admin = True
        else:
            usuario.is_admin = False
        if request.form.get('senha'):
            usuario.set_password(request.form['senha'])
        db.session.commit()
        flash('Usuário atualizado com sucesso!', 'success')
        return redirect(url_for('admin'))
    return render_template('editar_usuario.html', usuario=usuario)

@app.route('/admin/usuario/<int:user_id>/excluir')
@login_required
@admin_required
def excluir_usuario(user_id):
    usuario = Usuario.query.get_or_404(user_id)
    if usuario.id == current_user.id:
        flash('Você não pode excluir seu próprio usuário!', 'error')
        return redirect(url_for('admin'))
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuário excluído com sucesso!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/usuario/novo', methods=['GET', 'POST'])
@login_required
@admin_required
def novo_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        is_admin = request.form.get('is_admin') == 'on'
        
        if not email_valido(email):
            flash('Formato de e-mail incorreto!', 'error')
            return redirect(url_for('novo_usuario'))
        
        if Usuario.query.filter_by(email=email).first():
            flash('Email já cadastrado!', 'error')
            return redirect(url_for('novo_usuario'))
        
        usuario = Usuario(nome=nome, email=email, is_admin=is_admin)
        usuario.set_password(senha)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuário criado com sucesso!', 'success')
        return redirect(url_for('admin'))
    
    return render_template('novo_usuario.html')

@app.route('/admin/reserva/nova', methods=['POST'])
@login_required
@admin_required
def admin_nova_reserva():
    professor_id = request.form['professor_id']
    sala_id = request.form['sala_id']
    data = datetime.strptime(request.form['data'], '%Y-%m-%d').date()
    horario_inicio = datetime.strptime(request.form['horario_inicio'], '%H:%M').time()
    horario_fim = datetime.strptime(request.form['horario_fim'], '%H:%M').time()
    
    # Verificar se horário de início é igual ou posterior ao de fim
    if horario_inicio >= horario_fim:
        flash('O horário de início deve ser anterior ao horário de fim!', 'error')
        return redirect(url_for('admin'))
    
    # Verificar conflitos usando a função auxiliar
    tem_conflito, mensagem_erro = verificar_conflito_horarios(sala_id, data, horario_inicio, horario_fim)
    
    if tem_conflito:
        flash(mensagem_erro, 'error')
        return redirect(url_for('admin'))
    
    nova_reserva = Reserva(
        professor_id=professor_id,
        sala_id=sala_id,
        data=data,
        horario_inicio=horario_inicio,
        horario_fim=horario_fim
    )
    db.session.add(nova_reserva)
    db.session.commit()
    flash('Reserva criada com sucesso!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/reserva/<int:reserva_id>/editar', methods=['GET', 'POST'])
@login_required
@admin_required
def editar_reserva(reserva_id):
    reserva = Reserva.query.get_or_404(reserva_id)
    if request.method == 'POST':
        reserva.professor_id = request.form['professor_id']
        reserva.sala_id = request.form['sala_id']
        reserva.data = datetime.strptime(request.form['data'], '%Y-%m-%d').date()
        reserva.horario_inicio = datetime.strptime(request.form['horario_inicio'], '%H:%M').time()
        reserva.horario_fim = datetime.strptime(request.form['horario_fim'], '%H:%M').time()
        
        # Verificar se horário de início é igual ou posterior ao de fim
        if reserva.horario_inicio >= reserva.horario_fim:
            flash('O horário de início deve ser anterior ao horário de fim!', 'error')
            return redirect(url_for('admin'))
        
        # Verificar conflitos usando a função auxiliar
        tem_conflito, mensagem_erro = verificar_conflito_horarios(
            reserva.sala_id, 
            reserva.data, 
            reserva.horario_inicio, 
            reserva.horario_fim, 
            reserva_id
        )
        
        if tem_conflito:
            flash(mensagem_erro, 'error')
            return redirect(url_for('admin'))
        
        db.session.commit()
        flash('Reserva atualizada com sucesso!', 'success')
        return redirect(url_for('admin'))
    
    usuarios = Usuario.query.all()
    salas = Sala.query.all()
    return render_template('editar_reserva.html', 
                         reserva=reserva,
                         usuarios=usuarios,
                         salas=salas,
                         horarios_permitidos=HORARIOS_PERMITIDOS,
                         horarios_fim=HORARIOS_FIM)

@app.route('/admin/reserva/<int:reserva_id>/excluir')
@login_required
@admin_required
def excluir_reserva(reserva_id):
    reserva = Reserva.query.get_or_404(reserva_id)
    db.session.delete(reserva)
    db.session.commit()
    flash('Reserva excluída com sucesso!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/sala/nova', methods=['POST'])
@login_required
@admin_required
def admin_nova_sala():
    nome = request.form['nome']
    capacidade = request.form['capacidade']
    if not nome or not capacidade:
        flash('Preencha todos os campos da sala!', 'error')
        return redirect(url_for('admin'))
    try:
        capacidade = int(capacidade)
    except ValueError:
        flash('Capacidade deve ser um número inteiro!', 'error')
        return redirect(url_for('admin'))
    if Sala.query.filter_by(nome=nome).first():
        flash('Já existe uma sala com esse nome!', 'error')
        return redirect(url_for('admin'))
    nova_sala = Sala(nome=nome, capacidade=capacidade)
    db.session.add(nova_sala)
    db.session.commit()
    flash('Sala cadastrada com sucesso!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/sala/<int:sala_id>/excluir')
@login_required
@admin_required
def excluir_sala(sala_id):
    sala = Sala.query.get_or_404(sala_id)
    if sala.reservas:
        flash('Não é possível excluir uma sala com reservas associadas!', 'error')
        return redirect(url_for('admin'))
    db.session.delete(sala)
    db.session.commit()
    flash('Sala excluída com sucesso!', 'success')
    return redirect(url_for('admin'))



def create_default_admin_if_not_exists():
    """Cria o usuário administrador padrão se não existir."""
    with app.app_context():
        # Verifica se o admin já existe
        admin = Usuario.query.filter_by(email="admin@gmail.com").first()
        if not admin:
            # Cria o novo administrador
            novo_admin = Usuario(
                nome="Administrador do Sistema",
                email="admin@gmail.com",
                senha=generate_password_hash("@dm1n"),
                is_admin=True
            )
            db.session.add(novo_admin)
            db.session.commit()
            print("✅ Administrador padrão criado automaticamente!")
            print("   Email: admin@gmail.com")
            print("   Senha: @dm1n")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_default_admin_if_not_exists()
    app.run(debug=True) 