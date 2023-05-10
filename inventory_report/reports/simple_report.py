from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        data_de_fabricacao = min(
            product["data_de_fabricacao"] for product in products
        )
        produtos_validos = [
            product
            for product in products
            if product["data_de_validade"]
            and product["data_de_validade"]
            >= datetime.now().strftime("%Y-%m-%d")
        ]
        data_de_validade = (
            min(produtos_validos, key=lambda x: x["data_de_validade"])[
                "data_de_validade"
            ]
            if produtos_validos
            else None
        )
        empresas = {}
        for product in products:
            empresas[product["nome_da_empresa"]] = (
                empresas.get(product["nome_da_empresa"], 0) + 1
            )
        produtos_empresa = max(empresas, key=empresas.get)
        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {produtos_empresa}"
            )
