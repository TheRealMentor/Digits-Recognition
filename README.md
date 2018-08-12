# Digits Recognition
Recognizing digits other than 0 or 1 is a big step for machine to learn. This code will tell you how it is done using the algorithm present already on the internet.

<h4 align="center">Prediction: 0</h4>
<p align="center">
  <img src="https://raw.githubusercontent.com/TheRealMentor/Digits-Recognition/master/Figure_1.png" alt="Number 0">
</p>

## Where to get the dataset?
This is the important question we have in the beginning of every machine learning project. Because to do some task you need to have some data (by some I mean a lot of data) to train our machine, our code, to be able to predict or do whatever task we give to it do, efficiently. 

For this particular problem, I have used [sklearn's digits dataset](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) to train my model.

## What do we have in the dataset?
In the real world, most of the data is not labeled. We have to label it manually, or we can ask a machine to do it. (FYI, that's what we are trying to do here!) 

In this dataset, we have different values at different positions that eventually define the number. We have 10 classes (0-9) and for each class we have different type of data point that can be present in the real world regarding that class. For example, look at the following images.

<p align="center">
  <img src="https://raw.githubusercontent.com/TheRealMentor/Digits-Recognition/master/number8_1.png" alt="Number 8">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/TheRealMentor/Digits-Recognition/master/number8_2.png" alt="Number 8">
</p>

Both of these images are of number 8. They look different but both of these have same characteristics that machine is able to find and predict most of the time correctly. 

You can look at the documentation for more information on the dataset.

## I don't understand the code? How is this machine learning?
You don't have to understand the code if you are a beginner and have just started learning about ML. The best thing about machine learning is that it is the set of lines of code that is more or like similar to any other programming language, but in the end you tell the machine to do stuff on it's own. 

That's where training and testing comes into picture. You see that I have written a line or two that is used to divide the dataset into 2 parts. One into **training set** and another into **testing set**. 

Training set is used to train the model and testing set is used to check how accurate is the model.

## What do I learn here?
Well, this question is something that you should be able to answer yourself after writing this code and analysing it. What I understood is that there is a pipeline here.

### Pipeline
* Prepare the dataset
* Divide the dataset into training and testing set
* Define the classifier
* Fit the training set into the classifier
* Use the classifier to predict the outcome

#### *Note:*
Thank you for visiting this project repo. I'll making more repo like this one and try to make the complex concepts more approachable to all.
