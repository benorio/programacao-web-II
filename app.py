#rom repositories.tipo_produtos_repositories import TipoProdutoRepository
from flask_migrate import Migrate, migrate
from flask import Flask, render_template
from models.tipos_produtos import TipoProdutos
from models.produtos import Produtos

from shared.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:benorio@127.0.0.1:5432/loja"
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    tipo_produto_repository = TipoProdutoRepository()
    tipo = tipo_produto_repository.list()
    #tipos_repositories = TipoProdutoR()
    #tipos = tipos_repositories.list_id_tipo_produto(1)
    #print(produtos)
    #print(tipos)
    return render_template('index.html', tipos = tipo)

@app.route('/produtos')
def produtos():
    tipo_produto_repository = TipoProdutoRepository()
    tipo = tipo_produto_repository.list()
    return render_template('produtos.html', tipos = tipo)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contatos.html')

@app.route('/obras')
def obras():
    return render_template('obras.html')
