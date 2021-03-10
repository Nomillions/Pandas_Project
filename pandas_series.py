import pandas as pd

grades = pd.Series([87, 100, 94])
print(grades)
# demonstrates indexes on the left

same_grade = pd.Series(98.6, range(3))
print(same_grade)


print(grades[0])
"""
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()
"""

print(grades.describe())

grades = pd.Series([87, 100, 94], index=["Walley", "Eva", "Noah"])
print(grades)

grades = pd.Series({"Walley": 87, "Eva": 100, "Noah": 94})

print(grades["Eva"])
print(grades.Walley)
print(grades.dtype)
print(grades.values)