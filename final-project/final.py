import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv("final-project/winequality-red.csv", delimiter=';')
x = data["total sulfur dioxide"].values
y = data["free sulfur dioxide"].values

# Create your training and testing datasets:
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.2)
# Use reshape to turn the x values into 2D arrays:
xtrain = xtrain.reshape(-1,1)

# Create the model
model = LinearRegression().fit(xtrain, ytrain)
# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(xtrain, ytrain)

# Print out the linear equation and r squared value:
print("Model's Linear Equation: y=",coef, "x+", intercept)
print("R Squared value:", r_squared)
print(r_squared)

'''
**********TEST THE MODEL**********
'''
# reshape the xtest data into a 2D array
xtest = xtest.reshape(-1,1)
# get the predicted y values for the xtest values - returns an array of the results
predict = model.predict(xtest)
# round the value in the np array to 2 decimal places
predict = np.around(predict, 2)

# Test the model by looping through all of the values in the xtest dataset
print("\nTesting Linear Model with Testing Data:")
for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    print("x value:", float(x_coord), "Predicted y value:", predicted_y, "Actual y value:", actual)
'''
**********CREATE A VISUAL OF THE RESULTS**********
'''
plt.figure(figsize=(5,4))

plt.scatter(xtrain, ytrain, c="purple", label="Training Data")
plt.scatter(xtest, ytest, c="blue", label="Testing Data")
plt.scatter(xtest, predict, c="red", label="Predictions")

plt.xlabel("Total sulfur dioxide")
plt.ylabel("Free sulfur dioxide")
plt.title("Free sulfur dioxide vs Total sulfur dioxide")
plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()