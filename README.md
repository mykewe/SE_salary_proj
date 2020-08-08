# SOFTWARE ENGINEER SALARY ESTIMATOR
This predicts salaries of software engineers in the United Kingdom. 

* Built a model that estimates the salaries of software engineers (MAE K)
* Scrapped up to 1000 job describtions with the aid of python and selenium
* Cleaned the data collected to make it easier to understand
* Performed exploratory data analysis to understand and gain insight from the data, for example London has more software engineering jobs than any city in the whole of the United Kingdom
* Feature engineered job descriptions to understand the importance software engineering tools such as Java, Python etc
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Productionized the model by building a client facing API using flask


# Code and Resources Used

Python Version: 3.7
Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
For Web Framework Requirements: pip install -r requirements.txt
Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium
Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
Inspiration: https://github.com/PlayingNumbers/ds_salary_proj



