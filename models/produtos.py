from sqlalchemy.sql.schema import ForeignKey
from shared.models import db

class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_tipo_produto = db.Column(db.Integer, db.ForeignKey('id_tipo_produto'))
    name = db.Column(db.String(500), nullable=False)
    preco = db.Column(db.Integer, nullable=False)

    def __init__(self, name, preco):
        self.name = name
        self.preco = preco

    def __repr__(self):
        return f"<Produtos{self.name}>"

# class Produtos:
#     def __init__(self, id, id_tipo_produto, name, preco):
#         self.id = id
#         self.id_tipo_produto = id_tipo_produto
#         self.name = name
#         self.preco = preco
#         self.lista_produtos = []
        
  
