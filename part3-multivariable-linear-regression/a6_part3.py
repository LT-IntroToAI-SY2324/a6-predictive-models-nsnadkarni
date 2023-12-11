import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles(000)", "age"]].values
y = data["Price"].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression().fit(x_train, y_train)

coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(x, y), 2)

print(f"Model's Linear Equation: y = {coef[0]}x1 + {coef[1]}x2 + {intercept}")
print("R Squared value:", r_squared)
print("***************")
print("Testing Results")

pre = model.predict(x_test)
pre = np.around(pre, 2)

for e in range(len(x_test)):
    actual = round(y_test[e], 2)
    x_data = np.around(x_test[e], 2)
    print(f"Miles(000): {x_data[0]} Age: {x_data[1]} Actual: {actual} Predicted: {pre[e]}")
