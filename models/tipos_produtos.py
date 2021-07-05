#from repositories.produtos_repositories import ProdutosRepositories
from sqlalchemy.orm import backref, relationship
from shared.models import db

class TipoProdutos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    produtos = db.relationship('Produtos',backref='tipoproduto',lazy=True)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"<tipo_produto {self.name}>"
