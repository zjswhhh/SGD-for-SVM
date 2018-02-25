#!/usr/bin/python
import matplotlib  
matplotlib.use('Agg')
import os
import re
import getopt
import sys
import numpy as np
import matplotlib.pyplot as plt 

# Parser training data 
with open('/u/cs246/data/adult/a7a.train', 'r') as f:
    lines = f.readlines()
    line_num = len(lines)
    N = line_num
    #print lines
    #print line_num
    
training_data = [[[0 for i in range(123)], 1] for i in range(line_num)]

for i in range(line_num):
    if lines[i][0] == '+':
        training_data[i][1] = 1
    else:
        training_data[i][1] = -1
    digit =  re.findall(r'(\w*[0-9]+)\w*',lines[i])     # Get the digital numbers in every line 
    # print digit
    index =  digit[1::2]        # The even bits of digit are the indexes of features whose value is 1  
    # print index
    for j in index: 
        training_data[i][0][int(j)-1] = 1

# Parser test data
with open('/u/cs246/data/adult/a7a.test', 'r') as f:
    lines = f.readlines()
    line_num = len(lines)
    # print lines
    # print line_num
    
test_data = [[[0 for i in range(123)], 1] for i in range(line_num)]

for i in range(line_num):
    if lines[i][0] == '+':
        test_data[i][1] = 1
    else:
        test_data[i][1] = -1
    digit =  re.findall(r'(\w*[0-9]+)\w*',lines[i])     # Get the digital numbers in every line 
    # print digit
    index =  digit[1::2]        # The even bits of digit are the indexes of features whose value is 1  
    # print index
    for j in index: 
        test_data[i][0][int(j)-1] = 1

# Parser dev data
with open('/u/cs246/data/adult/a7a.dev', 'r') as f:
    lines = f.readlines()
    line_num = len(lines)
    # print lines
    # print line_num
    
dev_data = [[[0 for i in range(123)], 1] for i in range(line_num)]

for i in range(line_num):
    if lines[i][0] == '+':
        dev_data[i][1] = 1
    else:
        dev_data[i][1] = -1
    digit =  re.findall(r'(\w*[0-9]+)\w*',lines[i])     # Get the digital numbers in every line 
    # print digit
    index =  digit[1::2]        # The even bits of digit are the indexes of features whose value is 1  
    # print index
    for j in index: 
        dev_data[i][0][int(j)-1] = 1

# Initialization 
w = [0.0000000000 for i in range(123)]
b = 0.0
iterations = 5
p = 20 #number of plot
capacity = np.logspace(-3, 4, p)

# Update w&b
def update(item):
    global w, b, c
    for i in range(123):
        w[i] = w[i] - 0.1*(w[i]/N - c * item[1] * item[0][i])
#!/usr/bin/python
    b = b + 0.1*c * item[1]
 
# Calculate the distance between item and dicision surface
def dis(item):
    global w, b
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]
    res += b
    res *= item[1]
    return res
 
# One learning loop
def check():
    for item in training_data:
        if 1 - dis(item) > 0:
            update(item)
        else:
            for i in range(123):
                w[i] -= 0.1*w[i]/N
    
 
if __name__=="__main__":
    test_accuracy = [0 for i in range(p)]
    dev_accuracy = [0 for i in range(p)]
    for i in range(p):
        c = capacity[i]
        for j in range(int(iterations)):
            check()
        # Calcualte the Test Accuracy
        correctTest = 0.000000000000
        correctDev = 0.000000000000
        
        for item in test_data:
            if dis(item) > 0:
                correctTest += 1
        accuracyTest = correctTest / len(test_data)

        for item in dev_data:
            if dis(item) >0:
                correctDev += 1
        accuracyDev = correctDev / len(dev_data)

        test_accuracy[i] = accuracyTest
        dev_accuracy[i] = accuracyDev

# plot
plt.subplot(211)
plt.semilogx(capacity, test_accuracy, '*-')
plt.ylim(0.6,1)
plt.xlabel('C')
plt.ylabel('test_accuracy')

plt.subplot(212)
plt.semilogx(capacity, dev_accuracy, '*-')
plt.ylim(0.6,1)
plt.xlabel('C')
plt.ylabel('dev_accuracy')

plt.savefig('plot.png')

