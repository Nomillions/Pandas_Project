# Pandas Exercise
# MIS 4322
# Noah Miller

import pandas as pd
import random

print(""" Create a Series from the list [7, 11, 13, 17]. """)
Series = pd.Series([7, 11, 13, 17])
print(Series)
print()

print(""" Create a Series with five elements that are all 100.0. """)
Hundreds = pd.Series([100.0, 100.0, 100.0, 100.0, 100.0])
print(Hundreds)
print()

print(
    """Create a Series with 20 elements that are all random numbers in the range 0 to 100. 
    Use method describe to produce the Series’ basic descriptive statistics."""
)
twentyElements = []
for numbers in range(20):
    twentyElements.append(random.randrange(1, 101, 1))
PDtwentyElements = pd.Series(twentyElements)
print(PDtwentyElements)
print(
    """
Statistical Descriptions:
"""
)
print(PDtwentyElements.describe())

print(
    """
Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. 
Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.
Form a dictionary from the names and values in Part (4), then use it to initialize a Series.
"""
)
temperatures = pd.Series(
    [98.6, 98.9, 100.2, 97.9], index=["Julie", "Charlie", "Sam", "Andrea"]
)
print(temperatures)
print()
dictionary_temperatures = pd.Series(
    {"Julie": 98.6, "Charlie": 98.9, "Sam": 100.2, "Andrea": 97.9}
)
print(dictionary_temperatures)