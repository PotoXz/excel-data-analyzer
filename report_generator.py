def generate_report(data):

    with open("sales_report.txt", "w", encoding="utf-8") as file:

        file.write("RELATÓRIO DE VENDAS DE HARDWARE\n")
        file.write("=" * 50)
        file.write("\n\n")

        file.write(f"Total de registros analisados: {data['total_registros']}\n\n")

        file.write(f"Faturamento total: R$ {data['faturamento_total']:.2f}\n")
        file.write(f"Custo total: R$ {data['custo_total']:.2f}\n")
        file.write(f"Lucro total: R$ {data['lucro_total']:.2f}\n")

        file.write(f"Margem média de lucro: {data['margem_media']:.2f}%\n\n")

        file.write(f"Produto mais vendido: {data['produto_mais_vendido']}\n")
        file.write(f"Marca mais vendida: {data['marca_mais_vendida']}\n")
        file.write(f"Região com maior faturamento: {data['regiao_maior_faturamento']}\n")