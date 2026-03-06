from analyzer import analyze_excel
from pathlib import Path


def formatar_moeda(valor):
    return f"{valor:,}".replace(",", ".")


def main():

    # Caminho absoluto baseado na pasta do projeto
    base_path = Path(__file__).parent
    file_path = base_path / "hardware_sales_data.xlsx"

    results = analyze_excel(file_path)

    print("\n===== RELATÓRIO DE VENDAS =====\n")

    print(f"Total de registros analisados: {results['total_registros']}")
    print(f"Faturamento total: R$ {formatar_moeda(results['faturamento_total'])}")
    print(f"Custo total: R$ {formatar_moeda(results['custo_total'])}")
    print(f"Lucro total: R$ {formatar_moeda(results['lucro_total'])}")
    print(f"Margem média de lucro: {results['margem_media']:.2f}%")
    print(f"Produto mais vendido: {results['produto_mais_vendido']}")
    print(f"Marca mais vendida: {results['marca_mais_vendida']}")
    print(f"Região com maior faturamento: {results['regiao_maior_faturamento']}")

    print("\n===============================\n")


if __name__ == "__main__":
    main()