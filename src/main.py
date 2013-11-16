'''
Created on Jun 12, 2013

@author: Roque E. Lopez
'''
from classifier import Classifier

def read_data(file_path):
    ''' Read the data of a file and return a list with the format <IdClass, Sequences> '''
    f = open(file_path, 'r')
    lines = f.readlines()
    formatted_data = list()
    
    for line in lines:
        seq = line.split(' ')
        id_class = seq[0]
        tupla = (int(id_class), [float(i) for i in seq])
        formatted_data.append(tupla) 
    f.close()
    return formatted_data

if __name__ == '__main__':
    #training_file = "../resource/treino.txt"
    #test_file = "../resource/teste.txt"
    training_file = raw_input("Please, enter the path of the training file: ")
    test_file = raw_input("Please, enter the path of the test file: ")
    print("Running...")
    training_data = read_data(training_file)
    test_data = read_data(test_file)
    
    classifier = Classifier(training_data)
    classifier.evaluate_test_data(test_data)
