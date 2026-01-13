import csv


def validar_lancamentos(caminho_arquivo):
    """
    Executa validações básicas de integridade em lançamentos contábeis.
    """
    with open(caminho_arquivo, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            validar_valor(linha)
            validar_receita_negativa(linha)
            validar_centro_custo(linha)


def validar_valor(linha):
    if not linha['amount']:
        print(f"[ERRO] Lançamento {linha['id']} sem valor informado")


def validar_receita_negativa(linha):
    if 'Receita' in linha['account'] and linha['amount']:
        if float(linha['amount']) < 0:
            print(f"[ERRO] Lançamento {linha['id']} com valor negativo para receita")


def validar_centro_custo(linha):
    if not linha['cost_center']:
        print(f"[ERRO] Lançamento {linha['id']} sem centro de custo informado")


if __name__ == "__main__":
    validar_lancamentos("data/lancamentos_exemplo.csv")
