# SGD-for-SVM
Name: Jing Zhang
Email: zjsw1206@gmail.com
Course: CSC446
Homework: Implement SGD for SVM for the adult income dataset. Experiment with performance as a function of the capacity parameter C. 

************ Files *********
Zhang_Jing_hw3.py
plot.py
plot.png
README

************ Algorithm *****
SGD for SVM

************ Instructions ***
1) For Zhang_Jing_hw3.py 
CLI options: --epochos k --capacity c
example input: ./Zhang_Jing_hw3.py --epochs k --capacity c

The default value for epochs & capacity is 1 & 0.868. 

2) For plot.py
example input: ./plot.py
The result figure will be saved as plot.png under the same direction. 

************ Results *******
As for the accuracy, it doesn't vary much as the number of epochos increasing from 1 to 5. 
When I tried to experiments with capacity, the results show that while the value of C is between 10^-2 and 1, the accuracy is pretty stable. But when the capacity grows greater than 10, the value of accuracy just waves as the capacity increase. 

************ Your interpretation **** 
I think the reason that we don't need much times of iterations to get a good accuracy, is that the dataset is pretty separable in the first place. So even after only one time of iteration, we can get an accuracy rate over 83%. 

And for the capacity, from the formulations, I think it's like a "punish" factor. When C is bigger, we get a bigger "punishment" (updating) for w & b if we find a wrong classification data point. If C is too big, it may cause overfitting problem, which will reduce accuracies. So when C becomes bigger than 1, the accuracies just become "waving". And If C is too small, it may also cause problems like under-fitting. So when C is small enough, accuracies increase as C increases. 

************ References ************
Lecture Notes of CSC 446
