import datetime

# Simulando dados que viriam de uma query SQL no banco do Linx BIG
chamados = [
    {"id": "101", "modulo": "Fiscal", "erro": "Erro na emissão de nota", "prioridade": "Alta"},
    {"id": "102", "modulo": "PBM", "erro": "Autorização negada", "prioridade": "Média"},
    {"id": "103", "modulo": "Financeiro", "erro": "Conciliação de cartão", "prioridade": "Baixa"},
    {"id": "104", "modulo": "Configurações", "erro": "Erro de API / Webservice", "prioridade": "Alta"}
]

def gerar_relatorio_html(dados):
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    html_content = f"""
    <html>
    <head>
        <title>Relatório de Suporte - Linx BIG</title>
        <style>
            body {{ font-family: sans-serif; margin: 40px; background-color: #f4f4f9; }}
            table {{ border-collapse: collapse; width: 100%; background: white; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #0056b3; color: white; }}
            .alta {{ color: red; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>Resumo de Atendimentos - {data_atual}</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Módulo</th>
                <th>Descrição do Erro</th>
                <th>Prioridade</th>
            </tr>
    """

    for item in dados:
        cor_classe = "class='alta'" if item['prioridade'] == "Alta" else ""
        html_content += f"""
            <tr>
                <td>{item['id']}</td>
                <td>{item['modulo']}</td>
                <td>{item['erro']}</td>
                <td {cor_classe}>{item['prioridade']}</td>
            </tr>
        """

    html_content += "</table></body></html>"

    with open("relatorio_suporte.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Relatório gerado com sucesso!")

if __name__ == "__main__":
    gerar_relatorio_html(chamados)