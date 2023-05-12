import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:
        with open(file_path, newline="") as file:
            if file_path.endswith(".csv"):
                reader = csv.DictReader(file)
                stock = list(reader)
            elif file_path.endswith(".json"):
                stock = json.load(file)
            elif file_path.endswith("xml"):
                tree = ET.parse(file)
                root = tree.getroot()
                stock = []
                for product in root.findall("product"):
                    stock.append({
                        "id": product.get("id"),
                        "name": product.find("name").text,
                        "price": product.find("price").text,
                        "quantity": product.find("quantity").text,
                    })
            else:
                raise ValueError("Extensão de arquivo inválida")

        if report_type == "simples":
            report = SimpleReport.generate(stock)
        elif report_type == "completo":
            report = CompleteReport.generate(stock)
        else:
            raise ValueError("Tipo de relatório inválido")

        return report
