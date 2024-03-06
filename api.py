from app import app



if __name__ == '__main__':
    app.run(debug=True)


 

# @app.route("/")
# def obter_postagens():
#     return jsonify(postagens)



# @app.route('/postagem/<int:index>',methods=['GET'])
# def obter_postageM_por_index(index):
#     return jsonify(postagens[index])



# # Criar postagem
# @app.route('/postagem',methods=['POST'])
# def nova_postagem():
#     postagem = request.get_json()
#     postagens.append(postagem)

#     return jsonify(postagem,200)

# @app.route('/postagem/<int:index>',methods=['PUT'])
# def alterar_postagem(index):
#     postagem_alterada = request.get_json()
#     postagens[index].update(postagem_alterada)

#     return jsonify(postagens[index],200)


# @app.route('/postagem/<int:index>',methods=['DELETE'])
# def excluir_postagem(index):

#     try:
#         if postagens[index] is not None:
#             del postagens[index]
#             return jsonify(f'Foi excluída a postagem {postagens[index]}',200)
        
#     except:
#         return jsonify('Não foi possivel encontrar a postagem para excluir',404)



# @app.route('/autores')
# def obter_autores():
#     autores = Autor.query.all()
#     lista_de_autores = []
#     for autor in autores:
#         autor_atual = {}
#         autor_atual['id_autor'] = autor.id_autor
#         autor_atual['nome'] = autor.nome
#         autor_atual['email'] = autor.email
#         lista_de_autores.append(autor_atual)
#     return jsonify({'autores':lista_de_autores})

# @app.route('/autores/<int:index>',methods=['GET'])
# def obter_autores_id(index):
#     pass

# @app.route('/autores',methods=['POST'])
# def novo_autor():
#     pass

# @app.route('autores/<int:id_autor>',methods=['PUT'])
# def alterar_autor(id_autor):
#     pass


# @app.route('autores/<int:id_autor>',methods=['DELETE'])
# def excluir_autor(id_autor):
#     pass




    