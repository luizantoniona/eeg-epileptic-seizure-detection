"""
Module: metrics_generator

Provides class to calculate metrics from test and prediction
"""

class Metrics:
   """
   """
   def __init__(self, test, predictions):
      self.TruePositives = 0
      self.TrueNegatives = 0
      self.FalsePositives = 0
      self.FalseNegatives = 0
      self.Total = len(test)

      for i in range(self.Total):
         if test[i] == True and predictions[i] == True:
            self.TruePositives += 1
         elif test[i] == False and predictions[i] == False:
            self.TrueNegatives += 1
         elif test[i] == True and predictions[i] == False:
            self.FalsePositives += 1
         elif test[i] == False and predictions[i] == True:
            self.FalseNegatives += 1

      print('True Positives:', self.TruePositives)
      print('True Negatives:', self.TrueNegatives)
      print('False Positives:', self.FalsePositives)
      print('False Negatives:', self.FalseNegatives)
      print('Total Samples:', self.Total)

   def accuracy(self) -> float:
      """
      Accuracy:
      """
      Accuracy = (self.TruePositives + self.TrueNegatives)/(self.Total)
      return Accuracy

   def precision(self) -> float:
      """
      Precision:
      """
      Precision = (self.TruePositives)/(self.TruePositives + self.FalsePositives)
      return Precision

   def sensitivity(self) -> float:
      """
      Sensitivity:
      """
      Sensitivity = (self.TruePositives)/(self.FalseNegatives + self.TruePositives)
      return Sensitivity

   def specificity(self) -> float:
      """
      Specificity:
      """
      Specificity = (self.TrueNegatives)/(self.TrueNegatives + self.FalsePositives)
      return Specificity

   def true_positive_rate(self) -> float:
      """
      True Positive Rate (TPR):
      """
      TruePositiveRate = (self.TruePositives)/(self.TruePositives + self.FalsePositives)
      return TruePositiveRate

   def false_positive_rate(self) -> float:
      """
      False Positive Rate (FPR):
      """
      FalsePositiveRate = (self.FalsePositives)/(self.FalsePositives + self.TrueNegatives)
      return FalsePositiveRate

   def f1_score(self) -> float:
      """
      F1-Score:
      """
      F1Score = (2 * self.accuracy() * self.sensitivity())/(self.accuracy() + self.sensitivity())
      return F1Score

   def all_metrics(self):
      print('Accuracy:',self.accuracy())
      print('Precision:',self.precision())
      print('Sensitivity:',self.sensitivity())
      print('Specificity:',self.specificity())
      print('TPR:',self.true_positive_rate())
      print('FPR:',self.false_positive_rate())
      print('F1-Score:',self.f1_score())
