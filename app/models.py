from app import app,db



class Postagem(db.Model):
    __tablename__ ='postagem'
    id_postagem = db.Column(db.Integer, primary_key=True, nullable=False)
    titulo= db.Column(db.String, nullable=False)
    conteudo = db.column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'), nullable=False)
    
    
    
    
class Autor(db.Model):
    __tablename__ ='autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')
    
    
    
    
# def initialize_db():    
#     with app.app_context():
#         db.drop_all()  #    
#         db.create_all()
#     # Criando Admin

#         autor = Autor(nome='Natan',email='natan@gmail.com',senha="123456",admin=True)
#         db.session.add(autor)
#         db.session.commit()
        
#initialize_db()