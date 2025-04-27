# Previsão de Vendas de Sorvete com MLflow

Este projeto demonstra um fluxo de trabalho básico de machine learning para prever as vendas de sorvete com base na temperatura, utilizando o MLflow para rastreamento de experimentos, gerenciamento de ambientes e registro de modelos.

## Visão Geral

O objetivo principal deste projeto é construir um modelo de regressão linear simples para prever as vendas de sorvete usando a temperatura como variável preditora. O MLflow é integrado para:

* **Rastrear experimentos:** Registrar métricas de desempenho do modelo (RMSE).
* **Gerenciar ambientes:** Utilizar um ambiente `conda` para garantir a reprodutibilidade das dependências.
* **Registrar modelos:** Salvar o modelo treinado para futuras inferências e implantações.

## Estrutura do Projeto

* `data/`: Contém os arquivos de dados.
    ```
    data/
    └── raw/
        └── ice_cream_sales.csv       # Arquivo de dados com temperatura e vendas
    ```
* `src/`: Contém o código-fonte do projeto.
    ```
    src/
    └── train_model.py              # Script Python para treinar o modelo
    ```
* Arquivos de nível superior:
    ```
    ./
    ├── MLProject                       # Arquivo de definição do projeto MLflow
    └── conda.yaml                      # Arquivo de especificação do ambiente conda
    ```

## Pré-requisitos

* **Conda:** Necessário para o gerenciamento do ambiente definido em `conda.yaml`. Você pode instalar o Conda através do Anaconda Distribution ou Miniconda.
* **MLflow:** Instalado como dependência no ambiente `conda`.

## Como Executar o Projeto

1.  **Navegue até a raiz do diretório do projeto:**

    ```bash
    cd ice_cream_sales_forecast
    ```

2.  **Execute o projeto MLflow:**

    ```bash
    mlflow run . -e train
    ```

    Este comando fará com que o MLflow:
    * Crie (se não existir) ou use o ambiente `conda` especificado em `conda.yaml`.
    * Execute o script `src/train_model.py` dentro desse ambiente.
    * Rastreie as métricas (RMSE) usando o MLflow Tracking.
    * Registre o modelo treinado no MLflow Model Registry.

## Detalhes dos Arquivos

* **`data/raw/ice_cream_sales.csv`:** Um arquivo CSV contendo duas colunas: `Temperatura` (a temperatura ambiente) e `Vendas` (o número de unidades de sorvete vendidas).

* **`src/train_model.py`:** Um script Python que:
    * Carrega os dados de `ice_cream_sales.csv`.
    * Divide os dados em conjuntos de treinamento e teste.
    * Treina um modelo de regressão linear usando a temperatura para prever as vendas.
    * Avalia o modelo usando o Root Mean Squared Error (RMSE).
    * Registra a métrica RMSE com o MLflow Tracking.
    * Registra o modelo treinado com o MLflow Model Registry.
    * Inclui uma prática recomendada para registrar a assinatura e um exemplo de entrada do modelo (comentado por padrão, pode ser descomentado).

* **`MLProject`:** Um arquivo YAML que define o projeto MLflow, incluindo o nome e os pontos de entrada (neste caso, apenas o ponto de entrada `train` que executa o script de treinamento). Ele também especifica o ambiente `conda` a ser usado.

* **`conda.yaml`:** Um arquivo YAML que especifica o ambiente `conda` necessário para executar o projeto, incluindo a versão do Python e as dependências (`pandas`, `scikit-learn`, `mlflow`).

## Acompanhamento de Experimentos

Após executar o projeto, você pode visualizar os resultados e o modelo registrado usando a interface de usuário do MLflow:

```bash
mlflow ui
```

Abra o link que aparecer no seu navegador (geralmente http://localhost:5000). Você poderá explorar as execuções, visualizar a métrica RMSE e encontrar o modelo registrado na seção de artefatos da execução.

Próximos Passos (Opcionais)
Implementar o modelo: Crie um script para carregar o modelo registrado e fazer previsões com novos dados de temperatura.
Melhorar o modelo: Experimente com outros modelos de regressão ou adicione mais variáveis preditoras (se disponíveis).
Adicionar assinatura e exemplo de entrada: Descomente e configure a parte do código em train_model.py para registrar o modelo com sua assinatura e um exemplo de entrada.
Empacotar o modelo para implantação: Use as ferramentas do MLflow para empacotar o modelo para diferentes plataformas de implantação (por exemplo, Docker, Kubernetes, servidores REST).
Contribuição
Sinta-se à vontade para contribuir com melhorias neste projeto através de pull requests.

## Licença

MIT License

Copyright (c) 2025 Orcioly Andrade Alves

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.