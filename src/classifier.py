'''
Created on Jun 12, 2013

@author: Roque E. Lopez
'''
from DTW import DTW

No_CLASSES = 12

class Classifier(object):
    '''
    Class that classifies a set of sequences based in the 1-nearest neighbor
    '''

    def __init__(self, training_data):
        self.training_data = training_data # the set of training
    
    def evaluate_test_data(self, test_data):
        ''' Verify if the real class  is equal to the class returned by the classifier.
            Counts the number of correct answers and fills the confusion matrix.
         '''
        correct_answers = 0
        total_queries = len(test_data)
        confusion_matrix = self.create_confusion_matrix()
        
        for seq_test in test_data:
            real_idclass = seq_test[0]
            classifier_idclass = self.classify(seq_test[1])
            if real_idclass == classifier_idclass:
                correct_answers += 1
            confusion_matrix[real_idclass - 1][classifier_idclass - 1] += 1
            
        print("Result: %s of %s ==> %.2f %%" % (correct_answers, total_queries, correct_answers * 100.0 / total_queries))
        self.print_confusion_matrix(confusion_matrix)
        
    def classify(self, seq_test):
        ''' Classify a sequence based in its 1-nearest neighbor '''
        id_class = -1
        min_distance = float('inf')
                      
        for seq in self.training_data:
            dtw = DTW(seq[1], seq_test)
            tmp_distance = dtw.iterative_dtw() #recursive_dtw(len(seq[1])-1, len(seq_test)-1)
            if tmp_distance < min_distance:
                id_class = seq[0]
                min_distance = tmp_distance
               
        return id_class
                   
    def create_confusion_matrix(self):
        ''' Create an empty confusion matrix '''
        confusion_matrix = [0] * No_CLASSES
        
        for i in range(No_CLASSES):
            confusion_matrix[i] = [0] * No_CLASSES
        
        return confusion_matrix
    
    def print_confusion_matrix(self, confusion_matrix):
        ''' Show the results of the confusion matrix '''
        print("Confusion Matrix:")
        for i in range(No_CLASSES):
            print(confusion_matrix[i])
                