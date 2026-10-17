# freeCodeCamp: Data Analysis with Python

Os cinco projetos do certificado [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) do freeCodeCamp, reunidos num só repositório. Cada pasta é um projeto completo, com o próprio código, testes e dados.

| Projeto | O que faz | Principais bibliotecas |
|---|---|---|
| [Mean-Variance-Standard Deviation Calculator](mean-variance-standard-deviation-calculator/) | Calcula média, variância, desvio padrão, máximo, mínimo e soma de uma matriz 3×3, por linha, por coluna e no total. | NumPy |
| [Demographic Data Analyzer](demographic-data-analyzer/) | Responde perguntas sobre dados demográficos do censo dos EUA de 1994 (escolaridade, renda, horas trabalhadas, país de origem). | pandas |
| [Medical Data Visualizer](medical-data-visualizer/) | Normaliza dados de exames médicos e mostra a relação entre fatores de risco e doença cardíaca em gráficos categóricos e num mapa de calor de correlação. | pandas, seaborn, Matplotlib |
| [Page View Time Series Visualizer](page-view-time-series-visualizer/) | Limpa e visualiza as visitas diárias ao fórum do freeCodeCamp em gráfico de linha, de barras por mês e boxplots por ano e por mês. | pandas, seaborn, Matplotlib |
| [Sea Level Predictor](sea-level-predictor/) | Projeta o nível do mar até 2050 com regressão linear, comparando a tendência desde 1880 com a tendência desde 2000. | pandas, SciPy, Matplotlib |

## Como rodar

Cada projeto roda sozinho e tem o próprio `requirements.txt`. Entre na pasta, instale as dependências e rode o `main.py`, que executa o projeto e os testes unitários:

```bash
cd sea-level-predictor
pip install -r requirements.txt
python main.py
```

## Histórico

Os projetos começaram como repositórios separados e foram juntados aqui com `git subtree`. Os commits originais de cada um continuam no histórico deste repositório, ligados ao commit que trouxe o projeto para a sua pasta.
