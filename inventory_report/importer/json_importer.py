import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path: str) -> list:
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(file_path, "r") as json_file:
            return json.load(json_file)
