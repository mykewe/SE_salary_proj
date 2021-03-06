# SOFTWARE ENGINEER SALARY ESTIMATOR
This predicts salaries of software engineers in the United Kingdom. 

* Built a model that estimates the salaries of software engineers (MAE = £9K)
* Scrapped up to 1000 job descriptions with the aid of python and selenium
* Cleaned the data collected to make it easier to understand
* Performed exploratory data analysis to understand and gain insight from the data, for example London has more software engineering jobs than any city in the whole of the United Kingdom
* Feature engineered job descriptions to understand the importance software engineering tools such as Java, Python etc
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Productionized the model by building a client facing API using flask


# Code and Resources Used

Python Version: 3.7 \
Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle \
For Web Framework Requirements: pip install -r requirements.txt \
[Scraper Github]( https://github.com/arapfaik/scraping-glassdoor-selenium)\
[Scraper Article]( https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905) \
[Flask Productionization]( https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2) \
[Inspiration]( https://github.com/PlayingNumbers/ds_salary_proj)


# Web Scraping

Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors


# Data Cleaning

After scraping the data,  I did the following to clean the data to make it usable:

* Parsed numeric data out of salary 
* Removed rows without salary 
* Made a new column for mean salary 
* Parsed rating out of company text 
* Made a new column for company city and country 
* Added a column for if the job was at the company’s headquarters
* Converted founded date into age of company
* Made columns for if different skills were listed in the job description: 
  * Python 
  * Java 
  * Javascript 
  * C++ 
* Created column for simplified job title to see if the jobs are frontend, backend or fullstack 
* Made a column for description length 

# Exploratory Data Analysis (EDA)

I looked at the distributions of the data and the value counts for the various categorical variables. A few highlights are shown below. It is seen that there is a concentration of Jobs in London and that you likely to get paid more if you are a frontend developer than if you are full stack of backend.


![](Job_city.png)               ![](Job_title.png)

   ![](Correlation.png)

# Model Building

First, I one-hot encoded the categorical variables. I then split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. 

I tried three different models:
Multiple Linear Regression – Baseline for the model. \
Lasso Regression – Because of the sparse data from the many categorical variables. \
Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit. 
## Model performance

The Random Forest model far outperformed the other approaches on the test and validation sets.

Random Forest : MAE =  9.08 \
Lasso Regression: MAE = 9.63

# Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
