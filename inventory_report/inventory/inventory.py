import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def _load_csv(file_path):
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    @staticmethod
    def _load_json(file_path):
        with open(file_path) as file:
            return json.load(file)

    @staticmethod
    def _load_xml(file_path):
        tree = ET.parse(file_path)
        stock = []
        for root in tree.getroot():
            item = {subroot.tag: subroot.text for subroot in root}
            stock.append(item)
        return stock

    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:
        loaders = {
            "csv": Inventory._load_csv,
            "json": Inventory._load_json,
            "xml": Inventory._load_xml,
        }

        extension = file_path.split(".")[-1]
        if extension not in loaders:
            raise ValueError("Extensão de arquivo inválida")

        with open(file_path, newline=""):
            stock = loaders[extension](file_path)

        if report_type == "simples":
            report = SimpleReport.generate(stock)
        elif report_type == "completo":
            report = CompleteReport.generate(stock)
        else:
            raise ValueError("Tipo de relatório inválido")

        return report
