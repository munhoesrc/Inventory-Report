import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str) -> str:
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            stock = list(reader)

        if report_type == "simples":
            report = SimpleReport.generate(stock)
        elif report_type == "completo":
            report = CompleteReport.generate(stock)
        else:
            raise ValueError("Tipo de relatório inválido")

        return report
