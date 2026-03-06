import pandas as pd


def analyze_excel(file_path):
    """
    Função responsável por analisar uma planilha Excel contendo dados de vendas.

    Parâmetro:
        file_path (str): Caminho do arquivo Excel que será analisado.

    Retorno:
        dict: Dicionário contendo métricas calculadas a partir dos dados.
    """

    # Carrega a planilha Excel em um DataFrame do pandas
    df = pd.read_excel(file_path)

    # Total de registros presentes na planilha
    total_registros = len(df)

    # Soma total do valor de vendas
    faturamento_total = df["Valor de Venda"].sum()

    # Soma total do custo dos produtos
    custo_total = df["Custo"].sum()

    # Cálculo do lucro total
    lucro_total = faturamento_total - custo_total

    # Cálculo da margem média de lucro
    margem_media = (lucro_total / faturamento_total) * 100

    # Produto que mais aparece na planilha (mais vendido)
    produto_mais_vendido = df["Produto"].value_counts().idxmax()

    # Marca que mais aparece na planilha
    marca_mais_vendida = df["Marca"].value_counts().idxmax()

    # Região que possui maior faturamento total
    regiao_maior_faturamento = (
        df.groupby("Região de Venda")["Valor de Venda"]
        .sum()
        .idxmax()
    )

    # Retorna todas as métricas em formato de dicionário
    return {
        "total_registros": total_registros,
        "faturamento_total": faturamento_total,
        "custo_total": custo_total,
        "lucro_total": lucro_total,
        "margem_media": margem_media,
        "produto_mais_vendido": produto_mais_vendido,
        "marca_mais_vendida": marca_mais_vendida,
        "regiao_maior_faturamento": regiao_maior_faturamento
    }