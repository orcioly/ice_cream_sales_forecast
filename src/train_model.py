import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, root_mean_squared_error
import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

# Definir caminhos de arquivos e nome do modelo
DATA_PATH = 'data/raw/ice_cream_sales.csv'
MODEL_NAME = 'linear_regression_model'

if __name__ == "__main__":
    # Carregar os dados
    try:
        data = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {DATA_PATH}. Certifique-se de que o arquivo 'ice_cream_sales.csv' está na pasta data/raw/.")
        exit(1)

    # Definir as variáveis independentes (X) e dependente (y)
    if 'Temperatura' not in data.columns or 'Vendas' not in data.columns:
        print("Erro: As colunas 'Temperatura' e/ou 'Vendas' não foram encontradas no arquivo CSV.")
        exit(1)

    X = data[['Temperatura']]
    y = data['Vendas']

    # Dividir os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Iniciar um experimento MLflow
    with mlflow.start_run():
        # Criar e treinar o modelo
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Avaliar o modelo
        rmse = root_mean_squared_error(y_test, y_pred)
        print(f'Root Mean Squared Error no conjunto de teste: {rmse:.2f}')
        mlflow.log_metric("rmse", rmse)

        # Inferir a assinatura do modelo
        signature = infer_signature(X_train, y_train)
        input_example = X_train.head()

        # Registrar o modelo treinado com assinatura e exemplo
        mlflow.sklearn.log_model(model, MODEL_NAME, signature=signature, input_example=input_example)
        print(f'Modelo registrado no MLflow como: {MODEL_NAME}')