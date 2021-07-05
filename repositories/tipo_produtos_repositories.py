from repositories.base_repositories import BaseRepository
from models.tipos_produtos import TiposProdutos
#from repositories.db import DB

class TipoProdutoRepository(BaseRepository):
    def list(self):
        result = self.execute('select id, name from tipo_produto')

        tipo_produtos = []

        for row in result:
            tipo = TiposProdutos(id=row[0],name=row[1])
            tipo_produtos.append(tipo)
        
        return tipo_produtos