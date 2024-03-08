"""
Module: metrics

Provides class to calculate metrics from test and prediction
"""

import database.database_utils as db

class Metrics:
   """
   """
   def __init__(self, test, predictions, model_name, model_data_domain):

      self.model_name = model_name
      self.model_data_domain = model_data_domain

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
      db.insert_metrics_data(self.model_name, self.model_data_domain,
                             self.accuracy, self.precision, self.sensitivity, self.specificity, self.true_positive_rate, self.false_positive_rate, self.f1_score,
                             self.true_positives, self.true_negatives, self.false_positives, self.false_negatives, self.total_samples )
