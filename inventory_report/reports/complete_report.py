# class CompleteReport:
#     pass
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products: list) -> str:
        resposta = SimpleReport.generate(products)

        produtos_por_empresa = {}
        for product in products:
            empresa = product["nome_da_empresa"]
            produtos_por_empresa[empresa] = (
                produtos_por_empresa.get(empresa, 0) + 1
            )

        resposta += "\nProdutos estocados por empresa:\n"
        for empresa, produto in produtos_por_empresa.items():
            resposta += f"- {empresa}: {produto}\n"

        return resposta
