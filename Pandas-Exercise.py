"""
Perform the following tasks with pandas Series:

Create a Series from the list [7, 11, 13, 17].
Create a Series with five elements that are all 100.0.
Create a Series with 20 elements that are all random numbers in the range 0 to 100. Use method describe to produce the Series’ basic descriptive statistics.
Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.
Form a dictionary from the names and values in Part (4), then use it to initialize a Series.

"""
import pandas as pd
import random as r

Series = pd.Series([7, 11, 13, 17])
print(Series)

Hundreds = pd.Series([100.0, 100.0, 100.0, 100.0, 100.0])
print(Hundreds)
