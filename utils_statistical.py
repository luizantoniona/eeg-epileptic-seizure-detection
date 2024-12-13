import Utils.Commons as cm
from Utils.Graphics.ViolinPlot import ViolinPlot
from Metric.Evaluator import Evaluator
from Dataset.DatasetTypeEnum import dataset_enum_by_name
from Object.Signal.SignalTypeEnum import signal_enum_by_name
import pandas as pd

DATASET = dataset_enum_by_name("CHBMIT")
MODELS = cm.models()
SIGNAL = signal_enum_by_name("PSDWelch")
WINDOW = 5

dados_acumulados = []

for model in MODELS:
    model_evaluation = Evaluator(dataset_type=DATASET, model_type=model, signal_type=SIGNAL, window_length=WINDOW)

    dados = {
        "Grupo": (
            [f"{model.name} Accuracy"] * len(model_evaluation.accuracy)
            + [f"{model.name} Precision"] * len(model_evaluation.precision)
            + [f"{model.name} Sensitivity"] * len(model_evaluation.sensitivity)
            + [f"{model.name} Specificity"] * len(model_evaluation.accuracy)
            + [f"{model.name} F1-Score"] * len(model_evaluation.f1_score)
        ),
        "Valor": (model_evaluation.accuracy + model_evaluation.precision + model_evaluation.sensitivity + model_evaluation.specificity + model_evaluation.f1_score),
    }

    dados_acumulados.append(pd.DataFrame(dados))

import seaborn as sns
import matplotlib.pyplot as plt

df_consolidado = pd.concat(dados_acumulados, ignore_index=True)

df_consolidado["Modelo"] = df_consolidado["Grupo"].str.extract(r"^(.*?) ")
df_consolidado["Métrica"] = df_consolidado["Grupo"].str.extract(r" (.*?)$")

# Criar um FacetGrid com gráficos de violino por métrica
g = sns.catplot(data=df_consolidado, x="Modelo", y="Valor", col="Métrica", kind="violin", palette="muted", sharey=False, col_wrap=2, inner="quartile")

# Ajustar o layout e adicionar título
g.fig.set_size_inches(12, 8)
g.fig.subplots_adjust(top=0.9)
g.fig.subplots_adjust(bottom=0.1)
g.fig.suptitle(f"Metrics distribution {SIGNAL.name} - {WINDOW} seconds", fontsize=16)

# Personalizar os eixos
g.set_axis_labels("Models", "Metric value")
g.set_titles("{col_name}")  # Mostrar o nome da métrica em cada gráfico

plt.show()

# plt.figure(figsize=(10, 8))
# sns.violinplot(x="Grupo", y="Métrica", data=df, palette="muted", inner="quartile", density_norm="width")

# plt.title("Distribution of metric value for CNN")
# plt.ylabel("Value")

# plt.tight_layout()
# plt.show()
