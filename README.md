# Programming Assignment 3
Advanced Computer Programming

Joseph Bryn P. Carungay - 2ECE-C

# Advanced Computer Programming Assignment #3

## Problem 1
### A. Load the cars dataset into a dataframe
---
#### Code:
#### Loading and Displaying the Cars Dataset
```python
    import pandas as pd             #Import the pandas library as pd
    cars = pd.read_csv('cars.csv')  #Read the CSV file cars.csv into a DataFrame named cars
    cars                            #Display cars
```
<img width="899" height="713" alt="image" src="https://github.com/user-attachments/assets/5a0def88-9195-43de-ae51-ccbfb69b5bde" />

#### Key parts of the code:
    - import pandas as pd is used to load the pandas library
    - pd.read_csv('cars.csv') reads the cars.csv file
    - cars is the variable name for the dataframe
---
### B. Display the first five and last five rows
---
#### Code:
#### Displaying the First Five Rows of the Cars Dataset
```python
    print("First 5 rows of all cars")   #Print a label "First 5 rows of all cars"
    display(cars.head(5))               #Display the first 5 rows of the DataFrame using head(5)
```
<img width="823" height="444" alt="image" src="https://github.com/user-attachments/assets/db302024-2491-4cee-ae75-1b6fba9367cc" />

#### Displaying the Last Five Rows of the Cars Dataset
```python
    print("Last 5 rows of all cars")    #Print a label "Last 5 rows of all cars"
    display(cars.tail(5))               #Display the last 5 rows of the DataFrame using tail(5)
```
<img width="767" height="383" alt="image" src="https://github.com/user-attachments/assets/9590e5a1-da1d-4be8-b1e8-3bec2acc7a98" />

#### Key parts of the code
    - cars.head(5) shows the first five rows of the dataframe
    - cars.tail(5) shows the last five rows of the dataframe
    - print() and display() are used to label and output the results
---
## Problem 2
### A. Display the first five rows with odd-numbered columns
---
#### Code:
#### Selecting First Five Rows of Odd-Numbered Columns
```python
    print("First 5 odd-numbered columns of all cars")   #Print a label "First 5 odd-numbered columns of all cars"
    oddcars = cars.iloc[0:5,[1,3,5,7,9,11]]             #Select the first 5 rows and odd-numbered columns using iloc
    oddcars                                             #Store the result in oddcars and display it
```
<img width="1070" height="504" alt="image" src="https://github.com/user-attachments/assets/c22396d5-588c-405e-a612-f7f7c177582f" />

#### Key parts of the code:
    - .iloc[0:5,[1,3,5,7,9,11]] is used to select rows and odd-indexed columns
    - oddcars stores the extracted subset of the dataframe
---
### B. Display the row for the model 'Mazda RX4'
---
#### Code:
#### Filtering Rows for the Model 'Mazda RX4'
```python
    print("Model: Mazda RX4")                      #Print a label "Model: Mazda RX4"
    mazdarx4 = cars[cars['Model'] == 'Mazda RX4']  #Filter rows where the Model column equals "Mazda RX4"
    mazdarx4                                       #Store the result in mazdarx4 and display it
```
<img width="995" height="310" alt="image" src="https://github.com/user-attachments/assets/73f068be-08aa-440f-8d4e-5e2dcdf18436" />

#### Key parts of the code:
    - cars[cars['Model'] == 'Mazda RX4'] filters the dataframe to show the row with that model
    - mazdarx4 is the variable that stores the result
---
### C. Find how many cylinders the 'Camaro Z28' has
---
#### Code:
#### Retrieving the Cylinder Count for Camaro Z28
```python
    camarocylinders = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]   #Select the cylinders value of Camaro Z28 and store it in camarocylinders
    print(f"Cylinders of Camaro Z28: {camarocylinders} Cylinders")               #Print the cylinder count with a descriptive message
```
<img width="1453" height="200" alt="image" src="https://github.com/user-attachments/assets/1b3ce319-fb2c-42b2-a64c-a0cbb653b910" />

#### Key parts of the code:
    - .loc[] is used to select rows where Model == 'Camaro Z28'
    - ['cyl'] accesses the 'cyl' column of the filtered row
    - .values[0] extracts the single value
    - print() outputs the number of cylinders
---
### D. Determine cylinders and gears of selected models
---
#### Code:
#### Displaying Cylinders and Gears of Selected Car Models
```python
    print("Cylinder and Gears of Mazda RX4 Wag, Ford Pantera L, and Honda Civic")   #Print a label describing the task (showing cylinders and gears of specific models)
    models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']                     #Create a list of the target car models
    cars = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]           #Filter the DataFrame to include only these models and select columns Model, cyl, and gear
    cars                                                                            #Display the filtered DataFrame
```
<img width="1454" height="428" alt="image" src="https://github.com/user-attachments/assets/053c0c3e-168d-4dc1-bbdb-04b17b4a72d6" />

#### Key parts of the code:
    - .isin(models) is used to filter rows by multiple model names
    - ['Model','cyl','gear'] selects only the specified columns
    - cars is updated to display the filtered results
----
### Conclusion:
#### To conclude, this Pandas assignment demonstrated how to load a CSV file into a dataframe, display subsets of data, and extract information using subsetting, slicing, and indexing. By applying functions like .head(), .tail(), .iloc(), .loc(), and .isin(), specific rows and columns were successfully retrieved. This exercise showed the flexibility and efficiency of pandas for handling and analyzing tabular data.
---
##### Version 2: The README has been fully revised to include line-by-line and block-by-block explanations for each code segment, along with the results of each block, making it easier for viewers to follow the logic and flow of the notebook.
