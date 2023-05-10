from inventory_report.inventory.product import Product


def test_cria_produto():
    MENSAGEM_ARMAZENAMENTO = "Mantenha em local seco e fresco"
    produto = Product(
        id=1,
        nome_do_produto="Produto 1",
        nome_da_empresa="Empresa A",
        data_de_fabricacao="2023-05-08",
        data_de_validade="2024-05-08",
        numero_de_serie="1s4b3l4",
        instrucoes_de_armazenamento=MENSAGEM_ARMAZENAMENTO
    )
    assert produto.id == 1
    assert produto.nome_do_produto == "Produto 1"
    assert produto.nome_da_empresa == "Empresa A"
    assert produto.data_de_fabricacao == "2023-05-08"
    assert produto.data_de_validade == "2024-05-08"
    assert produto.numero_de_serie == "1s4b3l4"
    assert produto.instrucoes_de_armazenamento == MENSAGEM_ARMAZENAMENTO
