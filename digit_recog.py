"""
Written by: TheRealMentor
Date: 12-08-2018

"""

#Importing libraries
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import datasets

#Importing Dataset from sklearn
digits = datasets.load_digits()

#Preparing the classifier model
classifier = svm.SVC(gamma=0.001, C = 100)

#Splitting the dataset into the training set
X, y = digits['data'][:-10], digits['target'][:-10]
y = y.reshape(-1, 1)

#Fitting the training set into the model
classifier.fit(X, y)

#Predicting a number from the testing set
print('Prediction:', classifier.predict([digits['data'][-4]]))

#PLotting the image
plt.imshow(digits.images[-4], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()