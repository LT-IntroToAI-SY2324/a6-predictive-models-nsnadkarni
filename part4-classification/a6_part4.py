import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male', 'Female'], [0, 1], inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

print("Values of x:")
print(x)  
print("\nValues of y:")
print(y)  

scaler = StandardScaler()

x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2)

logistic_model = linear_model.LogisticRegression()
logistic_model.fit(x_train, y_train)

accuracy = logistic_model.score(x_test, y_test)
print("\nAccuracy of the model:", accuracy)

y_pred = logistic_model.predict(x_test)

print("\nActual ytest values:")
print(y_test)  

print("\nPredicted y values:")
print(y_pred)  