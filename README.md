# Laboratório Avançado de Física - IFSC/USP

Ferramentas de automação e análise estatística rigorosa para a disciplina de Laboratório Avançado.

Este projeto visa eliminar o trabalho repetitivo de formatação e cálculo, permitindo foco total na física e na análise de dados. Ele utiliza **Python (Scipy)** para ajustes não-lineares (Mínimos Quadrados Ponderados) e **LaTeX** para geração de relatórios profissionais.

## 🚀 Funcionalidades

* **Automação de Workflow:** Script `new_exp.py` cria a estrutura completa de pastas para novos experimentos em segundos.
* **Análise Estatística Robusta:**
    * Ajuste de curvas usando `scipy.optimize.curve_fit` (considerando erros em Y).
    * Cálculo automático de **Qui-Quadrado Reduzido** ($\chi^2_{red}$).
    * Geração de **Matriz de Covariância** para propagação de incertezas nos parâmetros.
* **Plotagem Profissional:** Gera uma figura única contendo o ajuste do modelo e a análise de resíduos (obrigatório para validação do modelo físico).
* **Relatórios LaTeX:** Template pré-configurado nas normas, pronto para inserir os gráficos gerados.

## 📂 Estrutura do Repositório

```text
/
├── new_exp.py             # Script de automação (Cria novos experimentos)
├── templates/             # Arquivos base
│   ├── base_script.py     # Script Python com cálculo de Chi2 e Resíduos
│   └── report_template.tex # Template LaTeX limpo
│
├── exp01-exemplo/         # (Exemplo de pasta gerada)
│   ├── analysis.py        # Script de análise específico
│   ├── data.csv           # Dados brutos
│   ├── fit_plot.png       # Gráfico gerado (Ajuste + Resíduos)
│   └── report.tex         # Relatório final
│
└── README.md
