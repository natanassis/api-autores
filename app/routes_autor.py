from flask import Flask,jsonify, request,make_response
from app import app,db
from app.models import Autor,Postagem
import jwt
from datetime import datetime, timedelta
from functools import wraps
from app.routes_auth import token_obrigatorio







@app.route('/autores', methods=['GET'])
@token_obrigatorio
def obter_autores(autor):
    autores = Autor.query.all()
    lista_de_autores = []
    try:
        for autor in autores:
            autor_atual = {}
            autor_atual['id_autor'] = autor.id_autor
            autor_atual['nome'] = autor.nome
            autor_atual['email'] = autor.email
            lista_de_autores.append(autor_atual)
        return jsonify({'autores':lista_de_autores})
    except:
        return jsonify(f'Erro na Busca',404)


@app.route('/autores/<int:id_autor>',methods=['GET'])
@token_obrigatorio
def obter_autores_id(autor,id_autor):
    autor =  Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify(f'Autor não encontrado!')
    autor_atual = {}
    autor_atual['id_autor'] = autor.id_autor
    autor_atual['nome'] = autor.nome
    autor_atual['email'] = autor.email
    
    return jsonify({'autore':autor_atual})
 
 
    
@app.route('/autores',methods=['POST'])
@token_obrigatorio
def novo_autor(autor):
    try:
        novo_autor = request.get_json()
        autor = Autor(nome=novo_autor['nome'],
                    senha=novo_autor['senha'],
                    email=novo_autor['email'])
        db.session.add(autor)
        db.session.commit()
        
        return jsonify('Usuario criado com sucesso',200)  
    except:
        return jsonify("erro ao cadastradas Usuario",404)  



@app.route('/autores/<int:id_autor>',methods=['PUT'])
@token_obrigatorio
def alterar_autor(autor,id_autor):
    usuario_alterar = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    
    if not autor:
        return jsonify({"Message": "Usuario não encontrado"})
    try:
        if usuario_alterar['nome']:
            autor.nome = usuario_alterar['nome']
    except:
        pass
    try:
        if usuario_alterar['email']:
            autor.email = usuario_alterar['email']
    except:
        pass 
    try:   
        if usuario_alterar['senha']:
            autor.senha = usuario_alterar['senha']
    except:
        pass
            
    db.session.commit()
    return jsonify({"Message": "Usuario alterado com sucesso!"},200)



@app.route('/autores/<int:id_autor>',methods=['DELETE'])
@token_obrigatorio
def excluir_autor(autor,id_autor):
    #usuario_excluido = request.get_json()
    try:
        autor_exists = Autor.query.filter_by(id_autor=id_autor).first()
        if not autor_exists:
            return jsonify({'mensagem':'Este autor não foi encontrado'})
        db.session.delete(autor_exists)
        db.session.commit()
        
        return jsonify({'message':'Autor excluido com sucesso !'})
    except:
        return jsonify({'mensagem':'Este autor não foi encontrado'})
