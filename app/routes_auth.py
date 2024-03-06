from flask import Flask,jsonify, request,make_response
from app import app,db
from app.models import Autor,Postagem
import jwt
from datetime import datetime, timedelta
from functools import wraps
import jwt
#from flask_jwt_extended import jwt_required,get_jwt_identity




def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # verifica se o token foi enviado com a requisição 
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'] 
        if not token:
            return jsonify({'message': 'token not included'},401)
        # se temos um token, validar acesso ao consultar o BD
        try:
            try:
                resultado = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
                autor = Autor.query.filter_by(id_autor=resultado['id_autor']).first()
            except:
                return jsonify({'message':'Invalid token'},401)
        
            return f(autor,*args,**kwargs)
        except Exception as e:
            app.logger.error(f"Erro ao validar token: {e}")
            return jsonify({'message': 'Internal server error'}, 500)
        
    return decorated


@app.route('/login')
def login():
    #tok = request.args.get('token')
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Login invalido',401, {'WWW-Authenticate':'Basic realm="Login obrigatorio"'})
    user= Autor.query.filter_by(nome=auth.username).first()
    if not user:
        return make_response('Login invalidor',401, {'WWW-Authenticate':'Basic realm="Login obrigatorio"'})
    
    if auth.password == user.senha:
        token = jwt.encode({'id_autor': user.id_autor, 'exp': datetime.utcnow() + timedelta(minutes=30)},
                       app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})
    
    return make_response('Login invalid',401, {'WWW-Authenticate':'Basic realm="Login obrigatorio"'})