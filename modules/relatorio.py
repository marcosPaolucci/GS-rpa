from jinja2 import Environment, FileSystemLoader
import os

def gerar_relatorio(contexto, template_dir='templates', template_nome='relatorio_template.html', saida_html='reports/relatorio_final.html'):
    """
    Gera um relatório em HTML a partir de um template e um dicionário de contexto.
    """
    os.makedirs(os.path.dirname(saida_html), exist_ok=True)

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_nome)

    html_renderizado = template.render(contexto)

    with open(saida_html, "w", encoding="utf-8") as f:
        f.write(html_renderizado)

    print(f"Relatório HTML gerado em: {saida_html}")