from repositories.base_repositories import BaseRepository
from repositories.db import DB
from models.produtos import Produtos

class ProdutosRepositories(BaseRepository):
    def list_tipo_produto(self, id_tipo_produto):
        result = self.execute(f"select id,id_tipo_produto,name, preco from produtos where id_tipo_produto = {id_tipo_produto}")
        
        produtos = []

        for row in result:
            produto = Produtos(
                id=row[0], 
                id_tipo_produto=row[1],
                name = row[2],
                preco = row[3]
                )
            produtos.append(produto)

       
        return produtos