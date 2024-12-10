from Metric.Evaluator import Evaluator
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from IA.NeuralNetworkTypeEnum import neural_network_enum_by_name
from Object.Signal.SignalTypeEnum import signal_enum_by_name

cnn_time_1 = Evaluator(dataset_type=dataset_enum_by_name("CHBMIT"), model_type=neural_network_enum_by_name("CNN"), signal_type=signal_enum_by_name("Time"), window_length=1)
cnn_multi_1 = Evaluator(dataset_type=dataset_enum_by_name("CHBMIT"), model_type=neural_network_enum_by_name("CNN"), signal_type=signal_enum_by_name("PSDMultitaper"), window_length=1)
cnn_welch_1 = Evaluator(dataset_type=dataset_enum_by_name("CHBMIT"), model_type=neural_network_enum_by_name("CNN"), signal_type=signal_enum_by_name("PSDWelch"), window_length=1)
cnn_spec_1 = Evaluator(dataset_type=dataset_enum_by_name("CHBMIT"), model_type=neural_network_enum_by_name("CNN"), signal_type=signal_enum_by_name("Spectrogram"), window_length=1)

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

dados = {
    "Grupo": (["CNN - Time"] * len(cnn_time_1.accuracy) + ["CNN - Multitaper"] * len(cnn_multi_1.accuracy) + ["CNN - Welch"] * len(cnn_welch_1.accuracy) + ["CNN - Spectrogram"] * len(cnn_spec_1.accuracy)),
    "Métrica": (cnn_time_1.accuracy + cnn_multi_1.accuracy + cnn_welch_1.accuracy + cnn_spec_1.accuracy),
}

# Criar DataFrame para o gráfico
df = pd.DataFrame(dados)

# Gerar o Violin Plot
plt.figure(figsize=(10, 10))  # Ajustar tamanho do gráfico
sns.violinplot(x="Grupo", y="Métrica", data=df, palette="muted", inner="quartile", density_norm="width")

# Adicionar títulos e rótulos
plt.title("Violin Plot - Comparação de Sinais e Janelas")
plt.ylabel("Acurácia")
plt.xlabel("Grupos de Modelos/Sinais")

# Exibir o gráfico
plt.xticks(rotation=30)  # Rodar os nomes no eixo X para melhorar a legibilidade
plt.tight_layout()  # Melhorar o espaçamento do gráfico
plt.show()
