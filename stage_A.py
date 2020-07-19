# Import necessary libraries
import pandas as pd
import numpy as np

# Load the fuel_dataset
url='https://github.com/WalePhenomenon/climate_change/blob/master/fuel_ferc1.csv?raw=true'
url='fuel_data.csv'
fuel_data = pd.read_csv(url, error_bad_lines=False)

## Question 1: How do you create an identity matrix in python?
print(np.identity(3))

## Question 2: The feature with missing values falls under what category? What missing value imputation technique would you use?
fuel_data.info()

## Question 3: Which of the features has the second and third lowest correlation with the Fuel Cost Per Unit Burned?
corr = fuel_data.corr()
print(corr)

## Question 4: For the fuel type coal, what is the percentage change in the fuel cost per unit burned in 1998 compared to 1994?
f= fuel_data[['fuel_type_code_pudl','report_year','fuel_cost_per_unit_burned']].groupby(['fuel_type_code_pudl','report_year']).sum().unstack()
p = f.T.reset_index()[['report_year', 'coal']].set_index('report_year')
p.index.name = None; p.columns.name = None
perc_change = (p.iloc[4]-p.iloc[0])/p.iloc[0]*100
print(round(perc_change))

## Question 5: Which year has the highest average fuel cost per unit delivered?
year = fuel_data.groupby('report_year').mean()['fuel_cost_per_unit_delivered'].idxmax()
print(year)

## Question 6: What is the standard deviation and 75th percentile of the measure of energy per unit (Fuel_mmbtu_per_unit) in two decimal places?
print(fuel_data.describe(exclude='object').T)

## Question 7: What is the skewness and kurtosis for the fuel quantity burned in two decimal places?
print(fuel_data.skew())
print(fuel_data.kurt())

## Question 8: Which feature has missing values and what is the total number of missing value and percentage of the missing rows as a factor of the total number of rows in three decimal places?
#feature has missing values and what is the total number of missing value
print(fuel_data.isnull().sum())
#percentage of the missing rows as a factor of the total number of rows in three decimal places
print(fuel_data.isnull().sum()/len(fuel_data)*100)

## Question 9: Which of the following fuel type code has the lowest average fuel cost per unit burned?
print(fuel_data[['fuel_type_code_pudl','fuel_cost_per_unit_burned']].groupby('fuel_type_code_pudl').mean())

## Question 10 If you’re given two lists: A = [1,2,3,4,5,6], B = [13, 21, 34] The task is to create a list with the elements of A and B in a single dimension with output: A_B =  [1,2,3,4,5,6,13, 21, 34] Which of the following option is the best way to create this list?
A = [1,2,3,4,5,6]
B = [13, 21, 34]
A.extend(B)
print(A)
