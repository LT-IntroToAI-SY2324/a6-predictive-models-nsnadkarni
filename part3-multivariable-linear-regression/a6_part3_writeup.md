# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

0.85, It means that the model is very correlated, as its pretty close to 1.

2. Is your model accurate? Why or why not?

It is pretty accurate as the R Squared value is close to 1.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

$8677.27 for the first and $1348.4.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Since the model is linear, it will eventually cross the x axis and start going negative, instead of being capped at 0.