# Programming Assignment 3
Advanced Computer Programming

Joseph Bryn P. Carungay - 2ECE-C

# Advanced Computer Programming Assignment #3

## Problem 1
### A. Load the cars dataset into a dataframe
    - Key parts of the code
      - import pandas as pd is used to load the pandas library
      - pd.read_csv('cars.csv') reads the cars.csv file
      - cars is the variable name for the dataframe

### B. Display the first five and last five rows
    - Key parts of the code
      - cars.head(5) shows the first five rows of the dataframe
      - cars.tail(5) shows the last five rows of the dataframe
      - print() and display() are used to label and output the results

## Problem 2
### A. Display the first five rows with odd-numbered columns
    - Key parts of the code
      - .iloc[0:5,[1,3,5,7,9,11]] is used to select rows and odd-indexed columns
      - oddcars stores the extracted subset of the dataframe

#### B. Display the row for the model 'Mazda RX4'
    - Key parts of the code
      - cars[cars['Model'] == 'Mazda RX4'] filters the dataframe to show the row with that model
      - mazdarx4 is the variable that stores the result

#### C. Find how many cylinders the 'Camaro Z28' has
    - Key parts of the code
      - .loc[] is used to select rows where Model == 'Camaro Z28'
      - ['cyl'] accesses the 'cyl' column of the filtered row
      - .values[0] extracts the single value
      - print() outputs the number of cylinders

#### D. Determine cylinders and gears of selected models
    - Key parts of the code
      - .isin(models) is used to filter rows by multiple model names
      - ['Model','cyl','gear'] selects only the specified columns
      - cars is updated to display the filtered results

### Conclusion
### To conclude, this Pandas assignment demonstrated how to load a CSV file into a dataframe, display subsets of data, and extract information using subsetting, slicing, and indexing. By applying functions like .head(), .tail(), .iloc(), .loc(), and .isin(), specific rows and columns were successfully retrieved. This exercise showed the flexibility and efficiency of pandas for handling and analyzing tabular data.
