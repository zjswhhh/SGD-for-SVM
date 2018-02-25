#!/usr/bin/python

import os
import re
import getopt
import sys

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
iterations = 1
c = 0.868

# Update w&b
def update(item):
    global w, b, c
    for i in range(123):
        w[i] = w[i] - 0.1*(w[i]/N - c * item[1] * item[0][i])
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
    
# Command Line Argument
def main(argv):
    global iterations, c
    try:
        opts, args = getopt.getopt(argv, "",["epochs=","capacity="])
    except getopt.GetoptError:
        print 'Error: Input Error.'
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--epochs":
            iterations = arg
        elif opt == "--capacity":
            c = float(arg)
            #print c
 
if __name__=="__main__":
    main(sys.argv[1:])
    #print iterations
    for i in range(int(iterations)):
        check()
    
# Calcualte the Test Accuracy
correctTrain = 0.000000000000
correctTest = 0.000000000000
correctDev = 0.000000000000

for item in training_data:
    if dis(item) > 0:
        correctTrain += 1
accuracyTrain = correctTrain / len(training_data)

for item in test_data:
    if dis(item) > 0:
        correctTest += 1
accuracyTest = correctTest / len(test_data)

for item in dev_data:
    if dis(item) >0:
        correctDev += 1
accuracyDev = correctDev / len(dev_data)

w.insert(0,b)

#Output 
print "EPOCHS: " + str(iterations)
print "CAPACITY: " + str(c)
print "TRAINING_ACCURACY: " + str(accuracyTrain)
print "TEST_ACCURACY: " + str(accuracyTest)
print "DEV_ACCURACY: " + str(accuracyDev)
print "FINAL_SVM: " + str(w)
    
