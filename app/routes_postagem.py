from flask import Flask,jsonify, request
from app import app,db
from app.models import Autor,Postagem
from app.routes_autor import token_obrigatorio



@app.route("/")
@token_obrigatorio
def obter_postagens(autor):
    postagens = Postagem.query.all()
    lista_de_postagens = []
    try:
        for postagem in postagens:
            postagem_atual = {}
            postagem_atual['id_postagem'] = postagem.id_postagem
            postagem_atual['titulo'] = postagem.titulo
            postagem_atual['conteudo'] = postagem.conteudo
            postagem_atual['id_autor'] = postagem.id_autor
            lista_de_postagens.append(postagem_atual)
        return jsonify({'postagens':lista_de_postagens})
    except:
        return jsonify(f'Erro na Busca',404)


@app.route('/postagem/<int:index>',methods=['GET'])
@token_obrigatorio
def obter_postagem_por_index(autor,index):
    postagem = Postagem.query.all()
    if not postagem:
        return jsonify({'message':'Postagem not found'})
    
    postagem_atual = {}
    postagem_atual['id_postagem'] = postagem.id_postagem
    postagem_atual['titulo'] = postagem.titulo
    postagem_atual['conteudo'] = postagem.conteudo
    postagem_atual['id_autor'] = postagem.id_autor

    return jsonify({'postagem':postagem_atual})



# Criar postagem
@app.route('/postagem',methods=['POST'])
@token_obrigatorio
def nova_postagem(autor):
    try:
        novo_postagem = request.get_json()
        postagem = Postagem(titulo=novo_postagem['titulo'],
                    id_autor=novo_postagem['id_autor'],conteudo=novo_postagem['conteudo'])
        db.session.add(postagem)
        db.session.commit()
        
        return jsonify('Postagem criada com sucesso',200)  
    except:
        return jsonify("erro ao criar a Postagem",404)  


@app.route('/postagem/<int:index>',methods=['PUT'])
@token_obrigatorio
def alterar_postagem(autor,index):
    postagem_alterar = request.get_json()
    postagem = Postagem.query.filter_by(id_postagem=index).first()
    
    if not postagem:
        return jsonify({"Message": "Postagem não encontrada"})
    try:
        if postagem_alterar['titulo']:
            postagem.titulo = postagem_alterar['titulo']
            postagem.conteudo = postagem_alterar['conteudo']
    except:
        pass

            
    db.session.commit()
    return jsonify({"Message": "Postagem alterada com sucesso!"},200)



@app.route('/postagem/<int:index>',methods=['DELETE'])
@token_obrigatorio
def excluir_postagem(autor,index):

    try:
        postagem_existents = Postagem.query.filter_by(id_postagem=index).first()
        if not postagem_existents:
            return jsonify({'Message':'Postaegem não encontrada!'})
        
        db.session.delete(postagem_existents)
        db.session.commit()
        
        return jsonify(f'Foi excluída a postagem',200)
        
    except:
        return jsonify('Não foi possivel encontrar a postagem para excluir',404)
