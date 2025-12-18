from argon2 import PasswordHasher
import re
from datetime import datetime



ph = PasswordHasher()


#RE de regex - usada para validar se o email enviado no formulário tem um formato válido.
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

# Mensagens HTML simples (você pode personalizar/usar templates reais)
OK_HTML = """<h2>Cadastro realizado com sucesso!</h2><p><a href="/login.html">Ir para login</a></p>"""
ERROR_HTML = """<h2>Erro</h2><p>{{msg}}</p><p><a href="javascript:history.back()">Voltar</a></p>"""



def limpar_e_validar(form):
    nome = (form.get('nome') or '').strip()
    sobrenome = (form.get('sobrenome') or '').strip()
    email = (form.get('email') or '').strip()
    data_nascimento_raw = form.get('data_nascimento')  # espera YYYY-MM-DD do input type=date
    senha = form.get('senha')
    confirmar = form.get('confirmar_senha')

    # validações básicas
    if not nome or len(nome) < 2:
        return False, 'Nome inválido (mín 2 caracteres).', None
    
    if not sobrenome or len(sobrenome) < 2:
        return False, 'Sobrenome inválido (mín 2 caracteres).', None
    
    if not EMAIL_RE.match(email):
        return False, 'Email inválido.', None
    
    if not senha or len(senha) < 8:
        return False, 'Senha inválida (mín 8 caracteres).', None
    
    if senha != confirmar:
        return False, 'Senhas não coincidem.', None
    
    # validação data
    data_nascimento = None
    if data_nascimento_raw:
        try:
            data_nascimento = datetime.strptime(data_nascimento_raw, '%Y-%m-%d').date()
        except ValueError:
            return False, 'Data de nascimento inválida (formato YYYY-MM-DD).', None
        
    try:
        senha_hash = ph.hash(senha) 
    except Exception as e:
        print(f"[ERROR] não foi possível criar senha | {e}")

    dic_limpo = {
        'nome': nome,
        'sobrenome': sobrenome,
        'email': email,
        'data_nascimento': data_nascimento,
        'senha_hash': senha_hash
    }

    return dic_limpo

 
