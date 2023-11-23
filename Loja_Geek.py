import random  

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.numero_de_serie = 0  
    def gerador_numero_de_serie(self):
        pass  
    def __str__(self):
        return f"Nome: {self.nome}, Preço: R${self.preco}, Número de Série: {self.numero_de_serie}"
        
class Camisa(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)  
        self.tamanho = tamanho
    def gerador_numero_de_serie(self):
        return random.randint(1, 100) * 5  
    def __str__(self):
        return super().__str__() + f", Tamanho: {self.tamanho}"
       
class Caneca(Produto):
    def __init__(self, nome, preco, capacidade):
        super().__init__(nome, preco)  
        self.capacidade = capacidade
    def gerador_numero_de_serie(self):
        return random.randint(1, 100) * 3  
    def __str__(self):
        return super().__str__() + f", Capacidade: {self.capacidade} ml"
    
class Quadrinho(Produto):
    def __init__(self, nome, preco, autor, editora):
        super().__init__(nome, preco)  
        self.autor = autor
        self.editora = editora
    def gerador_numero_de_serie(self):
        return random.randint(1, 100) * 7  
    def __str__(self):
        return super().__str__() + f", Autor: {self.autor}, Editora: {self.editora}"
    
def calcular_total(carrinho):
    total = 0
    for produto, quantidade in carrinho.items():
        total += produto.preco * quantidade
    return total

def imprimir_nota_fiscal(carrinho, produtos_na_promocao):
    carrinho_ordenado = sorted(carrinho.items(), key=lambda x: x[0].preco)
    for produto, quantidade in carrinho_ordenado:
        print(f"{quantidade}x {produto}, Número de Série: {produto.numero_de_serie}")
    print("Produtos na promoção:")
    for produto in produtos_na_promocao:
        print(produto)
    print(f"Total da compra: R${calcular_total(carrinho):.2f}")

def main():
    carrinho = {}
    produtos_na_promocao = []
    camisas_compradas = 0
    quadrinhos_comprados = 0
    while True:
        try:
            comando = input("Digite 'a' para adicionar produto, 'r' for para remover produto, 'f' para finalizar a compra ou 'q' para sair: ")
            
            if comando == 'a':
                tipo_produto = input("Digite 'camisa', 'caneca' ou 'quadrinho': ")
                nome = input("Nome do produto: ")
                preco = float(input("Preço do produto: "))

                if tipo_produto == 'camisa':
                    tamanho = input("Tamanho da camisa (P, M ou G): ")
                    produto = Camisa(nome, preco, tamanho)
                elif tipo_produto == 'caneca':
                    capacidade = int(input("Capacidade da caneca (ml): "))
                    produto = Caneca(nome, preco, capacidade)
                elif tipo_produto == 'quadrinho':
                    autor = input("Autor do quadrinho: ")
                    editora = input("Editora do quadrinho: ")
                    produto = Quadrinho(nome, preco, autor, editora)
                else:
                    print("Tipo de produto inválido.")
                    continue
                
                quantidade = int(input("Quantidade: "))
                produto.numero_de_serie = produto.gerador_numero_de_serie()
                if produto in carrinho:
                    carrinho[produto] += quantidade
                else:
                    carrinho[produto] = quantidade

                if tipo_produto == 'camisa':
                    camisas_compradas += quantidade
                    if camisas_compradas >= 4:
                        brinde_caneca = Caneca("Caneca de Brinde", 0, 250)
                        brinde_caneca.numero_de_serie = brinde_caneca.gerador_numero_de_serie()
                        if brinde_caneca in carrinho:
                            carrinho[brinde_caneca] += 1
                        else:
                            carrinho[brinde_caneca] = 1
                        produtos_na_promocao.append(brinde_caneca)
                        camisas_compradas -= 4
                    
                elif tipo_produto == 'quadrinho':
                    quadrinhos_comprados += quantidade
                    if quadrinhos_comprados >= 5:
                        menor_preco = min(carrinho.keys(), key=lambda p: p.preco)
                        del carrinho[menor_preco]
                        produtos_na_promocao.append(menor_preco)
                        quadrinhos_comprados -= 5
                   
            elif comando == 'r':
                nome_produto = input("Nome do produto a ser removido: ")
                for produto in carrinho.keys():
                    if produto.nome == nome_produto:
                        quantidade = int(input(f"Quantidade de '{nome_produto}' a ser removida: "))
                        if quantidade >= carrinho[produto]:
                            del carrinho[produto]
                        else:
                            carrinho[produto] -= quantidade
                        break
                else:
                    print(f"Produto '{nome_produto}' não encontrado no carrinho.")
                
            elif comando == 'f':
                imprimir_nota_fiscal(carrinho, produtos_na_promocao)
                break
                
            elif comando == 'q':
                break
                                                                 
            else:
                print("Comando inválido.")
                
        except ValueError:
            print("Entrada inválida. Verifique os valores digitados.")
            
if __name__ == "__main__":
    main()
   
