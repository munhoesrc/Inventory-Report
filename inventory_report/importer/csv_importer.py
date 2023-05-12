import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path: str) -> list:
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            return [row for row in csv_reader]
