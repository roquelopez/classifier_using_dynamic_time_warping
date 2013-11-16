'''
Created on Jun 12, 2013

@author: Roque E. Lopez
'''
from math import pow


class DTW(object):
    '''
    Class that implements the algorithm DTW(Dynamic Time Warping) using Dynamic Programming
    '''
    
    def __init__(self, seq_A, seq_B):
        self.seq_A = seq_A # represents the first sequence
        self.seq_B = seq_B # represents the second sequence
        self.memory = [None] * len(seq_A) # store values to avoid to repeat calculations
        
        for k in range(len(seq_A)):
            self.memory[k] = [None] * len(seq_B)
        
    def recursive_dtw(self, i, j):
        ''' Measure the similarity between two sequences recursively '''
        if i == 0 and j == 0:
            return 0
        if i == 0 or j == 0:
            return float('inf') 
        
        if self.memory[i][j] is not None:
            return self.memory[i][j]
        else:
            self.memory[i][j] =  pow(self.seq_A[i] - self.seq_B[j], 2) + min(self.recursive_dtw(i - 1, j - 1),
                                                                             self.recursive_dtw(i, j - 1),
                                                                             self.recursive_dtw(i - 1, j))
        return self.memory[i][j]
        
    def iterative_dtw(self):
        ''' Measure the similarity between two sequences iteratively '''
        m = len(self.seq_A)
        n = len(self.seq_B)
        matrix = [None] * m 
        
        for i in range(m):
            matrix[i] = [float('inf')] * n # initially with infinite values
        
        matrix[0][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                matrix [i][j] = pow(self.seq_A[i] - self.seq_B[j], 2) + min(matrix[i-1][j],
                                                                            matrix[i][j-1],   
                                                                            matrix[i-1][j-1])    
    
        return matrix[m-1][n-1]
                