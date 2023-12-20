# Project - Create your own predictive model

Predictive models are used across industries to analyze and make predictions about data. From sports to beauty products to app usage, predictive models provide individuals and businesses with data to make informed decisions.

Throughout this module, you have learned how to program both supervised and unsupervised learning models. In this final project, you will create your own! Throughout this project, you will work through activities to complete the following steps:

1. Choose a dataset.
2. Determine which algorithm is the best fit. Based on the dataset you choose, you will need to figure out which algorithm to use. This will require you to get to know your data and your goals! Is there a linear correlation between variables? Are you looking for numerical value or a label/category? Do you know the labels or do you need the model to create them for you?
- Do some tests with matplotlib and visualize your data.  Does it provide a good correlation?  Why or why not?
3. Program your model. Once you have chosen your type of model, it’s time to create it! In this step, you will write a program that fits your chosen model to the data. Your program and output will be specific to the model you choose.  
4. Analyze and present your findings. An important part of creating predictive models is being able to communicate the results. In this final step of the project, you will present your findings using slides or an infographic. Your product should include the following components:
- Your reasoning for the algorithm you chose
    I chose linear regression because I take in a value x and it should return a numerical value y. 
- An explanation and analysis of the output of your model: What results did your model produce? What do they mean?
    After training the linear regression model using 'total sulfur dioxide' as the independent variable (x) and 'free sulfur dioxide' as the dependent variable (y), the model generates coefficients for the linear equation (y = mx + c) that predicts 'free sulfur dioxide' based on 'total sulfur dioxide'.
- A prediction based on your model
    With 24 total sulfur dioxide, there will be 11.16 free sulfur dioxide
- A summary of the accuracy of your model
    The accuracy of the model, as indicated by the R-squared value of approximately 0.435, suggests that the linear regression model using 'total sulfur dioxide' to predict 'free sulfur dioxide' explains about 43.5% of the variability observed in 'free sulfur dioxide' based on this single feature.
- Real world implications
    A reliable model predicting 'free sulfur dioxide' in red wine based on 'total sulfur dioxide' levels can have practical applications in winemaking. Winemakers could use this predictive model to estimate 'free sulfur dioxide' concentrations during the production process, aiding in quality control and ensuring compliance with safety standards.

