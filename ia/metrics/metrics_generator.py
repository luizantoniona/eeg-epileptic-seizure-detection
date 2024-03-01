"""
Module: metrics_generator

Provides class to calculate metrics
"""

class Metrics:
   """
   """
   def __init__(self, y_test, predictions):
      self.TruePositives = 0
      self.TrueNegatives = 0
      self.FalsePositives = 0
      self.FalseNegatives = 0
      self.Total = len(y_test)

      for i in range(self.Total):
         if y_test[i] == True and predictions[i] == True:
            self.TruePositives += 1
         elif y_test[i] == False and predictions[i] == False:
            self.TrueNegatives += 1
         elif y_test[i] == True and predictions[i] == False:
            self.FalsePositives += 1
         elif y_test[i] == False and predictions[i] == True:
            self.FalseNegatives += 1

   def accuracy(self):
      """
      Accuracy:
      """
      Accuracy = (self.TruePositives + self.TrueNegatives)/(self.Total)
      print('Accuracy:', Accuracy)

   def precision(self):
      """
      Precision:
      """
      Precision = (self.TruePositives)/(self.TruePositives + self.FalsePositives)
      print('Precision:', Precision)

   def sensitivity(self):
      """
      Sensitivity:
      """
      Sensitivity = (self.TruePositives)/(self.FalseNegatives + self.TruePositives)
      print('Sensitivity:', Sensitivity)

   def specificity(self):
      """
      Specificity:
      """
      Specificity = (self.TrueNegatives)/(self.TrueNegatives + self.FalsePositives)
      print('Specificity:', Specificity)

   def true_positive_rate(self):
      """
      True Positive Rate (TPR):
      """
      TruePositiveRate = (self.TruePositives)/(self.TruePositives + self.FalsePositives)
      print('True Positive Rate:', TruePositiveRate)

   def false_positive_rate(self):
      """
      False Positive Rate (FPR):
      """
      FalsePositiveRate = (self.FalsePositives)/(self.FalsePositives + self.TrueNegatives)
      print('False Positive Rate:', FalsePositiveRate)

   def f1_score(self):
      """
      F1-Score:
      """
      F1Score = (2 * self.accuracy() * self.sensitivity())/(self.accuracy() + self.sensitivity())
      print('F1-Score:', F1Score)

   def all_metrics(self):
      self.accuracy()
      self.precision()
      self.sensitivity()
      self.specificity()
      self.true_positive_rate()
      self.false_positive_rate()
      self.f1_score()
