import Utils.Statistical.Mannwhitneyu as MN
import Utils.Statistical.KruskalWallis as KW
import Utils.Statistical.Friedman as FD
from Utils.Graphics.ConfusionMatrixPlotter import ConfusionMatrixPlotter


def manwhitneyu():
    confusion_matrix, combinations = MN.models_competition()
    plotter = ConfusionMatrixPlotter(confusion_matrix, combinations)
    plotter.plot()


# manwhitneyu()

# kruskalwallis_w = KW.kruskal_wallis_with_dunn_windows()

# kruskalwallis_r = KW.kruskal_wallis_with_dunn_representations()

friedman_a = FD.friedman_test_models()
