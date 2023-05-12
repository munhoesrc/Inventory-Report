import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path: str) -> list:
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        tree = ET.parse(file_path)
        root = tree.getroot()

        stock = []
        for item in root:
            row = {}
            for subitem in item:
                row[subitem.tag] = subitem.text
            stock.append(row)

        return stock
