"""
Module: metrics

Provides class to calculate metrics from test and prediction
"""

from Database.DatabaseMetrics import DatabaseMetrics
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

class Metric:
   """
   """
   def __init__(self, test, predictions, dataset_name, model_name, model_data_domain, model_window_length):

      self.dataset_name = dataset_name
      self.model_name = model_name
      self.model_data_domain = model_data_domain
      self.model_window_length = model_window_length

      self.true_positives = 0
      self.true_negatives = 0
      self.false_positives = 0
      self.false_negatives = 0
      self.total_samples = len(test)

      for i in range(self.total_samples):
         if test[i] == True and predictions[i] == True:
            self.true_positives += 1
         elif test[i] == False and predictions[i] == False:
            self.true_negatives += 1
         elif test[i] == True and predictions[i] == False:
            self.false_positives += 1
         elif test[i] == False and predictions[i] == True:
            self.false_negatives += 1

      self.accuracy = (self.true_positives + self.true_negatives)/(self.total_samples)
      self.precision = (self.true_positives)/(self.true_positives + self.false_positives)
      self.sensitivity = (self.true_positives)/(self.false_negatives + self.true_positives)
      self.specificity = (self.true_negatives)/(self.true_negatives + self.false_positives)
      self.true_positive_rate = (self.true_positives)/(self.true_positives + self.false_positives)
      self.false_positive_rate = (self.false_positives)/(self.false_positives + self.true_negatives)
      self.f1_score = (2 * self.accuracy * self.sensitivity)/(self.accuracy + self.sensitivity)

   def all_metrics(self):
      print('True Positives:', self.true_positives)
      print('True Negatives:', self.true_negatives)
      print('False Positives:', self.false_positives)
      print('False Negatives:', self.false_negatives)
      print('total Samples:', self.total_samples)
      print('Accuracy:',self.accuracy)
      print('Precision:',self.precision)
      print('Sensitivity:',self.sensitivity)
      print('Specificity:',self.specificity)
      print('TPR:',self.true_positive_rate)
      print('FPR:',self.false_positive_rate)
      print('F1-Score:',self.f1_score)

   def metrics_to_database(self):
      database = DatabaseMetrics()
      database.insert_metrics_data(self.dataset_name, self.model_name, self.model_data_domain, self.model_window_length,
                             self.accuracy, self.precision, self.sensitivity, self.specificity, self.true_positive_rate, self.false_positive_rate, self.f1_score,
                             self.true_positives, self.true_negatives, self.false_positives, self.false_negatives, self.total_samples )

   def plot_roc_auc(self, y_test, predictions):
      fpr, tpr, threshold = metrics.roc_curve(y_test, predictions)
      roc_auc = metrics.auc(fpr, tpr)

      plt.title('Receiver Operating Characteristic')
      plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
      plt.legend(loc = 'lower right')
      plt.plot([0, 1], [0, 1],'r--')
      plt.xlim([0, 1])
      plt.ylim([0, 1])
      plt.ylabel('True Positive Rate')
      plt.xlabel('False Positive Rate')
      plt.show()
